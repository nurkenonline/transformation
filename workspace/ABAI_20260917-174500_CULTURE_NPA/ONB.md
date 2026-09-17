# ONB — ABAI_20260917-174500_CULTURE_NPA / Phase A: Разработка аналитического модуля НПА МКИ РК и интеграция в Реестр

> **Date**: 2026-09-17  
> **Author**: Executor  
> **Status**: 🟢 ONB_RESOLVED — Ready for execution  
> **Parent HL**: [HL-ABAI_20260917-174500_CULTURE_NPA](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260917-174500_CULTURE_NPA/HL.md)  
> **TS**: [TS Phase A](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260917-174500_CULTURE_NPA/TS.md)  

---

## 1. Understanding

Задача Фазы A заключается в создании нового аналитического регуляторного модуля `docs/regulations/10_culture_archives_and_media_npa.md`, систематизирующего нормативные акты Министерства культуры и информации Республики Казахстан (МКИ РК), включении реестровых карточек актов в мастер-реестр `docs/regulations/external_npa_registry.md` (Раздел 10 с прямыми ссылками на ИПС «Әділет»), обновлении навигационного индекса `docs/regulations/README.md` и фиксации доказательств верификации первоисточников в `EV__CULTURE_NPA_PHASE_A.md`.

---

## 2. Entry Points (3 файла VALUE + 1 TRACE)

- `docs/regulations/10_culture_archives_and_media_npa.md` (AC-1) [CREATE]
- `docs/regulations/external_npa_registry.md` (AC-2) [MODIFY]
- `docs/regulations/README.md` (AC-3) [MODIFY]
- `workspace/ABAI_20260917-174500_CULTURE_NPA/evidence/EV__CULTURE_NPA_PHASE_A.md` (AC-4) [CREATE]

---

## 3. Questions (blocking)

Блокирующих вопросов нет. Первоисточники в ИПС «Әділет» проверены, реквизиты законов и приказов МКИ РК (включая Закон РК «О масс-медиа» № 94-VIII от 19.06.2024 и Приказ и.о. МКИ РК № 566-НҚ от 29.12.2023 со сроком 75 лет хранения) установлены.

---

## 4. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|---|:---:|---|---|
| 1 | `KNOWLEDGE.md` `FACT-006` | ✅ | Applied | Формирование контрольного контура нормативных модулей |
| 2 | `KNOWLEDGE.md` `FACT-023` | ✅ | Applied | Требования к документированию и архивам в универсальной модели ОВПО |
| 3 | `.tfw/conventions.md` §3 | ✅ | Applied | Заморозка контракта и ролевой шлюзовой контроль |

---

## 5. Scope Budget Check

- Новых файлов VALUE: 1 (лимит: 8)
- Всего затронуто файлов VALUE: 3 (лимит: 14)
- Планируемый объем строк: ~600 LOC (лимит: 1200 LOC)
- Бюджет соблюден полностью.

---

## 6. Execution Steps

1. Разработать `docs/regulations/10_culture_archives_and_media_npa.md` с детальным анализом 5 кластеров (Архивы/СЭД, Библиотеки, Масс-медиа, Музеи, Творческое образование).
2. Модифицировать `docs/regulations/external_npa_registry.md`, добавив Раздел 10 с подробными таблицами по МКИ РК.
3. Актуализировать навигационную структуру в `docs/regulations/README.md`.
4. Составить протокол доказательств `workspace/ABAI_20260917-174500_CULTURE_NPA/evidence/EV__CULTURE_NPA_PHASE_A.md`.
5. Сформировать `workspace/ABAI_20260917-174500_CULTURE_NPA/RF.md`.
