# Kazakhstan University Transformation Framework: Проектирование системы внутренних НПА и функций ОВПО РК

Универсальная система нормативного, функционального и цифрового проектирования для высших учебных заведений (ОВПО) Республики Казахстан по методологии **Trace-First Workflow (TFW v3.4.0)** на основе Новой регуляторной политики («С чистого листа» / РЧЛ).

---

## 🎯 Миссия и цели проекта
Целью проекта является создание целостной, непротиворечивой и юридически выверенной системы внутренних нормативных актов (НПА) университета на основе исчерпывающего свода законодательных функций, полномочий, прав и обязанностей ОВПО Республики Казахстан:

1. **Разработка Положений о структурных подразделениях:**
   - Институты, факультеты и кафедры;
   - Научно-исследовательские институты, центры и лаборатории;
   - Административные департаменты, управления, службы и проектные офисы.
2. **Разработка Должностных инструкций:**
   - Руководство (Ректор, проректоры, деканы/директора институтов, заведующие кафедрами);
   - Профессорско-преподавательский состав (профессора, доценты, ассоциированные профессора, старшие преподаватели, преподаватели);
   - Научные сотрудники (главные, ведущие, старшие, младшие научные сотрудники, постдокторанты);
   - Административно-управленческий и инженерно-технический персонал.
3. **Формирование Каталога функций и полномочий университета:**
   - Декомпозиция функций по 10 функциональным доменам;
   - Привязка каждой функции к статьям законов РК и приказам МНВО/МЗ/МЧС РК;
   - Построение матриц ответственности RACI для исключения дублирования и «серых зон».

---

## ⚖️ База внешних НПА Республики Казахстан (Архитектура РЧЛ + Стратегия, Безопасность, Архивы и Медиа: 101 НПА)
- 📑 [**Сводный реестр внешних НПА РК**](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/regulations/external_npa_registry.md) (21 Закон и Кодекс, 39 приказов МНВО/МОН, 20 актов МЗ, 9 актов МЧС, 6 актов МЦРИАП, 10 актов МНЭ/МФ, 6 актов МКИ РК).
- 🎓 [**1. Академический блок и образовательная деятельность**](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/regulations/01_academic_and_educational_npa.md) (ГОСО № 2, Приказ № 595, Приказ № 391, Кредитная система № 152, Прием № 600, ДО № 137).
- 🔬 [**2. Наука, инновации и технологическое развитие**](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/regulations/02_science_and_innovations_npa.md) (Закон о науке 2024 г., коммерциализация, диссоветы № 126, степени PhD № 127, звания № 128, КОКСНВО № 20).
- 👥 [**3. Кадровый потенциал, ППС и трудовые отношения**](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/regulations/03_hr_and_faculty_npa.md) (Трудовой кодекс, конкурсный отбор № 230, квалхарактеристики № 338, профстандарт «Педагог» № 374).
- 🧑‍🎓 [**4. Студенческий контингент и молодежная политика**](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/regulations/04_student_and_youth_npa.md) (Перевод/восстановление № 19, акадотпуски № 506, 3-летняя отработка грантов № 39, мобильность № 613, общежития № 606).
- 🏢 [**5. Корпоративное управление, финансы, комплаенс и оценка рисков**](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/regulations/05_governance_finance_compliance_npa.md) (Приказ № 166/116 — риски ОВПО по 10 направлениям, НАО, антикоррупция, госзакупки 2024 г., персданные).
- 🏥 [**6. Здравоохранение и санитарно-эпидемиологический контроль (20 НПА МЗ РК)**](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/regulations/06_healthcare_and_sanitary_npa.md) (СанПиН № ҚР ДСМ-76, медосмотры № 131/927, медпункт вуза, СанПиН общежитий № 68, утилизация отходов, производственный контроль).
- 🚒 [**7. Пожарная безопасность, ГО и защита при ЧС (9 НПА МЧС РК)**](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/regulations/07_fire_and_emergency_safety_npa.md) (Закон о гражданской защите, Правила ПБ № 55, Техрегламент № 405, обучение ПТМ № 280, гражданская оборона № 268, бомбоубежища № 368, промбезопасность).
- 💻 [**8. Цифровизация, информационная безопасность и ИИ (6 НПА МЦРИАП РК)**](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/regulations/08_digitalization_infosec_ai_npa.md) (ПДн № 395/НҚ, ЕТИКТ и ИБ № 832, Smart Bridge № 143/НҚ, аттестация ИС № 153/НҚ, ИИ № 604).
- 📈 [**9. Стратегическое планирование и корпоративное управление (10 НПА МНЭ и МФ РК)**](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/regulations/09_strategic_planning_and_governance_npa.md) (Планы развития НАО № 56, Кодекс корп. управления № 178, бухучет № 241, МСФО № 110, госаудит № 598).
- 🏛️ [**10. Культура, архивное дело, библиотечные фонды и масс-медиа (10 НПА МКИ РК)**](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/regulations/10_culture_archives_and_media_npa.md) (Закон об архивах № 326-I, Закон о культуре № 207-III, Закон о масс-медиа № 94-VIII от 19.06.2024, Закон о памятниках № 288-VI, Правила СЭД № 236, **Перечень со сроками хранения — 75 лет личные дела студентов № 566-НҚ**, архивы № 134, библиотеки № 153, музеи № 95, учет СМИ № 368-НҚ).

---

## 📋 Доска задач (Task Board)

| ID | Задача | Статус | Фаза TFW | Исполнитель | Ссылка на артефакты |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **ABAI-1** (`ABAI_20260914-190000_REG_BASE`) | Формирование реестра внешних НПА РК (67 актов РЧЛ) и первичная декомпозиция функций ОВПО | 🟢 Выполнено | `REV` / `DONE` | Coordinator / Reviewer | [`workspace/ABAI_20260914-190000_REG_BASE/review/REVIEW.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260914-190000_REG_BASE/review/REVIEW.md) |
| **ABAI_20260914-190500_AITU** | Бенчмаркинг ВНД Astana IT University на соответствие РЧЛ и выявление уникальных функций | 🟢 Выполнено | `REV` / `DONE` | Coordinator / Reviewer | [`workspace/ABAI_.../review/REVIEW.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260914-190500_AITU/review/REVIEW.md) |
| **ABAI_20260914-191500_ACAD** | Разработка пакета НПА академического блока (ДАВ, Офис регистратора, институты, кафедры, ДИ, ликвидация DEBT-001) | 🟢 Выполнено | `REV` / `DONE` | Coordinator / Reviewer | [`workspace/ABAI_.../review/REVIEW.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260914-191500_ACAD/review/REVIEW.md) |
| **ABAI_20260914-192000_COMP** | Сравнительный анализ типовых документов с ВНД AITU и подготовка поправок для Abai University | 🟢 Выполнено | `REV` / `DONE` | Coordinator / Reviewer | [`workspace/ABAI_.../review/REVIEW.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260914-192000_COMP/review/REVIEW.md) |
| **ABAI-3** (`ABAI_20260914-193000_SCI`) | Разработка пакета НПА научного блока и коммерциализации (Департамент науки, НИИ, СМУ, ликвидация DEBT-002) | 🟢 Выполнено | `REV` / `DONE` | Coordinator / Reviewer | [`workspace/ABAI_.../review/REVIEW.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260914-193000_SCI/review/REVIEW.md) |
| **ABAI-4** (`ABAI_20260914-194000_QA`) | Разработка пакета НПА обеспечения качества, аккредитации и комплаенса (Комплаенс, QA Committee, EdTech Board) | 🟢 Выполнено | `REV` / `DONE` | Coordinator / Reviewer | [`workspace/ABAI_.../review/REVIEW.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260914-194000_QA/review/REVIEW.md) |
| **ABAI-5** (`ABAI_20260915-100000_DIGIT`) | Разработка пакета НПА блока цифровизации, ИТ и интеграции с ЕПВО/НОБД (УЦ, УИТ, Реестр ИБ 4 уровня, ликвидация DEBT-003) | 🟢 Выполнено | `REV` / `DONE` | Coordinator / Reviewer | [`workspace/ABAI_.../review/REVIEW.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260915-100000_DIGIT/review/REVIEW.md) |
| **ABAI-6** (`ABAI_20260915-123000_STRAT`) | Нормативная база стратегического развития (Реестр НПА, Положение о ДСР, СОП Стратегии, Архитектурная модель 2026–2030, ДИ) | 🟢 Выполнено | `REV` / `DONE` | Coordinator / Reviewer | [`workspace/ABAI_20260915-123000_STRAT/review/REVIEW.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260915-123000_STRAT/review/REVIEW.md) |
| **ABAI-7** (`ABAI_20260915-133000_CYBER_TK`) | Имплементация новелл Трудового кодекса РК по кибербезопасности (СОП кибербезопасности персонала, ДИ ППС/ученых, обучение БиОТ) | 🟢 Выполнено | `REV` / `DONE` | Coordinator / Reviewer | [`workspace/ABAI_20260915-133000_CYBER_TK/review/REVIEW.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260915-133000_CYBER_TK/review/REVIEW.md) |
| **ABAI-8** (`ABAI_20260915-160000_OKR_STRAT`) | Внедрение методологии OKR в стратегические документы (Регламент OKR, Общеуниверситетские OKR 1 уровня, модель Run/Change) | 🟢 Выполнено | `REV` / `DONE` | Coordinator / Reviewer | [`workspace/ABAI_20260915-160000_OKR_STRAT/review/REVIEW.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260915-160000_OKR_STRAT/review/REVIEW.md) |
| **ABAI-9** (`ABAI_20260915-163000_KPI_SYSTEMATIZATION`) | Систематизация фонда KPI МНВО РК и Программы развития (239 требований, 65 KPI, 195 разрывов, 406 поручений 2026 г.) | 🟢 Выполнено | `REV` / `DONE` | Coordinator / Reviewer | [`workspace/ABAI_20260915-163000_KPI_SYSTEMATIZATION/review/REVIEW.md`](workspace/ABAI_20260915-163000_KPI_SYSTEMATIZATION/review/REVIEW.md) |
| **ABAI-10** (`ABAI_20260916-140000_STUD_SOC`) | Нормативная база студенческого блока (Положение о Департаменте, общежития по № 606, СанПиН № 68, Центр карьеры, отработка грантов по № 39, КДМ/Омбудсмен, ДИ) | 🟢 Выполнено | `REV` / `DONE` | Coordinator / Reviewer | [`workspace/ABAI_20260916-140000_STUD_SOC/review/REVIEW.md`](workspace/ABAI_20260916-140000_STUD_SOC/review/REVIEW.md) |
| **ABAI-11** (`ABAI_20260917-113000_GENERIC_OVPO`) | Универсализация модели ОВПО РК, обезличивание ВНД и сквозная интеграция эталонного профиля ИС в ДИ и Положения | 🟢 Выполнено | `REV` / `DONE` | Coordinator / Reviewer | [`workspace/ABAI_20260917-113000_GENERIC_OVPO/review/REVIEW.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260917-113000_GENERIC_OVPO/review/REVIEW.md) |
| **ABAI-12** (`ABAI_20260917-122500_HR_SYSTEM`) | Разработка пакета НПА блока HR (Положение об HR, конкурсный отбор ППС по № 230, 7-классная система и $K_{дос}$ по Приказу № 424, ДИ) | 🟢 Выполнено | `REV` / `DONE` | Coordinator / Reviewer | [`workspace/ABAI_20260917-122500_HR_SYSTEM/review/REVIEW.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260917-122500_HR_SYSTEM/review/REVIEW.md) |
| **ABAI-13** (`ABAI_20260917-123500_IS_RETROFIT`) | Сквозная интеграция требований УИС, регламентных сроков (SLA) и ответственности по ТК РК во внутренние акты (Фазы A, B, C: Академический, студенческий, научный, комплаенс, стратегия, ИТ, инфраструктура, безопасность, карьера — 34 акта) | 🟢 Выполнено (Фазы A, B, C — 34 акта) | `REV` / `DONE` | Coordinator / Reviewer | [`workspace/ABAI_20260917-123500_IS_RETROFIT/review/REVIEW_PHASE_C.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260917-123500_IS_RETROFIT/review/REVIEW_PHASE_C.md) |
| **ABAI-14** (`ABAI_20260917-174500_CULTURE_NPA`) | Разработка модуля внешних НПА сферы культуры, архивов, библиотечного дела и масс-медиа (МКИ РК) | 🟢 Выполнено (Фаза A: Модуль 10, Реестр 101 НПА) | `REV` / `DONE` | Coordinator / Reviewer | [`workspace/ABAI_20260917-174500_CULTURE_NPA/review/REVIEW.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260917-174500_CULTURE_NPA/review/REVIEW.md) |
| **ABAI-15** (`ABAI_20260918-100000_SCIENCE_ECOSYSTEM`) | Модернизация нормативной базы науки по новому Закону «О науке и технологической политике» № 103-VIII, TRL 1–9 | 🟢 Выполнено | `REV` / `DONE` | Coordinator / Reviewer | [`workspace/ABAI_20260918-100000_SCIENCE_ECOSYSTEM/review/REVIEW_PHASE_B.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260918-100000_SCIENCE_ECOSYSTEM/review/REVIEW_PHASE_B.md) |
| **ABAI-16** (`ABAI_20260919-124000_INTERNATIONAL`) | Разработка нормативной базы международного сотрудничества, академической мобильности и визового учета (Модуль 04, 115 НПА) | 🟢 Выполнено | `REV` / `DONE` | Coordinator / Reviewer | [`workspace/ABAI_20260919-124000_INTERNATIONAL/review/REVIEW_PHASE_B.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260919-124000_INTERNATIONAL/review/REVIEW_PHASE_B.md) |
| **ABAI-17** (`ABAI_20260921-122500_DIPLOMA_SOP`) | Регламент (СОП) генерации, выдачи и 75-летнего архивного учета дипломов собственного образца с QR-кодами ЕПВО | 🟢 Выполнено | `REV` / `DONE` | Coordinator / Reviewer | [`workspace/ABAI_20260921-122500_DIPLOMA_SOP/review/REVIEW.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260921-122500_DIPLOMA_SOP/review/REVIEW.md) |
| **ABAI-18** (`ABAI_20260921-143000_CSS_ITSM`) | Трансформация ЦОС в Единый сервисный центр обучающихся и сотрудников с интеграцией ITIL v4 / ITSM Service Desk | 🟢 Выполнено | `REV` / `DONE` | Coordinator / Reviewer | [`workspace/ABAI_20260921-143000_CSS_ITSM/review/REVIEW.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260921-143000_CSS_ITSM/review/REVIEW.md) |
| **ABAI-19** (`ABAI_20260921-153500_FIN_SYSTEM`) | Комплексная нормативная база финансового блока (ПЭД, Госзакупки № 106-VIII, Бухучет по МСФО, ДИ Главбуха и бухгалтеров, СОП инвентаризации МФ РК № 562) | 🟢 Выполнено (Фазы A и B) | `DONE` | Coordinator / Reviewer | [`workspace/ABAI_20260921-153500_FIN_SYSTEM/review/REVIEW_PHASE_B.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260921-153500_FIN_SYSTEM/review/REVIEW_PHASE_B.md) |
| **ABAI-20** (`ABAI_20260921-170500_SECTOR_STANDARDS`) | Обогащение и углубление Специальных отраслевых нормативных стандартов ОВПО и науки РК (ГОСО № 2, ECTS № 152, СУР № 166/116, PhD № 127, звания № 128, Профстандарт № 374, ESG 2015, Законы о науке и образовании — 10 стандартов) | 🟢 Выполнено (Фазы A и B) | `DONE` | Coordinator / Reviewer | [`workspace/ABAI_20260921-170500_SECTOR_STANDARDS/review/REVIEW_PHASE_B.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260921-170500_SECTOR_STANDARDS/review/REVIEW_PHASE_B.md) |
| **ABAI-21** (`ABAI_20260921-173000_FOUNDATION`) | Институциональная и нормативная модель Факультета довузовской подготовки и Центра Foundation (117 НПА, отраслевой стандарт № 554/№ 122, Положение, Правила учебного процесса, статус «слушатель», 3 ДИ) | 🟢 Выполнено | `DONE` | Coordinator / Reviewer | [`workspace/ABAI_20260921-173000_FOUNDATION/review/REVIEW.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260921-173000_FOUNDATION/review/REVIEW.md) |


---

## 📁 Структура репозитория

```text
├── .tfw/                           # Ядро методологии TFW v3.4.0
│   ├── VERSION                     # Текущая версия (3.4.0)
│   ├── CHANGELOG.md                # Полный журнал версий TFW
│   ├── project_config.yaml         # Конфигурация проекта, Scope Budget и роли
│   ├── conventions.md              # Соглашения, стандарты и правила Evidence Layer
│   ├── glossary.md                 # Глоссарий терминов высшего образования РК и TFW
│   ├── templates/                  # Шаблоны артефактов (HL, RES, TS, ONB, RF, EV, REVIEW, Положения, ДИ)
│   ├── workflows/                  # Канонические процессы (plan, handoff, review, resume, docs, knowledge, update...)
│   └── adapters/                   # Адаптеры для AI-инструментов (Antigravity, Claude Code, Cursor, Codex)
├── .agents/                        # Канонический корень настроек агентов (правила, воркфлоу, скиллы)
├── .agent/                         # Обратная совместимость для Antigravity
├── docs/                           # Предметная документация и базы данных
│   ├── generic_framework/         # Универсальный тиражируемый фреймворк ВНД и цифровой профиль ОВПО
│   ├── regulations/                # Реестр и 9 аналитических модулей НПА РК (91+ актов РЧЛ)
│   ├── functions_and_powers/       # Каталог функций университета по 10 функциональным доменам
│   ├── internal_acts/              # Разработанные проекты внутренних НПА (Reference Case: Abai University)
│   └── kpi_and_metrics/            # Фонд KPI МНВО РК, Программы развития и дорожные карты разрывов
├── workspace/                      # Артефакты задач жизненного цикла TFW
├── AGENTS.md                       # Ролевые протоколы и поведение ИИ-агентов
├── KNOWLEDGE.md                    # Сводная база верифицированных знаний проекта
├── TECH_DEBT.md                    # Реестр нормативных и процессных разрывов (Regulatory Debt)
└── README.md                       # Главная страница и Task Board
```
