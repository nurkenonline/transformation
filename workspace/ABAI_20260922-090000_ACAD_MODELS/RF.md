# RF — ABAI_20260922-090000_ACAD_MODELS / Phase A: Нормативная триада академических подразделений (Факультет, Институт, Школа)

> **Date**: 2026-09-22  
> **Author**: Executor / Legal & Educational Process Engineer  
> **Status**: 🟢 RF — Complete  
> **Parent HL**: [HL-ABAI_20260922-090000_ACAD_MODELS](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260922-090000_ACAD_MODELS/HL.md)  
> **TS**: [TS Phase A](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260922-090000_ACAD_MODELS/TS.md)  
> **Candidate Commit**: `5ccc07c`  

---

## 1. What Was Done

В рамках Фазы A задачи ABAI-23 сформирован полный комплект нормативно-правового и должностного обеспечения трех организационных моделей промежуточного академического звена (Middle Tier) ОВПО РК.

### Actual Value-Bearing Accounting

| Fact | Actual result |
|---|---|
| TS approval ref | `797bf66` |
| Baseline / Candidate | `797bf66` / `5ccc07c` |
| VALUE membership | 5 новых файлов (`faculty_model_regulation.md`, `jd_dean_faculty.md`, `school_model_regulation.md`, `jd_dean_school.md`, `jd_director_institute.md`), 1 модифицируемый файл (`institute_model_regulation.md`) |
| Arithmetic | 624 additions + 16 deletions = 640 touched LOC; 6 logical files |
| Membership deviations | None (100% совпадение с утвержденной спецификацией TS Phase A) |
| Trigger disposition | В рамках лимитов фазы (5 новых файлов $\le 8$, 6 файлов VALUE $\le 14$, 640 строк $\le 1200$) |
| Authority and timing | Утверждено в TS Phase A коммитом `797bf66` |

### New Files

| File | Description |
|---|---|
| [`docs/internal_acts/regulations/faculty_model_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/faculty_model_regulation.md) | Типовое положение о Факультете: структура деканата, кафедры, Совет факультета, метбюро, матрица RACI и регламент в УИС с дедлайнами SLA |
| [`docs/internal_acts/job_descriptions/jd_dean_faculty.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_dean_faculty.md) | Типовая ДИ Декана факультета: квалификационные требования Приказа № 338, уровень 8 НРК Профстандарта «Педагог», ТК РК |
| [`docs/internal_acts/regulations/school_model_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/school_model_regulation.md) | Типовое положение о Школе: матричная структура, Program Leads, Industry Advisory Board, Capstone, аккредитации ABET/AACSB/FIBAA |
| [`docs/internal_acts/job_descriptions/jd_dean_school.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_dean_school.md) | Типовая ДИ Декана школы: требования PhD/Doctorate, C1 английский, фандрайзинг, IAB, KPI трудоустройства $\ge 80\%$ |
| [`docs/internal_acts/job_descriptions/jd_director_institute.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_director_institute.md) | Типовая ДИ Директора института: интеграция R&D и образования, TRL 1–9, спин-офф, диссоветы PhD по Приказу № 126 |

### Modified Files

| File | Changes |
|---|---|
| [`docs/internal_acts/regulations/institute_model_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/institute_model_regulation.md) | Позиционирование института в рамках национальной триады моделей, интеграция R&D, TRL 1–9, диссоветов PhD, авторских роялти $\ge 30\%$ |

---

## 2. Key Decisions

1. **Обособление трех самостоятельных моделей:** Вместо попытки слить факультет, институт и школу в один громоздкий документ, разработаны три чистых типовых положения и три соответствующие ДИ, что позволяет любому вузу РК выбрать нужную модель без избыточных оговорок.
2. **Матричная специфика Школьной модели:** В Положении о Школе закреплен отказ от жестких традиционных кафедр в пользу гибких предметных кластеров (Subject Groups) и Комитетов образовательных программ во главе с Program Leads, а также обязательное участие работодателей через Industry Advisory Board.
3. **Лицензионная и квалификационная преемственность:** Во всех трех моделях строго выдержаны государственные лицензионные нормативы остепененности ($\ge 45-50\%$), требования 8 уровня НРК Профессионального стандарта «Педагог» и персональная ответственность руководителей по Трудовому кодексу РК.

---

## 3. Acceptance Criteria

- [x] **AC-1:** Разработано Типовое положение о факультете (`faculty_model_regulation.md`) с регламентацией структуры деканата, кафедр, Совета факультета, метбюро, RACI и цифрового регламента в УИС.
- [x] **AC-2:** Разработана Типовая ДИ Декана факультета (`jd_dean_faculty.md`) с квалификационными цензами Приказа № 338, уровнем 8 НРК Профстандарта «Педагог» и нормами ответственности по ТК РК.
- [x] **AC-3:** Разработано Типовое положение о Школе (`school_model_regulation.md`) с матричной структурой, Program Leads, Industry Advisory Board и международными аккредитациями.
- [x] **AC-4:** Разработана Типовая ДИ Декана школы (`jd_dean_school.md`) с компетенциями стратегического лидерства, фандрайзинга и индустриального партнерства.
- [x] **AC-5:** Разработана Типовая ДИ Директора института (`jd_director_institute.md`) и гармонизировано Положение об институте (`institute_model_regulation.md`) с акцентом на R&D, TRL 1–9 и диссоветы.
- [x] **AC-6:** Проверка ripgrep подтверждает 0 маркеров `[TODO]` и `[TBD]`, параметры `[V_*]` валидны, сформирован протокол доказательств `EV_PHASE_A.md`.

---

## 4. Verification

- **Проверка плейсхолдеров:** Поиск по маркерам `[TODO]`, `[TBD]`, `[WIP]`, «описать позже» дал **0 совпадений**.
- **Проверка синтаксиса параметров:** Все теги оформлены по стандарту `[V_*]` без нераскрытых скобок.
- **Соответствие законодательству:** Все документы выверены с Законами РК «Об образовании», «О науке и технологической политике», Приказами МОН/МНВО № 595, № 338, № 374, № 126, ТК РК и КоАП РК.

---

## 5. Evidence

См. протокол доказательств: [`workspace/ABAI_20260922-090000_ACAD_MODELS/evidence/EV_PHASE_A.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260922-090000_ACAD_MODELS/evidence/EV_PHASE_A.md).

Evidence verdict: **7/7 VERIFIED**, 0 DEFERRED, 0 BLOCKED, 0 N/A.

---

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|---|---|---|---|
| 1 | `docs/generic_framework/01_variable_registry_and_placeholders.md` | 55-60 | naming | В Группе 3 переменных целесообразно расширить перечень тегов переменной `[V_MIDDLE_TIER_BOARD_TITLE]` (Совет факультета / Совет института / Academic Board школы) в рамках Фазы B |

---

## 7. Fact Candidates

- **FACT-ACAD-TRIAD-001**: В высшем образовании Республики Казахстан организационная архитектура промежуточного академического звена (Middle Tier) нормативно дифференцируется на три базовые модели: классическую Факультетскую (Приказ № 595), укрупненную научно-исследовательскую Институтскую (Приказ № 126, Закон № 103-VIII) и корпоративную инновационную Школьную (матричная архитектура, Program Leads, Industry Advisory Board, ABET/AACSB).

---

## 8. Next Steps

1. Провести независимую экспертизу Фазы A в рамках `/tfw-review`.
2. Зафиксировать вердикт в `review/REVIEW_PHASE_A.md`.
3. Перейти к согласованию и реализации Фазы B (сквозная параметризация и гармонизация взаимодействия ДАВ, ОР, HR и ЦОС).

---

*RF — ABAI_20260922-090000_ACAD_MODELS / Phase A | 2026-09-22*
