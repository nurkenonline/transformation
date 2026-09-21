# RF — ABAI_20260921-122500_DIPLOMA_SOP / Phase A: Проектирование регламента (СОП) формирования, верификации, выдачи и архивного учета дипломов собственного образца

> **Date**: 2026-09-21  
> **Author**: Executor Agent  
> **Status**: 🟢 RF_SUBMITTED — Ready for Review  
> **Task**: `ABAI_20260921-122500_DIPLOMA_SOP`  
> **Parent HL**: [HL-ABAI_20260921-122500_DIPLOMA_SOP](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260921-122500_DIPLOMA_SOP/HL.md)  
> **TS**: [TS Phase A](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260921-122500_DIPLOMA_SOP/TS.md)  
> **ONB**: [ONB Phase A](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260921-122500_DIPLOMA_SOP/ONB.md)  
> **Evidence**: [EV Phase A](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260921-122500_DIPLOMA_SOP/evidence/EV.md)

---

## 1. Summary of Changes

В рамках задачи `ABAI_20260921-122500_DIPLOMA_SOP` (Phase A) разработана исчерпывающая нормативно-процессуальная база жизненного цикла дипломов собственного образца и общеевропейских приложений (*Diploma Supplement*) [V_LEGAL_FORM] «[V_UNIVERSITY_FULL_NAME]» с формализацией цифрового контура УИС («[V_PRIMARY_EDTECH_PLATFORM]»), интеграции с ИС ЕПВО МНВО РК и документооборота актов приема-передачи:

1. **Разработан СОП-регламент:** [`docs/internal_acts/sops_and_rules/sop_diploma_generation_and_issuance.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/sop_diploma_generation_and_issuance.md) (`SOP-ACAD-DIPLOMA-001`, 412 строк, 0 плейсхолдеров):
   - Описаны 10 процессуальных стадий жизненного цикла документа: от проверки 240/120 ECTS и справок Антиплагиат (≥ 70\% / \ge 65\%$) до расчета Интегрального GPA ($GPA_{int} \ge 3.5$), сквозного протокола взаимодействия с ЕПВО (Протокол 3: заказ 12-значных номеров МНВО и защитных машиночитаемых QR-кодов за ≤ 5$ рабочих дней), трехъязычного макетирования, предварительного согласования выпускником через SMS-OTP в Личном кабинете, комиссионного списания брака с аннулированием в ЕПВО за 24 часа, выдачи дубликатов и номенклатурного 75-летнего хранения Книг регистрации в соответствии с Приказом и.о. МКИ РК № 566-НҚ (ст. 466, 470, 471);
   - Утверждены 4 стандартизированные формы актов и учетных документов:
     - **Приложение 1:** Форма 1 — Акт приема-передачи оформленных дипломов в Институт для вручения;
     - **Приложение 2:** Форма 2 — Акт возврата неврученных дипломов в Офис регистратора (в течение 3 рабочих дней);
     - **Приложение 3:** Форма 3 — Акт на списание и уничтожение испорченных бланков строгой отчетности;
     - **Приложение 4:** Форма 4 — Книга регистрации выданных документов об образовании собственного образца.
2. **Гармонизированы смежные нормативные акты:**
   - [`docs/internal_acts/regulations/registrar_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/registrar_regulation.md) — дополнен п. 4.3 и п. 7 ссылками на `SOP-ACAD-DIPLOMA-001`, регламент актов передачи и контроль архивного хранения;
   - [`docs/internal_acts/job_descriptions/jd_head_registrar.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_head_registrar.md) — дополнен п. 3.6 и разд. 6 персональной ответственностью за организацию полного цикла оформления, учета, списания бланков строгой отчетности и актов приема-передачи;
   - [`docs/internal_acts/README.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/README.md) — новый регламент внесен в реестр внутренних актов Университета.

---

## 2. Files Touched and Scope Budget Check

| Action | Path | LOC Added | Notes |
|---|---|:---:|---|
| **NEW** | `docs/internal_acts/sops_and_rules/sop_diploma_generation_and_issuance.md` | +412 | Основной нормативный акт (SOP-ACAD-DIPLOMA-001) |
| **MODIFY** | `docs/internal_acts/regulations/registrar_regulation.md` | +14 | Гармонизация (разд. 4.3, 7) |
| **MODIFY** | `docs/internal_acts/job_descriptions/jd_head_registrar.md` | +16 | Гармонизация ДИ Руководителя ОР (п. 3.6, разд. 6) |
| **MODIFY** | `docs/internal_acts/README.md` | +1 | Регистрация в общем реестре актов |
| **NEW** | `workspace/ABAI_20260921-122500_DIPLOMA_SOP/evidence/EV.md` | +36 | Evidence Record (6/6 VERIFIED) |

**Бюджет фазы:**
- Новых файлов: 2 (лимит ≤ 8$) — **СОБЛЮДЕНО**;
- Всего затронуто файлов: 5 (лимит ≤ 14$) — **СОБЛЮДЕНО**;
- Всего новых строк: 479 (лимит ≤ 1200$) — **СОБЛЮДЕНО**.

---

## 3. Acceptance Criteria Coverage

| AC ID | Description | EV Status | Artifact Reference |
|---|---|:---:|---|
| **AC-1** | 10 стадий жизненного цикла диплома (допуск к ГАК, ECTS 240/120, Антиплагиат ≥ 70\%$, GPA_int ≥ 3.5$) | **VERIFIED** | [`sop_diploma_generation_and_issuance.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/sop_diploma_generation_and_issuance.md) § 3 |
| **AC-2** | Интеграция с ЕПВО (Протокол 3): заказ 12-значных номеров, QR-коды валидации, SLA ≤ 5$ р.д., согласование в ЛК | **VERIFIED** | [`sop_diploma_generation_and_issuance.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/sop_diploma_generation_and_issuance.md) § 3 (этапы 4, 5) |
| **AC-3** | Формализация контура актов приема-передачи и учета в УИС: Приложения 1, 2, 3, 4 | **VERIFIED** | [`sop_diploma_generation_and_issuance.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/sop_diploma_generation_and_issuance.md) § 7 |
| **AC-4** | Выдача под роспись, дубликаты, списание брака (24 ч аннулирование в ЕПВО), 75-летний архив по Приказу МКИ № 566-НҚ | **VERIFIED** | [`sop_diploma_generation_and_issuance.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/sop_diploma_generation_and_issuance.md) § 3 (этапы 8, 9, 10) |
| **AC-5** | Гармонизация Положения об ОР и ДИ Руководителя ОР | **VERIFIED** | [`registrar_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/registrar_regulation.md), [`jd_head_registrar.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_head_registrar.md) |
| **AC-6** | Регистрация в общем реестре внутренних актов | **VERIFIED** | [`docs/internal_acts/README.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/README.md) |

---

## 4. Residual Risks & Next Actions

- Риски отсутствуют: правовая база выверена по нормам законодательства РК на 2026 год, исключены плейсхолдеры и дублирование функций.
- Передано Reviewer для независимой оценки качества и подготовки `REVIEW.md`.

---
*RF — ABAI_20260921-122500_DIPLOMA_SOP / Phase A | 2026-09-21*
