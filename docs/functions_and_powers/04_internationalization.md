# Домен 04: Интернационализация и международное сотрудничество (Internationalization)

## 1. Архитектурная модель и организационный контур домена

Международная деятельность Университета выстроена по передовой модели **«Smart Split»** (гибридное разделение функций Front-Office и Back-Office), исключающей миграционные риски и административные издержки:
1. **Департамент международного сотрудничества (ДМС / Back-Office):** Стратегическое академическое партнерство, заключение меморандумов и договоров с зарубежными вузами, координация внешней кредитной академической мобильности (Erasmus+, Mevlana), привлечение зарубежных ученых (Visiting Professors) и визовое делопроизводство.
2. **Визово-миграционный сектор ДМС и окно International Student Desk в ЦОС (Front-Office):** Первичный очный прием паспортов иностранных обучающихся и слушателей Foundation в ЦОС, экспресс-сканирование ($\le 2$ ч), передача в миграционную службу и нотификация в ИС «Визово-миграционный портал» (vmp.gov.kz) в течение 24–72 часов.
3. **Сектор международного образования Факультета Foundation:** Языковая подготовка иностранных граждан (РКИ, казахский, English), нострификационное сопровождение и взаимодействие с ДМС по учебным визам категории **C9** (`STD-RK-FOUND-001`).
4. **Институты и Кафедры:** Разработка программ академической мобильности с перезачетом кредитов по форме Learning Agreement и ведение совместных/двудипломных программ.

---

## 2. Реестр функций домена

| Код функции | Наименование функции | Основание в НПА РК | Ответственный (Accountable) | Соисполнители (Responsible) | Реализующий ВНД |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `FUNC-INTL-MOB-001` | Организация академической мобильности обучающихся и ППС с оформлением Learning Agreement | Приказ МНВО РК № 613, Приказ МОН № 152 | Директор Департамента международного сотрудничества (ДМС) | Координатор мобильности ДМС, ДАВ, Институты | [`sop_academic_mobility_process.md`](../internal_acts/sops_and_rules/sop_academic_mobility_process.md), [`jd_coordinator_academic_mobility.md`](../internal_acts/job_descriptions/jd_coordinator_academic_mobility.md) |
| `FUNC-INTL-PARTN-002`| Заключение, правовая экспертиза и мониторинг исполнения международных соглашений | Закон РК «О международных договорах РК» | Проректор по международному сотрудничеству | Директор ДМС, Юридический департамент, ДАВ | [`international_cooperation_department_regulation.md`](../internal_acts/regulations/international_cooperation_department_regulation.md) |
| `FUNC-INTL-DDP-003`  | Проектирование и сопровождение программ двудипломного и совместного образования | Типовые правила ОВПО № 595, стандарты ECTS | Директор ДАВ | ДМС, Институты, Зарубежные вузы | [`regulations_joint_and_double_degree_programs.md`](../internal_acts/sops_and_rules/regulations_joint_and_double_degree_programs.md) |
| `FUNC-INTL-VISA-004` | Первичный прием, сканирование и учет паспортов иностранных студентов и слушателей в ЦОС | ПП РК № 148, ст. 518 КоАП РК | Руководитель ЦОСиС | Специалист Front-Office ЦОС, Визовый сектор ДМС | [`sop_visa_and_migration_compliance.md`](../internal_acts/sops_and_rules/sop_visa_and_migration_compliance.md) |
| `FUNC-INTL-MIG-005`  | Регистрация в vmp.gov.kz, оформление учебных виз C9 (студенты и Foundation) и миграционный комплаенс | Приказ МИД/МВД № 11-1-2/555, `STD-RK-FOUND-001`, ст. 518 КоАП | Директор ДМС | Визовый сектор ДМС, Центр Foundation | [`sop_visa_and_migration_compliance.md`](../internal_acts/sops_and_rules/sop_visa_and_migration_compliance.md), [`jd_visa_and_migration_support_specialist.md`](../internal_acts/job_descriptions/jd_visa_and_migration_support_specialist.md) |
| `FUNC-INTL-PROF-006` | Привлечение зарубежных профессоров (Visiting Professors) без квоты ИРС (визы B10/C3) | Закон о миграции (ст. 36), Приказ МОН № 613 | Директор ДМС | Институты, Департамент науки, HR, Бухгалтерия | [`sop_visiting_professors_recruitment.md`](../internal_acts/sops_and_rules/sop_visiting_professors_recruitment.md) |

---

## 3. Реестр локальных нормативных актов домена

1. **Положения о подразделениях:**
   - [`REG-INTL-DEPT-001` Положение о Департаменте международного сотрудничества](../internal_acts/regulations/international_cooperation_department_regulation.md)
   - [`REG-ACAD-FOUND-001` Положение о Факультете довузовской подготовки / Центре Foundation](../internal_acts/regulations/foundation_department_regulation.md)

2. **Должностные инструкции:**
   - [`JD-INTL-DIR-001` ДИ Директора Департамента международного сотрудничества](../internal_acts/job_descriptions/jd_director_international_cooperation.md)
   - [`JD-INTL-MOB-COORD-001` ДИ Координатора академической мобильности](../internal_acts/job_descriptions/jd_coordinator_academic_mobility.md)
   - [`JD-INTL-VISA-SPEC-001` ДИ Специалиста по визово-миграционному сопровождению](../internal_acts/job_descriptions/jd_visa_and_migration_support_specialist.md)
   - [`JD-ACAD-FOUND-COORD-001` ДИ Методиста-координатора программ кандасов и иностранных слушателей](../internal_acts/job_descriptions/jd_foundation_coordinator.md)

3. **Стандарты операционных процедур (СОП) и аналитика:**
   - [`SOP-INTL-MOB-001` Регламент (СОП) академической мобильности обучающихся и ППС с Learning Agreement](../internal_acts/sops_and_rules/sop_academic_mobility_process.md)
   - [`SOP-INTL-VISA-MIG-001` Регламент (СОП) визово-миграционного учета и сопровождения иностранных граждан (v2.0 со Smart Split)](../internal_acts/sops_and_rules/sop_visa_and_migration_compliance.md)
   - [`SOP-INTL-PROF-001` Регламент (СОП) конкурсного привлечения зарубежных ученых (Visiting Professors)](../internal_acts/sops_and_rules/sop_visiting_professors_recruitment.md)
   - [`NOTE-INTL-SMART-SPLIT-001` Пояснительная записка для Правления: Оптимизация модели обслуживания иностранных студентов и минимизация визовых рисков](../internal_acts/blueprints/explanatory_note_international_students_service_and_visa_risks.md)

---

## 4. Цифровой контур и функциональные модули УИС

1. **Модуль «Международное сотрудничество и договоры»:** учет меморандумов, сроков действия соглашений и дорожных карт партнерства.
2. **Модуль «Академическая мобильность (Erasmus/EWP)»:** онлайн-подача заявок студентами, расчет рейтингового балла и цифровое формирование трехстороннего договора Learning Agreement.
3. **Модуль «Визовый учет и миграционный мониторинг»:** контроль 72-часовых сроков нотификации, автоматические уведомления о дедлайнах продления виз C9 (за 45 дней до истечения) и интеграция со шлюзами МВД РК.
