# Домен 08: Цифровизация, ИТ и безопасность данных (Digital Transformation & IT)

## 1. Архитектурная модель и организационный контур домена

Цифровая экосистема Университета спроектирована по модульному принципу в соответствии с СТ РК 34.015-2002 и Едиными требованиями в области ИКТ и ИБ (ПП РК № 832). Она базируется на четком разграничении зон ответственности:
1. **Управление цифровизации (Software Engineering & Architecture):** Архитектурное проектирование, разработка и кастомизация 22 прикладных модулей УИС («[V_SIS_SYSTEM_NAME]» / Abai Digital), интеграционные шлюзы с государственными системами (Buffer-Mirror Sync с ЕПВО/НОБД по 5 протоколам МНВО РК, Smart Bridge).
2. **Управление информационных технологий (IT Infrastructure & Operations):** Эксплуатация серверного парка, виртуализации, систем хранения данных (СХД), резервного копирования (RPO $\le 1$ ч, RTO $\le 4$ ч), кампусных локальных и Wi-Fi сетей, телефонии и парка оргтехники.
3. **Служба информационной безопасности (Infosec):** Независимый контроль соблюдения политики ИБ (ISO 27001, 4-уровневая структура), предотвращение утечек данных, реагирование на инциденты (нотификация регулятора в течение 24 часов по Приказу МЦРИАП № 395/НҚ) и аудит системных логов Audit Trail.
4. **Служба Service Desk (ITIL v4):** 3-уровневая техническая поддержка пользователей: L1 — окна в ЦОС и тикет-система (целевой FCR $\ge 70\%$), L2 — системные администраторы УИТ, L3 — разработчики Управления цифровизации.

---

## 2. Реестр функций домена

| Код функции | Наименование функции | Основание в НПА РК | Ответственный (Accountable) | Соисполнители (Responsible) | Реализующий ВНД |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `FUNC-IT-ARCH-001`  | Архитектурное проектирование, разработка и внедрение модулей УИС | Закон РК «Об информатизации», СТ РК 34.015-2002 | Начальник Управления цифровизации | Отдел веб-разработки, Инженеры баз данных | [`digitalization_department_regulation.md`](../internal_acts/regulations/digitalization_department_regulation.md), [`jd_head_digitalization.md`](../internal_acts/job_descriptions/jd_head_digitalization.md) |
| `FUNC-IT-SYNC-002`  | Ежедневная синхронизация с государственными шлюзами ЕПВО и НОБД (Buffer-Mirror) | Приказы МНВО РК по интеграции данных, Квалтребования № 391 | Начальник Управления цифровизации | Офис регистратора, HR, Бухгалтерия | [`sop_epvo_nobd_integration.md`](../internal_acts/sops_and_rules/sop_epvo_nobd_integration.md) |
| `FUNC-IT-INFRA-003` | Администрирование серверов, СХД, кампусных сетей и обеспечение Uptime $\ge 99.8\%$ | ПП РК № 832 (ЕТИКТ), Квалтребования № 391 | Начальник Управления IT (УИТ) | Системные и сетевые администраторы УИТ | [`it_infrastructure_department_regulation.md`](../internal_acts/regulations/it_infrastructure_department_regulation.md), [`jd_head_it_infrastructure.md`](../internal_acts/job_descriptions/jd_head_it_infrastructure.md) |
| `FUNC-IT-DESK-004`   | Предоставление услуг технической поддержки Service Desk по методологии ITIL v4 | СТ РК ISO/IEC 20000-1-2019, ITIL v4 | Начальник УИТ / Руководитель ЦОС | Инженеры Service Desk L1/L2 | [`sop_itil_itsm_service_desk.md`](../internal_acts/sops_and_rules/sop_itil_itsm_service_desk.md), [`service_catalog_and_sla_matrix.md`](../internal_acts/sops_and_rules/service_catalog_and_sla_matrix.md) |
| `FUNC-IT-SEC-005`    | Защита персональных данных, 24-часовая нотификация регулятора об инцидентах | Закон «О персональных данных», Приказ МЦРИАП № 395/НҚ | Офицер информационной безопасности | Управление цифровизации, УИТ, Служба безопасности | [`sop_personal_data_protection.md`](../internal_acts/sops_and_rules/sop_personal_data_protection.md), [`is_4level_security_registry.md`](../internal_acts/regulations/is_4level_security_registry.md) |
| `FUNC-IT-AWARE-006`  | Обучение и проверка знаний работников по кибербезопасности и гигиене данных | ПП РК № 832, Трудовой кодекс РК (ст. 182) | Начальник УИТ / Офицер ИБ | Департамент HR, Руководители подразделений | [`sop_employee_cybersecurity_and_labor_safety.md`](../internal_acts/sops_and_rules/sop_employee_cybersecurity_and_labor_safety.md) |

---

## 3. Реестр локальных нормативных актов домена

1. **Положения о подразделениях:**
   - [`REG-IT-DIGI-001` Положение об Управлении цифровизации](../internal_acts/regulations/digitalization_department_regulation.md)
   - [`REG-IT-INFRA-001` Положение об Управлении информационных технологий (УИТ)](../internal_acts/regulations/it_infrastructure_department_regulation.md)
   - [`REG-IT-SEC-001` Сводный реестр 4-уровневой документации информационной безопасности (ISO 27001)](../internal_acts/regulations/is_4level_security_registry.md)

2. **Должностные инструкции:**
   - [`JD-IT-DIGI-HEAD-001` ДИ Начальника Управления цифровизации](../internal_acts/job_descriptions/jd_head_digitalization.md)
   - [`JD-IT-INFRA-HEAD-001` ДИ Начальника Управления информационных технологий](../internal_acts/job_descriptions/jd_head_it_infrastructure.md)
   - [`JD-IT-DESK-L1-001` ДИ Специалиста Service Desk 1-й линии (L1 Support)](../internal_acts/job_descriptions/jd_service_desk_l1_specialist.md)

3. **Стандарты операционных процедур (СОП) и правила:**
   - [`SOP-IT-DESK-001` Регламент (СОП) функционирования службы Service Desk по методологии ITIL/ITSM](../internal_acts/sops_and_rules/sop_itil_itsm_service_desk.md)
   - [`SOP-IT-SLA-001` Каталог IT-услуг и Соглашение об уровне обслуживания (Service Catalog & SLA)](../internal_acts/sops_and_rules/service_catalog_and_sla_matrix.md)
   - [`SOP-IT-EPVO-001` Регламент интеграционного взаимодействия с ЕПВО и НОБД](../internal_acts/sops_and_rules/sop_epvo_nobd_integration.md)
   - [`SOP-IT-DATA-001` Регламент защиты персональных данных обучающихся и работников](../internal_acts/sops_and_rules/sop_personal_data_protection.md)
   - [`SOP-IT-CYBER-001` Регламент обязательного обучения и соблюдения требований ИБ работниками](../internal_acts/sops_and_rules/sop_employee_cybersecurity_and_labor_safety.md)

4. **Архитектурные паспорта:**
   - [`BP-IT-SIS-001` Архитектурный паспорт: Интегрированная система «[V_SIS_SYSTEM_NAME]» (22 модуля для ГТС)](../internal_acts/blueprints/abai_digital_platform_architecture.md)

---

## 4. Цифровой контур и функциональные модули УИС

1. **Ядро УИС:** 22 модуля по СТ РК 34.015-2002 (Абитуриент, КЭД, Расписание, Сессия, Журнал, Общежития, Наука, Кадры, Приказы, ДФО).
2. **Интеграционный шлюз ЕПВО (v3.0.1):** 5 протоколов обмена (Студенты, Приказы, Дипломы, Стипендии, СУР КОКСНВО).
3. **Identity Management (Microsoft Entra ID / Azure AD):** единая учетная запись SSO, строгий протокол очной верификации личности при сбросе паролей.
4. **Контур информационной безопасности:** централизованный SIEM, хранение аудиторских логов Audit Trail $\ge 3$ лет.
