# Map — "What was done in Phase B?"
> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.  
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"  
> RF: [RF_PHASE_B.md](../RF_PHASE_B.md)  
> TS: [TS_PHASE_B.md](../TS_PHASE_B.md)  

## Understanding

В рамках Фазы B задачи ABAI-27 разработан контрольно-надзорный контур высшего эшелона Университета и гармонизирован Каталог функций:
1. Разработано Положение о Службе внутреннего аудита (`REG-GOV-IAS-001`, 119 строк, ст. 61 Закона об АО № 415-II, подотчетность Совету директоров через Комитет по аудиту, независимость от ректората, объекты: МСФО, гранты ГФ/ПЦФ по Закону № 103-VIII, госзакупки по Закону № 106-VIII);
2. Разработана ДИ Руководителя СВА (`JD-GOV-IAS-HEAD-001`, 122 строки, 8 уровень НРК, сертификация госаудитора/CIA/ACCA);
3. Разработана ДИ Главного аудитора СВА (`JD-GOV-IAS-AUDITOR-001`, 86 строк, 7 уровень НРК);
4. Разработан СОП проведения риск-ориентированных внутренних аудитов (`SOP-GOV-IAS-PLAN-EXEC-001`, 109 строк, 7-этапный цикл, Согласительное совещание, план CAP);
5. Гармонизирован Каталог функций: Домен 06 (`06_governance_and_legal.md`, 6 новых функций СД, Комитетов, Корпсекретаря и СВА) и Домен 07 (`07_finance_and_procurement.md`) с жестким правилом одного Accountable на процесс.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|---|---|:---:|
| **AC-1:** Положение о Службе внутреннего аудита (ст. 61 Закона об АО, независимость, объекты) | Разработано `internal_audit_service_regulation.md` (119 строк) | ✅ |
| **AC-2:** ДИ Руководителя (8 ур. НРК, сертификация) и Главного аудитора СВА (7 ур. НРК) | Разработаны `jd_head_internal_audit.md` (122 стр.) и `jd_internal_auditor.md` (86 стр.) | ✅ |
| **AC-3:** СОП риск-ориентированного аудита (7 этапов, CAP, классификация нарушений) | Разработано `sop_internal_audit_planning_and_execution.md` (109 стр.) | ✅ |
| **AC-4:** Гармонизация Домена 06 (функции СД, Комитетов, Корпсекретаря, СВА, RACI) | Обновлен `06_governance_and_legal.md` (73 строки, 6 новых функций, 1 Accountable) | ✅ |
| **AC-5:** Гармонизация Домена 07 (сопряжение финансов с надзором СД и СВА) | Обновлен `07_finance_and_procurement.md` (52 строки, функции СД и СВА) | ✅ |
| **AC-6:** Соблюдение Scope Budget ($\le 8$ новых файлов, $\le 1200$ LOC, 0 TODO) | 4 новых файла + 2 измененных (суммарно 6 файлов VALUE, 561 LOC, 0 TODO) | ✅ |

## Deviations from TS

Отклонений от спецификации TS Phase B нет.

## Checkpoint

Stage complete: YES
