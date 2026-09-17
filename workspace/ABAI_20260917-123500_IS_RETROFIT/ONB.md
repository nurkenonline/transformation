# ONB — ABAI_20260917-123500_IS_RETROFIT / Phase A: Сквозная интеграция требований УИС и SLA в академический и студенческий блок

> **Date**: 2026-09-17  
> **Author**: Executor  
> **Status**: 🟢 ONB_RESOLVED — Ready for execution  
> **Parent HL**: [HL-ABAI_20260917-123500_IS_RETROFIT](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260917-123500_IS_RETROFIT/HL.md)  
> **TS**: [TS Phase A](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260917-123500_IS_RETROFIT/TS.md)  

---

## 1. Understanding

Задача Фазы A заключается в содержательной модернизации 12 ключевых актов академического и студенческого блока (Положения о ДАВ, Офисе регистратора, Институтах, Кафедрах, молодежной политике, общежитиях; ДИ ППС, ДИ ОР, ДИ ДАВ, ДИ коменданта; СОПы ИУП и академической честности). Требуется дополнить их конкретными названиями модулей УИС («[V_PRIMARY_EDTECH_PLATFORM]»), разграничением ролей RBAC, строгими сроками (SLA: 48 ч на текущие оценки, 24 ч на экзаменационные ведомости, день-в-день на приказы, запрет заселения без электронного ордера в УИС) и нормами дисциплинарной и материальной ответственности по статьям 22, 23, 52, 120, 181, 182 Трудового кодекса РК.

---

## 2. Entry Points (12 файлов)

- `docs/internal_acts/regulations/dav_regulation.md` (AC-1)
- `docs/internal_acts/regulations/registrar_regulation.md` (AC-1)
- `docs/internal_acts/regulations/institute_model_regulation.md` (AC-1)
- `docs/internal_acts/regulations/department_chair_regulation.md` (AC-1)
- `docs/internal_acts/regulations/youth_and_social_affairs_department_regulation.md` (AC-4)
- `docs/internal_acts/regulations/student_dormitories_regulation.md` (AC-4)
- `docs/internal_acts/job_descriptions/jd_faculty_model.md` (AC-2)
- `docs/internal_acts/job_descriptions/jd_head_registrar.md` (AC-3)
- `docs/internal_acts/job_descriptions/jd_director_dav.md` (AC-3)
- `docs/internal_acts/job_descriptions/jd_dormitory_manager.md` (AC-4)
- `docs/internal_acts/sops_and_rules/sop_individual_curriculum_and_schedule.md` (AC-5)
- `docs/internal_acts/sops_and_rules/academic_integrity_policy.md` (AC-5)

---

## 3. Questions (blocking)

Вопросов нет. Матрица интеграции `02_digital_to_job_integration_matrix.md` и регламент `03_sop_digital_governance_and_sla.md` предоставляют детальный источник формулировок.

---

## 4. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|---|:---:|---|---|
| 1 | Трудовой кодекс РК (ст. 22, 23, 52, 120, 181, 182) | ✅ | Applied | Юридическая квалификация нарушений регламентов УИС |
| 2 | СТ РК 34.015-2002 и спецификации ТЗ ГТС (22 модуля) | ✅ | Applied | Единый глоссарий модулей УИС |
| 3 | Матрица цифровой интеграции (`02_digital_to_job_integration_matrix.md`) | ✅ | Applied | Базовый источник сроков SLA и ролей RBAC |
| 4 | Регламент цифрового взаимодействия (`03_sop_digital_governance_and_sla.md`) | ✅ | Applied | Протокол закрытия ведомостей и неизменяемости журнала |
| 5 | Закон РК «О персональных данных и их защите» (ст. 79 КоАП РК) | ✅ | Applied | Санкции за несанкционированную передачу учетных записей |

---

*ONB — ABAI_20260917-123500_IS_RETROFIT / Phase A | 2026-09-17*
