# Map — Review Stage 1 (Phase B)
## Task: ABAI_20260923-151500_AI_POLICY / Phase B
## Date: 2026-09-23 | Reviewer: Independent Reviewer / Academic Integrity Auditor

---

## 1. Input Verification Map

| Claim / Deliverable | Source in TS Phase B | Target File | Verification Method |
|---|---|---|---|
| **AC-1:** Методические указания по аутентичному оцениванию для ППС (`GUIDE-ACAD-AI-001`) | TS §5 AC-1, §4 | `docs/internal_acts/sops_and_rules/guidelines_ai_authentic_assessment_for_faculty.md` | Структурный аудит переосмысления таксономии Блума в эпоху GenAI, матрицы интеграции шкалы 0–3 в силлабусы, 4 моделей аутентичных заданий, чек-листа Viva Voce и рубрики оценивания |
| **AC-2:** Регламент (СОП) применения ИИ в научно-исследовательских работах и публикациях (`SOP-SCI-AI-ETHICS-001`) | TS §5 AC-2, §4 | `docs/internal_acts/sops_and_rules/sop_scientific_ai_ethics_and_publishing.md` | Проверка запрета авторства ИИ по COPE (2024), подраздела AI Disclosure, запрета фальсификации данных, защиты патентной чистоты, тайны Peer Review и синхронизации с диссертациями PhD |
| **AC-3:** Каталог функций Домена 01 (Academic Affairs) | TS §5 AC-3, §4 | `docs/functions_and_powers/01_academic_affairs.md` | Проверка закрепления функции `FUNC-ACAD-AI-011` за Директором ДАВ и обновления реестра ВНД |
| **AC-4:** Каталог функций Домена 02 (Science & Technology) | TS §5 AC-4, §4 | `docs/functions_and_powers/02_science_and_technology.md` | Проверка закрепления функции `FUNC-SCI-ETHIC-AI-010` за Проректором по науке / Директором науки и обновления реестра ВНД |
| **AC-5:** Каталог функций Домена 05 (Quality Assurance & Compliance) | TS §5 AC-5, §4 | `docs/functions_and_powers/05_quality_assurance_and_compliance.md` | Проверка закрепления функции `FUNC-QA-AI-AUDIT-009` за Председателем QA Committee и обновления реестра ВНД |
| **AC-6:** Стандарты оформления, реестр и 0 плейсхолдеров | TS §5 AC-6 | `docs/internal_acts/README.md` и созданные/измененные файлы | Проверка актуализации реестра, grep_search по `TODO|TBD|FIXME`, проверка системных переменных `[V_*]` |
| **AC-7:** Протокол объективных доказательств | TS §5 AC-7 | `workspace/.../evidence/EV_PHASE_B.md` | Анализ протокола доказательств, проверка 100% покрытия критериев AC-1 — AC-6 со статусом VERIFIED |

---

## 2. Scope & Budget Map

- **Плановый бюджет TS:** 2 новых файла VALUE, 4 модифицированных VALUE, объем $\approx 750$ LOC.
- **Фактическое исполнение RF:**
  - Новых файлов VALUE: 2 (`guidelines_ai_authentic_assessment_for_faculty.md`, `sop_scientific_ai_ethics_and_publishing.md`);
  - Модифицированных файлов VALUE: 4 (`01_academic_affairs.md`, `02_science_and_technology.md`, `05_quality_assurance_and_compliance.md`, `docs/internal_acts/README.md`);
  - Созданных файлов TRACE: 2 (`ONB_PHASE_B.md`, `EV_PHASE_B.md`, `RF_PHASE_B.md`);
  - Фактический объем изменений: $\approx 300$ LOC (в пределах лимита $\le 1200$ LOC).

---

## 3. Self-Check Gate (Map)

- [x] Все входные требования TS Phase B картированы на целевые файлы.
- [x] Объем заявленных изменений в RF сопоставлен с кодовой базой.
- [x] Ролевой шлюз соблюден: Reviewer приступает к независимой верификации без права изменения кода.
