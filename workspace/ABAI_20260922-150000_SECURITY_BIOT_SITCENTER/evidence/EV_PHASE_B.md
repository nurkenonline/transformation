# EV — ABAI_20260922-150000_SECURITY_BIOT_SITCENTER / Phase B: Самостоятельные нормативные пакеты Службы охраны труда (БиОТ) и Отдела Гражданской обороны (ГО и ЧС), СОП тренировок и Домен 09

> **Date**: 2026-09-22  
> **Author**: Executor / Institutional & Security Implementation Specialist  
> **Task**: ABAI_20260922-150000_SECURITY_BIOT_SITCENTER  
> **TS**: [TS Phase B](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260922-150000_SECURITY_BIOT_SITCENTER/TS_PHASE_B.md)  

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
| **E1** | AC-1 | Разработано самостоятельное Положение о Службе охраны труда (`occupational_safety_regulation.md`, `REG-BIOT-001`): статус обособленной службы с прямым подчинением первому руководителю (ст. 202 ТК РК, Приказ МЗСР № 1020), аттестация рабочих мест 1 раз в 5 лет (Приказ МЗСР № 1057), специальное расследование несчастных случаев (ст. 187–190 ТК РК), проверка знаний (Приказ № 1019) | Local Git Repo | `VERIFIED` | [`occupational_safety_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/occupational_safety_regulation.md) |
| **E2** | AC-2 | Разработана Должностная инструкция Руководителя Службы охраны труда (`jd_head_occupational_safety.md`, `JD-BIOT-HEAD-001`): квалификационные цензы, сертификация, право выдачи обязательных предписаний и приостановки работ при угрозе жизни, персональная ответственность по ст. 93, 96 КоАП РК и ст. 156 УК РК | Local Git Repo | `VERIFIED` | [`jd_head_occupational_safety.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_head_occupational_safety.md) |
| **E3** | AC-3 | Разработано самостоятельное Положение об Отделе Гражданской обороны и чрезвычайных ситуаций (`civil_defense_and_emergency_regulation.md`, `REG-GO-001`): рабочий орган Начальника ГО объекта (Ректора, ст. 18 Закона РК № 188-V), ведение ГО по Приказу МЧС РК № 268, План ГО, содержание укрытий (ПРУ), формирование невоенизированных формирований ГО, надзор за пожарной безопасностью по Приказу МЧС № 55 | Local Git Repo | `VERIFIED` | [`civil_defense_and_emergency_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/civil_defense_and_emergency_regulation.md) |
| **E4** | AC-4 | Разработана Должностная инструкция Начальника Отдела ГО и ЧС (`jd_head_civil_defense_and_emergency.md`, `JD-GO-HEAD-001`): функции начальника штаба ГО объекта, взаимодействие с ДЧС, допуск к госсекретам (форма 3), ответственность по ст. 359, 410 КоАП РК | Local Git Repo | `VERIFIED` | [`jd_head_civil_defense_and_emergency.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_head_civil_defense_and_emergency.md) |
| **E5** | AC-5 | Актуализированы СОП эвакуационных тренировок (`sop_emergency_and_evacuation_drills.md`, `SOP-EMERG-EVAC-001`) и Каталог функций Домена 09 (`09_infrastructure_and_facilities.md`): гармонизировано институциональное разделение 4 структур (СБ, БиОТ, ГО и ЧС, Ситуационный центр) в единой RACI-матрице с ровно одним `Accountable` на процесс | Local Git Repo | `VERIFIED` | [`sop_emergency_and_evacuation_drills.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/sop_emergency_and_evacuation_drills.md), [`09_infrastructure_and_facilities.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/functions_and_powers/09_infrastructure_and_facilities.md) |
| **E6** | AC-6 | Проверка ripgrep: 0 маркеров TODO/TBD/FIXME, соблюдение системных макропеременных `[V_*]`, стандартов TFW v3.4.0 и полное соответствие критериям приемки | Local Ripgrep | `VERIFIED` | 4 новых файла VALUE + 2 модифицированных VALUE |
| **E-accounting** | Accounting | 4 новых файла VALUE + 2 модифицированных файла VALUE = 6 файлов VALUE; суммарный объем ~720 строк (норматив $\le 8$ новых файлов, $\le 1200$ строк соблюден с запасом) | Git working tree | `VERIFIED` | 6 VALUE files within budget |

---

## Verdict

Evidence verdict: **7/7 VERIFIED**, 0 DEFERRED, 0 BLOCKED, 0 N/A.
