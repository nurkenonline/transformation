# Verify — "Are the claims true in ABAI-30?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.  
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"  
> Min verify ratio: 0.42  
> RF files claimed: 1 VALUE + 2 TRACE/DERIVED  
> Files to verify: 3 of 3 (100% full audit)  

## Verification Log

### V1: `docs/internal_acts/sops_and_rules/service_catalog_and_sla_matrix.md`
- **RF claim:** Общеуниверситетский каталог межфункциональных услуг (`SLA-ENT-CROSS-001`, v2.0): 199 строк, 14 доменов, B2B-сервисы, превенция ст. 24 ТК РК, светофорный контроль.
- **Actual:** Файл существует, объем 199 строк, 7 разделов. Преамбула и п. 1.2 ссылаются на статьи 11, 24, 64, 73 ТК РК, Постановление Правительства № 590 и Приказ МКС № 236. Разделы 3–4 содержат ровно 14 функциональных доменов с полными таблицами параметров (Код, Название, Заявитель, Исполнитель, Канал, FRT, RT, Условия). Разделы 5–7 детализируют правила паузы таймера, светофорный мониторинг и дисциплинарную ответственность.
- **Match:** ✅ Полное соответствие

### V2: `docs/internal_acts/README.md`
- **RF claim:** Обновлено название и статус каталога в реестре регламентов.
- **Actual:** Строка 120 содержит актуализированную запись: `[Общеуниверситетский каталог межфункциональных услуг и Соглашение об уровне обслуживания (Enterprise Service Catalog & Internal B2B SLA)](sops_and_rules/service_catalog_and_sla_matrix.md)`.
- **Match:** ✅ Полное соответствие

### V3: `docs/MASTER_DOCUMENT_CATALOG.md`
- **RF claim:** Каталог актуализирован, 191 документ, валидные относительные ссылки.
- **Actual:** Документ перегенерирован, содержит 191 документ, ссылка на обновленный каталог услуг активна и валидна.
- **Match:** ✅ Полное соответствие

## Commands Executed

| # | Command | Result |
|---|---|---|
| 1 | Проверка строк кода (LOC) и TODO | 199 LOC всего (+77 новых строк). TODO: 0. |
| 2 | Проверка доменов в каталоге | Ровно 14 доменов (7 фронт-офисных + 7 B2B). |
| 3 | Генерация каталога `regenerate_catalog_relative.py` | 191 документ, 0 ошибок. |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|---|---|---|:---:|
| C1 | Защита от отказов по не обусловленной работе | `service_catalog_and_sla_matrix.md` п. 1.2 | Трудовой кодекс РК ст. 24 | ✅ |
| C2 | Обязательный срок соисполнителя $\le 3$ дней | `service_catalog_and_sla_matrix.md` п. 1.2, 5.1 | Приказ МКС РК № 236 (`MCIS-01`) | ✅ |
| C3 | Исключение дублирования функций | `service_catalog_and_sla_matrix.md` п. 1.2 | Постановление Правительства РК № 590 (`PP-02`) | ✅ |
| C4 | Дисциплинарная ответственность за срыв SLA | `service_catalog_and_sla_matrix.md` разд. 7 | Трудовой кодекс РК ст. 64, 73 | ✅ |

## Discrepancies Found

No discrepancies.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|---|:---:|:---:|
| E1 | `workspace/ABAI_20260925-175500_ENTERPRISE_SLA/evidence/EV.md` | ✅ | ✅ Полное подтверждение всех 5 критериев AC-1 — AC-5 |
| E2 | Реестр `docs/internal_acts/README.md` | ✅ | ✅ Актуализирован |
| E3 | Каталог `docs/MASTER_DOCUMENT_CATALOG.md` | ✅ | ✅ 191 документ |

Stage complete: YES
