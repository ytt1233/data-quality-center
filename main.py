# main.py

import pandas as pd
from config.settings import settings
from data_sources.csv_reader import read_csv_data
from dq_engine.engine import load_rules, run_dq
from dq_engine.exceptions import DQGateRejected
from storage.dq_logger import log_dq_result
from ops.notifier import notify_ops
from utils.logger import log_system_error
from reports.report_generator import generate_dq_report
from storage.audit_logger import log_dq_audit




def main():
    print("🚀 Data Quality Center Starting...")
    # 使用时通过 settings 实例访问
    data_path = settings.DATA_PATH
    result_path = settings.RESULT_PATH
    rule_file = settings.RULE_FILE
    # Load data
    df = read_csv_data(data_path)
    # Load rules
    rules = load_rules(rule_file)

    # Run DQ
    try:
        dq_results = run_dq(df, rules)
        # Generate report
        report_path = generate_dq_report(dq_results)
        dq_results["report_path"] = report_path
        # 质量审计快照
        log_dq_audit(
            dq_results,
            dataset_name=data_path
        )
        #Gate
        if dq_results["gate_status"] == "REJECTED":
            raise DQGateRejected(dq_results)

    except DQGateRejected as e:
        log_dq_result(e.dq_result)#事件日志，用于记录和复盘
        notify_ops(
            error_type=e.error_type,
            error_code=e.error_code,
            message=str(e),
            context=e.context
        )#告警通告，这里只打印，真实场景会关联到邮箱、钉钉等

    except Exception as e:
        log_system_error(e)#系统异常日志
        notify_ops(
            error_type=e.error_type,
            error_code=e.error_code,
            message=str(e),
            context=e.context
        )


if __name__ == "__main__":
    main()
