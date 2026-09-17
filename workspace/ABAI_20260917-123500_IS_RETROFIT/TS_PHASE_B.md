# TS — ABAI_20260917-123500_IS_RETROFIT / Phase B: Сквозная интеграция требований УИС и SLA в научный блок, качество, комплаенс и стратегию

> **Date**: 2026-09-17  
> **Author**: Coordinator  
> **Status**: 🟢 APPROVED — approved by owner 2026-09-17  
> **Parent HL**: [HL-ABAI_20260917-123500_IS_RETROFIT](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260917-123500_IS_RETROFIT/HL.md)  

---

## 1. Objective

Осуществить нормативную модернизацию 12 внутренних актов научного контура, обеспечения качества, комплаенс-контроля и стратегического развития (Положения о подразделениях и Должностные инструкции). В документы системно вшиваются прямые требования по обязательному использованию специализированных функциональных модулей УИС («[V_PRIMARY_EDTECH_PLATFORM]»):
1. Модуль «Наука и НИОКР» (учет проектов ГФ/ПЦФ/ХДТ, публикаций Scopus/WoS, авторских профилей ORCID/ResearcherID, отчетов НЦГНТЭ);
2. Модуль «Коммерциализация и Стартапы» (реестр РИД, патентов, лицензионных соглашений, стартап-команд TRL 1–9);
3. Модуль «Комплаенс и Антикоррупция» (декларирование конфликта интересов, реестр подарков, горячая линия, антикоррупционная экспертиза ВНД);
4. Модуль «Качество образования и EdTech» (цифровой аудит УМКД/силлабусов, опросы студентов и стейкхолдеров);
5. Модуль «Аккредитация и Рейтинги» (паспорта ОП, агрегация показателей институциональной и программной аккредитации, синхронизация с ЕПВО);
6. Модуль «Стратегия и OKR» (дашборд 25 стратегических KPI Совета директоров, 90-дневные циклы OKR со скорингом 0.0–1.0).

В акты внедряются конкретные регламентные сроки (SLA), персональная ответственность по статьям 22, 23, 52 (п. 1 пп. 16), 120, 181, 182 Трудового кодекса РК и запрет параллельного бумажного документооборота.

---

## 2. Scope

### In Scope (12 файлов Phase B)

#### Положения структурных подразделений (6 файлов):
1. `docs/internal_acts/regulations/science_department_regulation.md` (Департамент науки)
2. `docs/internal_acts/regulations/commercialization_office_regulation.md` (Офис коммерциализации)
3. `docs/internal_acts/regulations/compliance_service_regulation.md` (Комплаенс-служба)
4. `docs/internal_acts/regulations/quality_assurance_committee_regulation.md` (Комитет по обеспечению качества)
5. `docs/internal_acts/regulations/accreditation_center_regulation.md` (Центр аккредитации и рейтингов)
6. `docs/internal_acts/regulations/strategic_development_department_regulation.md` (Департамент стратегического развития)

#### Должностные инструкции (6 файлов):
7. `docs/internal_acts/job_descriptions/jd_director_science.md` (Директор Департамента науки)
8. `docs/internal_acts/job_descriptions/jd_head_commercialization.md` (Начальник Офиса коммерциализации)
9. `docs/internal_acts/job_descriptions/jd_compliance_officer.md` (Комплаенс-офицер)
10. `docs/internal_acts/job_descriptions/jd_head_accreditation.md` (Руководитель Центра аккредитации и рейтингов)
11. `docs/internal_acts/job_descriptions/jd_researcher_model.md` (Типовая ДИ научного сотрудника / исследователя)
12. `docs/internal_acts/job_descriptions/jd_director_strategic_development.md` (Директор Департамента стратегического развития)

#### Артефакт доказательств:
- `workspace/ABAI_20260917-123500_IS_RETROFIT/evidence/EV__IS_RETROFIT_PHASE_B.md`

### Out of Scope
- Документы ИТ-блока, телекоммуникаций, информационной безопасности и материально-технического обеспечения (вынесены в Phase C).

---

## 3. Principles Check

| # | HL §7 principle | Enforced by | Gate |
|---|---|---|---|
| P0 | Трудовой кодекс РК (ст. 22, 23, 52, 120, 181, 182) | AC-4, AC-5 | Прямое указание статей ТК РК в ДИ ученых, комплаенс-офицера и директоров |
| P1 | Закон РК «О науке и технологической политике» 2024 г. | AC-1, AC-4 | Внесение РНТД, грантов и публикаций в единую цифровую базу ОВПО |
| P2 | Закон РК «О противодействии коррупции» | AC-2, AC-5 | Ведение антикоррупционного мониторинга, горячей линии и реестра интересов в УИС |
| P3 | Эталонный профиль УИС (22 модуля) | AC-1, AC-2, AC-3 | Ссылка на конкретные модули («Наука», «Комплаенс», «Стратегия и OKR» и др.) |
| P4 | Закон РК «О персональных данных и их защите» | AC-2, AC-5 | Запрет передачи учетных записей, конфиденциальность комплаенс-обращений |

---

## 4. Affected Files and Value-Bearing Accounting

| File / selector | Action | Class | Semantic reason / required result |
|---|---|---|---|
| `docs/internal_acts/regulations/science_department_regulation.md` | MODIFY | `VALUE` | Раздел регламентации в УИС: модуль «Наука/НИОКР», учет проектов ГФ/ПЦФ, РНТД, авто-верификация Scopus/WoS, SLA 5 дней на внесение |
| `docs/internal_acts/regulations/commercialization_office_regulation.md` | MODIFY | `VALUE` | Раздел регламентации в УИС: модуль «Коммерциализация», учет патентов, РИД, реестр спин-офф компаний, трекинг TRL |
| `docs/internal_acts/regulations/compliance_service_regulation.md` | MODIFY | `VALUE` | Раздел регламентации в УИС: модуль «Комплаенс», закрытый контур горячей линии «Whistleblowing», реестр конфликта интересов, 24 ч SLA на регистрацию инцидента |
| `docs/internal_acts/regulations/quality_assurance_committee_regulation.md` | MODIFY | `VALUE` | Раздел регламентации в УИС: модуль «Качество и EdTech», сквозная экспертиза силлабусов/УМКД, цифровые опросы студентов без ручной манипуляции данными |
| `docs/internal_acts/regulations/accreditation_center_regulation.md` | MODIFY | `VALUE` | Раздел регламентации в УИС: модуль «Аккредитация и Рейтинги», агрегация статистики институтов/кафедр для IQAA/ASIIN/QS, контроль синхронизации с ЕПВО |
| `docs/internal_acts/regulations/strategic_development_department_regulation.md` | MODIFY | `VALUE` | Раздел регламентации в УИС: модуль «Стратегия и OKR», план-факт анализ 25 KPI, квартальный скоринг 0.0–1.0 OKR кафедр/институтов |
| `docs/internal_acts/job_descriptions/jd_director_science.md` | MODIFY | `VALUE` | Роль `Science_SuperAdmin`: верификация научных отчетов, контроль внесения публикаций в УИС, блокировка недобросовестных записей, санкции по ТК РК |
| `docs/internal_acts/job_descriptions/jd_head_commercialization.md` | MODIFY | `VALUE` | Роль `Commercialization_Manager`: реестр патентов, стартап-проектов, электронные акты внедрения в производство |
| `docs/internal_acts/job_descriptions/jd_compliance_officer.md` | MODIFY | `VALUE` | Роль `Compliance_Auditor`: независимый доступ к логам УИС, согласование проектов ВНД в СЭД за 3 дня, защита заявителей о коррупции |
| `docs/internal_acts/job_descriptions/jd_head_accreditation.md` | MODIFY | `VALUE` | Роль `Accreditation_Analyst`: валидация выгрузок в ЕПВО/НОБД, аудит соответствия квалтребованиям МНВО № 391 |
| `docs/internal_acts/job_descriptions/jd_researcher_model.md` | MODIFY | `VALUE` | Обязанность исследователя вносить статьи Scopus/WoS и патенты в УИС в течение **5 рабочих дней** с момента публикации; ответственность по ст. 22, 23, 52 ТК РК |
| `docs/internal_acts/job_descriptions/jd_director_strategic_development.md` | MODIFY | `VALUE` | Роль `Strategy_Director`: мониторинг стратегического дашборда, фиксация квартальных OKR в УИС, аудит достоверности показателей |
| `workspace/ABAI_20260917-123500_IS_RETROFIT/evidence/EV__IS_RETROFIT_PHASE_B.md` | CREATE | `ASSURANCE` | Протокол объективных доказательств внедрения требований в 12 актов |

### Prospective accounting contract

| Fact | Approved value |
|---|---|
| Subject / exact VALUE selector | 12 модифицируемых файлов в `docs/internal_acts/` |
| Baseline / selector source | `v2.2-IS-RETROFIT-PHASE-A`; this TS at approval commit |
| Candidate rule | First tested Executor commit with required VALUE+ASSURANCE, before EV/RF/REVIEW/final transition |
| Logical VALUE files | 12 файлов |
| Touched text LOC | ~710 строк дополнений |
| Triggers / disposition | Terminal complete for Phase B |
| Multiplier / authority | Approved Coordinator / Owner 2026-09-17 |
| Approval epoch / failure | Owner approval received 2026-09-17 |

```powershell
git diff --name-status --find-renames=50% -z <BASELINE_SHA> <CANDIDATE_SHA> -- $valuePaths
git diff --numstat --find-renames=50% -z <BASELINE_SHA> <CANDIDATE_SHA> -- $valuePaths
```

### Prospective scope rulings

None. Модификация строго ограничена 12 файлами Phase B.

### Task-local hard constraints (when material)

| M1 consequence | M2 object/risk | M3 measure/selector | M4 pre-act check | M5 softer-control gap | M6 change authority |
|---|---|---|---|---|---|
| Утечка личности заявителя о коррупции | Персональная безопасность | Изоляция роли `Compliance_Auditor`, шифрование канала Whistleblowing | Аудит ВНД | Декларативные обещания конфиденциальности | Coordinator / Owner |
| Фальсификация научных отчетов в НЦГНТЭ | Отзыв грантов МНВО | Обязательный аудит публикаций по Scopus/WoS с DOI в течение 5 дней | Проверка ДИ исследователя | Отсутствие персонального срока внесения | Coordinator / Owner |

**Actions (not budget dimensions):** 12 files modified, 1 evidence file created.  
**Immutable owner-approved denominator:** 12 VALUE files, ~710 touched LOC.

---

## 5. Acceptance Criteria

### AC-1: Регламентация в УИС положений научного блока и коммерциализации
Положения Департамента науки и Офиса коммерциализации дополнены выделенным разделом регламентации деятельности в УИС.
- [ ] В `science_department_regulation.md` закреплены модули «Наука и НИОКР», «Диссертационные советы», «Антиплагиат», роли RBAC (`Science_SuperAdmin`, `Science_Grant_Manager`), SLA (3 дня на темы, 5 дней на публикации);
- [ ] В `commercialization_office_regulation.md` закреплены модуль «Коммерциализация и Стартапы», роли `Commercialization_Manager`, `Startup_Tracker`, SLA (2 дня на РИД, 3 дня на патенты, 5 дней на лицензии).

Gate: Проверка наличия разделов регламентации в УИС в обоих положениях.  
Evidence: `evidence/EV__IS_RETROFIT_PHASE_B.md` (AC-1 status: VERIFIED).

### AC-2: Регламентация комплаенс-контроля и обеспечения качества в УИС
Положения Комплаенс-службы, QA-комитета и Центра аккредитации дополнены разделами цифровой регламентации.
- [ ] В `compliance_service_regulation.md` внедрен модуль «Комплаенс», независимая роль `Compliance_Auditor` с доступом к логам Audit Trail, 24 ч SLA на инциденты;
- [ ] В `quality_assurance_committee_regulation.md` внедрены модули «Качество образования и EdTech», роль `QA_Auditor`, запрет фильтрации оценок опросов;
- [ ] В `accreditation_center_regulation.md` внедрены модуль «Аккредитация и Рейтинги», роль `Accreditation_Analyst`, 15 дней на выгрузку SER, сверка с ЕПВО до 5 числа.

Gate: Проверка разделов в 3 положениях.  
Evidence: `evidence/EV__IS_RETROFIT_PHASE_B.md` (AC-2 status: VERIFIED).

### AC-3: Регламентация стратегического управления и OKR в УИС
Положение о Департаменте стратегического развития дополнено регламентом функционирования модуля «Стратегия и OKR».
- [ ] В `strategic_development_department_regulation.md` регламентирован сбор факта по 25 KPI до 10 числа месяца, фиксация квартальных OKR в первые 5 дней и скоринг (0.0–1.0) за 5 дней;
- [ ] Введен запрет ручной модификации утвержденных показателей задним числом.

Gate: Проверка наличия раздела 8 в `strategic_development_department_regulation.md`.  
Evidence: `evidence/EV__IS_RETROFIT_PHASE_B.md` (AC-3 status: VERIFIED).

### AC-4: ДИ исследователей и научных руководителей
В ДИ научного сотрудника и Директора Департамента науки вшиты обязательные цифровые функции и персональная ответственность по ТК РК.
- [ ] В `jd_researcher_model.md` закреплены ведение профилей ORCID/Scopus ID, 5-дневный дедлайн внесения статей с DOI, запрет «хищнических» журналов, расторжение договора по пп. 16) п. 1 ст. 52 ТК РК за срыв сроков;
- [ ] В `jd_director_science.md` закреплена роль `Science_SuperAdmin`, контроль верификации публикаций, ответственность по ст. 22, 23, 52 ТК РК.

Gate: Проверка наличия пунктов цифровых обязанностей и статей ТК РК.  
Evidence: `evidence/EV__IS_RETROFIT_PHASE_B.md` (AC-4 status: VERIFIED).

### AC-5: ДИ руководителей комплаенса, аккредитации, стратегии и коммерциализации
В 4 руководящие ДИ интегрированы роли RBAC, персональные дедлайны визирования в СЭД и ответственность по законодательству.
- [ ] В `jd_compliance_officer.md` закреплены роль `Compliance_Auditor`, 24 ч на обращение, 3 дня на ВНД, увольнение по ст. 52 ТК РК за разглашение заявителя;
- [ ] В `jd_head_commercialization.md` закреплены роль `Commercialization_Manager`, материальная ответственность по ст. 120 ТК РК;
- [ ] В `jd_head_accreditation.md` закреплены роль `Accreditation_Analyst`, ответственность по ст. 52 ТК РК за искажение показателей;
- [ ] В `jd_director_strategic_development.md` закреплены роль `Strategy_Director`, 10 число на сбор 25 KPI, санкции ст. 52 и 120 ТК РК.

Gate: Проверка подразделов УИС и ответственности по ТК РК во всех 4 ДИ.  
Evidence: `evidence/EV__IS_RETROFIT_PHASE_B.md` (AC-5 status: VERIFIED).

### AC-6: Универсализация и сохранение переменных
Все документы Phase B строго сохраняют нейтральный профиль и системные переменные `[V_...]`.
- [ ] Отсутствуют локальные хардкоды университетов;
- [ ] Сохранены переменные `[V_ORGANIZATION_NAME]`, `[V_PRIMARY_EDTECH_PLATFORM]`, `[V_CHANCELLOR_TITLE]`.

Gate: Grep-валидация на отсутствие сторонних названий вузов.  
Evidence: `evidence/EV__IS_RETROFIT_PHASE_B.md` (AC-6 status: VERIFIED).

### Evidence Artifacts

| File | Description |
|---|---|
| `workspace/ABAI_20260917-123500_IS_RETROFIT/evidence/EV__IS_RETROFIT_PHASE_B.md` | Сводный протокол доказательств верификации изменений 12 файлов по критериям AC-1 — AC-6 |

---

## 6. Technical Guidance

- Использовать терминологию и спецификации из `docs/generic_framework/digital/01_university_is_reference_blueprint.md`.
- Сохранять существующую структуру положений и ДИ, аддитивно интегрируя специализированные разделы о работе в УИС.

---

## 7. Definition of Failure

- ❌ Отсутствие жесткого 5-дневного SLA на внесение статей в ДИ научного сотрудника.
- ❌ Отсутствие независимого статуса доступа к логам Audit Trail в актах комплаенс-службы.
- ❌ Отсутствие ссылок на статьи 22, 23, 52 (п. 1 пп. 16), 120 Трудового кодекса РК в ДИ.
- ❌ Появление локальных названий вместо `[V_...]`.

---

## 8. Phase Risks

| Risk | Mitigation |
|---|---|
| Несоответствие между планами НИР кафедр и реальными публикациями | Внедрение автоматической привязки DOI и номеров грантов МНВО РК в модуле «Наука» |
| Риск сокрытия конфликта интересов | Внедрение ежегодной цифровой декларации с автоматическим кросс-чеком аффилированности |

---

## 9. Cross-Phase Modifications (multi-phase only)

| File | Also modified in | Coordination note |
|---|---|---|
| `docs/internal_acts/regulations/science_department_regulation.md` | Phase A (referenced in DAV/Faculty) | Сквозная привязка к академическому календарю и нагрузке ППС |
| `docs/internal_acts/regulations/strategic_development_department_regulation.md` | Phase A (referenced in Institute/Chair) | Гармонизация со стратегическими KPI институтов и кафедр |

---

*TS — ABAI_20260917-123500_IS_RETROFIT / Phase B: Science, QA, Compliance & Strategy | 2026-09-17*
