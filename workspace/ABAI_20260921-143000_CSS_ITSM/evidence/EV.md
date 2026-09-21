# EV — Доказательный слой (Evidence Layer) по задаче ABAI-18: Трансформация ЦОС в Единый сервисный центр с ITIL/ITSM Service Desk

> **Идентификатор задачи:** `ABAI-18` (`ABAI_20260921-143000_CSS_ITSM`)  
> **Методология:** Trace-First Workflow (TFW v3.4.0)  
> **Статус аудита:** `100% VERIFIED` (5/5 подтверждено)  
> **Дата аудита:** 21 сентября 2026 г.  

---

## 1. МАТРИЦА ВЕРИФИКАЦИИ ТРЕБОВАНИЙ (CRITERIA AUDIT)

| Код критерия | Формулировка требования | Статус | Подтверждающий артефакт | Объективное доказательство (Evidence Quote / Metric) |
|:---:|---|:---:|---|---|
| `CRIT-CSS-01` | Разработка Положения о Центре обслуживания студентов и сотрудников (ЦОСиС) с 4 секторами и принципом One-Stop Shop | `VERIFIED` | [`student_and_staff_service_center_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/student_and_staff_service_center_regulation.md) | Закреплены 4 сектора: академический, ППС и АУП, International Student Desk, IT Service Desk L1; целевые метрики: CSAT $\ge 90\%$, FCR $\ge 70\%$, AWT $\le 7$ мин. |
| `CRIT-CSS-02` | Разработка СОП функционирования службы Service Desk по ITIL v4 / ITSM с 3 линиями поддержки (L1–L2–L3) | `VERIFIED` | [`sop_itil_itsm_service_desk.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/sop_itil_itsm_service_desk.md) | Регламентированы Incident & Service Request Management, приоритеты P1–P4, правила эскалации L1 (ЦОС) $\rightarrow$ L2 (УИТ) $\rightarrow$ L3 (Цифровизация / Вендоры). |
| `CRIT-CSS-03` | Безопасный Identity Management для Microsoft Entra ID (Azure AD), MFA и УИС с очной верификацией личности | `VERIFIED` | [`sop_itil_itsm_service_desk.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/sop_itil_itsm_service_desk.md) (Раздел 5) | Прямой запрет сброса паролей по телефону/мессенджерам; обязательное предъявление оригинала документа / eGov Mobile, принудительная смена при первом входе, нотификация ИБ $\le 15$ мин. |
| `CRIT-CSS-04` | Формирование официального Каталога IT-услуг и матрицы SLA (Service Catalog & SLA Matrix) по 7 доменам | `VERIFIED` | [`service_catalog_and_sla_matrix.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/sops_and_rules/service_catalog_and_sla_matrix.md) | Регламентированы 28 услуг в 7 доменах с жесткими таймингами реакции и решения, правила остановки таймера (Pending User/Hardware), цветовой мониторинг. |
| `CRIT-CSS-05` | Разработка комплекта ДИ Руководителя ЦОСиС и Специалиста Service Desk L1 с персональной ответственностью | `VERIFIED` | [`jd_head_student_and_staff_service_center.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_head_student_and_staff_service_center.md), [`jd_service_desk_l1_specialist.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_service_desk_l1_specialist.md) | Описаны функциональные обязанности, квалификационные требования (ITIL/ITSM, Entra ID, Microsoft 365), материальная ответственность по ст. 120, 123 ТК РК. |

---

## 2. АУДИТ ЧИСТОВЫХ PDF-ЭКСПОРТОВ

1. `Student_and_Staff_Service_Center_Regulation.pdf` — **181 215 байт** (`OK`).
2. `Service_Desk_ITIL_ITSM_SOP.pdf` — **200 698 байт** (`OK`).
3. `Service_Catalog_and_SLA_Matrix.pdf` — **321 315 байт** (`OK`).
*Итоговый вердикт доказательного слоя:* **ПОЛНОСТЬЮ СООТВЕТСТВУЕТ (5/5 VERIFIED)**.
