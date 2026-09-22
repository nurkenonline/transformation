# TS — ABAI_20260922-090000_ACAD_MODELS / Phase B: Параметризация фреймворка и сквозная гармонизация взаимодействия подразделений

> **Date**: 2026-09-22  
> **Author**: Coordinator / Institutional & Academic Architecture Lead  
> **Status**: 🔒 FROZEN — approved by owner 2026-09-22  
> **Parent HL**: [HL-ABAI_20260922-090000_ACAD_MODELS](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260922-090000_ACAD_MODELS/HL.md)  

---

## 1. Objective

Обеспечить бесшовную системную интеграцию разработанной триады моделей (Факультет, Институт, Школа) в общеуниверситетский фреймворк трансформации:
1. **Параметризация системного слоя фреймворка:**
   - Дополнить Реестр переменных (`01_variable_registry_and_placeholders.md`) переменными коллегиальных органов `[V_MIDDLE_TIER_BOARD_TITLE]` (Совет факультета / Совет института / Academic Board школы), уточнить правила подстановки для классических, исследовательских и корпоративных вузов;
   - Актуализировать архитектуру кейсов (`02_reference_cases_architecture.md`), закрепив типологию ОВПО РК по трем академическим моделям;
2. **Сквозная гармонизация взаимодействий в ключевых Положениях:**
   - **ДАВ (`dav_regulation.md`):** устранить жесткую монополию институтов, закрепить методическую координацию факультетов, институтов и школ;
   - **Офис регистратора (`registrar_regulation.md`):** синхронизировать учет успеваемости и регистрацию дисциплин с деканатами факультетов, дирекциями институтов и офисами школ;
   - **Департамент HR (`hr_department_regulation.md`):** гармонизировать конкурсный отбор руководителей академических структур (деканы факультетов, директора институтов, деканы школ) по Приказу МОН № 230 и 8 уровню НРК Профстандарта «Педагог»;
   - **ЦОС (`student_and_staff_service_center_regulation.md`):** настроить универсальную маршрутизацию справок, согласований и обращений студентов к деканатам факультетов, дирекциям институтов и офисам школ.

---

## 2. Scope

### In Scope (6 файлов VALUE + 1 TRACE)
1. `docs/generic_framework/01_variable_registry_and_placeholders.md` (MODIFY, `VALUE`) — Группа 3 переменных;
2. `docs/generic_framework/02_reference_cases_architecture.md` (MODIFY, `VALUE`) — Сравнительная матрица трех моделей;
3. `docs/internal_acts/regulations/dav_regulation.md` (MODIFY, `VALUE`) — Академический контур;
4. `docs/internal_acts/regulations/registrar_regulation.md` (MODIFY, `VALUE`) — Контур кредитной технологии;
5. `docs/internal_acts/regulations/hr_department_regulation.md` (MODIFY, `VALUE`) — Кадровый контур и конкурсы;
6. `docs/internal_acts/regulations/student_and_staff_service_center_regulation.md` (MODIFY, `VALUE`) — Сервисный контур ЦОС;
7. `workspace/ABAI_20260922-090000_ACAD_MODELS/evidence/EV_PHASE_B.md` (CREATE, `TRACE`) — Протокол доказательств Фазы B.

### Out of Scope
- Модификация ранее утвержденных в Фазе A положений о факультете, институте и школе.

---

## 3. Principles Check

| # | HL §7 principle | Enforced by | Gate |
|---|---|---|---|
| **P1** | Бесшовная параметризация | AC-1, AC-2 | Независимость всех базовых актов вуза от конкретной выбранной модели среднего звена. |
| **P2** | Структурный плюрализм | AC-3, AC-4, AC-5 | Отражение равного статуса факультетов, институтов и школ во всех сквозных регламентах. |
| **P3** | Отсутствие плейсхолдеров | AC-6 | 0 маркеров TODO/TBD, сохранение тегов `[V_*]`. |

---

## 4. Affected Files and Value-Bearing Accounting

| File / selector | Action | Class | Semantic reason / required result |
|---|---|---|---|
| `docs/generic_framework/01_variable_registry_and_placeholders.md` | MODIFY | `VALUE` | Расширение Группы 3 переменных: `[V_MIDDLE_TIER_BOARD_TITLE]` |
| `docs/generic_framework/02_reference_cases_architecture.md` | MODIFY | `VALUE` | Архитектурное описание Факультетской, Институтской и Школьной моделей |
| `docs/internal_acts/regulations/dav_regulation.md` | MODIFY | `VALUE` | Координация учебных планов и каталогов ОП с факультетами / институтами / школами |
| `docs/internal_acts/regulations/registrar_regulation.md` | MODIFY | `VALUE` | Взаимодействие ОР с деканатами факультетов / дирекциями институтов / офисами школ |
| `docs/internal_acts/regulations/hr_department_regulation.md` | MODIFY | `VALUE` | Конкурсный отбор деканов, директоров и руководителей программ (Приказ № 230) |
| `docs/internal_acts/regulations/student_and_staff_service_center_regulation.md` | MODIFY | `VALUE` | Маршрутизация студенческих заявлений в деканаты / дирекции / офисы школ |
| `workspace/ABAI_20260922-090000_ACAD_MODELS/evidence/EV_PHASE_B.md` | CREATE | `TRACE` | Протокол доказательств Фазы B по критериям AC-1 – AC-6 |

### Prospective accounting contract
- **Budget**: 0 новых файлов VALUE, 6 модифицируемых файлов VALUE, 1 TRACE файл, ~450 строк изменений.
- **Budget compliance**: Полностью укладывается в нормативы фазы (`touched_files: 6 <= 14`, `new_loc: ~450 <= 1200`).

---

## 5. Acceptance Criteria (AC)

- [ ] **AC-1:** В `01_variable_registry_and_placeholders.md` расширена Группа 3 переменных тегами `[V_MIDDLE_TIER_BOARD_TITLE]` (Совет факультета / Совет института / Academic Board) и детальными правилами подстановки.
- [ ] **AC-2:** В `02_reference_cases_architecture.md` добавлена сравнительная архитектурная матрица трех академических моделей ОВПО РК.
- [ ] **AC-3:** В `dav_regulation.md` и `registrar_regulation.md` внедрена универсальная триада «факультеты / институты / школы» и «деканаты / дирекции / офисы школ».
- [ ] **AC-4:** В `hr_department_regulation.md` гармонизированы процедуры конкурсного отбора академических руководителей по Приказу № 230.
- [ ] **AC-5:** В `student_and_staff_service_center_regulation.md` настроена сквозная маршрутизация услуг Front-Office ЦОС в Back-Office деканатов, институтов и школ.
- [ ] **AC-6:** Проверка ripgrep подтверждает 0 маркеров `[TODO]` и `[TBD]`, сформирован протокол `EV_PHASE_B.md`.

---

*TS — ABAI_20260922-090000_ACAD_MODELS / Phase B | 2026-09-22*
