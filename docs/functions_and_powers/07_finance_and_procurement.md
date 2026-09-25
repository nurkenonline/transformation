# Домен 07: Финансово-экономическая деятельность, бухгалтерский учет и государственные закупки (Finance & Procurement)

## 1. Архитектурная модель домена

В соответствии с институциональной реформой финансового блока (Вариант Б, задача `ABAI-19` / `ABAI_20260921-153500_FIN_SYSTEM`) и созданием высшего надзорного контура Совета директоров (задача `ABAI-27`) в Университете реализован принцип четкого разделения властей, операционного планирования, учета и независимого аудита:

1. **Совет директоров НАО и Комитет по аудиту:** Рассмотрение и утверждение пятилетнего Плана развития, годового бюджета, одобрение годовой финансовой отчетности по МСФО и отчетов внешних аудиторов (Big 4) по ст. 53 Закона об АО № 415-II.
2. **Служба внутреннего аудита (СВА):** Независимый аудит эффективности систем внутреннего контроля, целевого использования средств госзаказа и научных грантов (ГФ/ПЦФ), проверка процедур государственных закупок по Закону № 106-VIII (п. 2 ст. 61 Закона об АО).
3. **Планово-экономический департамент (ПЭД):** Стратегическое финансовое планирование, расчет себестоимости и стоимости кредита, формирование и мониторинг Плана развития НАО по Приказу МНЭ РК № 18/56, управление штатным расписанием.
4. **Управление государственных закупок (УГЗ):** Планирование и проведение процедур государственных закупок по новому Закону РК № 106-VIII от 01.07.2024, заключение договоров, администрирование электронных актов (ЭАВР) и изъятий для научных исследований по Приказу МНВО № 538.
5. **Управление бухгалтерского учета и отчетности (Бухгалтерия):** Сплошной бухгалтерский и налоговый учет по МСФО, расчет заработной платы и стипендий через ЕПВО (Протокол 4), учет активов, налоговая отчетность и проведение годовой инвентаризации по Приказам МФ РК № 241, 110, 562.

---

## 2. Реестр функций домена

| Код функции | Наименование функции | Основание в НПА РК | Ответственный (Accountable) | Соисполнители (Responsible) | Реализующий ВНД |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `FUNC-FIN-BOD-APPROVE-001` | Утверждение годовой финансовой отчетности, отчета внешнего аудитора и Плана развития НАО | Закон об АО (ст. 53), Приказ МНЭ № 18 | **Председатель Совета директоров** | Председатель Комитета по аудиту, Главный бухгалтер, Директор ПЭД | [`REG-GOV-BOD-001`](../internal_acts/regulations/board_of_directors_regulation.md), [`REG-GOV-COMMITTEES-001`](../internal_acts/regulations/board_committees_regulation.md) |
| `FUNC-FIN-BUDGET-002` | Формирование, корректировка и исполнение Плана развития (бюджета) НАО | Бюджетный кодекс РК, Закон «О госимуществе» (ст. 184), Приказ МНЭ № 18 | **Проректор по финансам / Директор ПЭД** | ПЭД, Бухгалтерия, УГЗ, Институты | [`SOP-FIN-BUDGET-001`](../internal_acts/sops_and_rules/sop_development_plan_budgeting.md), [`REG-FIN-PED-001`](../internal_acts/regulations/ped_department_regulation.md) |
| `FUNC-FIN-ACC-003` | Ведение бухгалтерского и налогового учета, расчет заработной платы и стипендий | Закон «О бухучете и финотчетности», Налоговый кодекс, Социальный кодекс РК, Приказ МФ № 241 | **Главный бухгалтер** | Расчетная группа Бухгалтерии, HR, ДАВ | [`REG-FIN-ACC-001`](../internal_acts/regulations/accounting_department_regulation.md), [`JD-FIN-ACC-PAY-001`](../internal_acts/job_descriptions/jd_accountant_payroll_and_stipends.md) |
| `FUNC-FIN-REP-004` | Составление и представление годовой и промежуточной финансовой отчетности по МСФО | Приказ МФ РК № 110, Закон «О бухучете», МСФО (IFRS) | **Главный бухгалтер** | Группа сводного учета Бухгалтерии, ПЭД | [`REG-FIN-ACC-001`](../internal_acts/regulations/accounting_department_regulation.md), [`JD-FIN-ACC-CHIEF-001`](../internal_acts/job_descriptions/jd_chief_accountant.md) |
| `FUNC-FIN-PROCURE-005` | Планирование и проведение процедур государственных закупок | Закон РК «О госзакупках» № 106-VIII от 01.07.2024, Приказ МНВО № 538 | **Начальник УГЗ** | УГЗ, Инициаторы заявок (Институты/Департаменты), ПЭД | [`REG-FIN-PROC-001`](../internal_acts/regulations/procurement_department_regulation.md), [`SOP-FIN-PROCURE-001`](../internal_acts/sops_and_rules/sop_procurement_interaction.md) |
| `FUNC-FIN-COMM-006` | Финансовое моделирование образовательных программ, расчет себестоимости кредита и тарифов | Закон РК «Об образовании», Критерии СУР МНВО/МНЭ | **Директор ПЭД** | ПЭД, ДАВ, Департамент науки | [`SOP-FIN-BUDGET-001`](../internal_acts/sops_and_rules/sop_development_plan_budgeting.md), [`JD-FIN-PED-BUDGET-001`](../internal_acts/job_descriptions/jd_economist_budget_planning.md) |
| `FUNC-FIN-AUDIT-007` | Независимый аудит финансовой отчетности, целевого расходования грантов и процедур госзакупок | Закон «Об АО» (ст. 61), Закон «О госаудите» № 392-V | **Руководитель Службы внутреннего аудита** | Аудиторы СВА, Главный бухгалтер, Директор ПЭД | [`REG-GOV-IAS-001`](../internal_acts/regulations/internal_audit_service_regulation.md), [`SOP-GOV-IAS-PLAN-EXEC-001`](../internal_acts/sops_and_rules/sop_internal_audit_planning_and_execution.md), [`JD-GOV-IAS-HEAD-001`](../internal_acts/job_descriptions/jd_head_internal_audit.md) |
| `FUNC-FIN-INVENT-008` | Учет движения активов, материальная ответственность и ежегодная сплошная инвентаризация | Приказ МФ РК № 562, Приказ МФ РК № 241, ст. 120, 123 ТК РК | **Главный бухгалтер** | Материальная группа Бухгалтерии, ЦИК, РИК, МОЛ | [`SOP-FIN-INVENT-001`](../internal_acts/sops_and_rules/sop_annual_asset_inventory.md), [`JD-FIN-ACC-MAT-001`](../internal_acts/job_descriptions/jd_accountant_materials_and_assets.md) |

---

## 3. Реестр локальных актов финансово-экономического блока

1. **Положения о подразделениях:**
   - [`REG-FIN-PED-001` Положение о Планово-экономическом департаменте](../internal_acts/regulations/ped_department_regulation.md)
   - [`REG-FIN-PROC-001` Положение об Управлении государственных закупок](../internal_acts/regulations/procurement_department_regulation.md)
   - [`REG-FIN-ACC-001` Положение об Управлении бухгалтерского учета и отчетности](../internal_acts/regulations/accounting_department_regulation.md)
   - [`REG-GOV-IAS-001` Положение о Службе внутреннего аудита](../internal_acts/regulations/internal_audit_service_regulation.md)

2. **Должностные инструкции:**
   - [`JD-FIN-PED-DIR-001` ДИ Директора Планово-экономического департамента (Главного экономиста)](../internal_acts/job_descriptions/jd_director_ped.md)
   - [`JD-FIN-PED-BUDGET-001` ДИ Ведущего экономиста по планированию и анализу бюджета](../internal_acts/job_descriptions/jd_economist_budget_planning.md)
   - [`JD-FIN-PROC-HEAD-001` ДИ Начальника Управления государственных закупок](../internal_acts/job_descriptions/jd_head_procurement.md)
   - [`JD-FIN-ACC-CHIEF-001` ДИ Главного бухгалтера](../internal_acts/job_descriptions/jd_chief_accountant.md)
   - [`JD-FIN-ACC-PAY-001` ДИ Ведущего бухгалтера расчетной группы (оплата труда и стипендии)](../internal_acts/job_descriptions/jd_accountant_payroll_and_stipends.md)
   - [`JD-FIN-ACC-MAT-001` ДИ Ведущего бухгалтера материальной группы (ОС и ТМЦ)](../internal_acts/job_descriptions/jd_accountant_materials_and_assets.md)
   - [`JD-GOV-IAS-HEAD-001` ДИ Руководителя Службы внутреннего аудита](../internal_acts/job_descriptions/jd_head_internal_audit.md)
   - [`JD-GOV-IAS-AUDITOR-001` ДИ Главного аудитора Службы внутреннего аудита](../internal_acts/job_descriptions/jd_internal_auditor.md)

3. **Стандарты операционных процедур (СОП):**
   - [`SOP-FIN-BUDGET-001` Регламент (СОП) формирования, корректировки и исполнения Плана развития (бюджета) НАО](../internal_acts/sops_and_rules/sop_development_plan_budgeting.md)
   - [`SOP-FIN-PROCURE-001` Регламент (СОП) взаимодействия структурных подразделений с УГЗ](../internal_acts/sops_and_rules/sop_procurement_interaction.md)
   - [`SOP-FIN-INVENT-001` Регламент (СОП) проведения годовой сплошной инвентаризации активов и материальных ценностей](../internal_acts/sops_and_rules/sop_annual_asset_inventory.md)
   - [`SOP-GOV-IAS-PLAN-EXEC-001` Регламент планирования, проведения внутренних аудитов и мониторинга устранения нарушений](../internal_acts/sops_and_rules/sop_internal_audit_planning_and_execution.md)
