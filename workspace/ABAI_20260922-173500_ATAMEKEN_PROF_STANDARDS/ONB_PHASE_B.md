# ONB — ABAI_20260922-173500_ATAMEKEN_PROF_STANDARDS / Phase B: Операционный регламент (СОП) применения профстандартов «Атамекен», Альбом паспортов должностей (Competency Cards), модернизация конкурсного отбора и актуализация функций HR

> **Date**: 2026-09-23  
> **Author**: Executor / HR Systems & Qualifications Implementation Specialist  
> **Status**: 🟢 ONB — Ready for implementation  
> **Parent HL**: [HL-ABAI_20260922-173500_ATAMEKEN_PROF_STANDARDS](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260922-173500_ATAMEKEN_PROF_STANDARDS/HL.md)  
> **Governing TS**: [TS Phase B](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260922-173500_ATAMEKEN_PROF_STANDARDS/TS_PHASE_B.md)  

---

## 1. Understanding

В рамках Фазы B задачи ABAI-25 требуется перевести нормативную базу и аналитический базис Фазы A (Отраслевой стандарт `STD-RK-013`, Реестр Модуль 11 и Мастер-матрицу Gap Analysis) в практический операционный кадровый инструментарий Университета:
1. **Разработать Регламент (СОП) `SOP-HR-PROF-STANDARDS-001`** (`docs/internal_acts/sops_and_rules/sop_professional_standards_and_qualifications.md`): исчерпывающая стандартная операционная процедура применения профессиональных стандартов НПП «Атамекен» при профилировании должностей, актуализации ДИ, интеграции требований НСК в конкурсы и валидации/зачете микроквалификаций (Microcredentials), сертификатов вендоров и неформального образования в соответствии со ст. 13–15 Закона РК № 14-VIII и Приказом МТСЗН РК от 06.09.2023 № 374;
2. **Разработать Альбом модельных паспортов компетенций должностей (Job Competency Cards)** (`docs/internal_acts/blueprints/job_competency_card_template_and_samples.md`): методология и типовая структура Карты компетенций + 4 детализированных эталона ключевых кластеров (Профессор кафедры 8 ур., Системный архитектор ИКТ 7 ур., Главный бухгалтер 7 ур., Директор Департамента HR 7–8 ур.);
3. **Модернизировать Регламент открытого конкурсного замещения должностей ППС и ученых** (`docs/internal_acts/sops_and_rules/sop_faculty_and_researcher_recruitment_competition.md`): интегрировать квалификационные дескрипторы 7–8 уровней НРК, критерии отраслевых профстандартов, механизм зачета Microcredentials и шкалу оценки практических кейсов;
4. **Закрепить институциональную функцию в Каталоге функций Домена 10** (`docs/functions_and_powers/10_human_capital_and_hr.md`): внести функцию `FUNC-HR-PROF-STANDARDS-012`, зафиксировать персональную роль `Accountable: Директор Департамента HR` и обновить реестр ВНД;
5. **Собрать объективные доказательства** в `evidence/EV_PHASE_B.md` и подготовить отчет `RF_PHASE_B.md`.

## 2. Entry Points

- `docs/regulations/sector_standards/STD-RK-013-PROF-STANDARDS-ATAMEKEN.md` — Отраслевой стандарт (базовые принципы и уровни 5–8 НРК);
- `docs/regulations/11_professional_standards_and_qualifications_registry.md` — Модуль 11 реестра профстандартов с нормами Приказа МТСЗН № 374;
- `docs/internal_acts/blueprints/atameken_job_descriptions_gap_analysis_matrix.md` — Мастер-матрица сопоставления 37 должностей;
- `docs/internal_acts/sops_and_rules/sop_faculty_and_researcher_recruitment_competition.md` — Регламент открытого конкурса;
- `docs/functions_and_powers/10_human_capital_and_hr.md` — Каталог функций Домена 10 (HR);
- `docs/regulations/external_npa_registry.md` — Реестр внешних НПА (Закон № 14-VIII, Приказы МТСЗН № 436, № 374, МНВО № 591, МОН № 230).

## 3. Questions (blocking — cannot proceed without answers)

Блокирующих вопросов нет. Все входные параметры, нормативные источники и требования спецификации `TS_PHASE_B.md` детально определены.

## 4. Recommendations (suggestions, not blocking)

1. В регламенте СОП `SOP-HR-PROF-STANDARDS-001` предусмотреть создание постоянной или созываемой **Комиссии по признанию профессиональных квалификаций и микроквалификаций ОВПО**, чтобы процедура верификации сертификатов Coursera, edX, Cisco, ACCA и др. имела строгую коллегиальную основу и протоколирование.
2. В Карты компетенций (Job Competency Cards) включить матрицу уровней владения навыками по шкале: Базовый (Awareness), Практический (Working), Продвинутый (Advanced), Экспертный (Expert), соотнесенную с дескрипторами НРК.
3. В Регламенте конкурса ППС (`sop_faculty_and_researcher_recruitment_competition.md`) выделить в Оценочном листе соискателя отдельный дифференцированный блок «Индустриальная квалификация, Microcredentials и практический опыт» (до 20 баллов из 100).

## 5. Risks Found (edge cases, potential issues not in TS)

- **Риск субъективности при зачете неформального образования:** для исключения произвольных решений в СОПе закрепляется обязательный перечень критериев верифицируемости микроквалификаций по Приказу МТСЗН РК № 374 (проверяемый Digital ID / URL сертификата, объем в ECTS/академических часах, наличие итогового экзамена/оценки, авторитет провайдера).
- **Соблюдение авторских прав и защита персональных данных:** при подаче портфолио и сертификатов соискателей в личном кабинете обеспечивается соблюдение Закона РК «О персональных данных и их защите».

## 6. Inconsistencies with Code (spec vs reality)

Несоответствий не выявлено. Целевые файлы и их структура согласованы с архитектурой репозитория.

## 7. Knowledge Citations

| # | HL / TS ref | Read? | Applied / N/A | Notes |
|---|---|:---:|---|---|
| 1 | `FACT-024` | ✅ | Applied | Конкурсный отбор ППС и ученых (Приказ МОН № 230, МНВО № 424) |
| 2 | `FACT-033` | ✅ | Applied | Применение ст. 116–118 ТК РК и ст. 98 КоАП |
| 3 | `FACT-043` | ✅ | Applied | Сопряжение с дескрипторами 6–8 уровней Профстандарта «Педагог» |
| 4 | `FACT-049` | ✅ | Applied | Интеграция 16 профстандартов НПП «Атамекен», Закона № 14-VIII и Приказа МТСЗН № 374 |

---

*ONB — ABAI_20260922-173500_ATAMEKEN_PROF_STANDARDS / Phase B | 2026-09-23*
