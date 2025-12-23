# dq_engine/validators.py

import pandas as pd
from datetime import datetime
import ast


def validate_not_null(df, rule):
    field = rule["field"]
    failed_rows = df[df[field].isnull()]

    return {
        "rule": rule["name"],
        "field": field,
        "failed_rows": failed_rows.index.tolist(),
        "level": rule["level"],
        "weight": rule["weight"],
        "failed_count": len(failed_rows),
        "passed_count": len(df) - len(failed_rows),
        "total_count": len(df),
        "rule_score": (len(df) - len(failed_rows)) / len(df) * 100
   
    }


def validate_regex(df, rule):
    import re

    field = rule["field"]
    pattern = re.compile(rule["pattern"])
    failed_rows = df[~df[field].astype(str).str.match(pattern)]
    

    return {
        # "rule": rule["name"],
        # "field": field,
        # "failed_count": len(failed_rows),
        # "level": rule["level"],
        # "failed_rows": failed_rows.index.tolist(),
        "rule": rule["name"],
        "field": field,
        "failed_rows": failed_rows.index.tolist(),
        "level": rule["level"],
        "weight": rule["weight"],
        "failed_count": len(failed_rows),
        "passed_count": len(df) - len(failed_rows),
        "total_count": len(df),
        "rule_score": (len(df) - len(failed_rows)) / len(df) * 100
    }


def validate_range(df, rule):
    field = rule["field"]
    min_val = rule.get("min")
    max_val = rule.get("max")

    failed_rows = df[(df[field] < min_val) | (df[field] > max_val)]

    return {
        "rule": rule["name"],
        "field": field,
        "failed_count": len(failed_rows),
        "level": rule["level"],
        "failed_rows": failed_rows.index.tolist(),
    }


def validate_date(df, rule):
    field = rule["field"]
    date_format = rule["format"]

    failed_rows = []

    for i, v in df[field].items():
        try:
            datetime.strptime(str(v), date_format)
        except Exception:
            failed_rows.append(i)

    return {
        "rule": rule["name"],
        "field": field,
        "failed_count": len(failed_rows),
        "level": rule["level"],
        "failed_rows": failed_rows,
    }


def validate_length_min(df, rule):
    field = rule["field"]
    min_len = rule["min"]
    failed_rows = df[df['skills'].apply(lambda x :len(ast.literal_eval(x)) < 1)]

    return {
        "rule": rule["name"],
        "field": field,
        "failed_rows": failed_rows.index.tolist(),
        "level": rule["level"],
        "weight": rule["weight"],
        "failed_count": len(failed_rows),
        "passed_count": len(df) - len(failed_rows),
        "total_count": len(df),
        "rule_score": (len(df) - len(failed_rows)) / len(df) * 100
    }
