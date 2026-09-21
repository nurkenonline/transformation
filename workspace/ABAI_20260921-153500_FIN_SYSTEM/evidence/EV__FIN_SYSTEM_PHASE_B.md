# EV — ABAI_20260921-153500_FIN_SYSTEM / Phase B: Бухгалтерский учет по МСФО, расчетная политика и сохранность активов

> **Date**: 2026-09-21  
> **Author**: Executor / AI Normalization Specialist  
> **Task**: ABAI-19 (`ABAI_20260921-153500_FIN_SYSTEM`)  
> **TS**: [TS Phase B](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260921-153500_FIN_SYSTEM/TS_PHASE_B.md)  

---

## Environment

| Field | Value |
|---|---|
| OS | Windows 11 Pro (10.0.26100) |
| Language / Runtime | Markdown / Python 3.11 |
| Deploy target | `docs/internal_acts/` |
| CI / Pipeline | Local verification |

---

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|:---:|---|
| E1 | AC-1 | Положение об Управлении бухучета и отчетности (`REG-FIN-ACC-001`): статус самостоятельного подразделения, учет по МСФО, Приказ МФ № 110, структура (4 группы), RACI-матрица, гарантии независимости (п. 4 ст. 8 Закона о бухучете) | Local filesystem | `VERIFIED` | [`accounting_department_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/accounting_department_regulation.md) |
| E2 | AC-2 | ДИ Главного бухгалтера (`JD-FIN-ACC-CHIEF-001`): право второй подписи, отказ от незаконных проводок, сертификат «Профессиональный бухгалтер РК», полная материальная ответственность по ст. 120, 123 ТК РК, защита ПДн | Local filesystem | `VERIFIED` | [`jd_chief_accountant.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_chief_accountant.md) |
| E3 | AC-3 | ДИ Ведущего бухгалтера расчетной группы (`JD-FIN-ACC-PAY-001`): расчет окладов и налогов, стипендиальное обеспечение через интеграцию с ЕПВО (Протокол 4) и АО «Финансовый центр», режим конфиденциальности ПДн (Закон № 94-V), ст. 120, 123 ТК РК | Local filesystem | `VERIFIED` | [`jd_accountant_payroll_and_stipends.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_accountant_payroll_and_stipends.md) |
| E4 | AC-4 | ДИ Ведущего бухгалтера материальной группы (`JD-FIN-ACC-MAT-001`): учет ОС по МСФО (IAS 16), НМА и ТМЦ, реестр договоров МОЛ по ст. 123 ТК РК, участие в инвентаризациях с формами МФ РК № 562, материальная ответственность | Local filesystem | `VERIFIED` | [`jd_accountant_materials_and_assets.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_accountant_materials_and_assets.md) |
| E5 | AC-5 | СОП годовой сплошной инвентаризации активов (`SOP-FIN-INVENT-001`): порядок ЦИК и РИК, таймлайн, натурная проверка кассы, складов, лабораторий, урегулирование дельт, списание по актам ОС-3/З-6, формы МФ РК № 562 (Инв-1, Инв-2, Инв-3), утилизация драгметаллов | Local filesystem | `VERIFIED` | [`sop_annual_asset_inventory.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/sop_annual_asset_inventory.md) |
| E6 | AC-6 | Универсальность и чистота: проверено отсутствие конструкций `[TODO]`, `[TBD]`, корректность использования системных переменных `[V_...]` | Ripgrep | `VERIFIED` | 0 совпадений по TODO/TBD |

---

## Verdict

Evidence verdict: **6/6 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A**

---

*EV — ABAI_20260921-153500_FIN_SYSTEM / Phase B | 2026-09-21*
