class DQException(Exception):
    """
    Base Exception for DQ
    """
    
    error_type = "DQ_ERROR"
    error_code = "DQ-000"
    def __init__(self, message=None, context=None):
        self.context = context or {}
        super().__init__(message or self.error_type)
    

class DQGateRejected(DQException):
    error_type = "DQ_GATE_REJECTED-"
    error_code = "DQ-001"
    def __init__(self, dq_result):
        self.dq_result = dq_result

        dq_score = dq_result.get("dq_score", "N/A")
        # dq_score = dq_result['hh']#用于测试异常情况
        rule_results = dq_result.get("rule_results", [])
        gate_status = dq_result.get("gate_status", "UNKNOWN")

        error_count = 0
        for r in rule_results:
            try:
                if r.get("level") == "error" and r.get("failed_count", 0) > 0:
                    error_count += 1
            except Exception:
                continue  # 异常信息构造阶段绝不失败

        message = (
            f"DQ Gate Rejected | "
            f"Score={dq_score} | "
            f"Status={gate_status} | "
            f"Errors_count={error_count} | "
        )

        context = {
            "dq_score": dq_score,
            "gate_status": gate_status,
            "rule_results": dq_result.get("rule_results", []),
            "report_path": dq_result.get("report_path")
        }

        super().__init__(message=message, context=context)

