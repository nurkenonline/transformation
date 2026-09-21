# EV — ABAI_20260917-174500_CULTURE_NPA: Гармонизация ВНД по архивам, библиотеке и масс-медиа (Фаза B)

> **Date**: 2026-09-17  
> **Author**: Executor  
> **Task**: ABAI_20260917-174500_CULTURE_NPA (Phase B)  
> **TS**: [TS Phase B](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260917-174500_CULTURE_NPA/TS_PHASE_B.md)  

---

## Environment

| Field | Value |
|---|---|
| OS | Windows (NT 10.0) |
| Framework | Trace-First Workflow (TFW v3.4.0) |
| Legal / Standard Basis | Приказ и.о. МКИ РК № 566-НҚ от 29.12.2023 (Перечень со сроками хранения), Приказ МКС РК № 236 (СЭД и номенклатура), Приказ МКС РК № 134 (Ведомственные архивы), Приказ МКС РК № 153 (Библиотечные фонды), Закон РК «О масс-медиа» № 94-VIII от 19.06.2024, Закон РК «О культуре» № 207-III |

---

## Evidence Table

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|---|---|
| E1 | AC-1 | В Положение об Офисе регистратора (`registrar_regulation.md`) добавлен Раздел 9: закреплен **75-летний срок ведомственного архивного хранения** студенческих личных дел (ст. 466 Приказа № 566-НҚ), книг регистрации дипломов (ст. 471), протоколов ГАК (ст. 470), 5-летний срок ведомостей и порядок передачи в архив через 3 года по описям (Приказ № 134). | Workspace / TFW | **VERIFIED** | [`registrar_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/registrar_regulation.md) |
| E2 | AC-2 | В Положение о Департаменте HR (`hr_department_regulation.md`) добавлен Раздел 10: закреплен **75-летний срок хранения** личных дел работников ППС и сотрудников (ст. 440 Приказа № 566-НҚ), приказов по личному составу и трудовых договоров; установлен запрет уничтожения дел без согласования с ЭПК госархива. | Workspace / TFW | **VERIFIED** | [`hr_department_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/hr_department_regulation.md) |
| E3 | AC-3 | Институционализирована Научная библиотека: разработано Положение (`scientific_library_regulation.md`) и регламент (`sop_library_collection_and_writeoff.md`). Закреплен статус Библиотечного совета, критерии книгообеспеченности (Приказ МОН № 391), периодичность инвентаризации (5 лет) и списание устаревшей литературы по Приказу МКС РК № 153, а также обязательный бесплатный экземпляр по ст. 25 Закона «О культуре». | Workspace / TFW | **VERIFIED** | [`scientific_library_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/scientific_library_regulation.md), [`sop_library_collection_and_writeoff.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/sop_library_collection_and_writeoff.md) |
| E4 | AC-4 | Институционализирован Медиа-центр: разработано Положение (`media_center_regulation.md`) и регламент со СМИ (`sop_media_interaction_and_press_accreditation.md`). Отражен **новый Закон РК «О масс-медиа» от 19.06.2024 № 94-VIII**, закреплен обязательный регламентный срок ответа на запросы СМИ — **не позднее 5 рабочих дней** (со санкциями по ст. 456-1 КоАП РК), правила учета сетевых медиа по Приказу № 368-НҚ. | Workspace / TFW | **VERIFIED** | [`media_center_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/media_center_regulation.md), [`sop_media_interaction_and_press_accreditation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/sop_media_interaction_and_press_accreditation.md) |
| E5 | AC-5 | Проведена проверка на сохранение системных переменных `[V_...]` и отсутствие хардкодов/плейсхолдеров во всех 6 документах Фазы B. | Workspace / TFW | **VERIFIED** | Grep analysis (0 violations) |

---

## Verdict

Evidence verdict: **5/5 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A**  
Все критерии приемки Фазы B полностью верифицированы. Внутренние акты университета гармонизированы с законодательством МКИ РК.

---

*EV — ABAI_20260917-174500_CULTURE_NPA / Phase B | 2026-09-17*
