# Реестр внутренних нормативных актов [V_UNIVERSITY_SHORT_NAME]

Данный репозиторий содержит утвержденные и разрабатываемые проекты локальных нормативных актов [V_LEGAL_FORM] «[V_UNIVERSITY_FULL_NAME]».

## Структура директории

```text
docs/
├── generic_framework/   # Универсальный параметризованный фреймворк ВНД и цифровой профиль ОВПО РК
│   ├── 00_framework_adaptation_guide.md            # Руководство по адаптации для вузов РК
│   ├── 01_variable_registry_and_placeholders.md    # Реестр системных переменных и плейсхолдеров
│   ├── 02_reference_cases_architecture.md          # Архитектура эталонных кейсов (Abai & AITU)
│   └── digital/                                    # Цифровой контур и сквозная интеграция
│       ├── 01_university_is_reference_blueprint.md # Эталонный профиль УИС (22 модуля, ГТС, ЕПВО)
│       ├── 02_digital_to_job_integration_matrix.md # Матрица интеграции функций ИС в ДИ и Положения
│       └── 03_sop_digital_governance_and_sla.md    # Регламент (СОП) цифрового взаимодействия и SLA
└── internal_acts/
    ├── regulations/        # Положения о структурных подразделениях (Reference Case: Abai University)
    ├── job_descriptions/   # Должностные инструкции сотрудников (с интегрированными цифровыми обязанностями)
    ├── sops_and_rules/     # Регламенты процессов, стандарты операционных процедур (SOP)
    └── blueprints/         # Архитектурные паспорта и бенчмарки ([V_SIS_SYSTEM_NAME], AITU)
```

## Универсальный тиражируемый фреймворк ОВПО РК (`docs/generic_framework/`)
- 📘 [**Руководство по адаптации фреймворка для вузов РК**](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/generic_framework/00_framework_adaptation_guide.md) (модели НАО, АО, ТОО, РГП)
- 🗂️ [**Реестр системных переменных и плейсхолдеров**](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/generic_framework/01_variable_registry_and_placeholders.md) (`[V_...]`)
- 🏛️ [**Архитектура позиционирования эталонных кейсов**](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/generic_framework/02_reference_cases_architecture.md) ([V_UNIVERSITY_SHORT_NAME] & AITU)
- 💻 [**Эталонный функционально-технический профиль УИС (SIS Blueprint)**](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/generic_framework/digital/01_university_is_reference_blueprint.md) (22 модуля, 4 класс ИБ, ЕПВО/НОБД)
- 📑 [**Матрица сквозной интеграции функционала ИС в ДИ и Положения**](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/generic_framework/digital/02_digital_to_job_integration_matrix.md) (дедлайны, роли RBAC, ст. 22, 23, 52 ТК РК)
- ⏱️ [**Регламент (СОП) цифрового взаимодействия, SLA и достоверности данных**](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/generic_framework/digital/03_sop_digital_governance_and_sla.md)

---

## Текущий реестр разработанных актов (Reference Case: Abai University)

### 1. Положения о подразделениях (`regulations/`):
- [Положение о Департаменте по академическим вопросам](regulations/dav_regulation.md)
- [Положение об Офисе регистратора](regulations/registrar_regulation.md)
- [Типовое положение об Институте](regulations/institute_model_regulation.md)
- [Типовое положение о Кафедре](regulations/department_chair_regulation.md)
- [Положение о Департаменте науки](regulations/science_department_regulation.md)
- [Положение об Офисе коммерциализации и трансфера технологий (ликвидация DEBT-002)](regulations/commercialization_office_regulation.md)
- [Положение о Совете молодых ученых (СМУ) при Ректоре](regulations/young_scientists_council_regulation.md)
- [Типовое положение о НИИ / научной лаборатории](regulations/research_institute_model_regulation.md)
- [Положение об Антикоррупционной комплаенс-службе (ст. 16 Закона о коррупции)](regulations/compliance_service_regulation.md)
- [Положение о Комитете по обеспечению качества (QA Committee, стандарты ESG)](regulations/quality_assurance_committee_regulation.md)
- [Положение о Центре аккредитации и постаккредитационного мониторинга](regulations/accreditation_center_regulation.md)
- [Положение о Совете образовательных стейкхолдеров (EdTech & School Advisory Board)](regulations/edtech_advisory_board_regulation.md)
- [Положение об Управлении цифровизации](regulations/digitalization_department_regulation.md)
- [Положение об Управлении информационных технологий (УИТ)](regulations/it_infrastructure_department_regulation.md)
- [Сводный реестр 4-уровневой документации информационной безопасности (ISO 27001)](regulations/is_4level_security_registry.md)
- [Положение о Департаменте по воспитательной, социальной работе и молодежной политике](regulations/youth_and_social_affairs_department_regulation.md)
- [Положение о студенческих общежитиях и Комиссии по распределению мест](regulations/student_dormitories_regulation.md)
- [Положение о Центре карьеры и мониторинга трудоустройства выпускников](regulations/career_center_and_grant_employment_regulation.md)
- [Положение о Департаменте управления человеческими ресурсами (HR)](regulations/hr_department_regulation.md)

### 2. Должностные инструкции (`job_descriptions/`):
- [ДИ Директора Департамента по академическим вопросам](job_descriptions/jd_director_dav.md)
- [ДИ Руководителя Офиса регистратора](job_descriptions/jd_head_registrar.md)
- [Типовая ДИ ППС (треки Teaching и High-Research Teacher)](job_descriptions/jd_faculty_model.md)
- [ДИ Директора Департамента науки](job_descriptions/jd_director_science.md)
- [ДИ Руководителя Офиса коммерциализации](job_descriptions/jd_head_commercialization.md)
- [Типовая ДИ научного сотрудника и постдокторанта](job_descriptions/jd_researcher_model.md)
- [ДИ Антикоррупционного комплаенс-офицера](job_descriptions/jd_compliance_officer.md)
- [ДИ Руководителя Центра аккредитации и обеспечения качества](job_descriptions/jd_head_accreditation.md)
- [ДИ Начальника Управления цифровизации](job_descriptions/jd_head_digitalization.md)
- [ДИ Начальника Управления информационных технологий](job_descriptions/jd_head_it_infrastructure.md)
- [ДИ Директора Департамента стратегического развития](job_descriptions/jd_director_strategic_development.md)
- [ДИ Директора Департамента по воспитательной, социальной работе и молодежной политике](job_descriptions/jd_director_youth_social_affairs.md)
- [ДИ Руководителя Центра карьеры и мониторинга трудоустройства](job_descriptions/jd_head_career_center.md)
- [ДИ Заведующего студенческим общежитием (коменданта)](job_descriptions/jd_dormitory_manager.md)
- [ДИ Директора Департамента управления человеческими ресурсами (HR)](job_descriptions/jd_director_hr.md)
- [ДИ Специалиста по кадровому администрированию, воинскому учету и интеграции с ЕСУТД Enbek.kz](job_descriptions/jd_hr_recruitment_and_records_specialist.md)

### 3. Регламенты и СОП (`sops_and_rules/`):
- [Регламент формирования ИУП и расписания (ликвидация DEBT-001)](sops_and_rules/sop_individual_curriculum_and_schedule.md)
- [Регламент разработки MVP (TRL 1–4) в НИР и посевных грантов Seed Grants](sops_and_rules/sop_mvp_and_internal_grants.md)
- [Регламент расчета рейтинга исследовательской активности обучающихся (ROS)](sops_and_rules/sop_research_output_score.md)
- [Политика академической честности и Регламент Дисциплинарной комиссии](sops_and_rules/academic_integrity_policy.md)
- [Регламент проведения внутреннего анализа коррупционных рисков (ВАКР)](sops_and_rules/sop_anti_corruption_risk_assessment.md)
- [Регламент интеграционного взаимодействия с ЕПВО и НОБД (ликвидация DEBT-003)](sops_and_rules/sop_epvo_nobd_integration.md)
- [Регламент защиты персональных данных обучающихся и работников](sops_and_rules/sop_personal_data_protection.md)
- [Стандарт качества и сертификации цифрового образовательного контента (онлайн-курсов)](sops_and_rules/sop_online_courses_quality_standard.md)
- [Регламент разработки, каскадирования и мониторинга Стратегии развития](sops_and_rules/sop_university_development_strategy.md)
- [Регламент обязательного обучения, инструктажа по кибербезопасности и соблюдения требований ИБ работниками](sops_and_rules/sop_employee_cybersecurity_and_labor_safety.md)
- [Регламент применения методологии OKR и скоринга результативности](sops_and_rules/sop_okr_framework_and_scoring.md)
- [Регламент студенческого самоуправления и деятельности Комитета по делам молодежи (КДМ)](sops_and_rules/sop_student_government_and_kdm.md)
- [Регламент (СОП) открытого конкурсного замещения должностей ППС и ученых (Приказ МОН № 230)](sops_and_rules/sop_faculty_and_researcher_recruitment_competition.md)
- [Регламент (СОП) 7-классного грейдирования и Комиссии по оценке достижений ученых по Приказу МНВО № 424](sops_and_rules/sop_researcher_compensation_and_kdos_commission.md)

### 4. Модельные регламенты инноваций и архитектура (`blueprints/`):
- [Модельные регламенты на основе бенчмаркинга Astana IT University](blueprints/aitu_innovations_for_abai.md)
- [Архитектурный паспорт: Интегрированная автоматизированная система «[V_SIS_SYSTEM_NAME]» (22 модуля ТЗ для ГТС)](blueprints/abai_digital_platform_architecture.md)
- [Архитектурный паспорт: Стратегия развития [V_UNIVERSITY_SHORT_NAME] на 2026–2030 годы (5 направлений, 25 KPI)](blueprints/abai_strategy_2026_2030_architecture.md)

---

## Стандарты разработки
- Все документы разрабатываются строго по унифицированным шаблонам из `.tfw/templates/`.
- Каждый акт проходит этапы TFW: `HL → RES → TS → ONB → DEV → RF → REVIEW → KNW → DONE`.
- Обязательна проверка на юридическое соответствие НПА РК и исключение дублирования функций.

