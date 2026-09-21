# ONB — ABAI_20260917-174500_CULTURE_NPA / Phase B: Гармонизация внутренних нормативных актов университета по архивам, СЭД, библиотечному делу и масс-медиа

> **Date**: 2026-09-17  
> **Author**: Executor  
> **Status**: 🟢 ONB_RESOLVED — Ready for execution  
> **Parent HL**: [HL-ABAI_20260917-174500_CULTURE_NPA](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260917-174500_CULTURE_NPA/HL.md)  
> **TS**: [TS Phase B](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260917-174500_CULTURE_NPA/TS_PHASE_B.md)  

---

## 1. Understanding

Задача Фазы B заключается в практической имплементации стандартов МКИ РК во внутренние документы университета:
1. Закрепить нормативный **75-летний срок хранения** студенческих дел и кадровой документации (Приказ № 566-НҚ) в положениях Офиса регистратора и HR;
2. Разработать Положение о Научной библиотеке и Регламент формирования, инвентаризации и списания библиотечного фонда (Закон «О культуре», Приказ № 153);
3. Разработать Положение о Медиа-центре и Регламент работы со СМИ (Закон «О масс-медиа» № 94-VIII от 19.06.2024 с предельным регламентным сроком ответа на запросы СМИ до 5 рабочих дней).

---

## 2. Entry Points (6 файлов VALUE + 1 TRACE)

1. `docs/internal_acts/regulations/registrar_regulation.md` (AC-1) [MODIFY]
2. `docs/internal_acts/regulations/hr_department_regulation.md` (AC-2) [MODIFY]
3. `docs/internal_acts/regulations/scientific_library_regulation.md` (AC-3) [CREATE]
4. `docs/internal_acts/regulations/media_center_regulation.md` (AC-4) [CREATE]
5. `docs/internal_acts/sops_and_rules/sop_library_collection_and_writeoff.md` (AC-3) [CREATE]
6. `docs/internal_acts/sops_and_rules/sop_media_interaction_and_press_accreditation.md` (AC-4) [CREATE]
7. `workspace/ABAI_20260917-174500_CULTURE_NPA/evidence/EV__CULTURE_NPA_PHASE_B.md` (AC-5) [CREATE]

---

## 3. Scope Budget Check

- Новых файлов VALUE: 4 (лимит: 8)
- Всего файлов VALUE: 6 (лимит: 14)
- Объем строк: ~900 LOC (лимит: 1200 LOC)
- Бюджет соблюден.

---

## 4. Execution Steps

1. Модифицировать `registrar_regulation.md`, добавив регламентацию 75-летнего архива по Приказу № 566-НҚ.
2. Модифицировать `hr_department_regulation.md`, добавив регламентацию 75-летнего архива кадровых документов по Приказам № 566-НҚ и № 134.
3. Разработать `scientific_library_regulation.md` (Положение о Научной библиотеке).
4. Разработать `sop_library_collection_and_writeoff.md` (Регламент комплектования и списания).
5. Разработать `media_center_regulation.md` (Положение о Медиа-центре).
6. Разработать `sop_media_interaction_and_press_accreditation.md` (Регламент работы со СМИ, SLA 5 дней).
7. Сформировать `EV__CULTURE_NPA_PHASE_B.md` и `RF_PHASE_B.md`.
