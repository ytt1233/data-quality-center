# ops/notifier.py

def notify_ops(error_type, error_code, message, context):
    print("🚨 DATA QUALITY ALERT 🚨")
    print(f"Error Type: {error_type}")
    print(f"Error Code: {error_code}")
    print(f"Message: {message}")
    print(f"Context: {context}")
