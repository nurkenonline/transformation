# EV — ABAI_20260923-151500_AI_POLICY / Phase A: Институциональная политика этичного использования искусственного интеллекта (GenAI), шкала прозрачности (AI Disclosure Scale) и процедура защиты от ложных детекций

> **Date**: 2026-09-23  
> **Author**: Executor (TFW v3.4.0)  
> **Task**: ABAI_20260923-151500_AI_POLICY  
> **TS**: [TS Phase A](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260923-151500_AI_POLICY/TS.md)  

---

## Environment

| Field | Value |
|---|---|
| OS | Windows 11 / PowerShell 5.1 |
| Language / Runtime | Markdown / Static Architecture Analysis |
| Repository Target | `Abai Unviersity Transformation` |
| Standards / Framework | TFW v3.4.0 (Scope Budget, Evidence Layer Protocol) |
| Base Norms | ПП РК № 604, Закон РК № 319-III, Закон РК № 94-V, Рекомендация ЮНЕСКО (2021), COPE (2024) |

---

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|:---:|---|
| E1 | AC-1 | Разработана Институциональная политика этичного использования ИИ `POL-AI-INTEGRITY-001` (11 разделов: преамбула, 4-уровневая шкала 0–3, права/обязанности, строгий запрет выгрузки ПДн по Закону № 94-V и ПП РК № 832). | Local Workspace | **VERIFIED** | `docs/internal_acts/sops_and_rules/ai_governance_and_integrity_policy.md` |
| E2 | AC-2 | Разработан стандартизированный формуляр AI Statement Form: паспортная часть, реестр моделей/версий, лог промптов, фактчекинг, декларация авторства, 3 модельных примера (эссе, Python код, ВКР). | Local Workspace | **VERIFIED** | `docs/internal_acts/sops_and_rules/ai_usage_statement_form.md` |
| E3 | AC-3 | Модернизирована Политика академической честности: обновлен п. 2.5 (AI Fraud), добавлен п. 3.1 (презумпция невиновности обучающегося при сработках детекторов ИИ) и п. 3.2 (регламент устного собеседования Viva Voce). | Local Workspace | **VERIFIED** | `docs/internal_acts/sops_and_rules/academic_integrity_policy.md#L25-L68` |
| E4 | AC-4 | Актуализирован сводный реестр внутренних нормативных актов Университета: `POL-AI-INTEGRITY-001` и формуляр `ai_usage_statement_form.md` внесены в классификатор с описанием. | Local Workspace | **VERIFIED** | `docs/internal_acts/README.md#L113-L115` |
| E5 | AC-5 | Проведена проверка на отсутствие плейсхолдеров (`TODO`, `TBD`, «уточнить позже») и соблюдение системных макропеременных `[V_*]`. Поиск ripgrep вернул 0 совпадений. | Local Workspace | **VERIFIED** | Ripgrep Search: 0 TODO/TBD in affected files |
| E6 | AC-6 | Сформирован настоящий протокол доказательств `EV_PHASE_A.md` со 100% покрытием критериев приемки Фазы A. | Local Workspace | **VERIFIED** | `workspace/ABAI_20260923-151500_AI_POLICY/evidence/EV_PHASE_A.md` |
| E-accounting | AC-Accounting | Бюджет Фазы A: Запланировано 4 файла VALUE (2 новых + 2 модифицированных). Фактически затронуто 4 файла VALUE + 1 TRACE. Добавлено/изменено $\approx 360$ LOC (норматив $\le 1200$ LOC, новые $\le 8$). | Git numstat | **VERIFIED** | Git status: 2 new VALUE, 2 modified VALUE, 0 overruns |

---

## Verdict

Evidence verdict: **7/7 VERIFIED**, 0 DEFERRED, 0 BLOCKED, 0 N/A.  
Статус выполнения критериев приемки: **100% подтверждено объективными артефактами**.

---

*EV — ABAI_20260923-151500_AI_POLICY / Phase A: Институциональная политика этичного использования искусственного интеллекта (GenAI), шкала прозрачности (AI Disclosure Scale) и процедура защиты от ложных детекций | 2026-09-23*
