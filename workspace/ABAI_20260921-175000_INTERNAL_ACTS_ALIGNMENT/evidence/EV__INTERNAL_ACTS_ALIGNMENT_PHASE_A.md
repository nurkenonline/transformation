# EV — ABAI_20260921-175000_INTERNAL_ACTS_ALIGNMENT / Phase A: Академический и исследовательский контур

> **Date**: 2026-09-21  
> **Author**: Executor / AI Normalization Specialist  
> **Task**: ABAI-22 Phase A (`ABAI_20260921-175000_INTERNAL_ACTS_ALIGNMENT`)  
> **TS**: [TS Phase A](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260921-175000_INTERNAL_ACTS_ALIGNMENT/TS.md)  

---

## Environment

| Field | Value |
|---|---|
| OS | Windows 11 Pro (10.0.26100) |
| Language / Runtime | Markdown / Python 3.11 |
| Deploy target | `docs/internal_acts/regulations/` & `docs/internal_acts/job_descriptions/` |
| CI / Pipeline | Local verification |

---

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|:---:|---|
| E1 | AC-1 | В Положение о ДАВ (`dav_regulation.md`) и ДИ Директора ДАВ (`jd_director_dav.md`) включены нормы координации Факультета довузовской подготовки / Foundation (`STD-RK-FOUND-001`), объемы ECTS ГОСО (240/120/180), пропорции СРО (1:2, 1:3, 1:5), Minor (20–30 ECTS) и Microcredentials (`STD-RK-GOSO-001`) | Local filesystem | `VERIFIED` | [`dav_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/dav_regulation.md), [`jd_director_dav.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_director_dav.md) |
| E2 | AC-2 | В Положение об ОР (`registrar_regulation.md`) и ДИ Руководителя ОР (`jd_head_registrar.md`) включена кредитная технология ECTS (`STD-RK-CREDIT-001`, Приказ МОН № 152), 4-балльная шкала GPA, бесплатная однократная пересдача FX в период сессии, платный повтор F (Retake) и Летний семестр ($\le 6$ недель) | Local filesystem | `VERIFIED` | [`registrar_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/registrar_regulation.md), [`jd_head_registrar.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_head_registrar.md) |
| E3 | AC-3 | В Положение о Департаменте науки (`science_department_regulation.md`) и ДИ Директора науки (`jd_director_science.md`) включены организация диссоветов PhD (Приказ № 126, `STD-RK-DEGREE-001`), онлайн-трансляция и тайное электронное голосование, антиплагиат $\ge 80\%$ в НЦГНТЭ, ученые звания профессора/доцента (Приказ № 128), шкала TRL 1–9 и роялти $\ge 30\%$ (`STD-RK-SCI-001`) | Local filesystem | `VERIFIED` | [`science_department_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/science_department_regulation.md), [`jd_director_science.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_director_science.md) |
| E4 | AC-4 | Полная гармонизация с Доменами: функции `FUNC-ACAD-FOUND-009`, `FUNC-ACAD-CREDIT-010`, `FUNC-SCI-DISSERT-009` из Доменов 01 и 02 получили 100% прямое текстуальное отражение в соответствующих Положениях и ДИ | Local filesystem | `VERIFIED` | Домены 01 и 02 |
| E5 | AC-5 | Фиксация SLA и персональной ответственности: дедлайны выставления оценок (48 ч), блокировки ведомостей (24 ч), регистрации приказов день-в-день, ответственность руководителей по ТК РК | Local filesystem | `VERIFIED` | Разделы ответственности всех 6 актов |
| E6 | AC-6 | Чистота кода и текста: проверка ripgrep подтвердила 0 маркеров `[TODO]` и `[TBD]`, параметры `[V_*]` валидны | Ripgrep | `VERIFIED` | 0 совпадений |

---

## Verdict

Evidence verdict: **6/6 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A**

---

*EV — ABAI_20260921-175000_INTERNAL_ACTS_ALIGNMENT / Phase A | 2026-09-21*
