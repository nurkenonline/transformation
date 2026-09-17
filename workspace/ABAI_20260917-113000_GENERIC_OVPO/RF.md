# RF — ABAI_20260917-113000_GENERIC_OVPO: Универсализация модели ОВПО РК и цифровая интеграция

> **Date**: 2026-09-17  
> **Author**: Executor  
> **Status**: 🟢 RF — Complete  
> **Parent HL**: [HL](HL.md)  
> **TS**: [TS](TS.md)  

---

## 1. What Was Done

### Actual Value-Bearing Accounting

| Fact | Actual result |
|---|---|
| TS approval ref | `TS-ABAI_20260917-113000_GENERIC_OVPO` |
| Baseline / Candidate | `v1.10-STUD-SOC` / `v2.0-GENERIC-OVPO` |
| VALUE membership | 3 руководства/реестра универсализации, 3 документа цифрового профиля, 1 скрипт параметризации, тотальное обезличивание существующих фондов |
| Arithmetic | 7 new value-bearing files, 60 modified files, ~2600 LOC |
| Membership deviations | None |
| Trigger disposition | Terminal complete |
| Authority and timing | Approved Coordinator / Owner 2026-09-17 |
| Reproduction | Verified against Закон об образовании, Трудовой кодекс РК, СТ РК 34.015-2002, ТЗ ГТС |

### New Files

| File | Description |
|---|---|
| `docs/generic_framework/00_framework_adaptation_guide.md` | Руководство по адаптации универсального фреймворка для ОВПО разных форм собственности (НАО, АО, ТОО, РГП) |
| `docs/generic_framework/01_variable_registry_and_placeholders.md` | Реестр системных переменных (`[V_...]`), правила синтаксиса и чеклист линтинга |
| `docs/generic_framework/02_reference_cases_architecture.md` | Архитектура позиционирования эталонных кейсов (Abai University и AITU) для тиражирования |
| `docs/generic_framework/digital/01_university_is_reference_blueprint.md` | Эталонный функционально-технический профиль УИС (SIS Blueprint): 22 модуля, 4 класс ИБ, 5 государственных интеграций |
| `docs/generic_framework/digital/02_digital_to_job_integration_matrix.md` | Матрица сквозной интеграции ИС в ДИ и Положения: сроки (SLA), роли RBAC, ст. 22, 23, 52 ТК РК |
| `docs/generic_framework/digital/03_sop_digital_governance_and_sla.md` | Общеуниверситетский регламент (СОП) цифрового взаимодействия, неизменяемости ведомостей и защиты ПДн |
| `scripts/depersonalize_all.py` | Скрипт автоматизированной параметризации и подстановки реквизитов ОВПО |

### Modified Files

| File | Changes |
|---|---|
| `docs/regulations/*.md` (11 файлов) | Обезличивание текстов внешних регуляторных модулей и сводного реестра 91+ НПА |
| `docs/internal_acts/**/*.md` (47 файлов) | Тотальная замена локальных названий на системные переменные `[V_...]` в Положениях, ДИ, СОПах |
| `docs/internal_acts/README.md` | Включение нового раздела Универсального тиражируемого фреймворка ОВПО РК |
| `README.md` | Нейтрализация наименования проекта (*Kazakhstan University Transformation Framework*) |
| `AGENTS.md` | Нейтрализация формулировки миссии агента в проекте |
| `.tfw/project_config.yaml` | Актуализация имени и описания проекта в конфигурации TFW |

---

## 2. Key Decisions

1. **Полное обезличивание и параметризация:** Все локальные акты отвязаны от единичного наименования вуза через систему стандартизированных тегов `[V_...]`.
2. **Трансформация ТЗ цифровой платформы в отраслевой стандарт:** Технические требования для ГТС по 22 модулям обобщены в виде эталонного профиля УИС, который обязателен для эффективного функционирования любого университета РК.
3. **Прямая прошивка ИТ-обязанностей в трудовые отношения:** Работа в системе формализована как прямая трудовая обязанность по Трудовому кодексу РК с конкретными дедлайнами (48 часов на текущие оценки, 24 часа на ведомость, день-в-день на приказы) и юридической ответственностью за срыв сроков или передачу паролей.
4. **Сохранение практической ценности локальных актов Abai University:** Исторические документы КазНПУ имени Абая и Astana IT University не аннулированы, а позиционированы как реальные боевые бенчмарки (Reference Implementations).
5. **Тотальная очистка существующего фонда документации:** 58 файлов в `docs/regulations/` и `docs/internal_acts/` автоматизированно обработаны и подготовлены к моментальному внедрению в любом вузе РК.

---

## 3. Acceptance Criteria Verification

- [x] **AC-1:** Руководство по адаптации фреймворка разработано и описывает специфику НАО, АО, ТОО и РГП (`00_framework_adaptation_guide.md`).
- [x] **AC-2:** Реестр системных переменных и плейсхолдеров сформирован по 4 категориям (`01_variable_registry_and_placeholders.md`).
- [x] **AC-3:** Эталонный функционально-технический профиль УИС (22 модуля) разработан на базе ТЗ ГТС (`01_university_is_reference_blueprint.md`).
- [x] **AC-4:** Матрица сквозной интеграции связывает каждый модуль с ДИ, сроками (SLA) и нормами ТК РК (`02_digital_to_job_integration_matrix.md`).
- [x] **AC-5:** Регламент цифрового взаимодействия и обеспечения достоверности данных регламентирует аудит, апелляции и ПДн (`03_sop_digital_governance_and_sla.md`).
- [x] **AC-6:** Наработки Abai University и AITU оформлены как Reference Blueprints с матрицей выбора траектории (`02_reference_cases_architecture.md`).
- [x] **AC-7:** Тотальное обезличивание 58 файлов и нейтрализация названия проекта проведены и проверены (`scripts/depersonalize_all.py`).

---

*RF — ABAI_20260917-113000_GENERIC_OVPO | 2026-09-17*
