import os
import subprocess
import sys
import tempfile

try:
    import markdown
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "markdown"], check=True)
    import markdown

# Setup paths
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(script_dir)
reg_dir = os.path.join(root_dir, "docs", "regulations")
func_dir = os.path.join(root_dir, "docs", "functions_and_powers")
export_dir = os.path.join(root_dir, "docs", "exports")
os.makedirs(export_dir, exist_ok=True)

html_path = os.path.join(export_dir, "master_transformation_folio.html")
pdf_path = os.path.join(export_dir, "Abai_University_Master_Transformation_Folio.pdf")

# Comprehensive sections pipeline
sections = [
    # --- PART 1: EXTERNAL REGULATIONS & REGULATORY POLICY (РЧЛ) ---
    os.path.join(reg_dir, "external_npa_registry.md"),
    os.path.join(reg_dir, "01_academic_and_educational_npa.md"),
    os.path.join(reg_dir, "02_science_and_innovations_npa.md"),
    os.path.join(reg_dir, "03_hr_and_faculty_npa.md"),
    os.path.join(reg_dir, "04_student_and_youth_npa.md"),
    os.path.join(reg_dir, "05_governance_finance_compliance_npa.md"),
    os.path.join(reg_dir, "06_healthcare_and_sanitary_npa.md"),
    os.path.join(reg_dir, "07_fire_and_emergency_safety_npa.md"),
    os.path.join(reg_dir, "08_digitalization_infosec_ai_npa.md"),
    os.path.join(reg_dir, "09_strategic_planning_and_governance_npa.md"),

    # --- PART 2: CATALOG OF FUNCTIONS AND RESPONSIBILITIES (10 DOMAINS RACI) ---
    os.path.join(func_dir, "README.md"),
    os.path.join(func_dir, "01_academic_affairs.md"),
    os.path.join(func_dir, "02_science_and_technology.md"),
    os.path.join(func_dir, "03_student_affairs.md"),
    os.path.join(func_dir, "04_internationalization.md"),
    os.path.join(func_dir, "05_quality_assurance_and_compliance.md"),
    os.path.join(func_dir, "06_governance_and_legal.md"),
    os.path.join(func_dir, "07_finance_and_procurement.md"),
    os.path.join(func_dir, "08_digitalization_and_it.md"),
    os.path.join(func_dir, "09_infrastructure_and_facilities.md"),
    os.path.join(func_dir, "10_human_capital_and_hr.md"),

    # --- PART 3: KNOWLEDGE BASE & REGULATORY DEBT ---
    os.path.join(root_dir, "KNOWLEDGE.md"),
    os.path.join(root_dir, "TECH_DEBT.md"),

    # --- PART 4: INTERNAL REGULATIONS, BLUEPRINTS & SOPS ---
    os.path.join(root_dir, "docs", "internal_acts", "README.md"),
    os.path.join(root_dir, "docs", "internal_acts", "regulations", "dav_regulation.md"),
    os.path.join(root_dir, "docs", "internal_acts", "regulations", "registrar_regulation.md"),
    os.path.join(root_dir, "docs", "internal_acts", "regulations", "institute_model_regulation.md"),
    os.path.join(root_dir, "docs", "internal_acts", "regulations", "department_chair_regulation.md"),
    os.path.join(root_dir, "docs", "internal_acts", "regulations", "science_department_regulation.md"),
    os.path.join(root_dir, "docs", "internal_acts", "regulations", "commercialization_office_regulation.md"),
    os.path.join(root_dir, "docs", "internal_acts", "regulations", "young_scientists_council_regulation.md"),
    os.path.join(root_dir, "docs", "internal_acts", "regulations", "research_institute_model_regulation.md"),
    os.path.join(root_dir, "docs", "internal_acts", "regulations", "compliance_service_regulation.md"),
    os.path.join(root_dir, "docs", "internal_acts", "regulations", "quality_assurance_committee_regulation.md"),
    os.path.join(root_dir, "docs", "internal_acts", "regulations", "accreditation_center_regulation.md"),
    os.path.join(root_dir, "docs", "internal_acts", "regulations", "edtech_advisory_board_regulation.md"),
    os.path.join(root_dir, "docs", "internal_acts", "regulations", "digitalization_department_regulation.md"),
    os.path.join(root_dir, "docs", "internal_acts", "regulations", "it_infrastructure_department_regulation.md"),
    os.path.join(root_dir, "docs", "internal_acts", "regulations", "is_4level_security_registry.md"),
    os.path.join(root_dir, "docs", "internal_acts", "regulations", "strategic_development_department_regulation.md"),
    os.path.join(root_dir, "docs", "internal_acts", "job_descriptions", "jd_director_dav.md"),
    os.path.join(root_dir, "docs", "internal_acts", "job_descriptions", "jd_head_registrar.md"),
    os.path.join(root_dir, "docs", "internal_acts", "job_descriptions", "jd_faculty_model.md"),
    os.path.join(root_dir, "docs", "internal_acts", "job_descriptions", "jd_director_science.md"),
    os.path.join(root_dir, "docs", "internal_acts", "job_descriptions", "jd_head_commercialization.md"),
    os.path.join(root_dir, "docs", "internal_acts", "job_descriptions", "jd_researcher_model.md"),
    os.path.join(root_dir, "docs", "internal_acts", "job_descriptions", "jd_compliance_officer.md"),
    os.path.join(root_dir, "docs", "internal_acts", "job_descriptions", "jd_head_accreditation.md"),
    os.path.join(root_dir, "docs", "internal_acts", "job_descriptions", "jd_head_digitalization.md"),
    os.path.join(root_dir, "docs", "internal_acts", "job_descriptions", "jd_head_it_infrastructure.md"),
    os.path.join(root_dir, "docs", "internal_acts", "job_descriptions", "jd_director_strategic_development.md"),
    os.path.join(root_dir, "docs", "internal_acts", "sops_and_rules", "sop_individual_curriculum_and_schedule.md"),
    os.path.join(root_dir, "docs", "internal_acts", "sops_and_rules", "sop_mvp_and_internal_grants.md"),
    os.path.join(root_dir, "docs", "internal_acts", "sops_and_rules", "sop_research_output_score.md"),
    os.path.join(root_dir, "docs", "internal_acts", "sops_and_rules", "academic_integrity_policy.md"),
    os.path.join(root_dir, "docs", "internal_acts", "sops_and_rules", "sop_anti_corruption_risk_assessment.md"),
    os.path.join(root_dir, "docs", "internal_acts", "sops_and_rules", "sop_epvo_nobd_integration.md"),
    os.path.join(root_dir, "docs", "internal_acts", "sops_and_rules", "sop_personal_data_protection.md"),
    os.path.join(root_dir, "docs", "internal_acts", "sops_and_rules", "sop_online_courses_quality_standard.md"),
    os.path.join(root_dir, "docs", "internal_acts", "sops_and_rules", "sop_university_development_strategy.md"),
    os.path.join(root_dir, "docs", "internal_acts", "sops_and_rules", "sop_employee_cybersecurity_and_labor_safety.md"),
    os.path.join(root_dir, "docs", "internal_acts", "blueprints", "aitu_innovations_for_abai.md"),
    os.path.join(root_dir, "docs", "internal_acts", "blueprints", "abai_digital_platform_architecture.md"),
    os.path.join(root_dir, "docs", "internal_acts", "blueprints", "abai_strategy_2026_2030_architecture.md"),

    # --- PART 5: BENCHMARKING PROPOSALS & MODEL AMENDMENTS ---
    os.path.join(root_dir, "workspace", "ABAI_20260914-192000_COMP", "PROPOSALS__model_acts_amendments.md"),
    os.path.join(root_dir, "docs", "benchmarking", "aitu_regulatory_policy_audit.md")
]

content_parts = []

# Title Page / Cover
cover_html = """
<div style="text-align: center; padding-top: 100px; padding-bottom: 80px;">
    <div style="font-size: 13pt; text-transform: uppercase; letter-spacing: 2px; color: #1e3a8a; font-weight: 700; margin-bottom: 20px;">
        Министерство науки и высшего образования Республики Казахстан<br>
        НАО «Казахский национальный педагогический университет имени Абая»
    </div>
    <div style="height: 4px; width: 120px; background-color: #1e40af; margin: 0 auto 40px auto;"></div>
    <h1 style="font-size: 26pt; color: #0f172a; margin-bottom: 18px; line-height: 1.25; border: none; padding: 0;">
        Сводная нормативно-функциональная система университета
    </h1>
    <h2 style="font-size: 15pt; color: #334155; font-weight: 500; border: none; margin-top: 0; margin-bottom: 40px;">
        Единый реестр внешних НПА РК (РЧЛ), сквозной каталог функций по 10 доменам и матрица ответственности RACI
    </h2>
    <div style="background-color: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 8px; padding: 20px 30px; text-align: left; max-width: 650px; margin: 0 auto;">
        <p style="margin: 6px 0; font-size: 10pt;"><strong>Методология:</strong> Trace-First Workflow (TFW v3.4.0)</p>
        <p style="margin: 6px 0; font-size: 10pt;"><strong>Регуляторная политика:</strong> «С чистого листа» (РЧЛ, 67 обязательных НПА + 13 профильных актов РК)</p>
        <p style="margin: 6px 0; font-size: 10pt;"><strong>База эталонных источников:</strong> Информационно-правовая система нормативных правовых актов РК (ИПС «Әділет»)</p>
        <p style="margin: 6px 0; font-size: 10pt;"><strong>Охват:</strong> Академический блок, Наука, Кадры, Контингент, Комплаенс, Здравоохранение, Безопасность и ГО</p>
    </div>
    <div style="margin-top: 140px; font-size: 10pt; color: #64748b;">
        Алматы — 2026
    </div>
</div>
<div class="page-break"></div>
"""

for fpath in sections:
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8") as f:
            text = f.read()
            # Convert file content to HTML
            html_chunk = markdown.markdown(
                text,
                extensions=["tables", "fenced_code", "nl2br", "sane_lists", "toc"]
            )
            content_parts.append(html_chunk)
    else:
        print(f"Warning: file not found {fpath}")

combined_body = cover_html + "\n\n<div class='page-break'></div>\n\n".join(content_parts)

css = """
@page {
    size: A4;
    margin: 16mm 12mm 16mm 12mm;
    @bottom-right {
        content: counter(page) " / " counter(pages);
        font-family: 'Segoe UI', Arial, sans-serif;
        font-size: 8pt;
        color: #64748b;
    }
    @bottom-left {
        content: "НАО «КазНПУ имени Абая» — Регуляторная политика и каталог функций";
        font-family: 'Segoe UI', Arial, sans-serif;
        font-size: 8pt;
        color: #64748b;
    }
}
* { box-sizing: border-box; }
body {
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Arial, sans-serif;
    color: #1e293b;
    line-height: 1.5;
    font-size: 9pt;
    background: #ffffff;
    margin: 0;
    padding: 0;
}
.page-break {
    page-break-after: always;
}
h1 {
    font-size: 17pt;
    font-weight: 800;
    color: #0f2b5c;
    border-bottom: 2.5px solid #1e40af;
    padding-bottom: 5px;
    margin-top: 20px;
    margin-bottom: 12px;
    page-break-before: auto;
    page-break-after: avoid;
}
h2 {
    font-size: 12.5pt;
    font-weight: 700;
    color: #1e3a8a;
    border-bottom: 1.5px solid #cbd5e1;
    padding-bottom: 4px;
    margin-top: 18px;
    margin-bottom: 8px;
    page-break-after: avoid;
}
h3 {
    font-size: 10.5pt;
    font-weight: 600;
    color: #1e293b;
    margin-top: 14px;
    margin-bottom: 6px;
    page-break-after: avoid;
}
p {
    margin-top: 0;
    margin-bottom: 8px;
    text-align: justify;
}
a {
    color: #1d4ed8;
    text-decoration: underline;
    font-weight: 500;
}
a:hover {
    color: #0c4a6e;
}
blockquote {
    margin: 10px 0;
    padding: 8px 14px;
    background-color: #eff6ff;
    border-left: 4px solid #2563eb;
    color: #1e3a8a;
    font-size: 8.8pt;
    border-radius: 0 5px 5px 0;
    page-break-inside: avoid;
}
table {
    width: 100%;
    border-collapse: collapse;
    margin: 10px 0;
    font-size: 8pt;
    page-break-inside: auto;
}
tr {
    page-break-inside: avoid;
    page-break-after: auto;
}
th, td {
    border: 1px solid #cbd5e1;
    padding: 5px 7px;
    vertical-align: top;
}
th {
    background-color: #1e3a8a;
    color: #ffffff;
    font-weight: 600;
    text-align: left;
}
tr:nth-child(even) { background-color: #f8fafc; }
code {
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 8pt;
    background-color: #f1f5f9;
    color: #0f172a;
    padding: 1px 4px;
    border-radius: 3px;
    border: 1px solid #e2e8f0;
}
pre {
    background-color: #0f172a;
    color: #f8fafc;
    padding: 10px 12px;
    border-radius: 5px;
    font-family: 'Consolas', monospace;
    font-size: 7.8pt;
    line-height: 1.35;
    page-break-inside: avoid;
    margin: 10px 0;
}
pre code { background-color: transparent; color: inherit; padding: 0; border: none; }
ul, ol { margin-top: 0; margin-bottom: 8px; padding-left: 18px; }
li { margin-bottom: 2px; }
hr { border: none; border-top: 1px solid #e2e8f0; margin: 15px 0; }
"""

full_html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>НАО «КазНПУ имени Абая» — Сводная нормативно-функциональная система</title>
    <style>{css}</style>
</head>
<body>
{combined_body}
</body>
</html>"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(full_html)

browser_candidates = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
]

browser_exe = None
for b in browser_candidates:
    if os.path.exists(b):
        browser_exe = b
        break

if not browser_exe:
    print("ERROR: No browser found to render PDF.")
    sys.exit(1)

temp_profile = tempfile.mkdtemp(prefix="edge_pdf_")

cmd = [
    browser_exe,
    "--headless",
    "--disable-gpu",
    "--no-sandbox",
    "--disable-extensions",
    "--no-first-run",
    "--no-default-browser-check",
    f"--user-data-dir={temp_profile}",
    "--no-pdf-header-footer",
    "--run-all-compositor-stages-before-draw",
    f"--print-to-pdf={pdf_path}",
    html_path
]

print(f"Executing: {' '.join(cmd)}", flush=True)
try:
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
except subprocess.TimeoutExpired:
    print("WARNING: Headless browser timed out after 90 seconds.", flush=True)
    res = None

if os.path.exists(pdf_path):
    print(f"SUCCESS: Master Transformation PDF generated at {pdf_path} (size: {os.path.getsize(pdf_path)} bytes)", flush=True)
else:
    err_msg = res.stderr if res else "Timeout"
    print(f"FAILED to generate PDF: {err_msg}", flush=True)
