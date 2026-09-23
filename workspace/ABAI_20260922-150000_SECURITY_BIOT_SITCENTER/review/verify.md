# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42  
> RF files claimed: 6  
> Files to verify: 6 (100% full verification applied)

## Verification Log

### V1: `docs/internal_acts/regulations/occupational_safety_regulation.md`
- **RF claim:** Положение о Службе охраны труда (`REG-BIOT-001`): статус обособленной службы с прямым подчинением первому руководителю (ст. 202 ТК РК), аттестация рабочих мест 1 раз в 5 лет (Приказ МЗСР № 1057), специальное расследование несчастных случаев со сроком хранения актов Н-1 45 лет (ст. 187–190 ТК РК).
- **Actual:** Файл существует (20 455 байт), содержит 8 разделов, четкую преамбулу, ссылки на ст. 181–183, 187–190, 201–204 ТК РК, Приказы МЗСР № 1020, 1019, 1057, 1054, прямое подчинение Ректору в п. 1.3, функции специального расследования и аттестации.
- **Match:** ✅ Match.

### V2: `docs/internal_acts/job_descriptions/jd_head_occupational_safety.md`
- **RF claim:** ДИ Руководителя Службы охраны труда (`JD-BIOT-HEAD-001`): квалификационные цензы, сертификация, исключительное право выдачи обязательных предписаний и приостановки работ при угрозе жизни, персональная ответственность по ст. 93, 96 КоАП РК и ст. 156 УК РК.
- **Actual:** Файл существует, регламентирует квалификацию, полномочия по ст. 202 ТК РК, право беспрепятственного доступа и приостановки опасных работ, персональную ответственность по ст. 93 КоАП и ст. 156 УК РК.
- **Match:** ✅ Match.

### V3: `docs/internal_acts/regulations/civil_defense_and_emergency_regulation.md`
- **RF claim:** Положение об Отделе ГО и ЧС (`REG-GO-001`): рабочий орган Начальника ГО объекта (Ректора, ст. 18 Закона РК № 188-V), ведение ГО по Приказу МЧС РК № 268, План ГО, содержание укрытий (ПРУ), формирование невоенизированных формирований ГО, надзор за пожарной безопасностью по Приказу МЧС № 55.
- **Actual:** Файл существует (18 433 байта), содержит 8 разделов, ссылки на Закон РК № 188-V, Приказы МЧС № 268 и 55, статус рабочего органа Ректора, подготовку формирований ГО, укрытия ПРУ, пожарную профилактику.
- **Match:** ✅ Match.

### V4: `docs/internal_acts/job_descriptions/jd_head_civil_defense_and_emergency.md`
- **RF claim:** ДИ Начальника Отдела ГО и ЧС (`JD-GO-HEAD-001`): функции начальника штаба ГО объекта, взаимодействие с ДЧС, допуск к госсекретам (форма 3), ответственность по ст. 359, 410 КоАП РК.
- **Actual:** Файл существует, регламентирует роль начальника штаба ГО, разработку оперативных планов, проверку укрытий, персональную ответственность по ст. 359 (нарушение правил ГО) и ст. 410 (нарушение правил пожарной безопасности) КоАП РК.
- **Match:** ✅ Match.

### V5: `docs/internal_acts/sops_and_rules/sop_emergency_and_evacuation_drills.md`
- **RF claim:** СОП эвакуационных тренировок (`SOP-EMERG-EVAC-001`): распределение зон ответственности между Отделом ГО и ЧС, Службой БиОТ, Службой безопасности и Ситуационным центром.
- **Actual:** Файл содержит обновленный состав владельцев процесса в п. 1.2, п. 5.1–5.4, Приложениях 1 и 3 с подписями всех 4 раздельных структур.
- **Match:** ✅ Match.

### V6: `docs/functions_and_powers/09_infrastructure_and_facilities.md`
- **RF claim:** Каталог функций Домена 09: институциональное закрепление 4 отдельных структур в архитектурной модели (п. 1), реестре функций (п. 2) и реестре ВНД (п. 3).
- **Actual:** Полностью отражены 4 структуры: СБ, Ситуационный центр, Служба охраны труда (БиОТ), Отдел ГО и ЧС. В RACI-матрице соблюдено правило единственного Accountable.
- **Match:** ✅ Match.

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `git status --short` | 4 новых файла VALUE, 2 модифицированных VALUE, артефакты EV/RF |
| 2 | ripgrep TODO/TBD search | 0 совпадений (чистый код) |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | Подчинение службы БиОТ первому руководителю | `occupational_safety_regulation.md` п. 1.3 | Ст. 202 ТК РК | ✅ |
| C2 | Обязательность аттестации рабочих мест 1 раз в 5 лет | `occupational_safety_regulation.md` п. 4.2 | Ст. 183 ТК РК, Приказ МЗСР № 1057 | ✅ |
| C3 | Статус начальника ГО объекта — Ректор | `civil_defense_and_emergency_regulation.md` п. 1.2 | Ст. 18 Закона РК № 188-V | ✅ |
| C4 | Сроки эвакуационных тренировок $\ge 2$ раз в год | `sop_emergency_and_evacuation_drills.md` п. 2.1 | Приказ МЧС РК № 55 п. 18 | ✅ |

## Discrepancies Found

No discrepancies.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|:---:|---|
| E1 | `evidence/EV_PHASE_B.md` AC-1 | ✅ | ✅ `occupational_safety_regulation.md` создан |
| E2 | `evidence/EV_PHASE_B.md` AC-2 | ✅ | ✅ `jd_head_occupational_safety.md` создан |
| E3 | `evidence/EV_PHASE_B.md` AC-3 | ✅ | ✅ `civil_defense_and_emergency_regulation.md` создан |
| E4 | `evidence/EV_PHASE_B.md` AC-4 | ✅ | ✅ `jd_head_civil_defense_and_emergency.md` создан |
| E5 | `evidence/EV_PHASE_B.md` AC-5 | ✅ | ✅ `sop_emergency_and_evacuation_drills.md` и Домен 09 обновлены |
| E6 | `evidence/EV_PHASE_B.md` AC-6 | ✅ | ✅ 0 TODO/TBD, макросы соблюдены |
| E7 | `evidence/EV_PHASE_B.md` Accounting | ✅ | ✅ 6 VALUE файлов, ~720 LOC $\le 1200$ LOC |

Stage complete: YES
