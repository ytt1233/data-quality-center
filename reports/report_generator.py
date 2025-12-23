import os
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

def generate_dq_report(dq_result, output_dir="reports/output"):
    os.makedirs(output_dir, exist_ok=True)

    env = Environment(
        loader=FileSystemLoader("reports/templates")
    )
    template = env.get_template("dq_report.html")

    for r in dq_result["rule_results"]:
        r["pass_rate"] = round(r["rule_score"],2) 

    html = template.render(
        dq_score=dq_result.get("dq_score"),
        gate_status=dq_result.get("gate_status"),
        rule_results=dq_result.get("rule_results", []),
        generated_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )


    report_path = f"{output_dir}/dq_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(html)

    return report_path
