def quality_gate(results, dq_score, dq_score_threshold):

    error_failed = [r for r in results if r["level"] == "error" and r["failed_count"] > 0]
    # print(f"error_failed: {error_failed}")
    if error_failed:
        return "REJECTED"
    if dq_score < dq_score_threshold:
        return "WARNING"
    
    return "PASSED"
