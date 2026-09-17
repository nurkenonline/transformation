# TS — ABAI_20260917-123500_IS_RETROFIT / Phase A: Сквозная интеграция требований УИС и SLA в академический и студенческий блок

> **Date**: 2026-09-17  
> **Author**: Coordinator  
> **Status**: 🟢 APPROVED — approved by owner 2026-09-17  
> **Parent HL**: [HL-ABAI_20260917-123500_IS_RETROFIT](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260917-123500_IS_RETROFIT/HL.md)  

---

## 1. Objective

Провести глубокую содержательную модернизацию 12 ключевых внутренних нормативных актов академического и студенческого контура (Положения, ДИ, СОПы) путем сквозного внедрения обязательных требований к использованию университетской информационной системы («[V_PRIMARY_EDTECH_PLATFORM]»), установления жестких регламентных сроков (SLA) и закрепления персональной ответственности работников по Трудовому кодексу Республики Казахстан (ст. 22, 23, 52, 120, 181, 182).

---

## 2. Scope

### In Scope (12 файлов Phase A)
- **Положения структурных подразделений:**
  1. `docs/internal_acts/regulations/dav_regulation.md` (Департамент по академическим вопросам)
  2. `docs/internal_acts/regulations/registrar_regulation.md` (Офис регистратора)
  3. `docs/internal_acts/regulations/institute_model_regulation.md` (Типовое положение об Институте)
  4. `docs/internal_acts/regulations/department_chair_regulation.md` (Типовое положение о Кафедре)
  5. `docs/internal_acts/regulations/youth_and_social_affairs_department_regulation.md` (Департамент по молодежной политике)
  6. `docs/internal_acts/regulations/student_dormitories_regulation.md` (Положение о студенческих общежитиях)
- **Должностные инструкции:**
  7. `docs/internal_acts/job_descriptions/jd_faculty_model.md` (Типовая ДИ ППС)
  8. `docs/internal_acts/job_descriptions/jd_head_registrar.md` (ДИ Руководителя Офиса регистратора)
  9. `docs/internal_acts/job_descriptions/jd_director_dav.md` (ДИ Директора ДАВ)
  10. `docs/internal_acts/job_descriptions/jd_dormitory_manager.md` (ДИ Заведующего общежитием)
- **Регламенты и СОПы:**
  11. `docs/internal_acts/sops_and_rules/sop_individual_curriculum_and_schedule.md` (Регламент ИУП и расписания)
  12. `docs/internal_acts/sops_and_rules/academic_integrity_policy.md` (Политика академической честности)
- **Артефакт доказательств:**
  - `workspace/ABAI_20260917-123500_IS_RETROFIT/evidence/EV__IS_RETROFIT_PHASE_A.md`

### Out of Scope
- Документы научного блока, комплаенс-службы и стратегического управления (вынесены в Phase B).
- Документы ИТ-департамента, службы безопасности и инфраструктуры (вынесены в Phase C).

---

## 3. Principles Check

| # | HL §7 principle | Enforced by | Gate |
|---|---|---|---|
| P0 | Трудовой кодекс РК (ст. 22, 23, 52, 120, 181, 182) | AC-2, AC-3, AC-4 | Проверка наличия формулировок ответственности в ДИ |
| P1 | СТ РК 34.015-2002 и спецификации ТЗ ГТС (22 модуля) | AC-1, AC-5 | Наличие ссылок на конкретные модули УИС |
| P2 | Матрица цифровой интеграции (`02_digital_to_job_integration_matrix.md`) | AC-1, AC-2, AC-3 | Соответствие ролей RBAC и сроков SLA |
| P3 | Регламент цифрового взаимодействия (`03_sop_digital_governance_and_sla.md`) | AC-2, AC-5 | Запрет передачи логинов/паролей, протокол закрытия ведомостей |
| P4 | Закон РК «О персональных данных и их защите» (ст. 79 КоАП РК) | AC-1, AC-4 | Обязательства по защите ПДн студентов и преподавателей |

---

## 4. Affected Files and Value-Bearing Accounting

| File / selector | Action | Class | Semantic reason / required result |
|---|---|---|---|
| `docs/internal_acts/regulations/dav_regulation.md` | MODIFY | `VALUE` | Добавление раздела «Регламентация в УИС» (модули ОР, Академпроцесс, Силлабусы) |
| `docs/internal_acts/regulations/registrar_regulation.md` | MODIFY | `VALUE` | Раздел «Регламентация в УИС» (модули Приказы, Дипломы с QR, ЕПВО/НОБД, SLA) |
| `docs/internal_acts/regulations/institute_model_regulation.md` | MODIFY | `VALUE` | Раздел «Регламентация в УИС» (модули Эдвайзер, Контроль успеваемости, Ведомости) |
| `docs/internal_acts/regulations/department_chair_regulation.md` | MODIFY | `VALUE` | Раздел «Регламентация в УИС» (модули Распределение нагрузки, Силлабусы, Ведомости) |
| `docs/internal_acts/regulations/youth_and_social_affairs_department_regulation.md` | MODIFY | `VALUE` | Раздел «Регламентация в УИС» (модули Общежития, Студент, Воспитательная работа) |
| `docs/internal_acts/regulations/student_dormitories_regulation.md` | MODIFY | `VALUE` | Включение нормы о заселении строго по электронным ордерам УИС |
| `docs/internal_acts/job_descriptions/jd_faculty_model.md` | MODIFY | `VALUE` | Цифровые обязанности ППС, дедлайны (48 ч / 24 ч), санкции по ТК РК |
| `docs/internal_acts/job_descriptions/jd_head_registrar.md` | MODIFY | `VALUE` | Обязанности администрирования УИС, контроль ведомостей, санкции по ТК РК |
| `docs/internal_acts/job_descriptions/jd_director_dav.md` | MODIFY | `VALUE` | Обязанности мониторинга целостности данных ОП и учебного графика в УИС |
| `docs/internal_acts/job_descriptions/jd_dormitory_manager.md` | MODIFY | `VALUE` | Обязанность заселения исключительно по электронному ордеру в УИС |
| `docs/internal_acts/sops_and_rules/sop_individual_curriculum_and_schedule.md` | MODIFY | `VALUE` | Сквозной безбумажный выбор дисциплин и генерация расписания в УИС |
| `docs/internal_acts/sops_and_rules/academic_integrity_policy.md` | MODIFY | `VALUE` | Интеграция модуля «Антиплагиат», неизменяемость цифрового журнала |
| `workspace/ABAI_20260917-123500_IS_RETROFIT/evidence/EV__IS_RETROFIT_PHASE_A.md` | CREATE | `ASSURANCE` | Артефакт доказательств реализации критериев Phase A |

### Prospective accounting contract

| Fact | Approved value |
|---|---|
| Subject / exact VALUE selector | 12 модифицируемых файлов в `docs/internal_acts/` |
| Logical VALUE files | 12 файлов |
| Touched text LOC | ~650–900 строк дополнений |
| Budget Triggers | В рамках лимитов Scope Budget TFW v3.4.0 (макс. 12 модифицируемых файлов) |

---

## 5. Acceptance Criteria

### AC-1: Регламентация работы в УИС в Положениях академического блока
- В `dav_regulation.md`, `registrar_regulation.md`, `institute_model_regulation.md` и `department_chair_regulation.md` добавлен отдельный раздел *«Регламентация деятельности в университетской информационной системе («[V_PRIMARY_EDTECH_PLATFORM]»)»*.
- Закреплены права доступа по модели RBAC к конкретным модулям (Офис регистратора, Академический процесс, Силлабусы, Эдвайзер, Приказы по контингенту, Распределение нагрузки, Дипломы с QR).
- Закреплен запрет на ведение параллельного бумажного документооборота при наличии электронного эквивалента в УИС.
- Gate: Проверка наличия выделенного раздела о работе в УИС во всех 4 положениях.

### AC-2: Должностная инструкция ППС (Цифровые обязанности и SLA)
- В `jd_faculty_model.md` внесены детальные пошаговые трудовые обязанности преподавателя:
  1. Загрузка силлабуса и УМКД в модуль «Силлабусы» не позднее **10 календарных дней** до начала семестра;
  2. Выставление оценок текущей успеваемости и посещаемости в модуль «Академический процесс» в течение **48 часов** с момента проведения занятия;
  3. Заполнение и подписание экзаменационной ведомости в течение **24 часов** с момента завершения экзамена;
  4. Проверка курсовых и выпускных работ в модуле «Антиплагиат»;
  5. Категорический запрет передачи учетной записи (логина и пароля) третьим лицам или обучающимся;
  6. Персональная дисциплинарная ответственность по статьям 22, 23, 52, 120, 181, 182 Трудового кодекса РК за нарушение сроков и несанкционированное изменение данных.
- Gate: Проверка наличия точных SLA (48 ч, 24 ч) и статей ТК РК.

### AC-3: Должностные инструкции руководителей академического блока
- В `jd_head_registrar.md` и `jd_director_dav.md` внедрены обязанности по системному аудиту полноты заполнения баз данных УИС, блокировке ведомостей по истечении 24 часов, контролю синхронизации контингента с ЕПВО/НОБД МНВО РК, персональной ответственности за достоверность данных по ТК РК и КоАП РК.
- Gate: Наличие норм аудита баз данных и блокировки ведомостей.

### AC-4: Цифровизация студенческого блока и общежитий
- В `youth_and_social_affairs_department_regulation.md`, `student_dormitories_regulation.md` и `jd_dormitory_manager.md` закреплено:
  1. Подача заявлений на общежитие осуществляется исключительно в цифровом виде через модуль «Общежития» в личном кабинете студента;
  2. Автоматический скоринг по 5 установленным законодательством категориям приоритетности;
  3. Категорический запрет заселения без сформированного в УИС цифрового ордера с QR-кодом;
  4. Дисциплинарная ответственность коменданта за заселение обучающихся в обход информационной системы.
- Gate: Проверка запрета заселения без электронного ордера УИС.

### AC-5: Модернизация регламентов и СОП (ИУП и академическая честность)
- В `sop_individual_curriculum_and_schedule.md` процесс выбора дисциплин и утверждения ИУП эдвайзером переведен на 100% цифровой регламент в модуле «Эдвайзер» УИС.
- В `academic_integrity_policy.md` регламентирована обязательная проверка всех видов письменных работ в модуле «Антиплагиат», фиксация протокола проверки (Digital Certificate) и неизменяемость журнала успеваемости с логированием транзакций (Audit Trail).
- Gate: Проверка цифрового контура в текстах обоих СОПов.

### AC-6: Универсальность и параметры `[V_...]`
- Все правки выполнены без упоминания конкретных вузов с использованием системных плейсхолдеров `[V_PRIMARY_EDTECH_PLATFORM]`, `[V_ORGANIZATION_NAME]`, `[V_CHANCELLOR_TITLE]`.
- Gate: Grep-валидация на отсутствие локальных хардкодов.

### Evidence Artifacts

| File | Description |
|---|---|
| `workspace/ABAI_20260917-123500_IS_RETROFIT/evidence/EV__IS_RETROFIT_PHASE_A.md` | Сводный протокол верификации модификаций 12 файлов по критериям AC-1 — AC-6 |

---

## 6. Technical Guidance

- Использовать единые термины из `docs/generic_framework/digital/01_university_is_reference_blueprint.md`.
- Сохранять исходную структуру нормативных актов, добавляя специальные пункты и разделы органично.

---

## 7. Definition of Failure

- ❌ Отсутствие точных сроков (48 ч / 24 ч) в ДИ преподавателя.
- ❌ Отсутствие прямого запрета заселения без ордера УИС в документах общежития.
- ❌ Появление локальных названий университетов вместо `[V_...]`.

---

## 8. Phase Risks

| Risk | Mitigation |
|---|---|
| Нарушение целостности существующих разделов актов | Точечная интеграция подразделов с сохранением сквозной нумерации |

---

*TS — ABAI_20260917-123500_IS_RETROFIT / Phase A: Academic & Student IS Integration | 2026-09-17*
