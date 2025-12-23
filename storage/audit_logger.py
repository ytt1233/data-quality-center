import csv
import os
from datetime import datetime
from config.settings import settings



def log_dq_audit(dq_result, dataset_name="default"):

    audit_log_dir = settings.AUDIT_LOG_DIR
    os.makedirs(audit_log_dir, exist_ok=True)
    filename = f"{audit_log_dir}/audit_log.csv"
    file_exists = os.path.exists(filename)
    dataset_name = settings.DATA_PATH
    row = {
        "run_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "dataset": dataset_name,
        "dq_score": dq_result["dq_score"],
        "gate_status": dq_result["gate_status"],
        "error_failed": sum(
            1 for r in dq_result["rule_results"]
            if r["level"] == "error" and r["failed_count"] > 0
        ),
        "warning_failed": sum(
            1 for r in dq_result["rule_results"]
            if r["level"] == "warning" and r["failed_count"] > 0
        ),
        "report_path": dq_result.get("report_path")
    }

    with open(filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=row.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)