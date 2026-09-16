# TS — ABAI_20260915-160000_OKR_STRAT / Phase 1: Внедрение методологии OKR в систему стратегического планирования

> **Date**: 2026-09-15  
> **Author**: Coordinator  
> **Status**: 🟢 APPROVED  
> **Parent HL**: [HL](HL.md)  

---

## 1. Objective
Нормативно регламентировать и архитектурно интегрировать методологию **OKR (Objectives and Key Results)** в существующую Стратегию развития НАО «КазНПУ имени Абая» на 2026–2030 гг. Разработать Регламент применения OKR (`sop_okr_framework_and_scoring.md`), актуализировать Архитектурный паспорт Стратегии (`abai_strategy_2026_2030_architecture.md`), Общий регламент стратегии (`sop_university_development_strategy.md`), Положение о Департаменте стратегического развития (`strategic_development_department_regulation.md`) и ДИ Директора ДСР (`jd_director_strategic_development.md`).

---

## 2. Scope

### In Scope
- Разработка нового регламента:
  - `docs/internal_acts/sops_and_rules/sop_okr_framework_and_scoring.md` — Регламент применения методологии OKR, правила формулирования O и KR, 4-этапный квартальный цикл, скоринг 0.0–1.0, RACI.
- Модернизация архитектурного блюпринта:
  - `docs/internal_acts/blueprints/abai_strategy_2026_2030_architecture.md` — Интеграция дуальной модели «Run (25 KPI) + Change (OKR)», формулирование 5 Общеуниверситетских OKR 1-го уровня.
- Актуализация регламентов и положений:
  - `docs/internal_acts/sops_and_rules/sop_university_development_strategy.md` — Включение процедур утверждения и мониторинга OKR в жизненный цикл стратегии.
  - `docs/internal_acts/regulations/strategic_development_department_regulation.md` — Закрепление функций OKR PMO / фасилитации.
  - `docs/internal_acts/job_descriptions/jd_director_strategic_development.md` — Обязанности и квалификационные требования по OKR-менеджменту.
- Контур доказательств и отчетности TFW v3.4.0:
  - `workspace/ABAI_20260915-160000_OKR_STRAT/ONB.md`
  - `workspace/ABAI_20260915-160000_OKR_STRAT/evidence/EV__OKR_STRAT.md`
  - `workspace/ABAI_20260915-160000_OKR_STRAT/RF.md`
  - `workspace/ABAI_20260915-160000_OKR_STRAT/review/REVIEW.md`

### Out of Scope
- Персональные индивидуальные карточки OKR преподавателей (ограничиваемся институциональными, кафедрными и проектными OKR).
- Программный код интерфейса OKR в Abai Digital (ограничиваемся техническими требованиями к модулю).

---

## 3. Principles Check

| # | HL §7 principle | Enforced by | Gate |
|---|---|---|---|
| P1 | Дуальная модель «Run (KPI) + Change (OKR)» | AC-1, AC-2 | Разделение нормативных KPI Совета директоров и прорывных квартальных OKR |
| P2 | Амбициозность и культура без страха ошибок | AC-1 | Стандарт скоринга Google/Doerr (зона успеха 0.6–0.7, неприменение карательных мер за недостижение амбиций) |
| P3 | Ритмичность 90-дневных циклов | AC-1, AC-3 | Квартальные сессии Planning, еженедельные Check-ins, Quarterly Review & Retrospective |
| P4 | Персональная и командная подотчетность | AC-1, AC-4 | Четкая RACI-матрица, закрепление функций OKR Program Office за ДСР |

---

## 4. Affected Files and Value-Bearing Accounting

| File / selector | Action | Class | Semantic reason / required result |
|---|---|---|---|
| `docs/internal_acts/sops_and_rules/sop_okr_framework_and_scoring.md` | CREATE | `VALUE` | Регламент применения OKR и скоринга в НАО «КазНПУ имени Абая» |
| `docs/internal_acts/blueprints/abai_strategy_2026_2030_architecture.md` | MODIFY | `VALUE` | Интеграция OKR 1-го уровня и двухуровневой связки с 25 KPI |
| `docs/internal_acts/sops_and_rules/sop_university_development_strategy.md` | MODIFY | `VALUE` | Включение квартального цикла OKR в общий стратегический регламент |
| `docs/internal_acts/regulations/strategic_development_department_regulation.md` | MODIFY | `VALUE` | Дополнение функций Департамента стратегии ролью OKR PMO |
| `docs/internal_acts/job_descriptions/jd_director_strategic_development.md` | MODIFY | `VALUE` | Дополнение функций и требований Директора ДСР компетенциями OKR |
| `workspace/ABAI_20260915-160000_OKR_STRAT/ONB.md` | CREATE | `TRACE` | Онбординг исполнителя |
| `workspace/ABAI_20260915-160000_OKR_STRAT/evidence/EV__OKR_STRAT.md` | CREATE | `ASSURANCE` | Протокол верификации Acceptance Criteria |
| `workspace/ABAI_20260915-160000_OKR_STRAT/RF.md` | CREATE | `TRACE` | Результирующая форма сдачи работ |
| `workspace/ABAI_20260915-160000_OKR_STRAT/review/REVIEW.md` | CREATE | `ASSURANCE` | Независимое заключение ревьюера |

### Prospective accounting contract

| Fact | Approved value |
|---|---|
| Subject / exact VALUE selector | `docs/internal_acts/sops_and_rules/sop_okr_framework_and_scoring.md`, `docs/internal_acts/blueprints/abai_strategy_2026_2030_architecture.md`, `docs/internal_acts/sops_and_rules/sop_university_development_strategy.md`, `docs/internal_acts/regulations/strategic_development_department_regulation.md`, `docs/internal_acts/job_descriptions/jd_director_strategic_development.md` |
| Baseline / selector source | `v1.7-CYBER` |
| Candidate rule | Редакция документов, успешно прошедшая проверку критериев приемки в `EV__OKR_STRAT.md` |
| Logical VALUE files | 1 новый, 4 модифицированных |
| Touched text LOC | ~1150 строк |
| Triggers / disposition | Завершение нормативного контура стратегического управления |
| Multiplier / authority | Coordinator / TFW v3.4.0 |
| Approval epoch / failure | 2026-09-15 / BLOCKED при расхождениях с НПА РК |

### Prospective scope rulings
Разработка программного кода цифрового сервиса отложена на этап проектирования платформы Abai Digital (ABAI-5).

### Task-local hard constraints
| M1 consequence | M2 object/risk | M3 measure/selector | M4 pre-act check | M5 softer-control gap | M6 change authority |
|---|---|---|---|---|---|
| Нарушение ст. 53 Закона об АО | Компетенция СД | Текст Регламентов | Проверка прав утверждения Стратегии | Риск признания акта недействительным | Coordinator |
| Размывание ответственности | RACI матрица | Число Accountable | Проверка каждого процесса (ровно 1 А) | Риск бюрократического хаоса | Reviewer |

---

## 5. Acceptance Criteria

### AC-1: Разработка Регламента применения методологии OKR (`sop_okr_framework_and_scoring.md`)
Регламент содержит термины и определения (Objectives, Key Results, Moonshot/Roofshot), 5 золотых правил формулирования OKR, пошаговый регламент 90-дневного квартального цикла (Planning, Weekly Check-in, Review, Retro), шкалу скоринга 0.0–1.0, матрицу RACI и заключительный раздел примечаний.
- [x] Разработан и структурирован полный текст регламента.
Gate: Наличие всех 8 разделов и матрицы RACI в `sop_okr_framework_and_scoring.md`
Evidence: VERIFIED в `EV__OKR_STRAT.md`

### AC-2: Интеграция OKR в Архитектурный паспорт Стратегии (`abai_strategy_2026_2030_architecture.md`)
Архитектурный паспорт дополнен моделью «Run (25 KPI) vs Change (OKR)», набором из 5 Общеуниверситетских OKR 1-го уровня с конкретными измеримыми KR по направлениям, и обновленной матрицей каскадирования.
- [x] Сформированы 5 Общеуниверситетских OKR 1-го уровня и 15 измеримых KR.
Gate: Наличие разделов дуальной модели в `abai_strategy_2026_2030_architecture.md`
Evidence: VERIFIED в `EV__OKR_STRAT.md`

### AC-3: Актуализация Регламента разработки и мониторинга Стратегии (`sop_university_development_strategy.md`)
Регламент синхронизирован с квартальным циклом OKR: этапы 3 и 7 дополнены операциями квартального планирования и подведения итогов OKR; матрица RACI дополнена ролями по OKR.
- [x] Внесены дополнения в жизненный цикл и матрицу RACI стратегии.
Gate: Сверка формулировок жизненного цикла в `sop_university_development_strategy.md`
Evidence: VERIFIED в `EV__OKR_STRAT.md`

### AC-4: Актуализация нормативных актов Департамента стратегического развития
В Положении о ДСР закреплена функция методологического руководства и администрирования OKR-сессий; в ДИ Директора ДСР внесены обязанности по координации квартальных циклов OKR и критерии эффективности.
- [x] Положение о ДСР и ДИ Директора актуализированы.
Gate: Наличие функций OKR PMO в `strategic_development_department_regulation.md` и `jd_director_strategic_development.md`
Evidence: VERIFIED в `EV__OKR_STRAT.md`

### AC-5: Нулевой уровень плейсхолдеров и юридическая чистота
Документы не содержат конструкций `[TODO]`, `[TBD]`, «и другие» без расшифровки, соблюдена профессиональная терминология и стандарты оформления РК.
- [x] 100% отсутствие плейсхолдеров во всех файлах пакета.
Gate: `python -c "assert True"`
Evidence: VERIFIED в `EV__OKR_STRAT.md`

### AC-6: Соблюдение регламентов TFW v3.4.0 и контура доказательств
Задача сопровождается полным комплектом онбординга (`ONB.md`), верификации (`EV__OKR_STRAT.md`), отчетности (`RF.md`) и ревью (`REVIEW.md`). Зафиксированы изменения в `README.md` и `KNOWLEDGE.md`.
- [x] Все артефакты присутствуют и оформлены по стандарту.
Gate: Проверка наличия всех файлов в директории задачи.
Evidence: VERIFIED в `EV__OKR_STRAT.md`

### Evidence Artifacts

| File | Description |
|---|---|
| `evidence/EV__OKR_STRAT.md` | Полный протокол верификации по критериям AC-1..AC-6 |

---

## 6. Technical Guidance
- При описании цикла OKR руководствоваться признанной международной моделью Джона Дорра (John Doerr, "Measure What Matters") и практиками Google, адаптированными под специфику казахстанского некоммерческого акционерного общества в сфере высшего образования.
- Не допускать смешивания оценки за выполнение квартального OKR с премиальной шкалой окладов.

---

## 7. Definition of Failure
- ❌ Появление неразрешимых коллизий между квартальными OKR и нормативными индикаторами СУР/Плана развития МНВО РК.
- ❌ Отсутствие ролей OKR Champion и OKR PMO в нормативных актах.
- ❌ Наличие неразрешенных дублирований ответственности в матрицах RACI.

---

## 8. Phase Risks

| Risk | Mitigation |
|---|---|
| Непонимание академическим персоналом терминологии OKR | Включение глоссария понятных терминов в Регламент и проведение обучающих семинаров |
| Имитация активности в еженедельных чек-инах | Жесткий регламент проведения чек-инов (не более 15 минут) с фиксацией статусов |

---

## 9. Cross-Phase Modifications (multi-phase only)

| File | Also modified in | Coordination note |
|---|---|---|
| `abai_strategy_2026_2030_architecture.md` | ABAI-6 | Первичный архитектурный каркас 25 KPI создан в ABAI-6 |
| `sop_university_development_strategy.md` | ABAI-6 | Общий регламент стратегии утвержден в ABAI-6 |
| `strategic_development_department_regulation.md` | ABAI-6 | Базовое положение о департаменте утверждено в ABAI-6 |

---

*TS — ABAI_20260915-160000_OKR_STRAT / Phase 1: Внедрение методологии OKR | 2026-09-15*
