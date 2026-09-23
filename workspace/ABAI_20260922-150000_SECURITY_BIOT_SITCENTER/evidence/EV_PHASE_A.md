# EV — ABAI_20260922-150000_SECURITY_BIOT_SITCENTER / Phase A: Реестр НПА (126 актов), антитеррор МНВО № 476 и 4-контурный Ситуационный центр (с диагностикой пожарных тревог)

> **Date**: 2026-09-22  
> **Author**: Executor / Legal & Infrastructure Security Engineer  
> **Task**: ABAI_20260922-150000_SECURITY_BIOT_SITCENTER  
> **TS**: [TS Phase A](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260922-150000_SECURITY_BIOT_SITCENTER/TS.md)  

---

## Environment

| Field | Value |
|---|---|
| OS | Windows 11 Pro / PowerShell 5.1 |
| Language / Runtime | Python 3.13.14 |
| Repository | Git 2.50.0 |
| Framework | Trace-First Workflow (TFW v3.4.0) |

---

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|:---:|---|
| **E1** | AC-1 | Сводный реестр внешних НПА `external_npa_registry.md` расширен со 117 до **126 НПА** (+9 актов: Закон «О противодействии терроризму» № 416-I, Закон «Об охранной деятельности» № 85-II, Закон «Об энергосбережении» № 541-IV, Приказ МНВО РК № 476 по защите УТО науки и ВО, ПП РК № 305, Приказы МЗСР № 1020, 1019, 1057 по БиОТ, Приказ МЧС № 268 по ГО) со ссылками на ИПС «Әділет» | Local Git Repo | `VERIFIED` | [`external_npa_registry.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/regulations/external_npa_registry.md) |
| **E2** | AC-2 | Разработан Отраслевой нормативный стандарт `STD-RK-012-SECURITY-BIOT-SITCENTER.md`, консолидирующий требования антитеррора УТО науки и ВО (Приказ МНВО № 476, ПП № 305), ГО (№ 268), ПБ (№ 55, ТР № 405), БиОТ (ТК РК, № 1020) и 4-контурного ситуационного диспетчирования | Local Git Repo | `VERIFIED` | [`STD-RK-012-SECURITY-BIOT-SITCENTER.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/regulations/sector_standards/STD-RK-012-SECURITY-BIOT-SITCENTER.md) |
| **E3** | AC-3 | Разработано Положение о Службе безопасности и режима `security_department_regulation.md`: пропускной и внутриобъектовый режим, СКУД Face ID, досмотр автотранспорта и ручной клади, Паспорт антитеррора УТО по Приказу МНВО № 476, RACI-матрица взаимодействия | Local Git Repo | `VERIFIED` | [`security_department_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/security_department_regulation.md) |
| **E4** | AC-4 | Разработано Положение о Ситуационном центре `situation_center_regulation.md` с **четырьмя контурами**: Контур 1 (CCTV, видеоаналитика, адресно-аналоговая телеметрия АПС/СОУЭ и PTZ-видеоверификация первопричин за 5–10 сек); Контур 2 (NOC 24/7 ЛВС, серверов Moodle/SIS, ЦОД, SLA $\le 15$ мин); Контур 3 (Smart Energy день/ночь, предотвращение рисков пожаров от нагревателей); Контур 4 (Академическая диспетчеризация расписания занятий ППС по SIS Abai Digital, фиксация срывов/опозданий, загрузка аудиторий) | Local Git Repo | `VERIFIED` | [`situation_center_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/situation_center_regulation.md) |
| **E5** | AC-5 | Разработана ДИ Начальника Службы безопасности `jd_head_security.md` (цензы, разработка паспорта УТО, координация с полицией/КНБ/ЧС, ответственность по ст. 149 КоАП РК) и ДИ Дежурного оператора-диспетчера `jd_situation_center_operator.md` (полномочия по всем 4 контурам, порядок видеоверификации пожарной тревоги, SLA 15 мин) | Local Git Repo | `VERIFIED` | [`jd_head_security.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_head_security.md), [`jd_situation_center_operator.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_situation_center_operator.md) |
| **E6** | AC-6 | Проверка ripgrep: 0 маркеров TODO/TBD/FIXME, макропеременные `[V_*]` валидны, структура документов соответствует стандартам фреймворка | Local Ripgrep | `VERIFIED` | 5 новых файлов VALUE + 1 модифицированный VALUE |
| **E7** | AC-7 | Создан настоящий протокол `EV_PHASE_A.md` с фиксацией 100% выполнения критериев спецификации | Local Git Repo | `VERIFIED` | `EV_PHASE_A.md` |
| **E-accounting** | Accounting | 5 новых файлов VALUE + 1 модифицированный файл VALUE = 6 файлов VALUE; объем изменений ~860 строк, укладывается в норматив ($\le 8$ новых файлов, $\le 1200$ строк) | Git working tree | `VERIFIED` | `git status -s` |

---

## Verdict

Evidence verdict: **8/8 VERIFIED**, 0 DEFERRED, 0 BLOCKED, 0 N/A.
