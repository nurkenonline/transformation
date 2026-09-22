# ONB — ABAI_20260922-090000_ACAD_MODELS / Phase B: Параметризация фреймворка и сквозная гармонизация взаимодействия подразделений

> **Date**: 2026-09-22  
> **Author**: Executor / Legal & Educational Process Engineer  
> **Status**: 🟢 ONB_RESOLVED — Ready for implementation  
> **Parent HL**: [HL-ABAI_20260922-090000_ACAD_MODELS](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260922-090000_ACAD_MODELS/HL.md)  
> **TS**: [TS Phase B](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260922-090000_ACAD_MODELS/TS_PHASE_B.md)  

---

## 1. Understanding

Задача Фазы B заключается в сквозной синхронизации и параметризации организационной триады (Факультет, Институт, Школа) во всех системообразующих документах Университета:
1. В Реестре системных переменных (`01_variable_registry_and_placeholders.md`) закрепить расширенные теги коллегиальных органов `[V_MIDDLE_TIER_BOARD_TITLE]` (Совет факультета / Совет института / Academic Board школы) с формализованными правилами;
2. В Архитектуре кейсов (`02_reference_cases_architecture.md`) описать три эталонных сценария ОВПО РК;
3. В Положениях о ДАВ, Офисе регистратора, HR и ЦОС заменить жесткую монопсонию института на универсальное равноправное взаимодействие со всеми тремя типами структурных подразделений («факультеты / институты / школы»).

---

## 2. Entry Points

- `docs/generic_framework/01_variable_registry_and_placeholders.md`
- `docs/generic_framework/02_reference_cases_architecture.md`
- `docs/internal_acts/regulations/dav_regulation.md`
- `docs/internal_acts/regulations/registrar_regulation.md`
- `docs/internal_acts/regulations/hr_department_regulation.md`
- `docs/internal_acts/regulations/student_and_staff_service_center_regulation.md`

---

## 3. Questions (blocking)

Блокирующие вопросы отсутствуют. Спецификация утверждена.

---

## 4. Recommendations

1. В матрицах RACI и пунктах взаимодействия использовать конструкцию «факультеты / институты / школы» и «деканаты факультетов / дирекции институтов / офисы школ», чтобы документ читался органично при любой структуре вуза.

---

## 5. Risks Found

Не выявлено. Бюджет фазы (~450 строк в 6 файлах) полностью соблюдается.

---

## 6. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|---|:---:|---|---|
| 1 | `FACT-016` (Generic OVPO Model) | ✅ | Applied | Правила параметризации и универсальности актов ОВПО РК |
| 2 | `FACT-ACAD-TRIAD-001` | ✅ | Applied | Наследуемый контекст триады моделей из Фазы A |

---

*ONB — ABAI_20260922-090000_ACAD_MODELS / Phase B | 2026-09-22*
