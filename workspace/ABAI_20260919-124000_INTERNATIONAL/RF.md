# RF — ABAI_20260919-124000_INTERNATIONAL / Phase A: Институциональное ядро международного блока, кадровые стандарты и актуализация Реестра НПА

> **Date**: 2026-09-21  
> **Author**: Executor Agent  
> **Status**: 🟢 RF_SUBMITTED — Ready for Review  
> **Task**: `ABAI_20260919-124000_INTERNATIONAL`  
> **Parent HL**: [HL-ABAI_20260919-124000_INTERNATIONAL](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260919-124000_INTERNATIONAL/HL.md)  
> **TS**: [TS Phase A](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260919-124000_INTERNATIONAL/TS.md)  
> **ONB**: [ONB Phase A](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260919-124000_INTERNATIONAL/ONB.md)  
> **Evidence**: [EV Phase A](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260919-124000_INTERNATIONAL/evidence/EV__INTERNATIONAL_PHASE_A.md)

---

## 1. Summary of Changes

В рамках Фазы A задачи `ABAI_20260919-124000_INTERNATIONAL` полностью сформировано институциональное ядро, кадровый каркас и внешняя нормативная база международного блока и визово-миграционного комплаенса:

1. **Разработано Положение о подразделении:**
   - [`docs/internal_acts/regulations/international_cooperation_department_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/international_cooperation_department_regulation.md) — Положение о Департаменте международного сотрудничества и интернационализации (182 строки): детальная структура из 3 секторов, цели, задачи, функции (международные договоры, открытые конкурсы академической мобильности по Приказу МОН № 613 с обязательным *Learning Agreement*, привлечение зарубежных ученых Visiting Professors, программы Double Degree), межструктурная матрица RACI, регламентация работы в модуле УИС («Интернационализация и мобильность» платформы `[V_PRIMARY_EDTECH_PLATFORM]`) с ролями `Intl_Manager`, `Visa_Officer`, жесткие SLA, дисциплинарная ответственность по ст. 22, 23, 52 ТК РК и материальная ответственность по ст. 120 ТК РК за риски по ст. 518 КоАП РК.
2. **Разработан комплект из 3 должностных инструкций:**
   - [`docs/internal_acts/job_descriptions/jd_director_international_cooperation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_director_international_cooperation.md) — ДИ Директора Департамента: стратегическое лидерство, показатели СУР Домен 07, международные рейтинги (QS, THE), партнерские альянсы, контроль регламентации труда (`SOP-HR-REG-JD-LIFECYCLE-001`, ст. 23 ТК РК).
   - [`docs/internal_acts/job_descriptions/jd_coordinator_academic_mobility.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_coordinator_academic_mobility.md) — ДИ Координатора программ академической мобильности и международных стажировок: организация конкурсов по Приказу № 613, трехсторонний *Learning Agreement*, координация ECTS-перезачета в УИС с Офисом регистратора за 2 рабочих дня.
   - [`docs/internal_acts/job_descriptions/jd_visa_and_migration_support_specialist.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_visa_and_migration_support_specialist.md) — ДИ Специалиста по визово-миграционному учету: императивное электронное уведомление органов миграционной службы МВД РК через портал `vmp.gov.kz` **до 3 рабочих дней (72 часов)** по ст. 9 Закона о миграции № 477-IV и ПП РК № 148, контроль виз C9/C3/B10 (алерты за 30 дней) и персональная материальная ответственность по ст. 120 ТК РК за штрафы по ст. 518 КоАП РК (до 500 МРП).
3. **Разработан аналитический модуль и актуализирован Реестр внешних НПА:**
   - [`docs/regulations/04_internationalization_npa.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/regulations/04_internationalization_npa.md) — подробный модуль (152 строки) с разбором норм академической мобильности (№ 613), правил пребывания иностранцев (№ 148), выдачи виз (№ 11-1-2/555), Double Degree (№ 595), налогообложения нерезидентов и штрафов ст. 518 КоАП РК.
   - [`docs/regulations/external_npa_registry.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/regulations/external_npa_registry.md) — внесен Закон РК «О миграции населения» (`LAW-26`), правила пребывания (`MIG-01`), правила выдачи виз (`MIG-02`), общее число актов доведено до 130.
   - [`docs/regulations/README.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/regulations/README.md) и [`docs/internal_acts/README.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/README.md) — зарегистрированы все созданные акты.

---

## 2. Files Touched and Scope Budget Check

| Action | Path | Class | Semantic Purpose |
|---|---|:---:|---|
| **CREATE** | `docs/internal_acts/regulations/international_cooperation_department_regulation.md` | `VALUE` | Положение о Департаменте с RACI, УИС, SLA и ответственностью |
| **CREATE** | `docs/internal_acts/job_descriptions/jd_director_international_cooperation.md` | `VALUE` | ДИ Директора Департамента |
| **CREATE** | `docs/internal_acts/job_descriptions/jd_coordinator_academic_mobility.md` | `VALUE` | ДИ Координатора программ академической мобильности |
| **CREATE** | `docs/internal_acts/job_descriptions/jd_visa_and_migration_support_specialist.md` | `VALUE` | ДИ Специалиста по визово-миграционному сопровождению |
| **CREATE** | `docs/regulations/04_internationalization_npa.md` | `VALUE` | Аналитический модуль НПА международного блока |
| **MODIFY** | `docs/regulations/external_npa_registry.md` | `VALUE` | Регистрация LAW-26, MIG-01, MIG-02 со ссылками на «Әділет» |
| **MODIFY** | `docs/regulations/README.md` | `VALUE` | Регистрация модуля 04 в индексе НПА |
| **MODIFY** | `docs/internal_acts/README.md` | `VALUE` | Регистрация новых внутренних актов |
| **CREATE** | `workspace/ABAI_20260919-124000_INTERNATIONAL/evidence/EV__INTERNATIONAL_PHASE_A.md` | `TRACE` | Протокол доказательств Фазы A (3/3 VERIFIED) |

**Соблюдение лимитов Scope Budget:**
- Новых файлов нормативной базы: 5 (лимит ≤ 8$) — **СОБЛЮДЕНО**;
- Всего файлов затронуто: 9 (лимит ≤ 14$) — **СОБЛЮДЕНО**;
- Объем добавленных строк: ~720 LOC (лимит ≤ 1200$ LOC) — **СОБЛЮДЕНО**;
- Плейсхолдеры: 0, параметризация через `[V_...]` — **100%**.

---

## 3. Acceptance Criteria Coverage

| AC ID | Description | EV Status | Artifact Reference |
|---|---|:---:|---|
| **AC-1** | Положение о Департаменте международного сотрудничества и интернационализации (структура, задачи, функции, RACI, УИС, SLA, ст. 22, 23, 52 ТК РК, ст. 518 КоАП РК, ст. 120 ТК РК) | **VERIFIED** | [`international_cooperation_department_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/international_cooperation_department_regulation.md) |
| **AC-2** | Комплект из 3 должностных инструкций ключевых сотрудников (Директор, Координатор мобильности по № 613, Специалист по визово-миграционному учету за 72 ч через vmp.gov.kz) | **VERIFIED** | [`jd_director_international_cooperation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_director_international_cooperation.md), [`jd_coordinator_academic_mobility.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_coordinator_academic_mobility.md), [`jd_visa_and_migration_support_specialist.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_visa_and_migration_support_specialist.md) |
| **AC-3** | Аналитический модуль и актуализация Реестра внешних НПА РК (Модуль 04, внесение LAW-26, MIG-01, MIG-02 в external_npa_registry.md, обновление README) | **VERIFIED** | [`04_internationalization_npa.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/regulations/04_internationalization_npa.md), [`external_npa_registry.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/regulations/external_npa_registry.md) |

---

## 4. Residual Risks & Next Actions

- Задачи Фазы A выполнены в полном объеме без замечаний;
- Передано Reviewer для проведения независимого экспертного аудита (`REVIEW.md`).

---
*RF — ABAI_20260919-124000_INTERNATIONAL / Phase A | 2026-09-21*
