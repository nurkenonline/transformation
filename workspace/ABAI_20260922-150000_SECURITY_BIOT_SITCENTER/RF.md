# RF — ABAI_20260922-150000_SECURITY_BIOT_SITCENTER / Phase A: Реестр НПА (126 актов), антитеррор МНВО № 476 и 4-контурный Ситуационный центр (с диагностикой пожарных тревог)

> **Date**: 2026-09-22  
> **Author**: Executor / Legal & Infrastructure Security Engineer  
> **Status**: 🟢 RF — Complete  
> **Parent HL**: [HL-ABAI_20260922-150000_SECURITY_BIOT_SITCENTER](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260922-150000_SECURITY_BIOT_SITCENTER/HL.md)  
> **TS**: [TS Phase A](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260922-150000_SECURITY_BIOT_SITCENTER/TS.md)  

---

## 1. What Was Done

В рамках Фазы A задачи ABAI-24 сформирован полный комплект нормативно-правового и операционного обеспечения безопасности кампуса и многофункционального ситуационного мониторинга:

### Actual Value-Bearing Accounting

| Fact | Actual result |
|---|---|
| VALUE membership | 5 новых файлов (`STD-RK-012-SECURITY-BIOT-SITCENTER.md`, `security_department_regulation.md`, `situation_center_regulation.md`, `jd_head_security.md`, `jd_situation_center_operator.md`), 1 модифицируемый файл (`external_npa_registry.md`) |
| Arithmetic | 5 новых файлов VALUE + 1 модифицированный файл VALUE = 6 файлов VALUE; ~870 строк добавления/изменения |
| Membership deviations | None (100% совпадение с утвержденной спецификацией TS Phase A) |
| Trigger disposition | В рамках лимитов фазы (5 новых файлов $\le 8$, 6 файлов VALUE $\le 14$, ~870 строк $\le 1200$) |
| Authority and timing | Утверждено в TS Phase A (шлюз 2 согласован) |

### New Files

| File | Description |
|---|---|
| [`docs/regulations/sector_standards/STD-RK-012-SECURITY-BIOT-SITCENTER.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/regulations/sector_standards/STD-RK-012-SECURITY-BIOT-SITCENTER.md) | Отраслевой нормативный стандарт комплексной безопасности, антитеррора УТО науки и ВО (Приказ МНВО № 476, ПП № 305), ГО (Приказ МЧС № 268), ПБ (Приказ МЧС № 55, ТР № 405), БиОТ (ст. 201–204 ТК РК) и 4 контуров диспетчирования |
| [`docs/internal_acts/regulations/security_department_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/security_department_regulation.md) | Положение о Службе безопасности и режима: пропускной и внутриобъектовый режим, Face ID, досмотр автотранспорта/багажа, Паспорт антитеррора УТО по Приказу МНВО № 476, RACI |
| [`docs/internal_acts/regulations/situation_center_regulation.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/regulations/situation_center_regulation.md) | Положение о Ситуационном центре (24/7): 4 взаимоувязанных контура (CCTV/Пожарная диагностика и PTZ-видеоверификация + NOC 24/7 SLA 15 мин + Smart Energy день/ночь + Академическая диспетчеризация расписания занятий ППС по SIS Abai Digital) |
| [`docs/internal_acts/job_descriptions/jd_head_security.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_head_security.md) | ДИ Начальника Службы безопасности: цензы, паспортизация УТО, контроль постов, координация с ДП/ДКНБ/ЧС, персональная ответственность по ст. 149 КоАП РК |
| [`docs/internal_acts/job_descriptions/jd_situation_center_operator.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/internal_acts/job_descriptions/jd_situation_center_operator.md) | ДИ Дежурного оператора-диспетчера СЦ: регламент дежурства, адресная видеоверификация пожарных тревог за 5–10 сек, эскалация ИТ-сбоев (SLA 15 мин), аудит ночного энергопотребления и контроль срывов занятий ППС |

### Modified Files

| File | Changes |
|---|---|
| [`docs/regulations/external_npa_registry.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/docs/regulations/external_npa_registry.md) | Расширение сводного реестра со 117 до **126 НПА** (+9 актов: Законы № 416-I, № 85-II, № 541-IV; Приказ МНВО РК от 04.10.2024 № 476; ПП РК № 305; Приказы МЗСР № 1020, 1019, 1057; Приказ МЧС № 268) |

---

## 2. Key Decisions

1. **Интеграция профильного Приказа МНВО РК № 476:** Вместо устаревших или общих нормативов в основу антитеррористической защиты вуза положен действующий отраслевой акт — Приказ МНВО РК от 04.10.2024 № 476 (МЮ РК № 35218), определяющий 30-суточный архив видеонаблюдения, СКУД, КТС и паспортизацию УТО.
2. **Адресная диагностика и PTZ-видеоверификация пожарных тревог в СЦ:** Решена проблема ложных срабатываний и паники в кампусе. При сигнале адресно-аналогового извещателя камера автоматически наводится на датчик за 5–10 секунд, позволяя оператору дифференцировать реальный пожар (запуск СОУЭ, вызов 101/112) от бытового пара в общежитии или запыленности при ремонте (кратковременная задержка сирены до 60 секунд для проверки нарядом охраны).
3. **Четырехконтурная модель Ситуационного центра:** СЦ трансформирован из классической «вахты видеонаблюдения» в многофункциональный интеллектуальный центр кампуса: Безопасность/Пожарный мониторинг + IT/NOC телеком/серверы + Smart Energy день/ночь + Академическая диспетчеризация учебного расписания занятий ППС.
4. **Контроль дисциплины расписания ППС через СЦ:** Сопряжение сетки занятий из SIS Abai Digital с камерами аудиторий и данными СКУД преподавателей на турникетах позволяет оперативно выявлять срывы занятий и опоздания более 15 минут, а также контролировать эффективность использования аудиторного фонда.

---

## 3. Acceptance Criteria

- [x] **AC-1:** Сводный реестр `external_npa_registry.md` расширен со 117 до 126 НПА (+9 актов со ссылками на ИПС «Әділет»).
- [x] **AC-2:** Разработан Отраслевой стандарт `STD-RK-012-SECURITY-BIOT-SITCENTER.md`.
- [x] **AC-3:** Разработано Положение о Службе безопасности и режима `security_department_regulation.md`.
- [x] **AC-4:** Разработано Положение о Ситуационном центре `situation_center_regulation.md` со всеми 4 технологическими контурами и пожарной телеметрией.
- [x] **AC-5:** Разработаны ДИ Начальника СБ (`jd_head_security.md`) и Дежурного оператора-диспетчера (`jd_situation_center_operator.md`).
- [x] **AC-6:** Отсутствуют плейсхолдеры TODO/TBD, макропеременные `[V_*]` валидны.
- [x] **AC-7:** Протокол доказательств `EV_PHASE_A.md` сформирован со статусом 8/8 VERIFIED.

---

## 4. Evidence Pointer

See [`evidence/EV_PHASE_A.md`](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260922-150000_SECURITY_BIOT_SITCENTER/evidence/EV_PHASE_A.md) for evidence details.  
Verdict summary: **8/8 VERIFIED**, 0 DEFERRED, 0 BLOCKED, 0 N/A.

---

## 5. Fact Candidates (for next agents and KNOWLEDGE.md)

1. **FACT-SEC-01 (Профильный антитеррор МНВО РК):** Базовым отраслевым нормативным актом антитеррористической защиты университетов РК является Приказ Министра науки и высшего образования РК от 04.10.2024 № 476 (МЮ РК № 35218), устанавливающий обязательность паспорта УТО, СКУД Face ID, хранения видеозаписей не менее 30 суток и кнопок тревожной сигнализации.
2. **FACT-SEC-02 (4-контурный Ситуационный центр ОВПО):** Ситуационный центр современного университета РК объединяет 4 контура: 1) Физическая охрана и пожарная телеметрия с PTZ-видеоверификацией тревог за 5–10 сек; 2) IT/NOC мониторинг сети и серверов (Moodle/SIS) с SLA 15 мин; 3) Smart Energy контроль суточных нагрузок день/ночь; 4) Академическая диспетчеризация проведения занятий ППС по расписанию SIS Abai Digital.
3. **FACT-SEC-03 (Внешний регуляторный реестр 126 НПА):** Контрольный контур нормативных правовых актов университета расширен со 117 до 126 актов прямого действия.

---

## 6. Observations (out-of-scope, not modified)

No observations.

---

## 🛑 Executor STOP

RF is complete. Start `/tfw-review` to review the results.
