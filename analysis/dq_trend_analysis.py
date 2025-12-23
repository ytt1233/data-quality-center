import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


def load_audit_log():
 
    # 获取当前脚本所在的目录（analysis文件夹）
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 构建绝对路径
    audit_log_file = os.path.join(current_dir, "..", "logs","audit_logs", "audit_log.csv")
    
    print(f"当前脚本位置: {__file__}")
    print(f"脚本所在目录: {current_dir}")
    print(f"目标文件路径: {audit_log_file}")
    print(f"绝对路径: {os.path.abspath(audit_log_file)}")
    return pd.read_csv(audit_log_file,parse_dates=["run_time"])

def plot_dq_score_trend(audit_log):
    plt.close("all")
    plt.figure()
    plt.plot(df["run_time"], df["dq_score"])
    plt.xlabel("Run Time")
    plt.ylabel("DQ Score")
    plt.title("DQ Score Trend")
    # plt.show()

def plot_gate_status_distribution(df):
    counts = df["gate_status"].value_counts()
    plt.figure()
    counts.plot(kind="bar")
    plt.xlabel("Gate Status")
    plt.ylabel("Count")
    plt.title("Gate Status Distribution")
    # plt.show()

def plot_error_warning_trend(df):
    plt.figure()
    plt.plot(df["run_time"], df["error_failed"], label="Error Failed")
    plt.plot(df["run_time"], df["warning_failed"], label="Warning Failed")
    plt.xlabel("Run Time")
    plt.ylabel("Failed Rule Count")
    plt.title("Rule Failure Trend")
    plt.legend()
    # plt.show()

if __name__ == "__main__":
    df = load_audit_log()
    plot_dq_score_trend(df)
    plot_gate_status_distribution(df)
    plot_error_warning_trend(df)
    plt.show()