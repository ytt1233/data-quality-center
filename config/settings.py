class Settings:
    DATA_PATH = 'data/sample/jobs_sample.csv'
    RESULT_PATH = 'data/dq_result.csv'
    RULE_FILE = "config/rules.yaml"
    DQ_SCORE_THRESHOLD = 0.9
    DQ_LOGS_DIR = 'logs/dq_logs'
    SYS_LOGS_DIR = 'logs/sys_logs'
    AUDIT_LOG_DIR = 'logs/audit_logs'

settings = Settings()