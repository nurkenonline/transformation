# Map — Review Stage 1 (Phase B)
## Task: ABAI_20260922-173500_ATAMEKEN_PROF_STANDARDS / Phase B
## Date: 2026-09-23 | Reviewer: Independent Reviewer / Quality Guardian

---

## 1. Input Verification Map

| Claim / Deliverable | Source in TS Phase B | Target File | Verification Method |
|---|---|---|---|
| **AC-1:** Регламент (СОП) применения профессиональных стандартов НПП «Атамекен» (`SOP-HR-PROF-STANDARDS-001`) | TS §5 AC-1, §4 | `docs/internal_acts/sops_and_rules/sop_professional_standards_and_qualifications.md` | Структурный аудит 7 разделов, проверка норм Закона № 14-VIII, ТК РК ст. 116–118, Приказа МТСЗН № 374, регламента Microcredentials и Квалификационной комиссии |
| **AC-2:** Альбом модельных паспортов компетенций должностей (Job Competency Cards) | TS §5 AC-2, §4 | `docs/internal_acts/blueprints/job_competency_card_template_and_samples.md` | Проверка формы JCC, 4-уровневой шкалы владения и 4 эталонов (Профессор 8 ур., Архитектор ИКТ 7 ур., Главбух 7 ур., HRD 7–8 ур.) с матрицами навыков |
| **AC-3:** Модернизация Регламента открытого конкурса ППС и ученых | TS §5 AC-3, §4 | `docs/internal_acts/sops_and_rules/sop_faculty_and_researcher_recruitment_competition.md` | Анализ сопряжения с дескрипторами НРК 7–8, документами НСК и 100-балльной дифференцированной оценочной шкалой |
| **AC-4:** Закрепление институциональной функции `FUNC-HR-PROF-STANDARDS-012` | TS §5 AC-4, §4 | `docs/functions_and_powers/10_human_capital_and_hr.md` | Проверка фиксации функции, роли `Accountable: Директор HR`, обновления реестра ВНД и Цифрового контура |
| **AC-5:** Чистота кода и отсутствие плейсхолдеров | TS §5 AC-5 | Все созданные и измененные файлы | Regex-поиск `\b(TODO|TBD|FIXME)\b`, проверка макропеременных `[V_*]` |
| **AC-6:** Протокол объективных доказательств | TS §5 AC-6 | `workspace/.../evidence/EV_PHASE_B.md` | Анализ протокола доказательств, проверка 100% покрытия критериев AC-1 — AC-5 |

---

## 2. Scope & Budget Map

- **Плановый бюджет TS:** 2 новых файла VALUE, 2 модифицированных VALUE, объем ~750 LOC.
- **Фактическое исполнение RF:**
  - Новых файлов VALUE: 2 (`sop_professional_standards_and_qualifications.md`, `job_competency_card_template_and_samples.md`);
  - Модифицированных файлов VALUE: 2 (`sop_faculty_and_researcher_recruitment_competition.md`, `10_human_capital_and_hr.md`);
  - Созданных файлов TRACE: 3 (`ONB_PHASE_B.md`, `EV_PHASE_B.md`, `RF_PHASE_B.md`);
  - Фактический объем изменений: ~413 LOC (в пределах лимита $\le 1200$ LOC).

---

## 3. Self-Check Gate (Map)

- [x] Все входные требования TS Phase B картированы на целевые файлы.
- [x] Объем заявленных изменений в RF сопоставлен с кодовой базой.
- [x] Ролевой шлюз соблюден: Reviewer приступает к независимой верификации без права изменения кода.
