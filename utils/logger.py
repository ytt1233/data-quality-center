
import logging
import os
import traceback
from config.settings import Settings  

sys_logs_dir = Settings.SYS_LOGS_DIR
os.makedirs(sys_logs_dir, exist_ok=True)
logging.basicConfig(
    filename=f"{sys_logs_dir}/system.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_system_error(exception: Exception):
    error_type = getattr(exception, "error_type", "SYSTEM_ERROR")
    error_code = getattr(exception, "error_code", "SYS-000")
    exception_class = exception.__class__.__name__

    message = (
        f"[{error_type}] "
        f"[{error_code}] "
        f"[{exception_class}] "
        f"{str(exception)}"
    )

    logging.error(message)
    logging.error("Stack trace:\n%s", traceback.format_exc())
