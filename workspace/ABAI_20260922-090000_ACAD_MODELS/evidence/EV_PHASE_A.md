# EV — ABAI_20260922-090000_ACAD_MODELS / Phase A: Нормативная триада академических подразделений (Факультет, Институт, Школа)

> **Date**: 2026-09-22  
> **Author**: Executor / Legal & Educational Process Engineer  
> **Task**: ABAI_20260922-090000_ACAD_MODELS  
> **TS**: [TS Phase A](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260922-090000_ACAD_MODELS/TS.md)  
> **Candidate Commit**: `5ccc07c`  

---

## Environment

| Field | Value |
|---|---|
| OS | Windows 11 Pro / PowerShell 5.1 |
| Language / Runtime | Python 3.13.14 |
| Repository | Git 2.50.0 |
| Framework | Trace-First Workflow (TFW v3.4.0) |

---

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|:---:|---|
| **E1** | AC-1 | Разработано Типовое положение о факультете: структура деканата (декан, 3 заместителя), кафедры, Совет факультета (ППС $\ge 70\%$, студенты $\ge 15\%$), методбюро, матрица RACI и регламент в УИС с дедлайнами SLA | Local Git Repo | `VERIFIED` | [`faculty_model_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/faculty_model_regulation.md) |
| **E2** | AC-2 | Разработана Типовая ДИ Декана факультета: квалификационные требования Приказа МОН № 338, уровень 8 НРК Профстандарта «Педагог», статьи 22, 23, 64 ТК РК и ст. 79 КоАП РК | Local Git Repo | `VERIFIED` | [`jd_dean_faculty.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_dean_faculty.md) |
| **E3** | AC-3 | Разработано Типовое положение о Школе: матричная структура, Program Leads, Industry Advisory Board, Capstone/PBL, форматы Minor 20–30 ECTS, аккредитации ABET/AACSB/FIBAA | Local Git Repo | `VERIFIED` | [`school_model_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/school_model_regulation.md) |
| **E4** | AC-4 | Разработана Типовая ДИ Декана школы: требования PhD/Doctorate, уровень C1 английского языка, руководство IAB, международные аккредитации, фандрайзинг, KPI трудоустройства $\ge 80\%$ | Local Git Repo | `VERIFIED` | [`jd_dean_school.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_dean_school.md) |
| **E5** | AC-5 | Разработана ДИ Директора института (`jd_director_institute.md`) и гармонизировано Положение об институте (`institute_model_regulation.md`): функции R&D, TRL 1–9, диссоветы PhD по Приказу № 126, авторские роялти $\ge 30\%$ | Local Git Repo | `VERIFIED` | [`jd_director_institute.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_director_institute.md), [`institute_model_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/institute_model_regulation.md) |
| **E6** | AC-6 | Проверка ripgrep/Python: 0 маркеров TODO/TBD, макропеременные `[V_*]` валидны, Candidate commit `5ccc07c` зафиксирован | Local Python 3.13 | `VERIFIED` | 6 файлов VALUE, 0 совпадений по маркерам незавершенности |
| **E-accounting** | Accounting | 5 новых файлов VALUE + 1 модифицированный VALUE = 6 файлов VALUE; 624 additions, 16 deletions = 640 touched LOC $\le 1200$ | Git `5ccc07c` | `VERIFIED` | `git diff --stat 797bf66 5ccc07c` |

---

## Verdict

Evidence verdict: **7/7 VERIFIED**, 0 DEFERRED, 0 BLOCKED, 0 N/A.

---

*EV — ABAI_20260922-090000_ACAD_MODELS / Phase A | 2026-09-22*
