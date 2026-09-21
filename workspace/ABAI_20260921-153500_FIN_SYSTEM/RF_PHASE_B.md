# RF — ABAI_20260921-153500_FIN_SYSTEM / Phase B: Бухгалтерский учет по МСФО, расчетная политика и сохранность активов

> **Date**: 2026-09-21  
> **Author**: Executor / AI Normalization Specialist  
> **Status**: 🟢 RF — Complete  
> **Parent HL**: [HL-ABAI_20260921-153500_FIN_SYSTEM](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260921-153500_FIN_SYSTEM/HL.md)  
> **TS**: [TS Phase B](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260921-153500_FIN_SYSTEM/TS_PHASE_B.md)  

---

## 1. What Was Done

В рамках Фазы B задачи `ABAI-19` полностью разработан пакет внутренних нормативных актов для контура бухгалтерского учета, расчетов с персоналом и студентами, а также регламентации инвентаризации и сохранности активов:

### Actual Value-Bearing Accounting

| Fact | Actual result |
|---|---|
| TS approval ref | Approved by owner 2026-09-21 |
| VALUE membership | 5 файлов ВНД (1 положение, 3 ДИ, 1 СОП) |
| Arithmetic | 5 новых файлов VALUE; 0 удалено; ~890 строк |
| Membership deviations | Отклонений нет, 100% соответствие TS |
| Trigger disposition | В рамках Scope Budget (`new_files: 8`, `new_loc: 1200`) |

### New Files

| File | Description |
|---|---|
| [`docs/internal_acts/regulations/accounting_department_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/accounting_department_regulation.md) | Положение об Управлении бухгалтерского учета и отчетности (`REG-FIN-ACC-001`) |
| [`docs/internal_acts/job_descriptions/jd_chief_accountant.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_chief_accountant.md) | ДИ Главного бухгалтера (`JD-FIN-ACC-CHIEF-001`) |
| [`docs/internal_acts/job_descriptions/jd_accountant_payroll_and_stipends.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_accountant_payroll_and_stipends.md) | ДИ Ведущего бухгалтера расчетной группы (оплата труда и стипендии) (`JD-FIN-ACC-PAY-001`) |
| [`docs/internal_acts/job_descriptions/jd_accountant_materials_and_assets.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_accountant_materials_and_assets.md) | ДИ Ведущего бухгалтера материальной группы (ОС и ТМЦ) (`JD-FIN-ACC-MAT-001`) |
| [`docs/internal_acts/sops_and_rules/sop_annual_asset_inventory.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/sop_annual_asset_inventory.md) | СОП проведения годовой сплошной инвентаризации активов и материальных ценностей (`SOP-FIN-INVENT-001`) |
| [`workspace/ABAI_20260921-153500_FIN_SYSTEM/evidence/EV__FIN_SYSTEM_PHASE_B.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260921-153500_FIN_SYSTEM/evidence/EV__FIN_SYSTEM_PHASE_B.md) | Протокол доказательств по критериям приемки Фазы B |

---

## 2. Key Decisions

1. **Гарантии профессиональной независимости Главного бухгалтера:** В Положении об Управлении и ДИ Главбуха нормативно закреплено право второй подписи и положение п. 4 ст. 8 Закона РК «О бухгалтерском учете и финансовой отчетности» (в случае незаконного письменного распоряжения руководства единоличную ответственность несет руководитель).
2. **Интеграция с ЕПВО (Протокол 4):** В ДИ Расчетного бухгалтера строго регламентирован порядок автоматизированной сверки контингента обучающихся-грантников для безошибочного начисления стипендий и закрытия актов финансирования с АО «Финансовый центр».
3. **Персональная материальная ответственность:** По статьям 120, 123 ТК РК во все инструкции и регламенты включены механизмы обеспечения сохранности активов и обязательного заключения договоров МОЛ.
4. **Стандартизация Альбома форм МФ РК № 562:** В СОП инвентаризации активов внедрена обязательная унифицированная матрица форм первичных документов (Инв-1, Инв-2, Инв-3, ОС-3, З-6) и порядок утилизации компьютерного лома с содержанием драгметаллов.

---

## 3. Acceptance Criteria

- [x] AC-1: Положение об Управлении бухгалтерского учета и отчетности разработано (`accounting_department_regulation.md`).
- [x] AC-2: ДИ Главного бухгалтера разработана (`jd_chief_accountant.md`).
- [x] AC-3: ДИ Ведущего бухгалтера расчетной группы разработана (`jd_accountant_payroll_and_stipends.md`).
- [x] AC-4: ДИ Ведущего бухгалтера материальной группы разработана (`jd_accountant_materials_and_assets.md`).
- [x] AC-5: СОП годовой сплошной инвентаризации активов разработан (`sop_annual_asset_inventory.md`).
- [x] AC-6: Универсальность и параметризация: 0 плейсхолдеров, корректные переменные `[V_...]`.

---

## 4. Evidence Summary

См. [EV__FIN_SYSTEM_PHASE_B.md](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260921-153500_FIN_SYSTEM/evidence/EV__FIN_SYSTEM_PHASE_B.md).  
Вердикт доказательств: **6/6 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A**.

---

*RF — ABAI_20260921-153500_FIN_SYSTEM / Phase B | 2026-09-21*
