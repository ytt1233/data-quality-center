def calculate_dq_score(results):
    total_weight = 0
    weight_score = 0

    for r in results:
        weight = r["weight"]
        score = r["rule_score"]
        total_weight += weight
        weight_score += weight * score

    if total_weight == 0:
        return 100.0
    
    return round(weight_score / total_weight, 2)