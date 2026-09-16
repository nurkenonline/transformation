# TS — ABAI_20260915-163000_KPI_SYSTEMATIZATION / Phase 1: Систематизация фонда KPI МНВО РК и Программы развития Abai University

> **Date**: 2026-09-15  
> **Author**: Coordinator  
> **Status**: 🟢 APPROVED  
> **Parent HL**: [HL](HL.md)  

---

## 1. Objective
Осуществить нормативно-методологическую обработку и систематизацию первичного массива данных из таблицы `kpi_reestr_abai_and_ministry.xlsx` (13 листов, 400 КБ). Сформировать 4 структурированных регистра в `docs/kpi_and_metrics/`, связать внешние требования госорганов со Сводным реестром НПА РК (`external_npa_registry.md`), декомпозировать 65 KPI действующей Программы развития до 2029 г. с маппингом на 25 KPI Стратегии 2026–2030 и OKR, сформировать дорожную карту устранения 195 разрывов и бэклог 406 поручений 2026 года.

---

## 2. Scope

### In Scope
- Размещение и фиксация эталонного файла: `docs/kpi_and_metrics/kpi_reestr_abai_and_ministry.xlsx`.
- Создание навигационного обзора: `docs/kpi_and_metrics/README.md`.
- Формирование 4 нормативных регистров:
  - `docs/kpi_and_metrics/01_government_requirements_registry.md`
  - `docs/kpi_and_metrics/02_university_development_program_kpi.md`
  - `docs/kpi_and_metrics/03_regulatory_gaps_roadmap.md`
  - `docs/kpi_and_metrics/04_action_plan_and_assignments_2026.md`
- Сквозное сопряжение первоисточников D01–D26 со Сводным реестром НПА РК (`docs/regulations/external_npa_registry.md`).
- Контур TFW v3.4.0: `workspace/ABAI_20260915-163000_KPI_SYSTEMATIZATION/` (`HL.md`, `TS.md`, `ONB.md`, `RF.md`, `evidence/EV__KPI_SYSTEMATIZATION.md`, `review/`).

### Out of Scope
- Аудит первичных бухгалтерских проводок за 2025 год.
- Изменение утвержденных значений плана финансирования в бюджете вуза.

---

## 3. Principles Check

| # | HL §7 principle | Enforced by | Gate |
|---|---|---|---|
| P1 | Trace-First (связь с НПА) | AC-2 | Сквозная привязка D01–D26 к `external_npa_registry.md` |
| P2 | Целостность данных реестра | AC-1, AC-3, AC-5 | Сверка контрольных сумм записей: 239, 65, 195, 406 |
| P3 | Гармонизация «Run vs Change» | AC-3, AC-4 | Маппинг 65 KPI на 25 стратегических KPI и OKR 1 уровня |

---

## 4. Affected Files and Value-Bearing Accounting

| File / selector | Action | Class | Semantic reason / required result |
|---|---|---|---|
| `docs/kpi_and_metrics/kpi_reestr_abai_and_ministry.xlsx` | CREATE | `VALUE` | Эталонный исходный XLSX-реестр |
| `docs/kpi_and_metrics/README.md` | CREATE | `VALUE` | Навигационный паспорт фонда показателей |
| `docs/kpi_and_metrics/01_government_requirements_registry.md` | CREATE | `VALUE` | 239 требований госорганов с привязкой к НПА РК |
| `docs/kpi_and_metrics/02_university_development_program_kpi.md` | CREATE | `VALUE` | 65 KPI Программы развития и маппинг на OKR |
| `docs/kpi_and_metrics/03_regulatory_gaps_roadmap.md` | CREATE | `VALUE` | Дорожная карта закрытия 195 разрывов |
| `docs/kpi_and_metrics/04_action_plan_and_assignments_2026.md` | CREATE | `VALUE` | Бэклог 406 поручений на 2026 год |
| `docs/regulations/external_npa_registry.md` | MODIFY | `VALUE` | Раздел 7: сопряжение с банком D01–D26 |
| `workspace/ABAI_20260915-163000_KPI_SYSTEMATIZATION/ONB.md` | CREATE | `TRACE` | Аналитический онбординг исполнителя |
| `workspace/ABAI_20260915-163000_KPI_SYSTEMATIZATION/evidence/EV__KPI_SYSTEMATIZATION.md` | CREATE | `ASSURANCE` | Протокол проверки Acceptance Criteria |
| `workspace/ABAI_20260915-163000_KPI_SYSTEMATIZATION/RF.md` | CREATE | `TRACE` | Итоговый результирующий отчет исполнителя |
| `workspace/ABAI_20260915-163000_KPI_SYSTEMATIZATION/review/REVIEW.md` | CREATE | `ASSURANCE` | Экспертное заключение и вердикт ревьюера |

### Prospective accounting contract

| Fact | Approved value |
|---|---|
| Subject / exact VALUE selector | Реестры в `docs/kpi_and_metrics/` и Раздел 7 в `docs/regulations/external_npa_registry.md` |
| Baseline / selector source | `v1.8-OKR` |
| Candidate rule | Редакция файлов, подтвержденная скриптом `scripts/generate_kpi_systematization_docs.py` и `EV__KPI_SYSTEMATIZATION.md` |
| Logical VALUE files | 6 новых, 1 модифицированный |
| Touched text LOC | ~2500 строк |
| Triggers / disposition | Завершение систематизации внешних требований госорганов |
| Multiplier / authority | Coordinator / TFW v3.4.0 |
| Approval epoch / failure | 2026-09-15 / BLOCKED при расхождениях сумм записей |

### Prospective scope rulings
Механическое редактирование исходного XLSX файла запрещено; все преобразования осуществляются через воспроизводимый скрипт `scripts/generate_kpi_systematization_docs.py`.

### Task-local hard constraints
| M1 consequence | M2 object/risk | M3 measure/selector | M4 pre-act check | M5 softer-control gap | M6 change authority |
|---|---|---|---|---|---|
| Потеря нормативных индикаторов | Полнота 239 требований | Сверка счетчика записей | Автоматический скрипт | Риск лицензионных штрафов | Reviewer |
| Искажение плановых цифр | 65 целевых KPI | Сверка контрольных сумм | Построчная сверка таблиц | Риск недостоверности отчета СД | Coordinator |

---

## 5. Acceptance Criteria

### AC-1: Техническая фиксация и целостность мастер-файла
Исходный файл таблицы зафиксирован в `docs/kpi_and_metrics/kpi_reestr_abai_and_ministry.xlsx`. Все 13 листов успешно прочитаны и валидированы без искажений.
- [x] Файл зафиксирован, 13 листов прочитаны.
Gate: `python -c "import openpyxl; wb=openpyxl.load_workbook('docs/kpi_and_metrics/kpi_reestr_abai_and_ministry.xlsx'); assert len(wb.sheetnames)==13"`
Evidence: VERIFIED в `EV__KPI_SYSTEMATIZATION.md`

### AC-2: Сводный реестр требований госорганов (239 записей)
Создан регистр `01_government_requirements_registry.md` с 239 требованиями. Все 26 источников (D01–D26) связаны с внешними НПА РК (`external_npa_registry.md`).
- [x] 239 требований систематизированы по 8 направлениям, D01–D26 сопряжены с НПА.
Gate: Наличие 239 записей и таблицы со связями с НПА в `01_government_requirements_registry.md`
Evidence: VERIFIED в `EV__KPI_SYSTEMATIZATION.md`

### AC-3: Реестр 65 KPI Программы развития и сопоставление со Стратегией
Создан документ `02_university_development_program_kpi.md` с 65 показателями. Установлена связь с 25 стратегическими показателями и OKR.
- [x] 65 показателей структурированы с целевыми значениями до 2029 г.
Gate: Проверка полноты 65 показателей (PRG001–PRG065)
Evidence: VERIFIED в `EV__KPI_SYSTEMATIZATION.md`

### AC-4: Дорожная карта устранения 195 регуляторных разрывов
Создан документ `03_regulatory_gaps_roadmap.md` с кластеризацией 195 гэпов. Сформированы механизмы закрытия гэпов через OKR.
- [x] 195 разрывов сгруппированы по тематическим кластерам.
Gate: Проверка наличия 195 позиций в таблице разрывов
Evidence: VERIFIED в `EV__KPI_SYSTEMATIZATION.md`

### AC-5: Матрица операционных поручений на 2026 год (406 задач)
Создан документ `04_action_plan_and_assignments_2026.md` с 406 поручениями. Задачи структурированы по 5 блокам проректоров.
- [x] 406 поручений распределены по кураторам со сроками и формами завершения.
Gate: Проверка объема записей (406 поручений)
Evidence: VERIFIED в `EV__KPI_SYSTEMATIZATION.md`

### AC-6: Соответствие TFW v3.4.0 и контуру доказательств
Оформлен полный пакет TFW: `HL.md`, `TS.md`, `ONB.md`, `EV__KPI_SYSTEMATIZATION.md`, `RF.md`, `review/`. Разделы примечаний и связанных артефактов присутствуют во всех файлах.
- [x] Полный канонический комплект артефактов сформирован.
Gate: Проверка наличия и полноты файлов в `workspace/ABAI_20260915-163000_KPI_SYSTEMATIZATION/`
Evidence: VERIFIED в `EV__KPI_SYSTEMATIZATION.md`

### Evidence Artifacts

| File | Description |
|---|---|
| `evidence/EV__KPI_SYSTEMATIZATION.md` | Полный протокол верификации по критериям AC-1..AC-6 |

---

## 6. Technical Guidance
- Использовать воспроизводимый Python-генератор [`scripts/generate_kpi_systematization_docs.py`](../../scripts/generate_kpi_systematization_docs.py) для исключения человеческого фактора при форматировании больших массивов данных.
- Сохранять точные идентификаторы требований и формулировки индикаторов в соответствии с первоисточниками.

---

## 7. Definition of Failure
- ❌ Потеря строк или данных при экспорте из XLSX (несовпадение контрольных сумм 239/65/195/406).
- ❌ Отсутствие сквозной связи между D01–D26 и внешними НПА РК.
- ❌ Неполнота доказательств в `EV__KPI_SYSTEMATIZATION.md`.

---

## 8. Phase Risks

| Risk | Mitigation |
|---|---|
| Рассинхронизация данных при ручном редактировании Markdown-файлов | Все изменения производятся строго через скрипт генерации из мастер-файла XLSX |

---

## 9. Cross-Phase Modifications (multi-phase only)

| File | Also modified in | Coordination note |
|---|---|---|
| `docs/regulations/external_npa_registry.md` | ABAI-1 | Внедрен Раздел 7 для сопряжения со систематизированным банком KPI |

---

*TS — ABAI_20260915-163000_KPI_SYSTEMATIZATION / Phase 1: Систематизация фонда KPI | 2026-09-15*
