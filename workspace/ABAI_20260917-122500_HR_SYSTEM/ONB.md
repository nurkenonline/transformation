# ONB — ABAI_20260917-122500_HR_SYSTEM / Phase A: Нормативная база кадрового блока (HR), конкурсного замещения ППС и 7-классной системы оплаты ученых по Приказу МНВО № 424

> **Date**: 2026-09-17  
> **Author**: Executor  
> **Status**: 🟢 ONB_RESOLVED — Ready for execution  
> **Parent HL**: [HL-ABAI_20260917-122500_HR_SYSTEM](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260917-122500_HR_SYSTEM/HL.md)  
> **TS**: [TS Phase A](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260917-122500_HR_SYSTEM/TS.md)  

---

## 1. Understanding

Задача заключается в создании целостного комплекса модельных внутренних нормативных актов для кадрового блока (HR) ОВПО Республики Казахстан. Комплекс включает Положение о Департаменте HR (с матрицей RACI и правами в модулях УИС), Регламент открытого конкурсного замещения должностей ППС и ученых (Приказ МОН РК № 230 с дифференциацией Teaching/Research треков), СОП дифференцированной оплаты труда научных работников по 7 классам должностей и регламент Комиссии по оценке достижений ($K_{дос}$ 1.0–1.5) по Приказу МНВО РК № 424 от 04.09.2026 (дедлайн 22.09.2026), а также две модельные должностные инструкции (Директор HR и Специалист по кадровому учету / Enbek.kz со строгим SLA по ст. 23 ТК РК). Все документы должны быть разработаны в директориях `docs/internal_acts/` с использованием системных переменных `[V_...]` без локальных хардкодов.

---

## 2. Entry Points

- `docs/internal_acts/regulations/hr_department_regulation.md` (AC-1)
- `docs/internal_acts/sops_and_rules/sop_faculty_and_researcher_recruitment_competition.md` (AC-2)
- `docs/internal_acts/sops_and_rules/sop_researcher_compensation_and_kdos_commission.md` (AC-3)
- `docs/internal_acts/job_descriptions/jd_director_hr.md` (AC-4)
- `docs/internal_acts/job_descriptions/jd_hr_recruitment_and_records_specialist.md` (AC-5)
- `docs/functions_and_powers/10_human_capital_and_hr.md` (AC-6)
- `docs/generic_framework/01_variable_registry_and_placeholders.md` (AC-7)

---

## 3. Questions (blocking)

Вопросов, блокирующих разработку, нет. Спецификация TS полностью детализирована, нормативная база определена.

---

## 4. Recommendations (suggestions, not blocking)

1. В СОПе по Приказу № 424 предусмотреть готовое Приложение 1 с формой Оценочного листа соискателя на установление коэффициента $K_{дос}$, чтобы вузы могли сразу использовать форму в работе Комиссии.
2. В ДИ специалиста четко разграничить ответственность по ЕСУТД Enbek.kz и воинскому учету, сославшись на статьи 23 и 52 Трудового кодекса РК и Закон РК «О воинской службе и статусе военнослужащих».

---

## 5. Risks Found

1. **Риск дедлайна (22.09.2026):** Вступающий в силу Приказ МНВО РК № 424 требует создания Комиссии вуза заблаговременно. Разработанный СОП должен содержать готовый проект распорядительного акта руководителя о формировании Комиссии.

---

## 6. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|---|:---:|---|---|
| 1 | Трудовой кодекс РК (ст. 22, 23, 52, 120, 181, 182) | ✅ | Applied | Юридическая основа прав, обязанностей, SLA по Enbek.kz и ответственности |
| 2 | Приказ МОН РК № 230 | ✅ | Applied | Правила конкурсного замещения должностей ППС и ученых |
| 3 | Приказ и.о. МНВО РК № 592 и Приказ МНВО РК № 424 | ✅ | Applied | 7 классов должностей и комиссия $K_{дос}$ |
| 4 | Приказ МОН РК № 338 | ✅ | Applied | Квалификационные характеристики должностей |
| 5 | `FACT-002`, `FACT-011`, `FACT-018`, `FACT-022`, `FACT-023` | ✅ | Applied | Общеуниверситетские факты из `KNOWLEDGE.md` |

---

*ONB — ABAI_20260917-122500_HR_SYSTEM / Phase A | 2026-09-17*
