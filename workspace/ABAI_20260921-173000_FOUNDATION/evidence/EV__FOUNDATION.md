# EV — ABAI_20260921-173000_FOUNDATION: Институциональная и нормативная модель Факультета довузовской подготовки и Центра Foundation

> **Date**: 2026-09-21  
> **Author**: Executor / AI Normalization Specialist  
> **Task**: ABAI-21 (`ABAI_20260921-173000_FOUNDATION`)  
> **TS**: [TS Foundation](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260921-173000_FOUNDATION/TS.md)  

---

## Environment

| Field | Value |
|---|---|
| OS | Windows 11 Pro (10.0.26100) |
| Language / Runtime | Markdown / Python 3.11 |
| Deploy target | `docs/regulations/` & `docs/internal_acts/` |
| CI / Pipeline | Local verification |

---

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|:---:|---|
| E1 | AC-1 | Внешний реестр `external_npa_registry.md` расширен до 117 актов (+Приказ МОН № 554, +Приказ МОН № 122), Модуль `01_academic_and_educational_npa.md` дополнен пунктами 1.9, 1.10 и маппингом ВНД | Local filesystem | `VERIFIED` | [`external_npa_registry.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/regulations/external_npa_registry.md) |
| E2 | AC-2 | Специальный отраслевой стандарт `rk_foundation_and_kandastar_rules.md` (`STD-RK-FOUND-001`): регламентированы нормы квот кандасов, 30–36 ч/нед нагрузки, режим виз C9, комплексные экзамены и свидетельства | Local filesystem | `VERIFIED` | [`rk_foundation_and_kandastar_rules.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/regulations/rk_foundation_and_kandastar_rules.md) |
| E3 | AC-3 | Положение о Факультете довузовской подготовки / Центре Foundation (`foundation_department_regulation.md`): утверждена структура из 4 секторов (кандасы, иностранцы, ЕНТ, тьюторы), задачи, SLA с ДАВ/ДМС/Бухгалтерией, роли в УИС | Local filesystem | `VERIFIED` | [`foundation_department_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/foundation_department_regulation.md) |
| E4 | AC-4 | Правила учебного процесса на подготовительном отделении (`rules_foundation_academic_process.md`): закреплен правовой статус «слушатель» (тыңдаушы), календарь (1 окт — 30 июня), стипендии по ПП № 116, комплексный экзамен, основания отчисления | Local filesystem | `VERIFIED` | [`rules_foundation_academic_process.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/rules_foundation_academic_process.md) |
| E5 | AC-5 | Комплект должностных инструкций в `docs/internal_acts/job_descriptions/`: разработаны ДИ Руководителя/Декана (`jd_foundation_dean.md`), ДИ Методиста-координатора (`jd_foundation_coordinator.md`), ДИ Старшего тьютора (`jd_foundation_tutor.md`) | Local filesystem | `VERIFIED` | [`jd_foundation_dean.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_foundation_dean.md) |
| E6 | AC-6 | Чистота и параметризация: проверка ripgrep подтвердила 0 совпадений маркеров `[TODO]` и `[TBD]`, параметры вуза `[V_*]` применены корректно | Ripgrep | `VERIFIED` | 0 совпадений TODO/TBD |

---

## Verdict

Evidence verdict: **6/6 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A**

---

*EV — ABAI_20260921-173000_FOUNDATION | 2026-09-21*
