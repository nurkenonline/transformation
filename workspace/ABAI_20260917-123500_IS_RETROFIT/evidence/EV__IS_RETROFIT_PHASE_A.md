# EV — ABAI_20260917-123500_IS_RETROFIT: Сквозная интеграция требований УИС и SLA в академический и студенческий блок (Фаза A)

> **Date**: 2026-09-17  
> **Author**: Executor  
> **Task**: ABAI_20260917-123500_IS_RETROFIT (Phase A)  
> **TS**: [TS Phase A](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260917-123500_IS_RETROFIT/TS.md)  

---

## Environment

| Field | Value |
|---|---|
| OS | Windows (NT 10.0) |
| Framework | Trace-First Workflow (TFW v3.4.0) |
| Legal / Standard Basis | Трудовой кодекс РК (ст. 22, 23, 52, 120, 181, 182), СТ РК 34.015-2002, ТЗ ГТС (22 модуля) |
| Digital Matrix Reference | `docs/generic_framework/digital/02_digital_to_job_integration_matrix.md`, `03_sop_digital_governance_and_sla.md` |

---

## Evidence Table

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|---|---|
| E1 | AC-1 | Добавлен специальный раздел «Регламентация деятельности в УИС» в 4 положениях академического ядра: `dav_regulation.md`, `registrar_regulation.md`, `institute_model_regulation.md`, `department_chair_regulation.md`. Закреплены роли RBAC, модули «Академический процесс», «Офис регистратора», «Силлабусы», «Эдвайзер», «Приказы», запрещено параллельное бумажное дублирование. | Workspace / TFW | **VERIFIED** | [`dav_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/dav_regulation.md), [`registrar_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/registrar_regulation.md), [`institute_model_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/institute_model_regulation.md), [`department_chair_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/department_chair_regulation.md) |
| E2 | AC-2 | Модернизирована типовая ДИ преподавателя (`jd_faculty_model.md`): зафиксированы жесткие SLA (выставление текущих оценок — **48 часов**, закрытие экзаменационной ведомости — **24 часа**, загрузка силлабуса — за 10 дней до семестра), категорический запрет передачи учетной записи/паролей, прямая дисциплинарная ответственность по ст. 22, 23, 52 (п. 1 пп. 16), 120, 181, 182 ТК РК. | Workspace / TFW | **VERIFIED** | [`jd_faculty_model.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_faculty_model.md) |
| E3 | AC-3 | Модернизированы ДИ руководящего состава ОР и ДАВ (`jd_head_registrar.md`, `jd_director_dav.md`): регламентированы функции системного контроля баз данных, блокировки ведомостей по истечении 24 часов, синхронизации с ЕПВО/НОБД, санкции по ТК РК и ст. 79 КоАП РК. | Workspace / TFW | **VERIFIED** | [`jd_head_registrar.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_head_registrar.md), [`jd_director_dav.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_director_dav.md) |
| E4 | AC-4 | Модернизирован студенческий контур и общежития (`youth_and_social_affairs_department_regulation.md`, `student_dormitories_regulation.md`, `jd_dormitory_manager.md`): внедрен жесткий запрет заселения без сгенерированного в модуле «Общежития» УИС электронного ордера с QR-кодом (срок 3 дня), установлена санкция увольнения коменданта по ст. 52 ТК РК за ручной допуск. | Workspace / TFW | **VERIFIED** | [`student_dormitories_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/student_dormitories_regulation.md), [`youth_and_social_affairs_department_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/youth_and_social_affairs_department_regulation.md), [`jd_dormitory_manager.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_dormitory_manager.md) |
| E5 | AC-5 | Модернизированы академические СОПы: в `sop_individual_curriculum_and_schedule.md` закреплен 100% цифровой выбор в модуле «Эдвайзер» и запрет преподавателям допускать незарегистрированных в УИС студентов; в `academic_integrity_policy.md` регламентирован модуль «Антиплагиат», неизменяемость цифровых журналов, блокировка ведомостей и Audit Trail. | Workspace / TFW | **VERIFIED** | [`sop_individual_curriculum_and_schedule.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/sop_individual_curriculum_and_schedule.md), [`academic_integrity_policy.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/academic_integrity_policy.md) |
| E6 | AC-6 | Проведена сплошная проверка на сохранение параметров `[V_...]` и отсутствие хардкодов конкретных вузов во всех 12 модифицированных файлах. | Workspace / TFW | **VERIFIED** | Grep analysis (0 matches) |

---

## Verdict

Evidence verdict: **6/6 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A**  
Все 12 файлов академического и студенческого блока успешно модернизированы, приведены в строгое соответствие с Трудовым кодексом РК и эталонным цифровым профилем УИС.

---

*EV — ABAI_20260917-123500_IS_RETROFIT / Phase A | 2026-09-17*
