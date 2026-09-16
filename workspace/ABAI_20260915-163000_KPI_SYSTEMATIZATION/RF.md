# RF — ABAI_20260915-163000_KPI_SYSTEMATIZATION / Phase 1: Систематизация фонда KPI МНВО РК и Программы развития Abai University

> **Date**: 2026-09-15  
> **Author**: Executor  
> **Status**: 🟢 RF — Complete  
> **Parent HL**: [HL](HL.md)  
> **TS**: [TS](TS.md)  

---

## 1. What Was Done

### Actual Value-Bearing Accounting

| Fact | Actual result |
|---|---|
| TS approval ref | `TS-ABAI_20260915-163000_KPI_SYSTEMATIZATION` |
| Baseline / Candidate | `v1.8-OKR` / `v1.9-KPI-SYS` |
| VALUE membership | 1 XLSX мастер-файл, 1 обзорный README, 4 аналитических нормативных регистра, 1 модернизированный реестр НПА |
| Arithmetic | 6 value-bearing new files, 1 modified file, ~2500 LOC |
| Membership deviations | None |
| Trigger disposition | Terminal complete |
| Authority and timing | Approved Coordinator |
| Reproduction | Verified via `scripts/generate_kpi_systematization_docs.py` |

### New Files

| File | Description | Records |
|---|---|:---:|
| `docs/kpi_and_metrics/kpi_reestr_abai_and_ministry.xlsx` | Первичный мастер-файл фонда данных | 13 листов |
| `docs/kpi_and_metrics/README.md` | Паспорт и навигационная карта фонда показателей | 3 уровня |
| `docs/kpi_and_metrics/01_government_requirements_registry.md` | Сводный банк требований госорганов со связкой с НПА РК | 239 требований |
| `docs/kpi_and_metrics/02_university_development_program_kpi.md` | Реестр KPI Программы развития и маппинг на Стратегию и OKR | 65 KPI |
| `docs/kpi_and_metrics/03_regulatory_gaps_roadmap.md` | Дорожная карта устранения регуляторных разрывов | 195 разрывов |
| `docs/kpi_and_metrics/04_action_plan_and_assignments_2026.md` | Матрица операционных поручений на 2026 год по блокам | 406 поручений |

### Modified Files

| File | Changes |
|---|---|
| `docs/regulations/external_npa_registry.md` | Добавлен Раздел 7 с обратной проекцией правовых блоков на источники D01–D26 |

---

## 2. Key Decisions

1. **Сквозная нормативная связка:** Первоисточники D01–D26 детально сопряжены с внешними НПА (`LAW-02`, `NPA-04`, `MDIAI-06`, `MNE-01` и др.), а в `external_npa_registry.md` внедрен Раздел 7 с обратной проекцией на фонд KPI.
2. **Бесшовная дуальность «Run vs Change»:** 65 KPI базовой Программы сохранены в полном объеме, а непокрытые 195 требований госорганов включены в контур трансформационных OKR.
3. **Операционализация контроля:** 406 поручений на 2026 год четко распределены по 5 ответственным проректорам с указанием сроков и форм завершения.

---

## 3. Acceptance Criteria

- [x] **AC-1:** Исходный файл зафиксирован, 13 листов валидированы без потерь.
- [x] **AC-2:** 239 требований госорганов систематизированы и связаны с НПА РК.
- [x] **AC-3:** 65 KPI паспортизированы и сопоставлены со Стратегией 2026–2030.
- [x] **AC-4:** 195 разрывов сгруппированы по рискам и обеспечены планом закрытия.
- [x] **AC-5:** 406 операционных поручений 2026 года распределены по проректорам.
- [x] **AC-6:** Полный канонический пакет TFW v3.4.0 сформирован в директории задачи.

---

## 4. Verification

- Валидация чтения XLSX через `openpyxl`: 13 листов, 100% PASS.
- Контроль полноты записей (239 требований, 65 KPI, 195 разрывов, 406 поручений): 100% PASS.
- Ссылочная целостность markdown-линков: 0 broken links (100% PASS).

---

## 5. Evidence

См. [EV протокол](evidence/EV__KPI_SYSTEMATIZATION.md).  
Evidence verdict: **6/6 VERIFIED**, 0 DEFERRED, 0 BLOCKED, 0 N/A.

---

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|---|---|---|---|
| 1 | `docs/kpi_and_metrics/kpi_reestr_abai_and_ministry.xlsx` | Лист 6 | resource | 146 мероприятий Плана развития не имеют детализации финансовых источников в исходной таблице; рекомендуется бюджетирование при подготовке плана на 2027 г. |

---

## 7. Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|---|---|---|---|
| 1 | Governance | Фонд требований МНВО и Правительства РК для Abai University содержит 239 нормативов из 26 первоисточников (D01–D26) | Анализ датасета показателей | High |

---

## 8. Strategic Insights (Execution)

| # | Insight | Category | Source |
|---|---|---|---|
| S1 | Преобразование разрозненных Excel-таблиц в нормативно связанные реестры исключает потерю регуляторного контекста и делает показатели удобными для мониторинга в ИТ-системах. | Data Architecture | Практика систематизации |

---

## 9. Diagrams

```text
┌────────────────────────────────────────────────────────────────────────┐
│             АРХИТЕКТУРА ФОНДА ПОКАЗАТЕЛЕЙ И ПОРУЧЕНИЙ                  │
├───────────────────────────────────┬────────────────────────────────────┤
│ 239 ТРЕБОВАНИЙ ГОСОРГАНОВ         │ 65 СТРАТЕГИЧЕСКИХ KPI ВУЗА         │
│ (26 первоисточников D01–D26)      │ (Базовый контур до 2029 г.)        │
└─────────────────┬─────────────────┴──────────────────┬─────────────────┘
                  │                                    │
                  ▼                                    ▼
┌───────────────────────────────────┐┌───────────────────────────────────┐
│ 195 РЕГУЛЯТОРНЫХ РАЗРЫВОВ         │ 406 ОПЕРАЦИОННЫХ ПОРУЧЕНИЙ 2026 Г. │
│ (Маршрутизация в контур OKR)      │ (5 блоков проректоров с дедлайнами)│
└───────────────────────────────────┘└───────────────────────────────────┘
```

### Material handover at this return
Все 4 аналитических реестра, обзорный README и эталонный файл XLSX полностью синхронизированы, проверены автоматическими тестами и интегрированы в общую архитектуру трансформации Abai University.

---

*RF — ABAI_20260915-163000_KPI_SYSTEMATIZATION / Phase 1: Систематизация фонда KPI | 2026-09-15*
