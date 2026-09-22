# ONB — ABAI_20260922-090000_ACAD_MODELS / Phase A: Нормативная триада академических подразделений (Факультет, Институт, Школа)

> **Date**: 2026-09-22  
> **Author**: Executor / Legal & Educational Process Engineer  
> **Status**: 🟢 ONB_RESOLVED — Ready for implementation  
> **Parent HL**: [HL-ABAI_20260922-090000_ACAD_MODELS](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260922-090000_ACAD_MODELS/HL.md)  
> **TS**: [TS Phase A](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260922-090000_ACAD_MODELS/TS.md)  

---

## 1. Understanding

Задача Фазы A заключается в создании полной нормативно-правовой базы для трех организационных моделей промежуточного академического звена (Middle Tier) высших учебных заведений Республики Казахстан. Необходимо разработать Положение о Факультете (`faculty_model_regulation.md`) и ДИ Декана факультета (`jd_dean_faculty.md`), Положение о Школе (`school_model_regulation.md`) и ДИ Декана школы (`jd_dean_school.md`), ДИ Директора института (`jd_director_institute.md`), а также гармонизировать существующее Положение об институте (`institute_model_regulation.md`). Все документы должны соответствовать Законам РК «Об образовании» и «О статусе педагога», Приказам МОН/МНВО № 595, № 338, № 374 (Профстандарт «Педагог») и Трудовому кодексу РК.

---

## 2. Entry Points

- `docs/internal_acts/regulations/institute_model_regulation.md` — базовый эталон для гармонизации структуры;
- `docs/internal_acts/regulations/` — директория для размещения `faculty_model_regulation.md` и `school_model_regulation.md`;
- `docs/internal_acts/job_descriptions/` — директория для размещения `jd_dean_faculty.md`, `jd_dean_school.md`, `jd_director_institute.md`;
- `docs/regulations/rk_ovpo_model_rules.md` (`STD-RK-OVPO-001`) — нормы Приказа МОН РК № 595;
- `docs/regulations/rk_pedagogue_professional_standard.md` (`STD-RK-PEDAGOGUE-001`) — квалификационные требования 8 уровня НРК/ОРК.

---

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|---|---|
| — | Блокирующие вопросы отсутствуют. Спецификация TS Phase A исчерпывающая и детерминированная. | Согласовано, переход к разработке разрешен. |

---

## 4. Recommendations (suggestions, not blocking)

1. В Положении о Школе четко зафиксировать статус Руководителя академической программы (Program Lead) и Индустриального совета (Industry Advisory Board) для безупречного отражения моделей передовых автономных и корпоративных ОВПО (AITU, AlmaU).
2. В ДИ Декана факультета и Директора института предусмотреть обязательное соблюдение порога остепененности кафедр не менее 45–50% в соответствии с Квалификационными требованиями МОН РК № 391.

---

## 5. Risks Found (edge cases, potential issues not in TS)

1. *Риск терминологической коллизии при гибридной структуре:* В некоторых университетах могут одновременно функционировать институты и факультеты (например, Факультет довузовского образования и 7 исследовательских институтов). Положения должны быть полностью автономны и не конфликтовать друг с другом.

---

## 6. Inconsistencies with Code (spec vs reality)

Несоответствий не выявлено. В `docs/internal_acts/` подготовлены необходимые разделы и шаблоны.

---

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|---|:---:|---|---|
| 1 | `FACT-016` (Generic OVPO Model) | ✅ | Applied | Соблюдение правил обезличивания и применения параметров `[V_*]` |
| 2 | `FACT-023` (IS Profile & Job Integration) | ✅ | Applied | Интеграция модулей УИС («Академический процесс», «Электронный журнал», «Силлабусы») и SLA |
| 3 | `FACT-043` (Pedagogue Standard & Laws) | ✅ | Applied | Дескрипторы 8 уровня НРК, НПР раз в 3 года $\ge 72$ ч |
| 4 | `STD-RK-OVPO-001` (Приказ МОН № 595) | ✅ | Applied | Нормы функционирования Советов факультета/института, кафедр и методического бюро |

---

*ONB — ABAI_20260922-090000_ACAD_MODELS / Phase A | 2026-09-22*
