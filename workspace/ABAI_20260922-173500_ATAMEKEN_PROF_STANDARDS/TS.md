# TS — ABAI_20260922-173500_ATAMEKEN_PROF_STANDARDS / Phase A: Отраслевой стандарт НПП «Атамекен», аналитический реестр НСК и Мастер-матрица сопоставления должностей (Gap Analysis)

> **Date**: 2026-09-22  
> **Author**: Coordinator / Institutional & HR Architecture Lead  
> **Status**: 🔒 FROZEN — approved by owner 2026-09-22  
> **Parent HL**: [HL-ABAI_20260922-173500_ATAMEKEN_PROF_STANDARDS](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260922-173500_ATAMEKEN_PROF_STANDARDS/HL.md)  
> **Baseline Commit**: Current HEAD  

---

## 1. Objective

Сформировать фундаментальный нормативно-методологический базис внедрения Национальной системы квалификаций (НСК) и профессиональных стандартов НПП «Атамекен» в деятельность Университета:
1. Разработать Отраслевой стандарт ОВПО РК `STD-RK-013-PROF-STANDARDS-ATAMEKEN.md`, регламентирующий переход вуза на дескрипторы Национальной рамки квалификаций (НРК 5–8 уровни), требования отраслевых рамок (ОРК) и профессиональные стандарты работодателей по Закону РК от 04.07.2023 № 14-VIII «О профессиональных квалификациях» и ст. 116–118 Трудового кодекса РК;
2. Сформировать аналитический модуль-реестр профессиональных стандартов `docs/regulations/11_professional_standards_and_qualifications_registry.md`, охватывающий 15+ стандартов НПП «Атамекен» и отраслевых министерств по 4 кластерам (Образование и наука, ИКТ, Финансы и закупки, Менеджмент и право);
3. Провести комплексный аудит и составить Мастер-матрицу Gap Analysis (`atameken_job_descriptions_gap_analysis_matrix.md`) для всех 34+ утвержденных в Университете должностей с выявлением нормативных разрывов между действующими ДИ и требованиями профстандартов «Атамекен» (Hard/Soft/Digital skills, уровни автономности по НРК, вендорные сертификаты);
4. Актуализировать сводный реестр внешних нормативных правовых актов `docs/regulations/external_npa_registry.md` с включением фундаментального блока НСК.

---

## 2. Scope

### In Scope (3 новых файла VALUE + 1 модифицируемый VALUE + 1 TRACE)
1. `docs/regulations/sector_standards/STD-RK-013-PROF-STANDARDS-ATAMEKEN.md` (CREATE, `VALUE`) — Отраслевой стандарт ОВПО РК по интеграции профессиональных стандартов НПП «Атамекен» и НСК;
2. `docs/regulations/11_professional_standards_and_qualifications_registry.md` (CREATE, `VALUE`) — Аналитический реестр 15+ профессиональных стандартов НПП «Атамекен» и отраслевых министерств с маппингом на ОРК и НРК;
3. `docs/internal_acts/blueprints/atameken_job_descriptions_gap_analysis_matrix.md` (CREATE, `VALUE`) — Мастер-матрица сопоставления (Gap Analysis) 34+ должностей университета со стандартами «Атамекен»;
4. `docs/regulations/external_npa_registry.md` (MODIFY, `VALUE`) — Интеграция законодательного блока Национальной системы квалификаций (Закон № 14-VIII, НРК);
5. `workspace/ABAI_20260922-173500_ATAMEKEN_PROF_STANDARDS/evidence/EV_PHASE_A.md` (CREATE, `TRACE`) — Протокол доказательств Фазы A.

### Out of Scope
- Разработка операционного СОПа HR по применению профстандартов (`sop_professional_standards_and_qualifications.md`), модельных паспортов должностей (Competency Cards) и актуализация Домена 03 (HR) — относятся к Фазе B.

---

## 3. Principles Check

| # | HL §7 Принцип | Механизм реализации в Фазе A |
|---|---|---|
| **P1** | **Примат Закона № 14-VIII и ст. 116–118 ТК РК** | Отраслевой стандарт `STD-RK-013` устанавливает обязательность применения профстандартов при формировании требований к должностям ОВПО. |
| **P2** | **Дескрипторная точность НРК** | В Матрице Gap Analysis каждая должность классифицируется по 8-уровневой шкале НРК (5 — прикладной бакалавриат, 6 — бакалавриат, 7 — магистратура, 8 — докторантура). |
| **P3** | **Индустриальные требования и сертификаты** | В реестре стандартов и матрице фиксируются требования к вендорным сертификациям (Cisco, Microsoft, AWS, 1С, ACCA, CAP/CIPA, PMI, ITIL). |
| **P4** | **Признание Microcredentials** | Нормативная фиксация зачета микроквалификаций по ст. 13–15 Закона № 14-VIII в стандарте `STD-RK-013`. |
| **P5** | **Нулевой плейсхолдер** | 0 маркеров `TODO`, `TBD`, сохранение общесистемных макропеременных `[V_*]`. |

---

## 4. Affected Files and Value-Bearing Accounting

| File / selector | Action | Class | Semantic reason / required result |
|---|---|---|---|
| `docs/regulations/sector_standards/STD-RK-013-PROF-STANDARDS-ATAMEKEN.md` | CREATE | `VALUE` | Отраслевой стандарт ОВПО РК: нормативная преамбула, архитектура НСК, связь ОРК/НРК/профстандартов, правила профилирования должностей, целевые KPI |
| `docs/regulations/11_professional_standards_and_qualifications_registry.md` | CREATE | `VALUE` | Аналитический модуль-реестр: 15+ профстандартов НПП «Атамекен» и министерств с кодами, уровнями НРК, дескрипторами и Adilet ссылками |
| `docs/internal_acts/blueprints/atameken_job_descriptions_gap_analysis_matrix.md` | CREATE | `VALUE` | Мастер-матрица сопоставления: аудит 34+ должностей университета, выявление несоответствий (гэпов), требования к Hard/Soft/Digital skills |
| `docs/regulations/external_npa_registry.md` | MODIFY | `VALUE` | Дополнение сводного реестра внешних актов блоком Национальной системы квалификаций |
| `workspace/ABAI_20260922-173500_ATAMEKEN_PROF_STANDARDS/evidence/EV_PHASE_A.md` | CREATE | `TRACE` | Протокол объективных доказательств верификации критериев AC-1 — AC-6 |

### Prospective accounting contract

| Fact | Approved value |
|---|---|
| Logical VALUE files | 3 новых файла VALUE + 1 модифицированный VALUE = 4 файла VALUE |
| Text LOC estimate | $\approx 850$ строк добавления/изменения (лимит $\le 1200$ строк) |
| Multiplier / authority | Норматив TFW v3.4.0: новые $\le 8$, суммарно $\le 14$, LOC $\le 1200$ |

---

## 5. Acceptance Criteria (DoD)

- [ ] **AC-1:** Разработан Отраслевой стандарт ОВПО РК `STD-RK-013-PROF-STANDARDS-ATAMEKEN.md`, содержащий нормативно-правовую преамбулу (Закон РК № 14-VIII, ст. 116–118 ТК РК), дескрипторы уровней НРК (5–8), правила сопряжения должностей с Отраслевыми рамками квалификаций (ОРК) и типовые требования к профилям компетенций.
- [ ] **AC-2:** Сформирован аналитический модуль-реестр `11_professional_standards_and_qualifications_registry.md`, систематизирующий 15+ профессиональных стандартов НПП «Атамекен» и отраслевых министерств по 4 кластерам (педагогический, научно-исследовательский, ИКТ, финансово-управленческий) с официальными реквизитами и уровнями НРК.
- [ ] **AC-3:** Составлена детальная Мастер-матрица Gap Analysis (`atameken_job_descriptions_gap_analysis_matrix.md`) для всех 34+ утвержденных должностей Университета с фиксацией нормативных разрывов между действующими ДИ и профессиональными стандартами «Атамекен» (уровень НРК, дефицит цифровых навыков, требования к сертификации).
- [ ] **AC-4:** Актуализирован реестр внешних нормативных правовых актов `docs/regulations/external_npa_registry.md` (включение законодательного блока Национальной системы квалификаций).
- [ ] **AC-5:** 0 маркеров `TODO`, `TBD`, корректное применение переменных `[V_*]`.
- [ ] **AC-6:** Сформирован протокол доказательств `EV_PHASE_A.md` со 100% подтверждением выполнения критериев.

---

## 6. Budget Enforcement

- Files to create: 3 VALUE + 1 TRACE = 4 files (Limit: $\le 8$ new files).
- Files to modify: 1 VALUE = 1 file (Limit total touched: 5 files $\le 14$).
- Lines budget: $\approx 850$ строк (Limit: $\le 1200$ LOC).
