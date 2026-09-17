# REVIEW — ABAI_20260917-123500_IS_RETROFIT: Экспертное заключение по сквозной интеграции требований УИС и SLA в академический и студенческий блок (Фаза A)

> **Date**: 2026-09-17  
> **Reviewer**: Reviewer  
> **Task ID**: `ABAI_20260917-123500_IS_RETROFIT` (Phase A)  
> **Scope**: Сквозная интеграция требований УИС, регламентных сроков (SLA) и дисциплинарной ответственности по Трудовому кодексу РК в 12 актов академического и студенческого контура (ABAI-13)  
> **Final Verdict**: `✅ APPROVE`  

---

## 1. Резюме аудита

Проведен детальный независимый аудит внесенных изменений в 12 актов по 4-этапной модели TFW v3.4.0 (`Map ➔ Verify ➔ Judge ➔ Decide`).

### Результаты проверок по стадиям:
- **1. Map (Картирование):**
  - Все 12 целевых файлов проверены на наличие внесенных дополнений;
  - Проверены связи с эталонным профилем УИС (`01_university_is_reference_blueprint.md`), матрицей интеграции (`02_digital_to_job_integration_matrix.md`) и регламентом взаимодействия (`03_sop_digital_governance_and_sla.md`);
  - Артефакт доказательств: [`evidence/EV__IS_RETROFIT_PHASE_A.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260917-123500_IS_RETROFIT/evidence/EV__IS_RETROFIT_PHASE_A.md) подтверждает вердикт `6/6 VERIFIED`.

- **2. Verify (Верификация норм и дедлайнов):**
  - **Положения академического блока (ДАВ, ОР, Институт, Кафедра):**
    - В каждом акте создан стандартизированный раздел «Регламентация деятельности в университетской информационной системе («[V_PRIMARY_EDTECH_PLATFORM]»)»;
    - Четко определены роли в ролевой модели RBAC (`Academic_Administrator`, `Curriculum_Validator`, `Registrar_SuperAdmin`, `Registrar_Operator`, `Dean_Director`, `Adviser_Coordinator`, `Department_Chair`);
    - Установлен прямой запрет на ведение параллельного бумажного документооборота.
  - **Должностная инструкция ППС (`jd_faculty_model.md`):**
    - Подтверждено наличие точных регламентных сроков: силлабусы — за 10 дней до семестра; текущий контроль — **в течение 48 часов**; закрытие экзаменационных ведомостей — **в течение 24 часов** с автоматической блокировкой;
    - Закреплена ответственность: повторное нарушение сроков влечет расторжение трудового договора по **подпункту 16) пункта 1 статьи 52 Трудового кодекса РК**; передача паролей — немедленное увольнение по ст. 52 ТК РК и санкции по ст. 79 КоАП РК.
  - **Должностные инструкции руководства ОР и ДАВ:**
    - Закреплена системная обязанность блокировки ведомостей по истечении 24 часов, проведение приказов по контингенту «день-в-день», ответственность за достоверность данных по ЕПВО/НОБД.
  - **Студенческий контур и общежития (`student_dormitories_regulation.md`, `jd_dormitory_manager.md`):**
    - Закреплен 100% цифровой регламент заселения строго по электронному ордеру с QR-кодом (срок 3 дня);
    - Установлена норма об увольнении коменданта по ст. 52 ТК РК за допуск без ордера УИС.
  - **Регламенты и СОПы (ИУП и Академическая честность):**
    - В `sop_individual_curriculum_and_schedule.md` закреплен запрет преподавателям допускать к занятиям студентов вне утвержденной группы УИС;
    - В `academic_integrity_policy.md` регламентирована 100% проверка работ в модуле «Антиплагиат», неизменяемость ведомостей и Audit Trail.
  - **Универсальность:** Во всех 12 файлах сохранены системные переменные `[V_...]`, локальные хардкоды отсутствуют.

- **3. Judge (Качество и непротиворечивость):**
  - Модернизация устранила исторический пробел, когда цифровые обязательства существовали только в ИТ-паспортах, но отсутствовали в персональных инструкциях сотрудников;
  - Положения и ДИ приобрели юридическую силу для правомерного привлечения к дисциплинарной ответственности по трудовому законодательству РК.

- **4. Decide (Решение):** `✅ APPROVE`.

---

## 2. Перечень утвержденных модернизированных актов

1. [`dav_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/dav_regulation.md) — Положение о Департаменте по академическим вопросам;
2. [`registrar_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/registrar_regulation.md) — Положение об Офисе регистратора;
3. [`institute_model_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/institute_model_regulation.md) — Типовое положение об Институте;
4. [`department_chair_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/department_chair_regulation.md) — Типовое положение о Кафедре;
5. [`youth_and_social_affairs_department_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/youth_and_social_affairs_department_regulation.md) — Положение о Департаменте по молодежной политике;
6. [`student_dormitories_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/student_dormitories_regulation.md) — Положение о студенческих общежитиях;
7. [`jd_faculty_model.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_faculty_model.md) — Типовая ДИ ППС;
8. [`jd_head_registrar.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_head_registrar.md) — ДИ Руководителя Офиса регистратора;
9. [`jd_director_dav.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_director_dav.md) — ДИ Директора Департамента по академическим вопросам;
10. [`jd_dormitory_manager.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_dormitory_manager.md) — ДИ Заведующего студенческим общежитием;
11. [`sop_individual_curriculum_and_schedule.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/sop_individual_curriculum_and_schedule.md) — Регламент формирования ИУП и расписания;
12. [`academic_integrity_policy.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/academic_integrity_policy.md) — Политика академической честности.

---

## 3. Итоговое предписание Координатору

Фаза A задачи `ABAI_20260917-123500_IS_RETROFIT` (`ABAI-13`) признана полностью завершенной.
Рекомендуется:
1. Зарегистрировать факт `FACT-025` в `KNOWLEDGE.md` о модернизации академического и студенческого блока и сквозной прошивке требований УИС, регламентных сроков (48 ч / 24 ч) и санкций ст. 52 ТК РК;
2. Обновить Task Board в `README.md` (статус Фазы A задачи ABAI-13: `🟢 Выполнено`).
