# EVIDENCE REPORT — ABAI_20260914-191500_ACAD: Нормативный пакет Академического блока

> **Task ID**: `ABAI_20260914-191500_ACAD`  
> **Date**: 2026-09-14  
> **Author**: Executor  
> **Status**: 🟢 VERIFIED (5/5)  
> **Reference TS**: [`TS-ABAI_20260914-191500_ACAD.md`](../TS-ABAI_20260914-191500_ACAD.md)

---

## 1. Summary of Acceptance Criteria Verification

| ID | Требование TS | Объект верификации | Фактическое подтверждение в артефакте | Статус |
|:---|:---|:---|:---|:---:|
| **AC-1** | Положения о ДАВ, ОР, Институте и Кафедре содержат RACI и нормативные ссылки (Приказ № 595, № 152, ГОСО № 2, № 391) | `dav_regulation.md`, `registrar_regulation.md`, `institute_model_regulation.md`, `department_chair_regulation.md` | Все 4 положения включают нормативную преамбулу с точными ссылками на законы РК и приказы МОН/МНВО, а также полные матрицы RACI (ровно 1 Accountable на процесс). | 🟢 VERIFIED |
| **AC-2** | Включение Startup Track в функции ДАВ и кафедр | `dav_regulation.md` (§ 4.2), `department_chair_regulation.md` (§ 4.3), `jd_director_dav.md` (§ 3.4) | Закреплена процедура сопровождения дипломных стартапов с критерием зрелости TRL ≥ 4 и привлечением венчурных трекеров в ГАК. | 🟢 VERIFIED |
| **AC-3** | Включение Интегрального GPA в задачи ОР и ДИ Руководителя ОР | `registrar_regulation.md` (§ 4.2), `jd_head_registrar.md` (§ 3.5) | Включена формула $GPA_{int} = (GPA \times 0.60) + (ROS \times 0.25) + (Social \times 0.15)$ и порядок её применения при формировании дипломов с отличием и рекомендаций. | 🟢 VERIFIED |
| **AC-4** | Устранение разрыва `DEBT-001` регламентом взаимодействия ИУП и расписания | `sop_individual_curriculum_and_schedule.md`, `TECH_DEBT.md` | Разработан 5-этапный регламент с таймлайном (mermaid sequence diagram), закреплены зоны исключительной ответственности ОР, институтов и эдвайзеров; в `TECH_DEBT.md` статус изменен на `🟢 Устранен`. | 🟢 VERIFIED |
| **AC-5** | Дифференциация нагрузки ППС (High-Research Teacher: 300–350 часов) | `jd_faculty_model.md` (§ 3.2), `department_chair_regulation.md` (§ 2.2) | Закреплен трек High-Research Teacher с педагогической нагрузкой 300–350 часов, обязательствами по публикациям Scopus/WoS Q1-Q2 и руководству проектами ГФ/ПЦФ. | 🟢 VERIFIED |

---

## 2. Traceability Matrix to Source Requirements

| Источник требований | Норма / Стандарт | Реализовано в локальном акте |
|:---|:---|:---|
| **Приказ МОН РК № 595** (п. 24) | Создание и функционирование Офиса регистратора | `docs/internal_acts/regulations/registrar_regulation.md` |
| **Приказ МОН РК № 152** | Кредитная технология обучения и регистрация на курсы | `docs/internal_acts/sops_and_rules/sop_individual_curriculum_and_schedule.md` |
| **Приказ МОН РК № 338** | Квалификационные характеристики должностей ППС | `docs/internal_acts/job_descriptions/jd_faculty_model.md` |
| **Приказ МОН РК № 230** | Конкурсное замещение должностей ППС и руководителей кафедр | `docs/internal_acts/regulations/department_chair_regulation.md` (§ 1.4) |
| **Опыт AITU (Бенчмаркинг)** | Startup Track, Интегральный GPA, High-Research Teacher | `dav_regulation.md`, `registrar_regulation.md`, `jd_faculty_model.md` |

---

## 3. Conclusion

Все 5 критериев приемки задачи `ABAI_20260914-191500_ACAD` проверены и полностью подтверждены фактическим содержимым нормативных документов. Нормативный долг `DEBT-001` ликвидирован. Пакет готов к утверждению.
