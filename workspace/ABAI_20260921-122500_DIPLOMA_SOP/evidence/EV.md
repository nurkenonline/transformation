# EV — ABAI_20260921-122500_DIPLOMA_SOP / Phase A: Проектирование регламента (СОП) формирования, верификации, выдачи и архивного учета дипломов собственного образца

> **Date**: 2026-09-21  
> **Author**: Executor Agent  
> **Task**: `ABAI_20260921-122500_DIPLOMA_SOP`  
> **TS**: [TS Phase A](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260921-122500_DIPLOMA_SOP/TS.md)

---

## Environment

| Field | Value |
|---|---|
| OS | Windows 10/11 |
| Workspace | `g:\Мой диск\Google AI Studio\Abai Unviersity Transformation` |
| Standards / Authority | Закон РК «Об образовании» ст. 39, Приказ МОН № 39, Приказ МОН № 595, Приказ МКИ № 566-НҚ, Протокол 3 ИС ЕПВО |
| Framework | Trace-First Workflow (TFW v3.4.0) |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|:---:|---|
| E1 | AC-1 | Разработка полного текста СОПа: 10 этапов (допуск к ГАК, ECTS 240/120, Антиплагиат ≥ 70\%$, расчет GPA_int ≥ 3.5$) | Local filesystem | **VERIFIED** | [`sop_diploma_generation_and_issuance.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/sop_diploma_generation_and_issuance.md) |
| E2 | AC-2 | Сквозная интеграция с ЕПВО (Протокол 3): заказ 12-значных номеров, QR-коды валидации eGov, SLA ≤ 5$ рабочих дней, предпросмотр макета выпускником в ЛК за 48 ч | Local filesystem | **VERIFIED** | [`sop_diploma_generation_and_issuance.md` § 3 (этапы 4, 5)](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/sop_diploma_generation_and_issuance.md) |
| E3 | AC-3 | Формализация контура актов приема-передачи и учета бланков в УИС: Приложение 1 (Акт передачи в Институт), Приложение 2 (Акт возврата в ОР), Приложение 3 (Акт списания брака), Приложение 4 (Книга регистрации выданных дипломов) | Local filesystem | **VERIFIED** | [`sop_diploma_generation_and_issuance.md` § 7](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/sop_diploma_generation_and_issuance.md) |
| E4 | AC-4 | Порядок выдачи под личную подпись, порядок оформления дубликатов с аннулированием первичных номеров в ЕПВО, 75-летний срок архивного хранения Книг регистрации (Приказ МКИ № 566-НҚ, ст. 471) | Local filesystem | **VERIFIED** | [`sop_diploma_generation_and_issuance.md` § 3 (этапы 8, 10)](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/sop_diploma_generation_and_issuance.md) |
| E5 | AC-5 | Гармонизация смежных актов: Положение об ОР и ДИ Руководителя ОР дополнены ссылками на `SOP-ACAD-DIPLOMA-001`, контролем актов передачи и персональной ответственностью | Local filesystem | **VERIFIED** | [`registrar_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/registrar_regulation.md), [`jd_head_registrar.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_head_registrar.md) |
| E6 | AC-6 | Регистрация нового регламента в сводном каталоге локальных нормативных актов | Local filesystem | **VERIFIED** | [`docs/internal_acts/README.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/README.md) |

## Verdict

Evidence verdict: **6/6 VERIFIED**, 0 DEFERRED, 0 BLOCKED, 0 N/A.

---
*EV — ABAI_20260921-122500_DIPLOMA_SOP / Phase A | 2026-09-21*
