# RF — ABAI_20260917-123500_IS_RETROFIT / Phase B: Сквозная интеграция требований УИС и SLA в научный блок, качество, комплаенс и стратегию

> **Date**: 2026-09-17  
> **Author**: Executor  
> **Status**: 🟢 RF — Complete  
> **Parent HL**: [HL](HL.md)  
> **TS**: [TS_PHASE_B](TS_PHASE_B.md)  

---

## 1. What Was Done

### Actual Value-Bearing Accounting

| Fact | Actual result |
|---|---|
| TS approval ref | `TS-ABAI_20260917-123500_IS_RETROFIT` (Phase B approved 2026-09-17) |
| Candidate | `v2.3-IS-RETROFIT-PHASE-B` |
| VALUE membership | 12 модернизированных внутренних актов контура науки, качества, комплаенса и стратегии |
| Arithmetic | 0 new files, 12 modified files, ~710 touched LOC |
| Membership deviations | None (все 12 целевых файлов обновлены в строгом соответствии со скоупом) |
| Trigger disposition | Terminal complete for Phase B |
| Authority and timing | Approved Coordinator / Owner 2026-09-17 |
| Reproduction | Verified against Трудовой кодекс РК (ст. 22, 23, 52, 120), Закон о науке и технологической политике РК 2024 г., Закон о противодействии коррупции РК, СТ РК 34.015-2002, ТЗ ГТС |

### Modified Files (12 файлов Phase B)

| File | Changes Made |
|---|---|
| [`docs/internal_acts/regulations/science_department_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/science_department_regulation.md) | Добавлен раздел 8 «Регламентация деятельности в УИС»: закреплены модули «Наука и НИОКР», «Диссертационные советы», «Антиплагиат», роли RBAC (`Science_SuperAdmin`, `Science_Grant_Manager`, `Dissertation_Secretary`), сроки SLA (3 дня на регистрацию тем, 5 дней на верификацию публикаций, 30 дней на публикацию диссертационных дел) и санкции по ст. 22, 23, 52 ТК РК. |
| [`docs/internal_acts/regulations/commercialization_office_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/commercialization_office_regulation.md) | Добавлен раздел 8 «Регламентация деятельности в УИС»: закреплен модуль «Коммерциализация и Стартапы», роли RBAC (`Commercialization_Manager`, `IP_Specialist`, `Startup_Tracker`), SLA (2 дня на служебный РИД, 3 дня на патенты, 5 дней на лицензии), запрет финансирования стартапов вне УИС, материальная ответственность по ст. 120 ТК РК. |
| [`docs/internal_acts/regulations/compliance_service_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/compliance_service_regulation.md) | Добавлен раздел 8 «Регламентация деятельности в УИС»: модуль «Комплаенс и Антикоррупция», независимая роль `Compliance_Auditor` с доступом к неизменяемым логам Audit Trail, 24 ч SLA на регистрацию инцидентов Whistleblowing, 3 рабочих дня на экспертизу ВНД в СЭД, немедленное расторжение договора по п. 1 ст. 52 ТК РК за раскрытие заявителя. |
| [`docs/internal_acts/regulations/quality_assurance_committee_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/quality_assurance_committee_regulation.md) | Добавлен раздел 7 «Регламентация деятельности в УИС»: модули «Качество образования и EdTech» и «Силлабусы», роль `QA_Auditor`, аудит силлабусов за 5 дней до семестра, 7 дней на аналитику опросов «Преподаватель глазами студентов», абсолютный запрет ручной манипуляции результатами опросов. |
| [`docs/internal_acts/regulations/accreditation_center_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/accreditation_center_regulation.md) | Добавлен раздел 8 «Регламентация деятельности в УИС»: модули «Аккредитация и Рейтинги», роль `Accreditation_Analyst`, 15 дней SLA на формирование сводного профиля ОП для SER, ежемесячная сверка с ЕПВО до 5 числа, 3 дня на внесение сертификатов, ответственность по ст. 52 ТК РК за искажение аккредитационных данных. |
| [`docs/internal_acts/regulations/strategic_development_department_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/strategic_development_department_regulation.md) | Добавлен раздел 8 «Регламентация деятельности в УИС»: модуль «Стратегия и OKR» и подсистема BI/Dashboard, роли `Strategy_Director` и `Strategy_Analyst`, дедлайн до 10 числа месяца на сбор 25 KPI, первые 5 дней квартала на фиксацию OKR, 5 дней на скоринг (0.0–1.0), запрет ручных корректировок утвержденных значений. |
| [`docs/internal_acts/job_descriptions/jd_director_science.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_director_science.md) | Закреплены цифровые обязанности в УИС (п. 3.8): роль `Science_SuperAdmin`, 3 дня на открытие карточек грантов, контроль 5-дневного SLA верификации публикаций, 100% антиплагиат-аудит диссертаций, санкции по ст. 22, 23, 52 (п. 1 пп. 16), 120 ТК РК (п. 5.4–5.6). |
| [`docs/internal_acts/job_descriptions/jd_head_commercialization.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_head_commercialization.md) | Закреплены цифровые обязанности в УИС (п. 3.8): роль `Commercialization_Manager`, внесение патентов в течение 3 дней, лицензионных договоров в течение 5 дней, ведение Startup Track (TRL 1–9), материальная ответственность за разглашение коммерческой тайны по ст. 120 ТК РК (п. 5.4–5.6). |
| [`docs/internal_acts/job_descriptions/jd_compliance_officer.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_compliance_officer.md) | Закреплены цифровые обязанности в УИС (п. 3.9, 4.1): роль `Compliance_Auditor`, 24 ч SLA на регистрацию обращений Whistleblowing, 3 дня на визирование ВНД в СЭД, аудит Audit Trail оценок и контингента, расторжение договора по п. 1 ст. 52 ТК РК за разглашение заявителя (п. 5.5–5.6). |
| [`docs/internal_acts/job_descriptions/jd_head_accreditation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_head_accreditation.md) | Закреплены цифровые обязанности в УИС (п. 3.8): роль `Accreditation_Analyst`, 15 дней на выгрузку цифрового профиля ОП для SER, ежемесячная сверка с базой ЕПВО до 5 числа, 3 дня на внесение сертификатов аккредитации, ответственность по ст. 52 ТК РК за искажение сведений (п. 5.4–5.6). |
| [`docs/internal_acts/job_descriptions/jd_researcher_model.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_researcher_model.md) | Закреплены цифровые обязанности исследователя (п. 3.9): роль `Researcher`, актуализация профилей ORCID/Scopus ID/WoS ResearcherID, жесткий **5-дневный SLA** на внесение публикаций в модуль «Наука» с DOI, запрет «хищнических» изданий, увольнение по пп. 16) п. 1 ст. 52 ТК РК за повторный срыв дедлайна или передачу паролей (п. 5.5–5.7). |
| [`docs/internal_acts/job_descriptions/jd_director_strategic_development.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_director_strategic_development.md) | Закреплены цифровые обязанности в УИС (п. 3.11): роль `Strategy_Director`, 10 число на сбор факта 25 KPI, 5 дней на фиксацию OKR и 5 дней на скоринг (0.0–1.0), запрет несанкционированных ручных правок, увольнение по ст. 52 ТК РК за искажение данных (п. 5.7–5.9). |

---

## 2. Key Decisions & Structural Alignment

1. **Юридическая ответственность за научную и институциональную дезинформацию:** Внедрена прямая ответственность исследователей и руководства за фальсификацию научных отчетов, манипуляцию показателями остепененности и публикаций. Применение пп. 16 п. 1 ст. 52 ТК РК закрывает практику уклонения от ответственности при подаче недостоверных данных в МНВО РК, КОКСНВО и НЦГНТЭ.
2. **Антикоррупционная независимость:** Комплаенс-офицер наделен независимой цифровой ролью `Compliance_Auditor` с прямым правом чтения транзакционных логов (Audit Trail) без возможности блокировки со стороны ректората.
3. **Бесшовный сбор данных для аккредитации и рейтингов:** Исключен ручной сбор справок с кафедр: Центр аккредитации и Департамент стратегического развития формируют отчеты исключительно на базе первичных электронных данных УИС.

---

## 3. Verification & Evidence

Все критерии приемки AC-1 — AC-6 подтверждены в артефакте доказательств [`workspace/ABAI_20260917-123500_IS_RETROFIT/evidence/EV__IS_RETROFIT_PHASE_B.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260917-123500_IS_RETROFIT/evidence/EV__IS_RETROFIT_PHASE_B.md). Вердикт: **6/6 VERIFIED**.
