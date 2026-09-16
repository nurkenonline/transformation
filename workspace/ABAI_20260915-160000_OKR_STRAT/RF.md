# RF — ABAI_20260915-160000_OKR_STRAT / Phase 1: Внедрение методологии OKR в систему стратегического планирования

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
| TS approval ref | `TS-ABAI_20260915-160000_OKR_STRAT` |
| Baseline / Candidate | `v1.7-CYBER` / `v1.8-OKR` |
| VALUE membership | 1 новый регламент OKR, 4 модернизированных стратегических акта |
| Arithmetic | 1 new file, 4 modified files, ~1150 LOC changes |
| Membership deviations | None |
| Trigger disposition | Terminal complete |
| Authority and timing | Approved Coordinator |
| Reproduction | Verified against Приказ МНЭ № 56, СУР ОВПО № 166/116, Google/Doerr OKR Model |

### New Files

| File | Description |
|---|---|
| `docs/internal_acts/sops_and_rules/sop_okr_framework_and_scoring.md` | Регламент применения методологии OKR и скоринга результативности (8 разделов, формула 0.0–1.0, RACI) |

### Modified Files

| File | Changes |
|---|---|
| `docs/internal_acts/blueprints/abai_strategy_2026_2030_architecture.md` | Интеграция дуальной модели «Run (25 KPI) + Change (OKR)», 5 Общеуниверситетских OKR с 15 KR |
| `docs/internal_acts/sops_and_rules/sop_university_development_strategy.md` | Синхронизация общего регламента стратегии с 90-дневными квартальными спринтами OKR и RACI |
| `docs/internal_acts/regulations/strategic_development_department_regulation.md` | Закрепление за ДСР задач (п. 3.6) и функций (п. 4.4) Проектного офиса OKR (OKR PMO) |
| `docs/internal_acts/job_descriptions/jd_director_strategic_development.md` | Дополнение квалификационных требований (OKR Coach), обязанностей (п. 3.9–3.10) и ответственности Директора |

---

## 2. Key Decisions

1. **Дуальное стратегическое управление:** законодательно обязательный для НАО контур долгосрочных показателей KPI («Run») гармонично объединен с динамичными квартальными циклами трансформации OKR («Change»).
2. **5 Общеуниверситетских OKR 1-го уровня:** сформулированы качественные вдохновляющие Objectives и 15 измеримых Key Results по ключевым доменам (Педагогическое лидерство, Исследовательский университет, Цифровая среда/ИИ, Интернационализация, Устойчивость/ESG).
3. **Безопасная культура амбиций:** принята шкала скоринга 0.0–1.0 (Google/Doerr) с фиксацией коридора 0.6–0.7 как эталонного успеха Moonshot целей, исключающая карательную привязку к окладам.

---

## 3. Acceptance Criteria

- [x] **AC-1:** Разработан Регламент применения методологии OKR и скоринга результативности.
- [x] **AC-2:** Интегрированы Общеуниверситетские OKR 1-го уровня в Архитектурный паспорт Стратегии.
- [x] **AC-3:** Актуализирован Общий регламент разработки и мониторинга Стратегии.
- [x] **AC-4:** Закреплена роль OKR PMO за ДСР и обновлена ДИ Директора ДСР.
- [x] **AC-5:** Нулевой уровень плейсхолдеров и юридическая выверенность терминов.
- [x] **AC-6:** Полный комплект артефактов TFW v3.4.0 и соблюдение Scope Budget.

---

## 4. Verification

- Соответствие нормативной базе РК и международной методологии OKR: 100% PASS.
- Анализ матриц RACI (строго один Accountable на каждый процесс): 100% PASS.
- Аудит связности артефактов через разделы «Примечания и связанные артефакты»: 100% PASS.

---

## 5. Evidence

См. [EV протокол](evidence/EV__OKR_STRAT.md).  
Evidence verdict: **6/6 VERIFIED**, 0 DEFERRED, 0 BLOCKED, 0 N/A.

---

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|---|---|---|---|
| 1 | `docs/internal_acts/blueprints/abai_strategy_2026_2030_architecture.md` | — | enhancement | В дальнейшем целесообразно разработать отдельный интерфейс дашборда OKR в модуле Abai Digital |

---

## 7. Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|---|---|---|---|
| 1 | Methodology | Внедрение методологии OKR в казахстанском государственном вузе эффективно исключительно в дуальной связке с нормативными показателями СУР и Плана развития | Опыт адаптации ТК РК и закона об АО | High |

---

## 8. Strategic Insights (Execution)

| # | Insight | Category | Source |
|---|---|---|---|
| S1 | Разделение контуров «Run» (KPI, ответственность СД и Правления) и «Change» (OKR, амбиции кафедр и институтов) снимает конфликт между строгой государственной отчетностью и гибкостью академических инноваций. | Strategy | Практика реализации задачи |

---

## 9. Diagrams

```text
┌────────────────────────────────────────────────────────────────────────┐
│             КВАРТАЛЬНЫЙ РИТМ OKR НАО «КАЗНПУ ИМЕНИ АБАЯ»               │
├───────────────────┬───────────────────┬────────────────────────────────┤
│ НЕДЕЛЯ 1:         │ НЕДЕЛИ 2–11:      │ НЕДЕЛИ 12–13:                  │
│ OKR Planning      │ Weekly Check-in   │ Scoring & Retro                │
│ Постановка целей  │ 15-мин апдейты    │ Оценка 0.0–1.0                 │
│ и выравнивание    │ и снятие блокеров │ Анализ успехов и постановка Q+1│
└───────────────────┴───────────────────┴────────────────────────────────┘
```

### Material handover at this return
Все разработанные нормативные акты и дополнения к архитектурному паспорту стратегии полностью согласованы, не содержат плейсхолдеров, готовы к практическому рассмотрению Правлением университета и утверждению Советом директоров НАО.

---

*RF — ABAI_20260915-160000_OKR_STRAT / Phase 1: Внедрение методологии OKR | 2026-09-15*
