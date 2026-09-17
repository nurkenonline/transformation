# REVIEW — ABAI_20260917-123500_IS_RETROFIT: Экспертное заключение по сквозной интеграции требований УИС и SLA в научный блок, качество, комплаенс и стратегию (Фаза B)

> **Date**: 2026-09-17  
> **Reviewer**: Reviewer  
> **Task ID**: `ABAI_20260917-123500_IS_RETROFIT` (Phase B)  
> **Scope**: Сквозная интеграция требований УИС, регламентных сроков (SLA) и дисциплинарной ответственности по Трудовому кодексу РК в 12 актов научного контура, обеспечения качества, комплаенса и стратегии (ABAI-13 Phase B)  
> **Final Verdict**: `✅ APPROVE`  

---

## 1. Резюме аудита

Проведен детальный независимый аудит внесенных изменений в 12 актов по 4-этапной модели TFW v3.4.0 (`Map ➔ Verify ➔ Judge ➔ Decide`).

### Результаты проверок по стадиям:
- **1. Map (Картирование):**
  - Все 12 целевых файлов проверены на наличие внесенных дополнений;
  - Проверены взаимные связи с эталонным профилем УИС (`01_university_is_reference_blueprint.md`), матрицей цифровой интеграции (`02_digital_to_job_integration_matrix.md`) и регламентом взаимодействия (`03_sop_digital_governance_and_sla.md`);
  - Артефакт доказательств: [`evidence/EV__IS_RETROFIT_PHASE_B.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260917-123500_IS_RETROFIT/evidence/EV__IS_RETROFIT_PHASE_B.md) подтверждает вердикт `6/6 VERIFIED`.

- **2. Verify (Верификация норм, SLA и санкций):**
  - **Положения подразделений:**
    - `science_department_regulation.md`: внедрен Раздел 8, регламентирующий модули «Наука и НИОКР», «Диссертационные советы», «Антиплагиат», роли RBAC (`Science_SuperAdmin`, `Science_Grant_Manager`), дедлайны (3 дня на темы, 5 дней на публикации) и запрет бумажных отчетов;
    - `commercialization_office_regulation.md`: внедрен Раздел 8, модуль «Коммерциализация и Стартапы», 2 дня на РИД, 3 дня на патенты, 5 дней на лицензии, материальная ответственность по ст. 120 ТК РК;
    - `compliance_service_regulation.md`: внедрен Раздел 8, модуль «Комплаенс», независимая роль `Compliance_Auditor` с доступом к неизменяемым логам Audit Trail, 24 ч SLA на инциденты Whistleblowing, 3 дня на ВНД, увольнение по ст. 52 ТК РК за раскрытие заявителя;
    - `quality_assurance_committee_regulation.md`: внедрен Раздел 7, модуль «Качество и EdTech», роль `QA_Auditor`, аудит силлабусов за 5 дней до семестра, 7 дней на аналитику опросов, абсолютный запрет ручной манипуляции результатами опросов;
    - `accreditation_center_regulation.md`: внедрен Раздел 8, модуль «Аккредитация и Рейтинги», роль `Accreditation_Analyst`, 15 дней на выгрузку SER до визита комиссии, ежемесячная сверка с ЕПВО до 5 числа, ответственность по ст. 52 ТК РК;
    - `strategic_development_department_regulation.md`: внедрен Раздел 8, модуль «Стратегия и OKR», роли `Strategy_Director` и `Strategy_Analyst`, дедлайн до 10 числа месяца на 25 KPI, первые 5 дней квартала на фиксацию OKR, 5 дней на скоринг (0.0–1.0), запрет ручных корректировок утвержденных значений.
  - **Должностные инструкции:**
    - `jd_director_science.md`: закреплены цифровые обязанности в УИС (п. 3.8), роль `Science_SuperAdmin`, санкции по ст. 22, 23, 52 (п. 1 пп. 16), 120 ТК РК (п. 5.4–5.6);
    - `jd_head_commercialization.md`: закреплены цифровые обязанности в УИС (п. 3.8), роль `Commercialization_Manager`, материальная ответственность по ст. 120 ТК РК (п. 5.4–5.6);
    - `jd_compliance_officer.md`: закреплены цифровые обязанности в УИС (п. 3.9, 4.1), роль `Compliance_Auditor`, аудит Audit Trail, увольнение по ст. 52 ТК РК за разглашение заявителя (п. 5.5–5.6);
    - `jd_head_accreditation.md`: закреплены цифровые обязанности в УИС (п. 3.8), роль `Accreditation_Analyst`, ответственность по ст. 52 ТК РК за искажение сведений (п. 5.4–5.6);
    - `jd_researcher_model.md`: закреплены цифровые обязанности исследователя (п. 3.9), роль `Researcher`, обязательное внесение Scopus/WoS публикаций за **5 рабочих дней** с DOI, запрет «хищнических» журналов, расторжение договора по пп. 16) п. 1 ст. 52 ТК РК за срыв сроков и фальсификацию (п. 5.5–5.7);
    - `jd_director_strategic_development.md`: исправлено форматирование, закреплены цифровые обязанности в УИС (п. 3.11), роль `Strategy_Director`, 10 число на сбор 25 KPI, санкции ст. 52 и 120 ТК РК (п. 5.7–5.9).
  - **Универсальность:** Во всех 12 файлах сохранены системные переменные `[V_...]`, локальные хардкоды отсутствуют.

- **3. Judge (Качество и юридическая сила):**
  - Впервые в нормативной практике научно-исследовательский и стратегический контур ОВПО получил прямую правовую связку с трудовым законодательством: научный работник более не может ссылаться на отсутствие регламента при несвоевременном внесении публикаций или попытке сокрытия грантовых результатов;
  - Комплаенс-контроль защищен от манипуляций за счет предоставления роли `Compliance_Auditor` прямого чтения неизменяемых логов Audit Trail.

- **4. Decide (Решение):** `✅ APPROVE`.

---

## 2. Перечень утвержденных модернизированных актов Фазы B

1. [`science_department_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/science_department_regulation.md) — Положение о Департаменте науки;
2. [`commercialization_office_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/commercialization_office_regulation.md) — Положение об Офисе коммерциализации;
3. [`compliance_service_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/compliance_service_regulation.md) — Положение об Антикоррупционной комплаенс-службе;
4. [`quality_assurance_committee_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/quality_assurance_committee_regulation.md) — Положение о Комитете по обеспечению качества;
5. [`accreditation_center_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/accreditation_center_regulation.md) — Положение о Центре аккредитации;
6. [`strategic_development_department_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/strategic_development_department_regulation.md) — Положение о Департаменте стратегического развития;
7. [`jd_director_science.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_director_science.md) — ДИ Директора Департамента науки;
8. [`jd_head_commercialization.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_head_commercialization.md) — ДИ Руководителя Офиса коммерциализации;
9. [`jd_compliance_officer.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_compliance_officer.md) — ДИ Антикоррупционного комплаенс-офицера;
10. [`jd_head_accreditation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_head_accreditation.md) — ДИ Руководителя Центра аккредитации;
11. [`jd_researcher_model.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_researcher_model.md) — Типовая ДИ научного сотрудника (исследователя);
12. [`jd_director_strategic_development.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_director_strategic_development.md) — ДИ Директора Департамента стратегического развития.

---

## 3. Итоговое предписание Координатору

Фаза B задачи `ABAI_20260917-123500_IS_RETROFIT` признана полностью завершенной.
Рекомендуется:
1. Зарегистрировать факт `FACT-026` в `KNOWLEDGE.md` о модернизации контура науки, коммерциализации, качества, комплаенса и стратегии, прошивке 5-дневного регламента внесения публикаций, независимого аудита логов Audit Trail комплаенс-офицером и санкций ст. 52 ТК РК;
2. Обновить Task Board в `README.md`;
3. Подготовить запуск финальной Фазы C (ИТ-блок, инфраструктура, безопасность, СОПы кибербезопасности и ПДн).
