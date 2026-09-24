import os
import subprocess
import markdown

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

DOCS = [
    {
        "input": r"docs/internal_acts/sops_and_rules/ai_governance_and_integrity_policy.md",
        "title": "Институциональная политика этичного использования искусственного интеллекта (POL-AI-INTEGRITY-001)",
        "output_name": "POL-AI-INTEGRITY-001_ai_governance_and_integrity_policy.pdf"
    },
    {
        "input": r"docs/internal_acts/sops_and_rules/ai_usage_statement_form.md",
        "title": "Декларация об использовании технологий искусственного интеллекта (AI Statement Form)",
        "output_name": "FORM-AI-STATEMENT-001_ai_usage_statement_form.pdf"
    },
    {
        "input": r"docs/internal_acts/sops_and_rules/academic_integrity_policy.md",
        "title": "Политика академической честности (POL-ACAD-HONEST-001)",
        "output_name": "POL-ACAD-HONEST-001_academic_integrity_policy.pdf"
    },
    {
        "input": r"docs/internal_acts/sops_and_rules/guidelines_ai_authentic_assessment_for_faculty.md",
        "title": "Методические указания по аутентичному оцениванию для ППС (GUIDE-ACAD-AI-001)",
        "output_name": "GUIDE-ACAD-AI-001_guidelines_ai_authentic_assessment_for_faculty.pdf"
    },
    {
        "input": r"docs/internal_acts/sops_and_rules/sop_scientific_ai_ethics_and_publishing.md",
        "title": "Регламент этики научных исследований и публикаций (SOP-SCI-AI-ETHICS-001)",
        "output_name": "SOP-SCI-AI-ETHICS-001_sop_scientific_ai_ethics_and_publishing.pdf"
    },
    {
        "input": r"workspace/ABAI_20260923-151500_AI_POLICY/review/REVIEW.md",
        "title": "Сводный итоговый отчет и заключение аудита (ABAI-26 Master Review)",
        "output_name": "REVIEW_ABAI-26_AI_POLICY_Master_Report.pdf"
    }
]

CSS = """
@page {
    size: A4;
    margin: 20mm 15mm 20mm 15mm;
    @bottom-right {
        content: counter(page);
    }
}
body {
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif;
    color: #1e293b;
    line-height: 1.55;
    font-size: 10.5pt;
}
h1 {
    font-size: 17pt;
    color: #0f2744;
    border-bottom: 2px solid #1e3a8a;
    padding-bottom: 6px;
    margin-top: 0;
    margin-bottom: 14px;
    line-height: 1.25;
}
h2 {
    font-size: 13pt;
    color: #1e3a8a;
    border-bottom: 1px solid #cbd5e1;
    padding-bottom: 4px;
    margin-top: 18px;
    margin-bottom: 10px;
    page-break-after: avoid;
}
h3 {
    font-size: 11pt;
    color: #334155;
    margin-top: 14px;
    margin-bottom: 6px;
    page-break-after: avoid;
}
p {
    margin-top: 0;
    margin-bottom: 8px;
    text-align: justify;
}
blockquote {
    border-left: 4px solid #2563eb;
    margin: 10px 0;
    padding: 8px 14px;
    background-color: #f8fafc;
    color: #334155;
    font-size: 9.5pt;
    border-radius: 0 4px 4px 0;
}
blockquote p {
    margin-bottom: 4px;
}
blockquote p:last-child {
    margin-bottom: 0;
}
table {
    width: 100%;
    border-collapse: collapse;
    margin: 12px 0;
    font-size: 9pt;
    page-break-inside: auto;
}
tr {
    page-break-inside: avoid;
    page-break-after: auto;
}
th, td {
    border: 1px solid #cbd5e1;
    padding: 6px 8px;
    text-align: left;
    vertical-align: top;
}
th {
    background-color: #f1f5f9;
    color: #0f172a;
    font-weight: 600;
}
tr:nth-child(even) {
    background-color: #f8fafc;
}
pre {
    background-color: #f8fafc;
    border: 1px solid #e2e8f0;
    padding: 10px;
    border-radius: 4px;
    font-family: Consolas, 'Courier New', monospace;
    font-size: 8.5pt;
    overflow-x: auto;
    white-space: pre-wrap;
    word-break: break-all;
    margin: 10px 0;
}
code {
    font-family: Consolas, 'Courier New', monospace;
    font-size: 9pt;
    background-color: #f1f5f9;
    padding: 1px 4px;
    border-radius: 3px;
    color: #0f172a;
}
pre code {
    background: none;
    padding: 0;
    color: inherit;
}
ul, ol {
    margin-top: 4px;
    margin-bottom: 10px;
    padding-left: 20px;
}
li {
    margin-bottom: 4px;
}
hr {
    border: 0;
    height: 1px;
    background: #e2e8f0;
    margin: 14px 0;
}
.header-badge {
    display: inline-block;
    background: #e0f2fe;
    color: #0369a1;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 8.5pt;
    font-weight: 600;
    margin-bottom: 8px;
}
.footer-note {
    margin-top: 25px;
    font-size: 8pt;
    color: #64748b;
    border-top: 1px solid #e2e8f0;
    padding-top: 6px;
    text-align: right;
}
"""

def convert_md_to_pdf():
    base_dir = os.path.abspath(".")
    pdf_out_dir = os.path.join(base_dir, "docs", "internal_acts", "pdf")
    os.makedirs(pdf_out_dir, exist_ok=True)
    
    workspace_pdf_dir = os.path.join(base_dir, "workspace", "ABAI_20260923-151500_AI_POLICY", "pdf")
    os.makedirs(workspace_pdf_dir, exist_ok=True)
    
    temp_dir = os.path.join(base_dir, "workspace", "ABAI_20260923-151500_AI_POLICY", "temp_html")
    os.makedirs(temp_dir, exist_ok=True)

    results = []

    for item in DOCS:
        in_path = os.path.join(base_dir, item["input"])
        if not os.path.exists(in_path):
            print(f"Missing: {in_path}")
            continue

        with open(in_path, "r", encoding="utf-8") as f:
            md_text = f.read()

        html_body = markdown.markdown(
            md_text,
            extensions=["tables", "fenced_code", "sane_lists", "nl2br"]
        )

        full_html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<title>{item['title']}</title>
<style>
{CSS}
</style>
</head>
<body>
{html_body}
<div class="footer-note">
Официальный нормативный документ НАО «КазНПУ имени Абая» | Система управления качеством TFW
</div>
</body>
</html>"""

        html_file = os.path.join(temp_dir, os.path.splitext(item["output_name"])[0] + ".html")
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(full_html)

        pdf_target1 = os.path.join(pdf_out_dir, item["output_name"])
        pdf_target2 = os.path.join(workspace_pdf_dir, item["output_name"])

        cmd = [
            EDGE_PATH,
            "--headless",
            "--disable-gpu",
            "--run-all-compositor-stages-before-draw",
            f"--print-to-pdf={pdf_target1}",
            "--no-pdf-header-footer",
            f"file:///{os.path.abspath(html_file).replace(os.sep, '/')}"
        ]

        print(f"Generating PDF: {item['output_name']}...")
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode == 0 and os.path.exists(pdf_target1):
            import shutil
            shutil.copy2(pdf_target1, pdf_target2)
            size_kb = round(os.path.getsize(pdf_target1) / 1024, 1)
            print(f"Success! {pdf_target1} ({size_kb} KB)")
            results.append((item["output_name"], size_kb, pdf_target1))
        else:
            print(f"Error generating PDF for {item['output_name']}: {proc.stderr}")

    print("\nSummary of generated PDFs:")
    for name, size, path in results:
        print(f" - {name} ({size} KB)")

if __name__ == "__main__":
    convert_md_to_pdf()
