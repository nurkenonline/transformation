# REVIEW — ABAI_20260917-122500_HR_SYSTEM: Экспертное заключение по кадровому блоку (HR), конкурсному отбору ППС и 7-классной системе оплаты ученых по Приказу МНВО № 424

> **Date**: 2026-09-17  
> **Reviewer**: Reviewer  
> **Task ID**: `ABAI_20260917-122500_HR_SYSTEM`  
> **Scope**: Нормативная база управления человеческими ресурсами, открытый конкурс ППС (Приказ № 230), 7-классная система оплаты ученых и Комиссия по оценке достижений $K_{дос}$ (Приказ № 424 от 04.09.2026), модельные ДИ, актуализация каталога функций (ABAI-12)  
> **Final Verdict**: `✅ APPROVE`  

---

## 1. Резюме аудита

Проведен независимый юридический, регуляторный и содержательный аудит результатов выполнения задачи ABAI-12 по канонической модели TFW v3.4.0 (`Map ➔ Verify ➔ Judge ➔ Decide`).

### Результаты проверок по стадиям:
- **1. Map (Картирование):**
  - Разработано модельное Положение о Департаменте HR: [`hr_department_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/hr_department_regulation.md);
  - Разработан модельный Регламент конкурсного замещения должностей ППС и ученых: [`sop_faculty_and_researcher_recruitment_competition.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/sop_faculty_and_researcher_recruitment_competition.md);
  - Разработан СОП оплаты труда ученых и Комиссии по $K_{дос}$: [`sop_researcher_compensation_and_kdos_commission.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/sop_researcher_compensation_and_kdos_commission.md);
  - Разработана модельная ДИ Директора Департамента HR: [`jd_director_hr.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_director_hr.md);
  - Разработана модельная ДИ Специалиста по кадровому учету и Enbek.kz: [`jd_hr_recruitment_and_records_specialist.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_hr_recruitment_and_records_specialist.md);
  - Актуализирован каталог функций Домена 10: [`10_human_capital_and_hr.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/functions_and_powers/10_human_capital_and_hr.md);
  - Артефакт доказательств: [`evidence/EV__HR_SYSTEM.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260917-122500_HR_SYSTEM/evidence/EV__HR_SYSTEM.md) подтверждает вердикт `7/7 VERIFIED`.

- **2. Verify (Верификация соответствия нормам РК):**
  - **Имплементация новелл Приказа МНВО РК № 424 от 04.09.2026 (вступает в силу 22.09.2026):**
    - Введена исчерпывающая квалификационная сетка 7 классов должностей научных работников (от Главного научного сотрудника до Лаборанта);
    - Установлен правовой статус и регламент деятельности Комиссии по оценке персональных достижений научных работников;
    - Разработана объективная балльная шкала для расчета повышающего коэффициента $K_{дос}$ в диапазоне 1.00–1.50 на основе публикаций Scopus/WoS Q1–Q3, патентов, индекса Хирша и привлеченных грантов;
    - Создана готовая форма Оценочного листа соискателя (Приложение 1).
  - **Конкурсный отбор (Приказ МОН РК № 230):**
    - Закреплена обязательная 40% квота внешних экспертов в составе Конкурсной комиссии;
    - Зафиксирован 30-дневный срок публичного объявления в республиканских СМИ и на портале Enbek.kz;
    - Внедрена подача документов через личный кабинет соискателя в УИС, обязательная видеозапись открытых занятий и процедура тайного голосования;
    - Формализованы дуальные треки ППС: Teaching Track (650–750 ч) и Research Track (300–350 ч + Scopus Q1-Q2).
  - **Трудовая дисциплина и SLA по Enbek.kz (Трудовой кодекс РК ст. 23, КоАП ст. 98):**
    - В ДИ специалиста и руководителя закреплен жесткий безусловный дедлайн: регистрация сведений о трудовых договорах в ЕСУТД Enbek.kz не позднее **3 рабочих дней** со дня подписания приказа;
    - Зафиксирована прямая персональная ответственность по ст. 98 КоАП РК и ст. 79 КоАП РК (персональные данные).
  - **Отсутствие хардкодов:** Все документы проверены линтером — 0 прямых упоминаний локальных вузов, 100% параметризация системными тегами `[V_...]`.

- **3. Judge (Качество и непротиворечивость):**
  - Документы полностью закрывают критический нормативный дедлайн от 22.09.2026;
  - Матрица RACI в Положении об HR исключает дублирование ответственности;
  - Созданные акты логично дополняют модельный пакет `docs/internal_acts/`.

- **4. Decide (Решение):** `✅ APPROVE`.

---

## 2. Перечень утвержденных модельных актов

1. [`hr_department_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/hr_department_regulation.md) — Модельное Положение о Департаменте управления человеческими ресурсами (HR);
2. [`sop_faculty_and_researcher_recruitment_competition.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/sop_faculty_and_researcher_recruitment_competition.md) — Регламент (СОП) открытого конкурсного замещения должностей ППС и научных работников;
3. [`sop_researcher_compensation_and_kdos_commission.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/sop_researcher_compensation_and_kdos_commission.md) — Регламент (СОП) 7-классного грейдирования и Комиссии по оценке личных достижений ученых ($K_{дос}$);
4. [`jd_director_hr.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_director_hr.md) — Модельная должностная инструкция Директора Департамента HR;
5. [`jd_hr_recruitment_and_records_specialist.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_hr_recruitment_and_records_specialist.md) — Модельная должностная инструкция Специалиста по кадровому администрированию, воинскому учету и интеграции с ЕСУТД Enbek.kz;
6. [`10_human_capital_and_hr.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/functions_and_powers/10_human_capital_and_hr.md) — Каталог функций Домена 10.

---

## 3. Итоговое предписание Координатору

Задача `ABAI_20260917-122500_HR_SYSTEM` (`ABAI-12`) утверждена к закрытию (`DONE`).
Рекомендуется:
1. Зарегистрировать факт `FACT-024` в `KNOWLEDGE.md` о внедрении кадровой модели, конкурсного отбора и 7-классной системы оплаты ученых по Приказу № 424;
2. Обновить Task Board в `README.md` (статус задачи ABAI-12: `🟢 Выполнено`).
