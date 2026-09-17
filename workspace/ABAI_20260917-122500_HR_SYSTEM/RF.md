# RF — ABAI_20260917-122500_HR_SYSTEM: Нормативная база кадрового блока (HR), конкурсного отбора ППС и 7-классной системы оплаты ученых по Приказу МНВО № 424

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
| TS approval ref | `TS-ABAI_20260917-122500_HR_SYSTEM` (approved 2026-09-17) |
| Baseline / Candidate | `v2.0-GENERIC-OVPO` / `v2.1-HR-SYSTEM` |
| VALUE membership | 1 модельное Положение о подразделении, 2 модельных регламента (СОП), 2 модельные ДИ, актуализация каталога функций |
| Arithmetic | 5 new value-bearing files, 1 modified file (`10_human_capital_and_hr.md`), ~1120 LOC |
| Membership deviations | None (полное соответствие спецификации TS) |
| Trigger disposition | Terminal complete |
| Authority and timing | Approved Coordinator / Owner 2026-09-17 |
| Reproduction | Verified against Трудовой кодекс РК, Приказ МОН № 230, Приказ МОН № 338, Приказ МНВО № 424 от 04.09.2026, Приказ МТСЗН № 353 (Enbek.kz) |

### New Files

| File | Description |
|---|---|
| [`docs/internal_acts/regulations/hr_department_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/hr_department_regulation.md) | Модельное Положение о Департаменте управления человеческими ресурсами (HR): структура из 3 секторов, 15+ детальных функций, матрица ответственности RACI, права в модулях УИС («Кадры и ППС», «Приказы», «Enbek.kz»), отдельный раздел защиты ПДн по Закону РК № 94-V. |
| [`docs/internal_acts/sops_and_rules/sop_faculty_and_researcher_recruitment_competition.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/sop_faculty_and_researcher_recruitment_competition.md) | Регламент (СОП) открытого конкурсного замещения должностей ППС и ученых (Приказ МОН РК № 230): порядок формирования Конкурсной комиссии (не менее 40% внешних экспертов), 30-дневный срок публикации, 3 обязательных этапа отбора, цифровой личный кабинет соискателя, академические треки Teaching Track (650–750 ч) и Research Track (300–350 ч + Scopus Q1-Q2). |
| [`docs/internal_acts/sops_and_rules/sop_researcher_compensation_and_kdos_commission.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/sop_researcher_compensation_and_kdos_commission.md) | Регламент (СОП) 7-классного грейдирования и Комиссии по оценке достижений ученых ($K_{дос}$): полная имплементация **Приказа МНВО РК № 424 от 04.09.2026 (дедлайн 22.09.2026)**: 7 квалификационных классов должностей научных сотрудников, регламент постоянной университетской Комиссии, прозрачная шкала оценки личных результатов (WoS/Scopus Q1–Q3, патенты, индекс Хирша) для расчета $K_{дос}$ (1.00–1.50) с готовой формой Оценочного листа (Приложение 1). |
| [`docs/internal_acts/job_descriptions/jd_director_hr.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_director_hr.md) | Модельная должностная инструкция Директора Департамента HR: квалификационные требования по Приказу № 338, обязанности по стратегическому рекрутингу, конкурсным процедурам по № 230, внедрению 7 классов должностей и участию в Комиссии по $K_{дос}$, персональная ответственность по ТК РК и ст. 98 КоАП РК. |
| [`docs/internal_acts/job_descriptions/jd_hr_recruitment_and_records_specialist.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_hr_recruitment_and_records_specialist.md) | Модельная должностная инструкция Ведущего специалиста по кадровому администрированию, воинскому учету и интеграции с ЕСУТД Enbek.kz: регламент кадрового документооборота, воинский учет (взаимодействие с УДО), и **жесткий безусловный SLA по ст. 23 ТК РК: регистрация договоров в ЕСУТД Enbek.kz в течение 3 рабочих дней** под угрозой персональной ответственности по ст. 98 КоАП РК. |

### Modified Files

| File | Description |
|---|---|
| [`docs/functions_and_powers/10_human_capital_and_hr.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/functions_and_powers/10_human_capital_and_hr.md) | Актуализация каталога функций Домена 10: расширение реестра функций до 10 позиций с привязкой к ТК РК, Приказу № 230, Приказу № 338, Приказу № 424, статьям КоАП РК, распределением ролей RACI и кросс-ссылками на новые акты. |

---

## 2. Key Decisions & Regulatory Innovations

1. **Экстренная имплементация Приказа МНВО РК № 424 от 04.09.2026 (вступает в силу 22.09.2026):**
   - Внедрена обязательная 7-классная иерархия научных должностей: Главный научный сотрудник (1 класс), Ведущий научный сотрудник (2 класс), Старший научный сотрудник (3 класс), Научный сотрудник (4 класс), Младший научный сотрудник (5 класс), Инженер лаборатории (6 класс), Лаборант (7 класс).
   - Институционализирована университетская Комиссия по оценке персональных достижений научных работников и утверждена математически прозрачная балльная шкала перевода публикаций Q1–Q3, патентов и индекса Хирша в повышающий коэффициент $K_{дос}$ от 1.00 до 1.50.
   - Разработана типовая форма Оценочного листа соискателя для немедленного запуска расчетов в ОВПО.
2. **Открытый меритократический конкурсный отбор (Приказ МОН РК № 230):**
   - Закреплена обязательная квота внешних независимых экспертов и работодателей в Конкурсной комиссии (не менее 40%).
   - Установлены жесткие процессуальные гарантии: 30-дневный срок публикации объявления в республиканских СМИ и на портале Enbek.kz, подача документов через личный кабинет соискателя в ИС «[V_PRIMARY_EDTECH_PLATFORM]», обязательная видеозапись открытых занятий и тайное голосование.
3. **Дуальные треки профессорско-преподавательского состава:**
   - Преподавательский трек (Teaching Track): 650–750 часов нагрузки с фокусом на образовательные инновации и методическое наставничество.
   - Исследовательский трек (Research Track / High-Research): 300–350 часов аудиторной нагрузки при закреплении персональных KPI по публикациям в журналах квартилей Q1–Q2 (Scopus / WoS) и привлечению грантов ГФ/ПЦФ.
4. **Юридически обязывающий SLA по интеграции с ЕСУТД Enbek.kz:**
   - В ДИ специалиста и руководителя закреплен дедлайн: внесение сведений о заключении, изменении и прекращении трудовых договоров на портале Enbek.kz в течение **3 рабочих дней** со дня издания приказа (ст. 23 ТК РК).
   - Зафиксирована прямая персональная ответственность по ст. 98 КоАП РК за просрочку или искажение данных.
5. **Абсолютная универсальность:**
   - Все 5 актов созданы непосредственно в канонической директории `docs/internal_acts/` без локальных хардкодов с применением переменных `[V_...]` согласно единому реестру.

---

## 3. Verification & Evidence

Все критерии приемки AC-1 — AC-7 подтверждены фактическими файлами и проверены в артефакте доказательств [`workspace/ABAI_20260917-122500_HR_SYSTEM/evidence/EV__HR_SYSTEM.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260917-122500_HR_SYSTEM/evidence/EV__HR_SYSTEM.md):
- **AC-1:** Verified (`hr_department_regulation.md`)
- **AC-2:** Verified (`sop_faculty_and_researcher_recruitment_competition.md`)
- **AC-3:** Verified (`sop_researcher_compensation_and_kdos_commission.md`)
- **AC-4:** Verified (`jd_director_hr.md`)
- **AC-5:** Verified (`jd_hr_recruitment_and_records_specialist.md`)
- **AC-6:** Verified (`10_human_capital_and_hr.md`)
- **AC-7:** Verified (0 local hardcodes, 100% `[V_...]` compliance)

---

*RF — ABAI_20260917-122500_HR_SYSTEM | 2026-09-17*
