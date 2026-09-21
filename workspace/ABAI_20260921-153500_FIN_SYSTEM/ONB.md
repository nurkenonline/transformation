# ONB — ABAI_20260921-153500_FIN_SYSTEM / Phase A: Планово-экономический блок, бюджетирование и государственные закупки

> **Date**: 2026-09-21  
> **Author**: Executor / AI Normalization Specialist  
> **Status**: 🟢 ONB_COMPLETE — Ready for Implementation  
> **Parent HL**: [HL-ABAI_20260921-153500_FIN_SYSTEM](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260921-153500_FIN_SYSTEM/HL.md)  
> **TS**: [TS Phase A](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260921-153500_FIN_SYSTEM/TS.md)  

---

## 1. Understanding
В рамках Фазы A задачи ABAI-19 требуется институционализировать контур финансового планирования и государственных закупок университета: разработать Положение о Планово-экономическом департаменте (ПЭД) по Варианту Б, Положение об Управлении государственных закупок (УГЗ) по Закону № 106-VIII, должностные инструкции ключевых должностей (Директор ПЭД, Экономист по бюджету, Начальник УГЗ) и два регламентирующих СОПа (План развития НАО и взаимодействие по госзакупкам). Все акты должны быть взаимоувязаны через RACI-матрицы, исключать коррупционные риски и содержать разделы по защите персональных данных по Закону № 94-V.

---

## 2. Entry Points
- Шаблоны: `.tfw/templates/DEPARTMENT_REGULATION.md`, `.tfw/templates/JOB_DESCRIPTION.md`.
- Законодательные базы: `docs/regulations/05_governance_finance_compliance_npa.md`, `docs/regulations/09_strategic_planning_and_governance_npa.md`.
- Каталог функций: `docs/functions_and_powers/07_finance_and_procurement.md`.
- Гайд по ПДн: `docs/internal_acts/sops_and_rules/guidelines_personal_data_in_job_descriptions.md`.

---

## 3. Questions (blocking)
*Вопросов, блокирующих реализацию, нет. Все вводные согласованы в HL и TS.*

---

## 4. Recommendations
1. В Положении об УГЗ и СОП закупок прямо отразить изъятие п. 2 ст. 4 Закона «О науке и технологической политике» и Приказа МНВО № 538 для ускорения научных закупок.
2. В ДИ Начальника УГЗ предусмотреть обязательное наличие сертификата специалиста в сфере государственных закупок РК.

---

## 5. Risks Found
- Риск конфликта сроков: институты могут затягивать подачу ТЗ, срывая план закупок. В СОП необходимо закрепить жесткий дедлайн: подача ТЗ за 45 календарных дней до плановой даты закупки.

---

## 6. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|---|:---:|---|---|
| 1 | ТК РК ст. 120, 123 | ✅ | Applied | Включение норм ответственности в ДИ |
| 2 | Закон РК № 106-VIII | ✅ | Applied | Регламентация процедур УГЗ |
| 3 | Приказ МНЭ № 56 | ✅ | Applied | Методика Плана развития в СОП |
| 4 | Приказ МФ № 648 | ✅ | Applied | Правила государственных закупок |

---

### Material handover at this return
- **Producer unit**: Executor (AI Normalization Specialist)
- **Bounded context**: Задача ABAI-19 / Фаза A
- **Currentness**: Контекст изучен, шаблоны загружены, переход к реализации ВНД.

---

*ONB — ABAI_20260921-153500_FIN_SYSTEM / Phase A | 2026-09-21*
