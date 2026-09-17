# RF — ABAI_20260917-123500_IS_RETROFIT / Phase A: Сквозная интеграция требований УИС и SLA в академический и студенческий блок

> **Date**: 2026-09-17  
> **Author**: Executor  
> **Status**: 🟢 RF — Complete  
> **Parent HL**: [HL](HL.md)  
> **TS**: [TS](TS.md)  

---

## 1. What Was Done

### Actual Value-Bearing Accounting

| Fact | Actual result |
|---|---|
| TS approval ref | `TS-ABAI_20260917-123500_IS_RETROFIT` (Phase A approved 2026-09-17) |
| Baseline / Candidate | `v2.1-HR-SYSTEM` / `v2.2-IS-RETROFIT-PHASE-A` |
| VALUE membership | 12 модернизированных внутренних актов академического и студенческого контура |
| Arithmetic | 0 new files, 12 modified files, ~780 touched LOC |
| Membership deviations | None (все 12 целевых файлов обновлены в соответствии со скоупом) |
| Trigger disposition | Terminal complete for Phase A |
| Authority and timing | Approved Coordinator / Owner 2026-09-17 |
| Reproduction | Verified against Трудовой кодекс РК (ст. 22, 23, 52, 120, 181, 182), СТ РК 34.015-2002, ТЗ ГТС |

### Modified Files (12 файлов)

| File | Changes Made |
|---|---|
| [`docs/internal_acts/regulations/dav_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/dav_regulation.md) | Добавлен раздел 8 «Регламентация деятельности в УИС»: закреплены модули «Академический процесс», «Силлабусы», «ЕПВО/НОБД», «Академический календарь», роли RBAC (`Academic_Administrator`, `Curriculum_Validator`), сроки SLA и ответственность по ст. 22, 64 ТК РК. |
| [`docs/internal_acts/regulations/registrar_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/registrar_regulation.md) | Добавлен раздел 8 «Регламентация деятельности в УИС»: закреплены модули «Офис регистратора», «Приказы по контингенту», «Экзаменационные ведомости», «Дипломы с QR-кодом», интеграции с ЕПВО, автоматическая блокировка ведомостей через **24 часа**, проведение приказов **день-в-день**, запрет изменения ведомостей без протокола апелляции и комплаенс-офицера. |
| [`docs/internal_acts/regulations/institute_model_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/institute_model_regulation.md) | Добавлен раздел 8 «Регламентация деятельности в УИС»: закреплены модули «Эдвайзер», «Академический процесс», «Выпускные работы и Антиплагиат», роли `Dean_Director`, `Adviser_Coordinator`, дедлайн утверждения ИУП эдвайзерами (**до 3 дней**), запрет сбора бумажных дубликатов. |
| [`docs/internal_acts/regulations/department_chair_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/department_chair_regulation.md) | Добавлен раздел 8 «Регламентация деятельности в УИС»: закреплены модули «Распределение нагрузки», «Силлабусы и УМКД», «Электронный журнал», «Экзаменационные ведомости», роль `Department_Chair`, жесткие дедлайны ввода нагрузки (25 августа / 15 января) и персональная ответственность зав. кафедрой по ТК РК. |
| [`docs/internal_acts/regulations/youth_and_social_affairs_department_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/youth_and_social_affairs_department_regulation.md) | Добавлен раздел 6 «Регламентация деятельности в УИС»: закреплены модули «Студент и молодежные инициативы», «Общежития», «Психологическая поддержка», роли `Youth_Affairs_Admin`, `Dormitory_Commission_Member`, 48-часовой SLA рассмотрения заявок на соцподдержку и ответственность за ПДн по ст. 79 КоАП РК. |
| [`docs/internal_acts/regulations/student_dormitories_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/student_dormitories_regulation.md) | Внедрен раздел 6: категорический запрет ручного заселения без сгенерированного в модуле «Общежития» электронного ордера с QR-кодом (срок действия 3 дня), сканирование ордера при вселении, немедленное расторжение трудового договора с комендантом по ст. 52 ТК РК за допуск без ордера УИС. |
| [`docs/internal_acts/job_descriptions/jd_faculty_model.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_faculty_model.md) | Внесены жесткие цифровые обязанности ППС: силлабусы — за 10 дней до семестра; ввод текущих оценок — **в течение 48 часов**; подписание экзаменационной ведомости — **в течение 24 часов** с автоматической блокировкой; запрет передачи учетных записей; дисциплинарная ответственность по ст. 22, 23, 52 (п. 1 пп. 16), 120, 181, 182 ТК РК. |
| [`docs/internal_acts/job_descriptions/jd_head_registrar.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_head_registrar.md) | Закреплен 24-часовой регламент блокировки экзаменационных ведомостей, проведение приказов по контингенту «день-в-день», запрет разблокировки без протокола апелляции и комплаенс-контроля, персональная ответственность по ст. 52 ТК РК и ст. 79 КоАП РК. |
| [`docs/internal_acts/job_descriptions/jd_director_dav.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_director_dav.md) | Закреплены обязанности непрерывного мониторинга баз данных УИС, контроль соблюдения дедлайнов валидации силлабусов (за 5 дней) и каталогов ОП (за 30 дней), верификация интеграции с ЕПВО, персональная ответственность по ст. 22, 23, 52 ТК РК. |
| [`docs/internal_acts/job_descriptions/jd_dormitory_manager.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_dormitory_manager.md) | Закреплена обязанность вселения обучающихся исключительно при предъявлении персонального Электронного ордера с QR-кодом со сканированием в модуле «Общежития», запрет ручного заселения, персональная ответственность в виде увольнения по ст. 52 ТК РК. |
| [`docs/internal_acts/sops_and_rules/sop_individual_curriculum_and_schedule.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/sop_individual_curriculum_and_schedule.md) | Внедрен раздел 5 «Цифровой контур и ответственность в УИС»: 100% безбумажный выбор в модуле «Эдвайзер», дедлайн согласования ИУП (3 дня), категорический запрет преподавателям допускать к занятиям студентов вне утвержденной группы УИС со ссылкой на ст. 22 ТК РК. |
| [`docs/internal_acts/sops_and_rules/academic_integrity_policy.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/academic_integrity_policy.md) | Добавлен раздел 5 «Цифровой контур и защита неизменяемости данных в УИС»: обязательная загрузка 100% работ в модуль «Антиплагиат», неизменяемость журнала успеваемости, блокировка ведомостей через 24 часа, журналирование Audit Trail, увольнение по ст. 52 ТК РК за подлог или передачу паролей. |

---

## 2. Key Decisions & Structural Alignment

1. **Юридическая бесшовность:** Требования по работе в цифровой системе теперь закреплены не в виде абстрактных пожеланий, а в виде официальных трудовых обязанностей работников со строгой привязкой к мерам дисциплинарного взыскания (ст. 64 ТК РК) и увольнения за повторное неисполнение (пп. 16 п. 1 ст. 52 ТК РК).
2. **Ликвидация параллельного документооборота:** Во всех 4 Положениях академического ядра наложен прямой запрет на сбор бумажных копий ведомостей, заявлений и транскриптов при наличии цифровых эквивалентов в УИС.
3. **Защита от коррупционных рисков в сессию и общежития:**
   - Закрытие экзаменационных ведомостей жестко ограничено **24 часами**, после чего редактирование блокируется автоматически на уровне СУБД;
   - Заселение в общежития осуществляется исключительно по сканированию QR-кода электронного ордера УИС с автоматической аннуляцией через 3 дня при неявке.

---

## 3. Verification & Evidence

Все критерии приемки AC-1 — AC-6 подтверждены фактическими файлами и проверены в артефакте доказательств [`workspace/ABAI_20260917-123500_IS_RETROFIT/evidence/EV__IS_RETROFIT_PHASE_A.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260917-123500_IS_RETROFIT/evidence/EV__IS_RETROFIT_PHASE_A.md). Вердикт: **6/6 VERIFIED**.

---

*RF — ABAI_20260917-123500_IS_RETROFIT / Phase A | 2026-09-17*
