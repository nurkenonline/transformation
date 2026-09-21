# Домен 10: Человеческий капитал и управление персоналом (Human Capital & HR)

## 1. Архитектурная модель и организационный контур домена

Контур управления человеческими ресурсами Университета ориентирован на привлечение и удержание талантов, прозрачный конкурсный отбор и соблюдение трудового законодательства Республики Казахстан:
1. **Департамент управления человеческими ресурсами (HR):** Формирование кадровой политики, планирование потребности в персонале, организация открытых конкурсов на занятие должностей ППС и исследователей, оценка эффективности, повышение квалификации и кадровое делопроизводство.
2. **Университетская конкурсная комиссия:** Открытый коллегиальный отбор профессорско-преподавательского состава по Приказу МОН РК № 230 с квотой внешних экспертов $\ge 40\%$ и разделением на академические треки (Teaching Track и High-Research Teacher).
3. **Комиссия по оценке достижений ученых ($K_{дос}$):** Постоянно действующий экспертный орган под председательством Проректора по науке, начисляющий персональные повышающие коэффициенты (от 1.0 до 1.5) по Приказу МНВО РК № 424 от 04.09.2026.
4. **Сектор кадрового администрирования и воинского учета:** Оперативный кадровый учет, обязательная регистрация трудовых договоров в ЕСУТД Enbek.kz в течение 3 рабочих дней (ст. 23 ТК РК) и воинский учет военнообязанных.

---

## 2. Реестр функций домена

| Код функции | Наименование функции | Основание в НПА РК | Ответственный (Accountable) | Соисполнители (Responsible) | Реализующий ВНД |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `FUNC-HR-RECRUIT-001`| Открытый конкурсный отбор ППС и научных сотрудников (Приказ МОН № 230) | Закон «Об образовании» (ст. 52), Закон «О науке», Приказ № 230 | Директор Департамента HR | Конкурсная комиссия, Институты, Кафедры | [`sop_faculty_and_researcher_recruitment_competition.md`](../internal_acts/sops_and_rules/sop_faculty_and_researcher_recruitment_competition.md), [`hr_department_regulation.md`](../internal_acts/regulations/hr_department_regulation.md) |
| `FUNC-HR-TRACK-002`  | Дифференциация и администрирование треков ППС (Teaching Track vs Research Track) | Закон РК «О статусе педагога», Приказ МОН № 230 | Директор Департамента HR | Проректор по академической деятельности, Проректор по науке | [`sop_faculty_and_researcher_recruitment_competition.md`](../internal_acts/sops_and_rules/sop_faculty_and_researcher_recruitment_competition.md), [`jd_faculty_model.md`](../internal_acts/job_descriptions/jd_faculty_model.md) |
| `FUNC-HR-GRADE-003`  | 7-классная классификация должностей ученых и базовые оклады по Приказу МНВО № 424 | Приказ и.о. МНВО № 592, Приказ МНВО РК № 424 от 04.09.2026 | Директор Департамента HR | Директор Департамента науки, ПЭД, Бухгалтерия | [`sop_researcher_compensation_and_kdos_commission.md`](../internal_acts/sops_and_rules/sop_researcher_compensation_and_kdos_commission.md) |
| `FUNC-HR-KDOS-004`   | Оценка персональных достижений ученых и начисление коэффициента $K_{дос}$ (1.0–1.5) | Приказ МНВО РК № 424 от 04.09.2026 | Проректор по науке (Председатель комиссии) | Директор HR, Директор Департамента науки | [`sop_researcher_compensation_and_kdos_commission.md`](../internal_acts/sops_and_rules/sop_researcher_compensation_and_kdos_commission.md) |
| `FUNC-HR-ENBEK-005`  | Регистрация и учет трудовых договоров в ЕСУТД Enbek.kz (дедлайн $\le 3$ рабочих дней) | Трудовой кодекс РК (ст. 23), Приказ МТСЗН № 353, КоАП (ст. 98) | Директор Департамента HR | Специалист по кадровому администрированию | [`jd_hr_recruitment_and_records_specialist.md`](../internal_acts/job_descriptions/jd_hr_recruitment_and_records_specialist.md) |
| `FUNC-HR-QUAL-006`   | Мониторинг соответствия ППС квалификационным требованиям МОН/МНВО № 391 | Приказ МОН РК № 338, Приказ МОН № 391 | Директор Департамента HR | Департамент обеспечения качества, Кафедры | [`hr_department_regulation.md`](../internal_acts/regulations/hr_department_regulation.md), [`jd_director_hr.md`](../internal_acts/job_descriptions/jd_director_hr.md) |
| `FUNC-HR-TRAIN-007`  | Организация непрерывного повышения квалификации ППС (не реже 1 раза в 3 года) | Закон РК «Об образовании» (ст. 51), Квалтребования № 391 | Руководитель сектора развития персонала | Институты, Кафедры | [`hr_department_regulation.md`](../internal_acts/regulations/hr_department_regulation.md) |
| `FUNC-HR-MILITARY-008`| Персональный воинский учет военнообязанных и призывников, отчетность в УДО | Закон «О воинской службе и статусе военнослужащих», КоАП (ст. 643) | Специалист по кадровому администрированию | Служба безопасности и ГО, УДО | [`jd_hr_recruitment_and_records_specialist.md`](../internal_acts/job_descriptions/jd_hr_recruitment_and_records_specialist.md) |
| `FUNC-HR-CYBER-009`  | Инструктажи и проверки знаний по охране труда (БиОТ) и информационной безопасности | Трудовой кодекс РК (ст. 22, 23, 181, 182), ПП РК № 832 | Директор Департамента HR | Служба ИБ, Инженер по БиОТ | [`sop_employee_cybersecurity_and_labor_safety.md`](../internal_acts/sops_and_rules/sop_employee_cybersecurity_and_labor_safety.md) |
| `FUNC-HR-DATA-010`   | Защита персональных данных сотрудников и конфиденциальность кадровых дел | Закон РК «О персональных данных и их защите», КоАП РК (ст. 79) | Директор Департамента HR | Все специалисты Департамента HR, Служба ИБ | [`sop_personal_data_protection.md`](../internal_acts/sops_and_rules/sop_personal_data_protection.md), [`guidelines_personal_data_in_job_descriptions.md`](../internal_acts/sops_and_rules/guidelines_personal_data_in_job_descriptions.md) |

---

## 3. Реестр локальных нормативных актов домена

1. **Положения о подразделениях:**
   - [`REG-HR-DEPT-001` Положение о Департаменте управления человеческими ресурсами (HR)](../internal_acts/regulations/hr_department_regulation.md)

2. **Должностные инструкции:**
   - [`JD-HR-DIR-001` ДИ Директора Департамента управления человеческими ресурсами (HR)](../internal_acts/job_descriptions/jd_director_hr.md)
   - [`JD-HR-REC-SPEC-001` ДИ Специалиста по кадровому администрированию, воинскому учету и ЕСУТД Enbek.kz](../internal_acts/job_descriptions/jd_hr_recruitment_and_records_specialist.md)

3. **Стандарты операционных процедур (СОП) и методические руководства:**
   - [`SOP-HR-RECRUIT-001` Регламент (СОП) открытого конкурсного замещения должностей ППС и ученых (Приказ МОН № 230)](../internal_acts/sops_and_rules/sop_faculty_and_researcher_recruitment_competition.md)
   - [`SOP-HR-COMP-001` Регламент (СОП) 7-классного грейдирования и Комиссии по оценке достижений ученых по Приказу МНВО № 424](../internal_acts/sops_and_rules/sop_researcher_compensation_and_kdos_commission.md)
   - [`GUIDE-HR-LABOR-001` Руководство по интеграции новелл Трудового кодекса РК (4-дневка, шеринг, ЕСУТД)](../internal_acts/sops_and_rules/guidelines_labor_code_novelties_implementation.md)
   - [`GUIDE-HR-DATA-001` Методическое руководство по регламентации защиты персональных данных в ДИ (Закон № 94-V)](../internal_acts/sops_and_rules/guidelines_personal_data_in_job_descriptions.md)

---

## 4. Цифровой контур и функциональные модули УИС

1. **Модуль «Кадры и ППС»:** электронные личные карточки (Т-2), учет стажа, ученых званий и остепененности.
2. **Модуль «Приказы по личному составу»:** электронное визирование приказов о приеме, переводах, отпусках и увольнениях.
3. **Модуль «Личный кабинет соискателя»:** подача портфолио кандидатами на конкурс ППС онлайн.
4. **Интеграционный шлюз ЕСУТД Enbek.kz:** автоматическая передача данных трудовых договоров в государственную систему учета.
