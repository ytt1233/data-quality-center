import json
import os
from config.settings import settings
from datetime import datetime

def log_dq_result(dq_result):
    dq_logs_dir = settings.DQ_LOGS_DIR
    os.makedirs(dq_logs_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"{dq_logs_dir}/dq_{timestamp}.json"

    with open(path, "w", encoding="utf-8") as f:
        json.dump(dq_result, f, ensure_ascii=False, indent=2)

    print(f"📝 DQ result logged to {path}")