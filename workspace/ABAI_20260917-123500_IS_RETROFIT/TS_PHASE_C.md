# TS — ABAI_20260917-123500_IS_RETROFIT / Phase C: Сквозная интеграция требований УИС, кибербезопасности, ЕПВО и защиты данных в ИТ и обеспечивающий контур

> **Date**: 2026-09-17  
> **Author**: Coordinator  
> **Status**: 🟢 APPROVED — approved by owner 2026-09-17  
> **Parent HL**: [HL-ABAI_20260917-123500_IS_RETROFIT](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260917-123500_IS_RETROFIT/HL.md)  

---

## 1. Objective

Осуществить нормативную финализацию сквозной цифровой модернизации нормативной базы университета: переработать 10 оставшихся актов обеспечивающего, ИТ- и карьерного контура (Положения об ИТ-подразделениях, Центре карьеры, ДИ руководителей и специализированные СОПы по ИБ, ПДн и ЕПВО). В акты юридически вшиваются требования по:
1. Администрированию модулей «Инфраструктура и Доступ», «Интеграция с ЕПВО/НОБД», «Выпускник и Трудоустройство» информационной системы («[V_PRIMARY_EDTECH_PLATFORM]»);
2. 5 государственным протоколам интеграции МНВО РК (ЕПВО, НОБД, Smart Bridge, Enbek.kz, ОСМС);
3. Безусловному соблюдению 24-часового регламента нотификации МЦРИАП РК об инцидентах безопасности персональных данных (Приказ № 395/НҚ);
4. Персональной ответственности ИТ-персонала и администраторов баз данных по статьям 22, 23, 52 (п. 1 пп. 16), 120 Трудового кодекса РК и статье 79 КоАП РК.

---

## 2. Scope

### In Scope

- **Положения структурных подразделений (3 файла):**
  1. `docs/internal_acts/regulations/digitalization_department_regulation.md` (Управление цифровизации)
  2. `docs/internal_acts/regulations/it_infrastructure_department_regulation.md` (Управление информационных технологий)
  3. `docs/internal_acts/regulations/career_center_and_grant_employment_regulation.md` (Центр карьеры и распределения выпускников)
- **Должностные инструкции (3 файла):**
  4. `docs/internal_acts/job_descriptions/jd_head_digitalization.md` (Начальник Управления цифровизации)
  5. `docs/internal_acts/job_descriptions/jd_head_it_infrastructure.md` (Начальник УИТ)
  6. `docs/internal_acts/job_descriptions/jd_head_career_center.md` (Руководитель Центра карьеры)
- **Регламенты и СОПы (4 файла):**
  7. `docs/internal_acts/sops_and_rules/sop_employee_cybersecurity_and_labor_safety.md` (СОП кибербезопасности и БиОТ)
  8. `docs/internal_acts/sops_and_rules/sop_personal_data_protection.md` (Регламент защиты персональных данных)
  9. `docs/internal_acts/sops_and_rules/sop_epvo_nobd_integration.md` (СОП интеграции с ЕПВО и НОБД)
  10. `docs/internal_acts/regulations/is_4level_security_registry.md` (4-уровневый реестр документации ИБ)
- **Артефакт доказательств:**
  - `workspace/ABAI_20260917-123500_IS_RETROFIT/evidence/EV__IS_RETROFIT_PHASE_C.md`

### Out of Scope

- Акты академического, студенческого, научного, комплаенс и стратегического блоков (уже полностью модернизированы в Phase A и Phase B — 24 акта).

---

## 3. Principles Check

| # | HL §7 principle | Enforced by | Gate |
|---|---|---|---|
| P0 | Трудовой кодекс РК (ст. 22, 23, 52, 120, 181, 182) | AC-2, AC-3 | Наличие прямых статей ТК РК в ДИ ИТ-руководителей и СОПе кибербезопасности |
| P1 | Закон РК «О персональных данных и их защите», Приказ МЦРИАП № 395/НҚ | AC-1, AC-3 | Наличие жесткого 24-часового регламента нотификации регулятора об утечках |
| P2 | ЕТИКТ и ИБ (Постановление Правительства РК № 832) | AC-1, AC-3 | Регламентация сетевого периметра, ЦОД, RPO/RTO и ролевой модели RBAC |
| P3 | СТ РК 34.015-2002 и спецификации ТЗ ГТС (22 модуля) | AC-1, AC-2 | Ссылки на конкретные модули («Инфраструктура», «ЕПВО/НОБД», «Выпускник») |
| P4 | Приказ МОН РК № 39 (3-летняя отработка грантов) | AC-1, AC-2 | Автоматическая выгрузка данных в Enbek.kz и ГЦВП |

---

## 4. Affected Files and Value-Bearing Accounting

| File / selector | Action | Class | Semantic reason / required result |
|---|---|---|---|
| `docs/internal_acts/regulations/digitalization_department_regulation.md` | MODIFY | `VALUE` | Добавление раздела регламентации в УИС: администрирование 22 модулей, ролевая модель RBAC, СТ РК 34.015-2002, аттестация ГТС |
| `docs/internal_acts/regulations/it_infrastructure_department_regulation.md` | MODIFY | `VALUE` | Добавление раздела регламентации в УИС: поддержка серверного парка, ЦОД, СКУД, Wi-Fi 6, регламенты RPO ≤ 1 ч / RTO ≤ 4 ч |
| `docs/internal_acts/regulations/career_center_and_grant_employment_regulation.md` | MODIFY | `VALUE` | Добавление раздела регламентации в УИС: модуль «Выпускник и Трудоустройство», 3-летняя отработка грантов, сверка с Enbek.kz |
| `docs/internal_acts/job_descriptions/jd_head_digitalization.md` | MODIFY | `VALUE` | Роль `IT_SuperAdmin`, контроль 5 протоколов ЕПВО, целостность баз данных, ответственность по ст. 52 ТК РК и ст. 79 КоАП РК |
| `docs/internal_acts/job_descriptions/jd_head_it_infrastructure.md` | MODIFY | `VALUE` | Роль `Network_Admin`, бесперебойность ЦОД (SLA 99.8%), предотвращение инцидентов ИТ, ответственность по ст. 52 ТК РК |
| `docs/internal_acts/job_descriptions/jd_head_career_center.md` | MODIFY | `VALUE` | Роль `Career_Manager`, цифровой реестр вакансий и отработки, выгрузка данных в Минтруда РК, санкции по ст. 52 ТК РК |
| `docs/internal_acts/sops_and_rules/sop_employee_cybersecurity_and_labor_safety.md` | MODIFY | `VALUE` | Интеграция кибергигиены в БиОТ по ТК РК, ответственность за передачу паролей и фишинг по ст. 52 (п. 1 пп. 16) ТК РК |
| `docs/internal_acts/sops_and_rules/sop_personal_data_protection.md` | MODIFY | `VALUE` | Прошивка жесткого 24-часового срока нотификации МЦРИАП об утечках ПДн (Приказ № 395/НҚ), ст. 79 КоАП РК |
| `docs/internal_acts/sops_and_rules/sop_epvo_nobd_integration.md` | MODIFY | `VALUE` | 5 отраслевых протоколов ЕПВО МНВО РК, сквозная валидация дипломов с QR-кодом, регламент ежедневного обновления зеркал |
| `docs/internal_acts/regulations/is_4level_security_registry.md` | MODIFY | `VALUE` | Актуализация 4 уровней ИБ (ISO 27001) под эталонную архитектуру УИС, неизменяемый Audit Trail, контроль прав RBAC |
| `workspace/ABAI_20260917-123500_IS_RETROFIT/evidence/EV__IS_RETROFIT_PHASE_C.md` | CREATE | `ASSURANCE` | Артефакт доказательств реализации критериев Phase C |

### Prospective accounting contract

| Fact | Approved value |
|---|---|
| Subject / exact VALUE selector | 10 модифицируемых файлов в `docs/internal_acts/` |
| Baseline / selector source | `v2.3-IS-RETROFIT-PHASE-B`; this TS at approval commit |
| Candidate rule | First tested Executor commit with required VALUE+ASSURANCE, before EV/RF/REVIEW/final transition |
| Logical VALUE files | 10 файлов |
| Touched text LOC | ~550–750 строк дополнений |
| Triggers / disposition | Terminal complete for Phase C (финализация всей задачи ABAI-13) |
| Multiplier / authority | Approved Coordinator / Owner 2026-09-17 |
| Approval epoch / failure | Owner approval required at TS Freeze Gate |

```powershell
git diff --name-status --find-renames=50% -z <BASELINE_SHA> <CANDIDATE_SHA> -- $valuePaths
git diff --numstat --find-renames=50% -z <BASELINE_SHA> <CANDIDATE_SHA> -- $valuePaths
```

### Prospective scope rulings

None. Изменения строго ограничены перечнем 10 файлов Phase C.

### Task-local hard constraints (when material)

| M1 consequence | M2 object/risk | M3 measure/selector | M4 pre-act check | M5 softer-control gap | M6 change authority |
|---|---|---|---|---|---|
| Разрушение ролевой изоляции | ИТ-администраторы правят оценки | Запрет роли `IT_SuperAdmin` изменять оценки в обход Audit Trail | Проверка текста положений и ДИ | Общие фразы «обеспечивает безопасность» | Coordinator / Owner |
| Сокрытие утечек ПДн | Штрафы по ст. 79 КоАП РК | Фиксация 24-часового срока нотификации регулятора | Проверка `sop_personal_data_protection.md` | Отсутствие дедлайна в часах | Coordinator / Owner |

**Actions (not budget dimensions):** 10 files modified, 1 evidence file created.  
**Immutable owner-approved denominator:** 10 VALUE files, ≤750 touched LOC.

---

## 5. Acceptance Criteria

### AC-1: Регламентация деятельности ИТ-подразделений и Центра карьеры в УИС

Положения об Управлении цифровизации, УИТ и Центре карьеры дополнены профильными разделами регламентации в информационной системе («[V_PRIMARY_EDTECH_PLATFORM]»).
- [ ] В `digitalization_department_regulation.md` закреплены полномочия администрирования 22 модулей, управление ролями RBAC, аттестация ГТС по СТ РК 34.015-2002;
- [ ] В `it_infrastructure_department_regulation.md` закреплены требования обеспечения доступности серверов (SLA 99.8%), СКУД, резервного копирования RPO ≤ 1 ч, RTO ≤ 4 ч;
- [ ] В `career_center_and_grant_employment_regulation.md` закреплена работа в модуле «Выпускник и Трудоустройство», персональный учет обязательной 3-летней отработки грантов по Приказу МОН № 39 и интеграция с Enbek.kz.

Gate: Проверка наличия разделов регламентации в УИС во всех 3 положениях.  
Evidence: `evidence/EV__IS_RETROFIT_PHASE_C.md` (AC-1 status).

### AC-2: Должностные инструкции руководящего состава ИТ и Центра карьеры

В ДИ Начальника Управления цифровизации, Начальника УИТ и Руководителя Центра карьеры вшиты точные цифровые обязанности, SLA и ответственность по ТК РК.
- [ ] В `jd_head_digitalization.md` закреплены роли `IT_SuperAdmin`, SLA устранения системных сбоев, ответственность по ст. 52 ТК РК и ст. 79 КоАП РК;
- [ ] В `jd_head_it_infrastructure.md` закреплена роль `Network_Admin`, круглосуточный мониторинг периметра сети и ЦОД, ответственность по ст. 52 ТК РК;
- [ ] В `jd_head_career_center.md` закреплена роль `Career_Manager`, 3-дневный срок заведения договоров отработки, ответственность по ст. 52 ТК РК.

Gate: Проверка наличия подразделов по УИС, SLA и статей 22, 23, 52 ТК РК во всех 3 ДИ.  
Evidence: `evidence/EV__IS_RETROFIT_PHASE_C.md` (AC-2 status).

### AC-3: СОПы по кибербезопасности, защите данных, ЕПВО и реестр ИБ

Модернизированы 4 регламентирующих акта информационной безопасности и внешних интеграций.
- [ ] В `sop_employee_cybersecurity_and_labor_safety.md` правила кибергигиены юридически включены в контур БиОТ (ст. 181, 182 ТК РК), установлены санкции по ст. 52 ТК РК за передачу паролей;
- [ ] В `sop_personal_data_protection.md` закреплен жесткий дедлайн информирования регулятора (МЦРИАП РК) об инцидентах безопасности ПДн — **в течение 1 рабочего дня (24 часов)** по Приказу № 395/НҚ;
- [ ] В `sop_epvo_nobd_integration.md` регламентированы 5 протоколов обмена с ЕПВО МНВО РК, генерация номеров дипломов с QR-кодом и ежедневное обновление зеркал;
- [ ] В `is_4level_security_registry.md` актуализированы требования 4-уровневой модели ИБ (ISO 27001) с неизменяемым Audit Trail и матрицей RBAC.

Gate: Текстовая проверка наличия 24-часового SLA, ссылок на ЕПВО и ТК РК.  
Evidence: `evidence/EV__IS_RETROFIT_PHASE_C.md` (AC-3 status).

### AC-4: Универсализация и сохранение переменных

Все документы строго сохраняют нейтральный профиль и системные переменные `[V_...]`.
- [ ] Отсутствуют локальные наименования сторонних вузов;
- [ ] Используются унифицированные плейсхолдеры `[V_ORGANIZATION_NAME]`, `[V_PRIMARY_EDTECH_PLATFORM]`, `[V_CHANCELLOR_TITLE]`.

Gate: Grep-валидация на отсутствие неразрешенных локальных хардкодов.  
Evidence: `evidence/EV__IS_RETROFIT_PHASE_C.md` (AC-4 status).

### Evidence Artifacts

| File | Description |
|---|---|
| `workspace/ABAI_20260917-123500_IS_RETROFIT/evidence/EV__IS_RETROFIT_PHASE_C.md` | Сводный протокол доказательств верификации изменений 10 файлов по критериям AC-1 — AC-4 |

---

## 6. Technical Guidance

- Использовать спецификации из `docs/generic_framework/digital/01_university_is_reference_blueprint.md` и `02_digital_to_job_integration_matrix.md`.
- Сохранять существующую архитектонику локальных нормативных актов, встраивая новые цифровые разделы без нарушения базовой нумерации.

---

## 7. Definition of Failure

- ❌ Отсутствие 24-часового дедлайна уведомления регулятора в `sop_personal_data_protection.md`.
- ❌ Отсутствие статей 22, 23, 52 ТК РК в должностных инструкциях ИТ-руководителей.
- ❌ Появление локальных хардкодов вместо переменных `[V_...]`.
- ❌ Превышение Scope Budget (более 10 модифицируемых файлов).

---

## 8. Phase Risks

| Risk | Mitigation |
|---|---|
| Риск противоречия между полномочиями Управления цифровизации и УИТ | Четкое разделение: УЦ отвечает за прикладные модули, БД и интеграции; УИТ — за «железо», сеть, серверы и СКУД |
| Риск разглашения персональных данных при интеграции с ЕПВО | Применение защищенных каналов связи и валидация токенов доступа по протоколам Smart Bridge |

---

## 9. Cross-Phase Modifications (multi-phase only)

| File | Also modified in | Coordination note |
|---|---|---|
| `docs/internal_acts/regulations/is_4level_security_registry.md` | Initial in ABAI-5 | Гармонизируется с 22 модулями УИС и матрицей RBAC Phase A/B |
| `docs/internal_acts/sops_and_rules/sop_epvo_nobd_integration.md` | Initial in ABAI-5 | Согласован с регламентами Офиса регистратора (Phase A) и Центра аккредитации (Phase B) |

---

*TS — ABAI_20260917-123500_IS_RETROFIT / Phase C: IT, Security, Career & Integration Retrofit | 2026-09-17*
