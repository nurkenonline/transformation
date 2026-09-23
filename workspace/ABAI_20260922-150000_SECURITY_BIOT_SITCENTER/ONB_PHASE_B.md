# ONB — ABAI_20260922-150000_SECURITY_BIOT_SITCENTER / Phase B: Раздельные нормативные пакеты Службы охраны труда (БиОТ) и Отдела Гражданской обороны (ГО и ЧС)

> **Date**: 2026-09-22  
> **Author**: Executor / Safety & Regulatory Implementation Engineer  
> **Status**: 🟢 ONB_RESOLVED — Ready for implementation  
> **Parent HL**: [HL-ABAI_20260922-150000_SECURITY_BIOT_SITCENTER](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260922-150000_SECURITY_BIOT_SITCENTER/HL.md)  
> **TS**: [TS Phase B](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260922-150000_SECURITY_BIOT_SITCENTER/TS_PHASE_B.md)  

---

## 1. Understanding

Задача Фазы B — институционализировать строгое разделение контуров безопасности кампуса на самостоятельные структуры:
1. **Служба охраны труда (БиОТ) — обособленное структурное подразделение:**
   - Прямое подчинение первому руководителю (Ректору / Председателю Правления) в соответствии с п. 2 ст. 202 Трудового кодекса РК;
   - Компетенция: производственная безопасность, санитарно-гигиенические условия труда, обязательная аттестация рабочих мест и лабораторий по условиям труда 1 раз в 5 лет (Приказ МЗСР № 1057), обеспечение СИЗ, обучение БиОТ и ПДЭК (Приказ МЗСР № 1019), специальное расследование несчастных случаев на производстве (ст. 187–190 ТК РК);
   - ВНД: `occupational_safety_regulation.md` (`REG-BIOT-001`) и ДИ `jd_head_occupational_safety.md` (`JD-BIOT-HEAD-001`).
2. **Отдел Гражданской обороны и чрезвычайных ситуаций (ГО и ЧС) — обособленное структурное подразделение:**
   - Реализация Закона РК «О гражданской защите» № 188-V и Приказа МЧС РК № 268;
   - Компетенция: разработка и ведение Плана Гражданской обороны Университета, содержание и готовность защитных сооружений ГО (ПРУ), формирование и обучение невоенизированных формирований ГО (санитарные посты, звенья пожаротушения, спасатели), пожарный надзор по Приказу МЧС № 55;
   - ВНД: `civil_defense_and_emergency_regulation.md` (`REG-GO-001`) и ДИ `jd_head_civil_defense_and_emergency.md` (`JD-GO-HEAD-001`).
3. **Общеуниверситетский СОП эвакуационных тренировок:**
   - `sop_emergency_and_evacuation_drills.md` (`SOP-EMERG-EVAC-001`): разграничение ответственности между 4 структурами (ГО и ЧС, БиОТ, СБ и СЦ).
4. **Каталог функций Домена 09:**
   - `09_infrastructure_and_facilities.md`: отражение 4 самостоятельных структур и их закрепление в RACI-матрицах.

---

## 2. Plan of Execution

1. Разработать `docs/internal_acts/regulations/occupational_safety_regulation.md` (`REG-BIOT-001`).
2. Разработать `docs/internal_acts/job_descriptions/jd_head_occupational_safety.md` (`JD-BIOT-HEAD-001`).
3. Разработать `docs/internal_acts/regulations/civil_defense_and_emergency_regulation.md` (`REG-GO-001`).
4. Разработать `docs/internal_acts/job_descriptions/jd_head_civil_defense_and_emergency.md` (`JD-GO-HEAD-001`).
5. Актуализировать `docs/internal_acts/sops_and_rules/sop_emergency_and_evacuation_drills.md` (`SOP-EMERG-EVAC-001`).
6. Актуализировать `docs/functions_and_powers/09_infrastructure_and_facilities.md`.
7. Провести проверку на отсутствие плейсхолдеров ripgrep, скомпилировать `EV_PHASE_B.md` и `RF_PHASE_B.md`.
