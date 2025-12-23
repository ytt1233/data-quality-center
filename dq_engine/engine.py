# dq_engine/engine.py

import yaml
from dq_engine.validators import (
    validate_not_null,
    validate_regex,
    validate_range,
    validate_date,
    validate_length_min,
)
from dq_engine.gate import quality_gate
from dq_engine.score import calculate_dq_score 
from config.settings import settings
 
VALIDATOR_MAP = {
    "not_null": validate_not_null,
    "regex": validate_regex,
    "range": validate_range,
    "date": validate_date,
    "length_min": validate_length_min,
}


def load_rules(path="config/rules.yaml"):
    """Load YAML rule definitions."""
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def run_dq(df, rules_config):
    """Run all DQ rules against the DataFrame."""
    rule_results = []

    for rule in rules_config.get("rules", []):
        if not rule.get("enabled", True):
            continue

        rule_type = rule["type"]
        validator = VALIDATOR_MAP.get(rule_type)
        if validator is None: 
            print(f"⚠ Unknown rule type: {rule_type}")
            continue

        result = validator(df, rule)
        rule_results.append(result)
    dq_score = calculate_dq_score(rule_results)
    gate_status = quality_gate(rule_results, dq_score, settings.DQ_SCORE_THRESHOLD)
    print(f"gate_status: {gate_status}")

    return {
        "rule_results": rule_results, 
        "dq_score": dq_score, 
        "gate_status": gate_status
        }
