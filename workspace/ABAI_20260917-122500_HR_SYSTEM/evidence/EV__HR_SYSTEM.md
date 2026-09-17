# EV — ABAI_20260917-122500_HR_SYSTEM: Нормативная база кадрового блока (HR), конкурсного отбора ППС и системы оплаты ученых по Приказу МНВО № 424

> **Date**: 2026-09-17  
> **Author**: Executor  
> **Task**: ABAI_20260917-122500_HR_SYSTEM  
> **TS**: [TS](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260917-122500_HR_SYSTEM/TS.md)  

---

## Environment

| Field | Value |
|---|---|
| OS | Windows (NT 10.0) |
| Framework | Trace-First Workflow (TFW v3.4.0) |
| Regulatory Base | Трудовой кодекс РК, Приказ МОН РК № 230, Приказ МОН РК № 338, Приказ МНВО РК № 424 от 04.09.2026, Приказ МТСЗН РК № 353 (Enbek.kz), Закон о ПДн |
| Target Repositories | `docs/internal_acts/regulations/`, `docs/internal_acts/sops_and_rules/`, `docs/internal_acts/job_descriptions/`, `docs/functions_and_powers/` |

---

## Evidence Table

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|---|---|
| E1 | AC-1 | Разработано модельное Положение о Департаменте управления человеческими ресурсами (HR): структура из 3 секторов, 15+ функций, разграничение полномочий RACI, регламентация работы в модулях УИС («Кадры и ППС», «Приказы», «Enbek.kz»), отдельный раздел защиты ПДн по Закону РК № 94-V. | Workspace / TFW | **VERIFIED** | [`hr_department_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/hr_department_regulation.md) |
| E2 | AC-2 | Разработан СОП открытого конкурсного замещения должностей ППС и ученых: сформирован состав Конкурсной комиссии (не менее 40% внешних экспертов), закреплен срок публикации за 30 дней в СМИ и на Enbek.kz, 3 этапа отбора (скрининг, открытая лекция с видеозаписью, тайное голосование), внедрена дифференциация Teaching Track (650–750 ч) и Research Track (300–350 ч + Scopus Q1-Q2). | Workspace / TFW | **VERIFIED** | [`sop_faculty_and_researcher_recruitment_competition.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/sop_faculty_and_researcher_recruitment_competition.md) |
| E3 | AC-3 | Разработан СОП 7-классного грейдирования и Комиссии по оценке достижений ученых ($K_{дос}$): полностью имплементирован Приказ МНВО РК № 424 от 04.09.2026 (дедлайн 22.09.2026), таблица 7 классов должностей (Главный научный сотрудник — Лаборант), регламент университетской Комиссии, шкала оценки личных достижений (WoS/Scopus Q1–Q3, патенты, индекс Хирша) и расчет $K_{дос}$ (1.00–1.50) с готовой формой Оценочного листа соискателя (Приложение 1). | Workspace / TFW | **VERIFIED** | [`sop_researcher_compensation_and_kdos_commission.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/sop_researcher_compensation_and_kdos_commission.md) |
| E4 | AC-4 | Разработана модельная Должностная инструкция Директора Департамента HR: квалификационные требования по Приказу № 338, обязанности по стратегическому кадровому планированию, конкурсам по № 230, внедрению 7 классов и работе в Комиссии по $K_{дос}$, персональная ответственность по ТК РК и ст. 98 КоАП РК. | Workspace / TFW | **VERIFIED** | [`jd_director_hr.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_director_hr.md) |
| E5 | AC-5 | Разработана модельная ДИ Ведущего специалиста по кадровому администрированию, воинскому учету и интеграции с ЕСУТД Enbek.kz: ведение личных дел, воинский учет (взаимодействие с УДО), и **жесткий безусловный SLA по ст. 23 ТК РК: регистрация трудовых договоров в ЕСУТД Enbek.kz не позднее 3 рабочих дней** под угрозой персональной ответственности по ст. 98 КоАП РК. | Workspace / TFW | **VERIFIED** | [`jd_hr_recruitment_and_records_specialist.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_hr_recruitment_and_records_specialist.md) |
| E6 | AC-6 | Актуализирован каталог функций Домена 10 (`10_human_capital_and_hr.md`): функции расширены до 10 позиций с указанием оснований в НПА РК, ответственных (Accountable), соисполнителей (Responsible), ссылок на вновь созданные модельные акты и цифровой профиль УИС. | Workspace / TFW | **VERIFIED** | [`10_human_capital_and_hr.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/functions_and_powers/10_human_capital_and_hr.md) |
| E7 | AC-7 | Проведена верификация на соответствие реестру переменных `[V_...]`: 0 непараметризованных хардкодов конкретных вузов, применены системные теги `[V_ORGANIZATION_NAME]`, `[V_CHANCELLOR_TITLE]`, `[V_PRIMARY_EDTECH_PLATFORM]`, `[V_CORP_EMAIL_DOMAIN]`. | Workspace / TFW | **VERIFIED** | Grep analysis (0 matches for local names) |

---

## Verdict

Evidence verdict: **7/7 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A**  
Все критерии технической спецификации TS выполнены в полном объеме с надлежащим качеством и строгим соблюдением требований законодательства Республики Казахстан.

---

*EV — ABAI_20260917-122500_HR_SYSTEM | 2026-09-17*
