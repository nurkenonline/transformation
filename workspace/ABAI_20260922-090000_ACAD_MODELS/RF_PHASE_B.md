# RF — ABAI_20260922-090000_ACAD_MODELS / Phase B: Параметризация фреймворка и сквозная гармонизация взаимодействия подразделений

> **Date**: 2026-09-22  
> **Author**: Executor / Legal & Educational Process Engineer  
> **Status**: 🟢 RF — Complete  
> **Parent HL**: [HL-ABAI_20260922-090000_ACAD_MODELS](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260922-090000_ACAD_MODELS/HL.md)  
> **TS**: [TS Phase B](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260922-090000_ACAD_MODELS/TS_PHASE_B.md)  
> **Candidate Commit**: `d14b944`  

---

## 1. What Was Done

В рамках Фазы B задачи ABAI-23 обеспечена полная сквозная интеграция триады организационных моделей (Факультет, Институт, Школа) во все системные и операционные регламенты Университета:

### Actual Value-Bearing Accounting

| Fact | Actual result |
|---|---|
| TS approval ref | `27e3cc1` |
| Baseline / Candidate | `27e3cc1` / `d14b944` |
| VALUE membership | 6 модифицированных файлов (`01_variable_registry_and_placeholders.md`, `02_reference_cases_architecture.md`, `dav_regulation.md`, `hr_department_regulation.md`, `registrar_regulation.md`, `student_and_staff_service_center_regulation.md`) |
| Arithmetic | 46 additions + 23 deletions = 69 touched LOC; 6 logical files |
| Membership deviations | None (100% совпадение с утвержденной спецификацией TS Phase B) |
| Trigger disposition | В рамках лимитов фазы (0 новых файлов $\le 8$, 6 файлов VALUE $\le 14$, 69 строк $\le 1200$) |
| Authority and timing | Утверждено в TS Phase B коммитом `27e3cc1` |

### Modified Files

| File | Changes |
|---|---|
| [`docs/generic_framework/01_variable_registry_and_placeholders.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/generic_framework/01_variable_registry_and_placeholders.md) | Расширена Группа 3 переменных (`[V_MIDDLE_TIER_BOARD_TITLE]`, `[V_MIDDLE_TIER_OFFICE_TITLE]`, `[V_MIDDLE_TIER_ADVISORY_BODY]`), формализовано «Правило применения академической триады» |
| [`docs/generic_framework/02_reference_cases_architecture.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/generic_framework/02_reference_cases_architecture.md) | Добавлен раздел 4 «Архитектурная триада организационных моделей среднего звена (Middle Tier)» со сравнительной таблицей и обновленной матрицей выбора бенчмарка |
| [`docs/internal_acts/regulations/dav_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/dav_regulation.md) | Академический контур: устранена эксклюзивная фиксация на институтах, закреплена координация разработки ОП и РУП с факультетами, институтами и школами, обновлена RACI-матрица |
| [`docs/internal_acts/regulations/registrar_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/registrar_regulation.md) | Контур кредитной технологии: в RACI-матрицу и регламент взаимодействия внесены деканаты факультетов, дирекции институтов и офисы школ |
| [`docs/internal_acts/regulations/hr_department_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/hr_department_regulation.md) | Кадровый контур: актуализированы процедуры открытого конкурсного отбора (Приказ № 230) для деканов факультетов, директоров институтов, зав. кафедрами и Program Leads с учетом 8 уровня НРК |
| [`docs/internal_acts/regulations/student_and_staff_service_center_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/student_and_staff_service_center_regulation.md) | Сервисный контур ЦОС: закреплена сквозная маршрутизация студенческих заявлений из Front-Office в соответствующие бэк-офисы деканатов, дирекций и офисов школ |

---

## 2. Key Decisions

1. **Единый стандарт подстановки переменных (Rule of Academic Triad):** В системном слое зафиксировано правило, согласно которому университет при конфигурировании нормативной базы выбирает базовый профиль, после чего переменные подставляются транспарентно и однозначно во все взаимосвязанные Положения.
2. **Симметричное позиционирование в RACI:** Во всех матрицах сквозных департаментов (ДАВ, ОР, ЦОС, HR) среднее звено обозначено равноправно: «Факультеты / Институты / Школы (Деканаты / Дирекции / Офисы школ)», что гарантирует применимость положений для любого типа университета.

---

## 3. Acceptance Criteria

- [x] **AC-1:** В `01_variable_registry_and_placeholders.md` расширена Группа 3 переменных тегами `[V_MIDDLE_TIER_BOARD_TITLE]` (Совет факультета / Совет института / Academic Board) и детальными правилами подстановки.
- [x] **AC-2:** В `02_reference_cases_architecture.md` добавлена сравнительная архитектурная матрица трех академических моделей ОВПО РК.
- [x] **AC-3:** В `dav_regulation.md` и `registrar_regulation.md` внедрена универсальная триада «факультеты / институты / школы» и «деканаты / дирекции / офисы школ».
- [x] **AC-4:** В `hr_department_regulation.md` гармонизированы процедуры конкурсного отбора академических руководителей по Приказу № 230.
- [x] **AC-5:** В `student_and_staff_service_center_regulation.md` настроена сквозная маршрутизация услуг Front-Office ЦОС в Back-Office деканатов, институтов и школ.
- [x] **AC-6:** Проверка ripgrep подтверждает 0 маркеров `[TODO]` и `[TBD]`, сформирован протокол `EV_PHASE_B.md`.

---

## 4. Verification

- **Проверка плейсхолдеров:** Поиск по маркерам `[TODO]`, `[TBD]`, `[WIP]`, «описать позже» дал **0 совпадений**.
- **Проверка синтаксиса параметров:** Все теги оформлены по стандарту `[V_*]` без нераскрытых скобок.
- **Соответствие законодательству:** Все документы выверены с Законами РК «Об образовании», Приказами МОН/МНВО № 595, № 230, № 338, ТК РК.

---

## 5. Evidence

См. протокол доказательств: [`workspace/ABAI_20260922-090000_ACAD_MODELS/evidence/EV_PHASE_B.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260922-090000_ACAD_MODELS/evidence/EV_PHASE_B.md).

Evidence verdict: **7/7 VERIFIED**, 0 DEFERRED, 0 BLOCKED, 0 N/A.

---

## 6. Observations (out-of-scope, not modified)

Нет замечаний.

---

## 7. Fact Candidates

- **FACT-ACAD-PARAM-001**: При параметризации универсальной нормативной базы высшего учебного заведения сквозные регламенты университетских служб (ДАВ, Офис регистратора, HR, ЦОС) формулируются в нейтрально-агрегированном виде («факультеты, институты и школы» / «деканаты, дирекции и офисы школ»), что позволяет адаптировать документацию под любую организационную структуру без изменения базовых процессов.

---

## 8. Next Steps

1. Провести независимую экспертизу Фазы B в рамках `/tfw-review`.
2. Зафиксировать вердикт в `review/REVIEW_PHASE_B.md`.
3. Координатору обновить `KNOWLEDGE.md` (добавить `FACT-046` по академической триаде) и `README.md` (закрыть задачу ABAI-23).
