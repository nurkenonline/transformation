# Домен 05: Управление качеством, аккредитация и комплаенс (Quality Assurance & Compliance)

## 1. Архитектурная модель и организационный контур домена

Контур обеспечения качества и комплаенс-контроля Университета функционирует на основе стандартов ESG 2015 Part 1 (`STD-RK-ESG-001`), критериев Системы управления рисками КОКСНВО (`STD-RK-SUR-001`) и антикоррупционного законодательства РК:
1. **Комитет по обеспечению качества (QA Committee):** Независимый коллегиальный орган при Ученом совете, проводящий системную валидацию образовательных программ, силлабусов, мониторинг студентоцентрированного обучения и результатов опросов.
2. **Центр аккредитации и качества:** Организация и сопровождение международной и национальной институциональной и специализированной аккредитации в агентствах из Реестра EQAR (IQAA, IAAR, ASIIN, ACQUIN раз в 5 лет), мониторинг соответствия Квалификационным требованиям (`STD-RK-QUAL-001`).
3. **Антикоррупционная комплаенс-служба:** Обособленное подразделение, непосредственно подотчетное Совету директоров (ст. 16 Закона РК «О противодействии коррупции»), проводящее внутренний анализ коррупционных рисков (ВАКР), антикоррупционную экспертизу проектов ВНД и администрирование каналов Whistleblowing.
4. **Совет образовательных стейкхолдеров (EdTech & School Advisory Board):** Привлечение директоров передовых школ, лидеров EdTech-индустрии и работодателей к оценке практикоориентированности программ.

---

## 2. Реестр функций домена

| Код функции | Наименование функции | Основание в НПА РК | Ответственный (Accountable) | Соисполнители (Responsible) | Реализующий ВНД |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `FUNC-QA-AUDIT-001` | Внутренний аудит образовательных программ и процессов по 10 стандартам ESG 2015 | Закон РК «Об образовании» (ст. 9-1), `STD-RK-ESG-001` | Председатель QA Committee | Комитет по обеспечению качества, ДАВ, Институты | [`quality_assurance_committee_regulation.md`](../internal_acts/regulations/quality_assurance_committee_regulation.md), [`rk_esg_quality_assurance_standards.md`](../regulations/rk_esg_quality_assurance_standards.md) |
| `FUNC-QA-QUAL-002`  | Непрерывный мониторинг соответствия деятельности Квалификационным требованиям (№ 391) | Приказ МОН РК № 391, `STD-RK-QUAL-001` (остепененность 45–50%/60%/100%, площади $\ge 6\text{ м}^2$) | Руководитель Центра аккредитации | ДАВ, HR, Департамент науки, Библиотека | [`accreditation_center_regulation.md`](../internal_acts/regulations/accreditation_center_regulation.md), [`jd_head_accreditation.md`](../internal_acts/job_descriptions/jd_head_accreditation.md) |
| `FUNC-QA-ACCRED-003`| Координация институциональной и специализированной аккредитации в агентствах из Реестра EQAR | Закон «Об образовании» (ст. 59-1), стандарты НААР/НКАОКО | Руководитель Центра аккредитации | Институты, Кафедры, ДАВ, ДСР | [`accreditation_center_regulation.md`](../internal_acts/regulations/accreditation_center_regulation.md) |
| `FUNC-QA-ONLINE-004`| Сертификация качества и стандартизация цифровых онлайн-курсов и MOOC | Закон «Об образовании», ГОСО, `STD-RK-GOSO-001` | Председатель QA Committee | Отдел цифровых образовательных технологий, ДАВ | [`sop_online_courses_quality_standard.md`](../internal_acts/sops_and_rules/sop_online_courses_quality_standard.md) |
| `FUNC-QA-COMPL-005` | Проведение ежегодного внутреннего анализа коррупционных рисков (ВАКР) | Закон «О противодействии коррупции» (ст. 8, 16), Типовые правила ВАКР | Руководитель Антикоррупционной службы | Юридический департамент, Руководители подразделений | [`compliance_service_regulation.md`](../internal_acts/regulations/compliance_service_regulation.md), [`sop_anti_corruption_risk_assessment.md`](../internal_acts/sops_and_rules/sop_anti_corruption_risk_assessment.md) |
| `FUNC-QA-ETHIC-006` | Антикоррупционная экспертиза проектов внутренних актов и договоров, комплаенс-контроль | Закон РК «О противодействии коррупции» | Антикоррупционный комплаенс-офицер | Инициаторы актов, Канцелярия, Юристы | [`jd_compliance_officer.md`](../internal_acts/job_descriptions/jd_compliance_officer.md) |
| `FUNC-QA-STAKE-007` | Организация диалога со стейкхолдерами образования и работодателями | Стандарты ESG 1.1, ГОСО | Директор ДАВ | EdTech Advisory Board, Институты, Центр карьеры | [`edtech_advisory_board_regulation.md`](../internal_acts/regulations/edtech_advisory_board_regulation.md) |
| `FUNC-QA-SUR-008`   | Мониторинг критериев Системы управления рисками (СУР КОКСНВО) по 10 направлениям | Совместный приказ МНВО № 166 и МНЭ № 116, `STD-RK-SUR-001` | Руководитель Центра аккредитации | QA Committee, ДАВ, HR, Департамент науки | [`accreditation_center_regulation.md`](../internal_acts/regulations/accreditation_center_regulation.md), [`rk_sur_risk_assessment_standard.md`](../regulations/rk_sur_risk_assessment_standard.md) |
| `FUNC-QA-AI-AUDIT-009` | Независимый аудит соблюдения Институциональной политики ИИ, прозрачности декларирования в силлабусах и мониторинг недопущения неправомерных санкций к студентам по индикаторам AI-детекторов (аудит процедур Viva Voce) | Стандарты ESG 1.3, 1.4 (`STD-RK-ESG-001`), Рекомендация ЮНЕСКО (2021) | Председатель QA Committee | QA Committee, Центр аккредитации, Студенческий омбудсмен, Дисциплинарная комиссия | [`quality_assurance_committee_regulation.md`](../internal_acts/regulations/quality_assurance_committee_regulation.md), [`ai_governance_and_integrity_policy.md`](../internal_acts/sops_and_rules/ai_governance_and_integrity_policy.md), [`academic_integrity_policy.md`](../internal_acts/sops_and_rules/academic_integrity_policy.md) |

---

## 3. Реестр локальных нормативных актов домена

1. **Положения о подразделениях и комиссиях:**
   - [`REG-QA-COMM-001` Положение о Комитете по обеспечению качества (QA Committee)](../internal_acts/regulations/quality_assurance_committee_regulation.md)
   - [`REG-QA-ACCRED-001` Положение о Центре аккредитации и постаккредитационного мониторинга](../internal_acts/regulations/accreditation_center_regulation.md)
   - [`REG-QA-COMPL-001` Положение об Антикоррупционной комплаенс-службе](../internal_acts/regulations/compliance_service_regulation.md)
   - [`REG-QA-STAKE-001` Положение о Совете образовательных стейкхолдеров (EdTech & School Advisory Board)](../internal_acts/regulations/edtech_advisory_board_regulation.md)

2. **Должностные инструкции:**
   - [`JD-QA-ACCRED-HEAD-001` ДИ Руководителя Центра аккредитации и обеспечения качества](../internal_acts/job_descriptions/jd_head_accreditation.md)
   - [`JD-QA-COMPL-OFF-001` ДИ Антикоррупционного комплаенс-офицера](../internal_acts/job_descriptions/jd_compliance_officer.md)

3. **Стандарты операционных процедур (СОП) и регламенты:**
   - [`POL-AI-INTEGRITY-001` Институциональная политика этичного использования искусственного интеллекта и генеративных моделей](../internal_acts/sops_and_rules/ai_governance_and_integrity_policy.md)
   - [`SOP-QA-VAKR-001` Регламент проведения внутреннего анализа коррупционных рисков (ВАКР)](../internal_acts/sops_and_rules/sop_anti_corruption_risk_assessment.md)
   - [`SOP-QA-ONLINE-001` Стандарт качества и сертификации цифрового образовательного контента (онлайн-курсов)](../internal_acts/sops_and_rules/sop_online_courses_quality_standard.md)

---

## 4. Цифровой контур и функциональные модули УИС

1. **Модуль «Качество и опросы»:** анонимное анкетирование обучающихся «Преподаватель глазами студентов», оценка качества образовательных программ и дисциплин по циклу PDCA.
2. **Модуль «Аккредитация и мониторинг рекомендаций»:** контроль сроков дорожных карт постаккредитационных мероприятий.
3. **Модуль «Мониторинг СУР и Квалтребований»:** дашборд превентивной оценки рисков ОВПО по 10 направлениям КОКСНВО для предотвращения перехода в красную зону ($\ge 60$ баллов).
4. **Модуль «Комплаенс и Whistleblowing»:** анонимная горячая линия по сообщениям о фактах коррупции, конфликта интересов и вымогательства с шифрованием обращений.
