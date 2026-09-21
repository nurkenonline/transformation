# RF — ABAI_20260921-153500_FIN_SYSTEM / Phase A: Планово-экономический блок, бюджетирование и государственные закупки

> **Date**: 2026-09-21  
> **Author**: Executor / AI Normalization Specialist  
> **Status**: 🟢 RF — Complete  
> **Parent HL**: [HL-ABAI_20260921-153500_FIN_SYSTEM](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260921-153500_FIN_SYSTEM/HL.md)  
> **TS**: [TS Phase A](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260921-153500_FIN_SYSTEM/TS.md)  

---

## 1. What Was Done

В рамках Фазы A задачи `ABAI-19` полностью разработан пакет внутренних нормативных актов для контура планирования и государственных закупок:

### Actual Value-Bearing Accounting

| Fact | Actual result |
|---|---|
| TS approval ref | Approved by owner 2026-09-21 |
| VALUE membership | 7 файлов ВНД (2 положения, 3 ДИ, 2 СОПа) |
| Arithmetic | 7 новых файлов VALUE; 0 удалено; ~1140 строк |
| Membership deviations | Отклонений нет, 100% соответствие TS |
| Trigger disposition | В рамках Scope Budget (`new_files: 8`, `new_loc: 1200`) |

### New Files

| File | Description |
|---|---|
| [`docs/internal_acts/regulations/ped_department_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/ped_department_regulation.md) | Положение о Планово-экономическом департаменте (`REG-FIN-PED-001`) |
| [`docs/internal_acts/regulations/procurement_department_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/procurement_department_regulation.md) | Положение об Управлении государственных закупок (`REG-FIN-PROC-001`) |
| [`docs/internal_acts/job_descriptions/jd_director_ped.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_director_ped.md) | ДИ Директора ПЭД / Главного экономиста (`JD-FIN-PED-DIR-001`) |
| [`docs/internal_acts/job_descriptions/jd_economist_budget_planning.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_economist_budget_planning.md) | ДИ Ведущего экономиста по планированию и анализу бюджета (`JD-FIN-PED-BUDGET-001`) |
| [`docs/internal_acts/job_descriptions/jd_head_procurement.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_head_procurement.md) | ДИ Начальника Управления государственных закупок (`JD-FIN-PROC-HEAD-001`) |
| [`docs/internal_acts/sops_and_rules/sop_development_plan_budgeting.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/sop_development_plan_budgeting.md) | СОП формирования и исполнения Плана развития НАО (`SOP-FIN-BUDGET-001`) |
| [`docs/internal_acts/sops_and_rules/sop_procurement_interaction.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/sop_procurement_interaction.md) | СОП взаимодействия структурных подразделений с УГЗ (`SOP-FIN-PROCURE-001`) |
| [`workspace/ABAI_20260921-153500_FIN_SYSTEM/evidence/EV__FIN_SYSTEM_PHASE_A.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260921-153500_FIN_SYSTEM/evidence/EV__FIN_SYSTEM_PHASE_A.md) | Протокол доказательств по критериям приемки Фазы A |

---

## 2. Key Decisions

1. **Реализация Варианта Б (обособленный ПЭД):** Функция финансового планирования, расчета тарифов и штатов нормативно отделена от Бухгалтерии и УГЗ, что исключает конфликт интересов при согласовании смет.
2. **Имплементация новелл Закона РК № 106-VIII от 01.07.2024 года:** В Положении об УГЗ и СОП взаимодействия закреплены жесткие антикоррупционные нормы к техспецификациям (запрет товарных знаков, персональная ответственность экспертов).
3. **Защита научных закупок по Приказу МНВО № 538:** В СОП закупок внедрен специальный ускоренный порядок приобретения товаров/услуг для научных проектов в соответствии с п. 2 ст. 4 Закона «О науке и технологической политике».
4. **Персональная ответственность:** В ДИ Начальника УГЗ закреплена ответственность по ст. 207 КоАП РК, а во все ДИ включены разделы по защите персональных данных по Закону № 94-V.

---

## 3. Acceptance Criteria

- [x] AC-1: Положение о Планово-экономическом департаменте разработано (`ped_department_regulation.md`).
- [x] AC-2: Положение об Управлении государственных закупок разработано (`procurement_department_regulation.md`).
- [x] AC-3: ДИ Директора ПЭД и Ведущего экономиста разработаны (`jd_director_ped.md`, `jd_economist_budget_planning.md`).
- [x] AC-4: ДИ Начальника УГЗ разработана (`jd_head_procurement.md`).
- [x] AC-5: СОП бюджетирования и Плана развития НАО разработан (`sop_development_plan_budgeting.md`).
- [x] AC-6: СОП взаимодействия по закупкам разработан (`sop_procurement_interaction.md`).
- [x] AC-7: Универсальность и параметризация: 0 плейсхолдеров, корректные переменные `[V_...]`.

---

## 4. Evidence Summary

См. [EV__FIN_SYSTEM_PHASE_A.md](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260921-153500_FIN_SYSTEM/evidence/EV__FIN_SYSTEM_PHASE_A.md).  
Вердикт доказательств: **7/7 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A**.

---

*RF — ABAI_20260921-153500_FIN_SYSTEM / Phase A | 2026-09-21*
