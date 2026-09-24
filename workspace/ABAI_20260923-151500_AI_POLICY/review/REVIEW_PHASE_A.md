# REVIEW — ABAI-26 / Phase A: Институциональная политика этичного использования искусственного интеллекта (GenAI), шкала прозрачности (AI Disclosure Scale) и процедура защиты от ложных детекций

> **Date**: 2026-09-23  
> **Author**: Reviewer / Academic Integrity & AI Governance Auditor  
> **Verdict**: ✅ APPROVE  
> **RF**: [RF Phase A](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260923-151500_AI_POLICY/RF.md)  
> **TS**: [TS Phase A](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260923-151500_AI_POLICY/TS.md)  
> **Stage files**: `review/1_map.md`, `review/2_verify.md`, `review/3_judge.md`  

---

## 1. Map

В рамках Фазы A задачи ABAI-26 проведена независимая комплексная экспертиза институциональной нормативной базы и регламентов этичного применения искусственного интеллекта (GenAI/LLM) в образовательном процессе и научной деятельности Университета:
1. **Институциональная политика:** [`POL-AI-INTEGRITY-001`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/ai_governance_and_integrity_policy.md) — 11 структурированных разделов, преамбула на базе ПП РК № 604 (`MDIAI-06`), Закона РК «Об образовании» (ст. 43-1, 47), Закона РК № 94-V «О персональных данных», Рекомендаций ЮНЕСКО (2021) и позиции COPE (2024); 4-уровневая шкала силлабусов (AI Disclosure Scale 0–3) и категорический запрет выгрузки ПДн;
2. **Типовой формуляр декларации:** [`ai_usage_statement_form.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/ai_usage_statement_form.md) — паспортная часть, реестр моделей, лог промптов с авторской рефлексией, чек-лист фактчекинга и 3 готовых примера заполнения;
3. **Модернизация Политики академической честности:** [`academic_integrity_policy.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/academic_integrity_policy.md) — разграничение AI Ghostwriting, процессуальная презумпция невиновности обучающегося при срабатывании детекторов ИИ и регламент устного собеседования Viva Voce;
4. **Регистрация в сводном реестре:** [`docs/internal_acts/README.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/README.md) — акты зарегистрированы в классификаторе внутренних документов.

Все материалы строго соответствуют канону TFW v3.4.0 и нормам законодательства РК.

---

## 2. Verify

| # | What was checked | Result | Evidence |
|---|---|:---:|---|
| **V1** | Институциональная политика `POL-AI-INTEGRITY-001` | `VERIFIED` | 11 разделов, привязка к ПП РК № 604, Закону № 319-III, Закону № 94-V, ЮНЕСКО, COPE; шкала 0–3; запрет выгрузки ПДн по ст. 52 ТК РК и ст. 79 КоАП РК. AC-1 выполнен на 100%. |
| **V2** | Формуляр `ai_usage_statement_form.md` | `VERIFIED` | Паспорт, реестр версий LLM, лог промптов, верификация галлюцинаций, 3 модельных примера (эссе, Python, ВКР). AC-2 выполнен на 100%. |
| **V3** | Модернизация `academic_integrity_policy.md` | `VERIFIED` | П. 2.5 (AI Ghostwriting), п. 3.1 (презумпция невиновности и статус детекторов), п. 3.2 (Viva Voce), разд. 6 (связанные артефакты). AC-3 выполнен на 100%. |
| **V4** | Реестр `docs/internal_acts/README.md` | `VERIFIED` | Внесены оба документа в разд. 3 «Регламенты и СОП». AC-4 выполнен на 100%. |
| **V5** | Стандарты оформления и 0 плейсхолдеров | `VERIFIED` | Ripgrep показал 0 совпадений `TODO`/`TBD`. Макропеременные `[V_*]` соблюдены. AC-5 выполнен на 100%. |
| **V6** | Протокол доказательств `EV_PHASE_A.md` | `VERIFIED` | 7 из 7 доказательств подтверждены ссылками и цитатами со статусом `VERIFIED`. AC-6 выполнен на 100%. |
| **V-accounting** | Independent value-bearing replay | `VERIFIED` | 2 новых VALUE + 2 модифицированных VALUE = 4 файла VALUE (лимит $\le 8$ новых, $\le 14$ суммарно); $\approx 360$ LOC (лимит $\le 1200$ LOC). Превышений нет. |

> Raw log: `review/2_verify.md`. Сплошная проверка 100% файлов (4 из 4), 4 первичных источника нормативного права подтверждены, 10 из 10 цитат знаний верифицированы.

---

## 3. Judge

| # | Check | Status | Evidence |
|---|---|:---:|---|
| 1 | DoD / all TS AC | ✅ | Критерии AC-1 — AC-6 спецификации TS выполнены в полном объеме |
| 2 | Purpose and design | ✅ | Обеспечен баланс между развитием ИИ-грамотности (ПП РК № 604) и защитой прав обучающихся от ошибочных обвинений (ЮНЕСКО, Viva Voce) |
| 3 | Debt disposed by consequence | ✅ | Единственное наблюдение из RF §6 корректно классифицировано и маршрутизировано в Фазу B |
| 4 | Style and standards | ✅ | Юридическая техника безупречна, 0 маркеров TODO/TBD, переменные `[V_*]` выдержаны |
| 5 | Observations collected | ✅ | Наблюдение по гармонизации порогов оригинальности для диссертаций учтено |
| 6 | RF §7–§9 complete | ✅ | Разделы Fact Candidates, Strategic Insights и Mermaid-диаграмма процессуального маршрута заполнены исчерпывающе |
| 7 | Evidence exists | ✅ | `EV_PHASE_A.md` сформирован и зафиксирован в директории `evidence/` |
| 8 | Evidence is sufficient | ✅ | 7/7 критериев доказаны прямыми цитатами и верифицируемыми строками артефактов |
| 9 | Backward compatibility | ✅ | Действующая редакция Политики честности органично расширена без ломки существующих дисциплин и комиссий |
| 10 | Safety | ✅ | Закреплен жесткий запрет выгрузки персональных данных обучающихся и сотрудников в открытые нейросети со ссылкой на ст. 52 ТК РК и ст. 79 КоАП РК |

---

## 4. Verdict

### **✅ APPROVE**

Фаза A задачи `ABAI-26` (`ABAI_20260923-151500_AI_POLICY`) полностью соответствует каноническим критериям качества TFW v3.4.0, требованиям нормативных правовых актов РК (ПП РК № 604, Закон об образовании ст. 43-1, 47, Закон о персональных данных № 94-V) и передовым международным стандартам (ЮНЕСКО, COPE). Все артефакты верифицированы и готовы к передаче в контур управления знаниями (`KNW`).

---

## 5. Tech Debt Collected and Disposed

| # | Source | Severity | File | Description | Disposition |
|---|---|---|---|---|---|
| 1 | RF §6 Observation 1 | Low | `docs/internal_acts/sops_and_rules/academic_integrity_policy.md` | Синхронизация порогов текстовой оригинальности диссертаций (75–80%) с методикой аутентичного оценивания и использования GenAI. | `promoted — phase-B` |

---

## 6. Traces Updated

- [x] Independent verdict, applicability limits and authorized KNW transition/return recorded
- [x] Coordinator's §5 dispositions complete; 1 row promoted to Phase B
- [x] tfw-docs: Applied — зарегистрированы `POL-AI-INTEGRITY-001` и `ai_usage_statement_form.md` в `docs/internal_acts/README.md`
- [x] tfw-knowledge: Applied — подготовлен кандидат `FACT-050` для `KNOWLEDGE.md`
- [x] Final accepted output identity and affected evidence/independent judgment recorded
- [x] Actual required final effects, including selected landing, complete
- [x] Complete status/outcome/updated and actual event validated before terminal write

---

## 7. Fact Candidates

| # | Category | Human-sourced candidate | Source | Confidence |
|---|---|---|---|:---:|
| 1 | AI Policy / Academic Integrity | В ОВПО РК индикаторы коммерческих AI-детекторов плагиата не могут являться юридическим основанием для дисциплинарных взысканий ввиду погрешности до 30% на текстах на казахском языке и ESL; обязательным процессуальным фильтром является состязательная защита Viva Voce. | Разработка `POL-AI-INTEGRITY-001`, ПП РК № 604, ЮНЕСКО 2021 | High |
| 2 | Infosec / AI Compliance | Загрузка персональных данных обучающихся и сотрудников ОВПО в открытые публичные нейросети квалифицируется как грубое нарушение трудовой дисциплины (ст. 52 ТК РК) и административное правонарушение по ст. 79 КоАП РК. | Закон РК № 94-V, ПП РК № 832 | High |

### Material handover at this return
- **Producer / Unit**: Reviewer (TFW v3.4.0)
- **Inspected Context**: Phase A of task `ABAI_20260923-151500_AI_POLICY` (4 VALUE files, 1 TRACE file)
- **Continuation**: Рекомендован переход задачи в статус `KNW` для фиксации факта `FACT-050` в `KNOWLEDGE.md`, с последующим открытием Фазы B (Методические указания по аутентичному оцениванию `guidelines_ai_authentic_assessment_for_faculty.md`, Регламент этики научных публикаций `sop_scientific_ai_ethics_and_publishing.md`, гармонизация Доменов 01, 02, 05).

---

*REVIEW — ABAI-26 / Phase A: Институциональная политика этичного использования искусственного интеллекта (GenAI) и академическая честность в ОВПО РК | 2026-09-23*
