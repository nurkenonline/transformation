# Verify — "Are the claims true in Phase B?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.  
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"  
> Min verify ratio: 0.42  
> RF files claimed: 6  
> Files to verify: 6 of 6 (100% full audit)  

## Verification Log

### V1: `docs/internal_acts/regulations/internal_audit_service_regulation.md`
- **RF claim:** Положение о Службе внутреннего аудита (`REG-GOV-IAS-001`): 119 строк, 8 разделов, ст. 61 Закона об АО, подчинение только СД через Комитет по аудиту, объекты: МСФО, гранты, закупки.
- **Actual:** Файл существует, объем 119 строк, 8 разделов. П. 2.1 фиксирует подчинение СД. П. 2.3 гарантирует независимость от ректората. Раздел 3 охватывает СВК, МСФО, гранты ГФ/ПЦФ (Закон № 103-VIII) и госзакупки по Закону № 106-VIII. Раздел 4 дает право прямого доступа ко всем помещениям и базам данных.
- **Match:** ✅ Полное соответствие

### V2: `docs/internal_acts/job_descriptions/jd_head_internal_audit.md`
- **RF claim:** ДИ Руководителя СВА (`JD-GOV-IAS-HEAD-001`): 122 строки, 8 уровень НРК, сертификация госаудитора/CIA/ACCA, подчинение только СД.
- **Actual:** Файл существует, объем 122 строки, 6 разделов. Раздел 2: квалификация (8 ур. НРК, сертификаты госаудитора или CIA/ACCA/DipIFR, стаж $\ge 7$ лет). Раздел 3: обязанности по составлению риск-плана, руководству проверками, докладам Комитету по аудиту. Раздел 5: ответственность исключительно перед СД.
- **Match:** ✅ Полное соответствие

### V3: `docs/internal_acts/job_descriptions/jd_internal_auditor.md`
- **RF claim:** ДИ Главного аудитора СВА (`JD-GOV-IAS-AUDITOR-001`): 86 строк, 7 уровень НРК, стаж $\ge 3$ лет, проведение проверок.
- **Actual:** Файл существует, объем 86 строк, 6 разделов. Раздел 2: квалификационные требования (7 ур. НРК, стаж $\ge 3$ лет). Раздел 3: проведение аудиторских тестов, сбор доказательств, составление рабочих документов.
- **Match:** ✅ Полное соответствие

### V4: `docs/internal_acts/sops_and_rules/sop_internal_audit_planning_and_execution.md`
- **RF claim:** СОП проведения внутренних аудитов (`SOP-GOV-IAS-PLAN-EXEC-001`): 109 строк, 7-этапный цикл, Согласительное совещание, план CAP, матрица нарушений Red/Yellow/Green.
- **Actual:** Файл существует, объем 109 строк, 5 разделов. Раздел 2: визуализация 7 этапов. Раздел 3: пошаговое описание с уведомлением за 5 дней, 3 дня на разногласия и 10 дней на план CAP. Раздел 4: матрица классификации нарушений со сроками устранения.
- **Match:** ✅ Полное соответствие

### V5: `docs/functions_and_powers/06_governance_and_legal.md`
- **RF claim:** Гармонизация Домена 06: 73 строки, функции СД, Комитетов, Корпсекретаря и СВА, строго 1 Accountable на процесс.
- **Actual:** Файл существует, объем 73 строки. Раздел 1 дополнен описанием высших органов. В таблицу функций введены `FUNC-GOV-BOD-001`, `FUNC-GOV-AUDIT-COMM-002`, `FUNC-GOV-NOM-COMM-003`, `FUNC-GOV-STRAT-COMM-004`, `FUNC-GOV-CORPSEC-005`, `FUNC-GOV-IAS-006`. На каждую функцию назначен ровно 1 Accountable.
- **Match:** ✅ Полное соответствие

### V6: `docs/functions_and_powers/07_finance_and_procurement.md`
- **RF claim:** Гармонизация Домена 07: 52 строки, функции утверждения финотчетности СД и аудиторского контроля СВА.
- **Actual:** Файл существует, объем 52 строки. Введены `FUNC-FIN-BOD-APPROVE-001` и `FUNC-FIN-AUDIT-007` с привязкой к актам СВА. Назначен строго 1 Accountable.
- **Match:** ✅ Полное соответствие

## Commands Executed

| # | Command | Result |
|---|---|---|
| 1 | Проверка строк кода (LOC) и плейсхолдеров | 561 LOC суммарно по 6 файлам (лимит $\le 1200$). TODO: 0. |
| 2 | Анализ каталога `analyze_docs.py` | Total markdown documents: 184. |
| 3 | Проверка ссылок в каталоге | `Links with spaces: 0`. Все 184 ссылки валидны. |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|---|---|---|:---:|
| C1 | Подчиненность СВА Совету директоров | `REG-GOV-IAS-001` п. 2.1 | Закон РК от 13.05.2003 № 415-II ст. 61 | ✅ |
| C2 | Сертификация госаудитора | `JD-GOV-IAS-HEAD-001` п. 2.1 | Закон РК от 12.11.2015 № 392-V | ✅ |
| C3 | Аудит научных грантов по Закону о науке | `REG-GOV-IAS-001` п. 3.1 пп. 5 | Закон РК от 10.06.2024 № 103-VIII | ✅ |
| C4 | RACI дисциплина (1 Accountable) | `06_governance_and_legal.md` | `KNOWLEDGE.md` FACT-001 | ✅ |

## Discrepancies Found

No discrepancies.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|---|:---:|:---:|
| E1 | `evidence/EV_PHASE_B.md` | ✅ | ✅ Полное подтверждение всех 6 критериев AC-1 — AC-6 |
| E2 | Реестр `docs/internal_acts/README.md` | ✅ | ✅ Все 4 новых акта внесены |
| E3 | Каталог `docs/MASTER_DOCUMENT_CATALOG.md` | ✅ | ✅ Каталог актуализирован, 184 документа |

Stage complete: YES
