# TS — ABAI-1: Формирование исчерпывающего реестра внешних НПА РК и функциональной декомпозиции

> **Date**: 2026-09-14  
> **Author**: Coordinator  
> **Status**: 🟢 APPROVED  
> **Parent HL**: [HL](HL.md)  

---

## 1. Objective
Сформировать исчерпывающий, структурированный нормативно-правовой реестр внешних актов Республики Казахстан (Законы, Кодексы, Приказы МНВО/МОН, МЗ, МЧС, МЦРИАП, МНЭ, МФ) с прямыми эталонными гиперссылками на ИПС «Әділет» (`adilet.zan.kz`), разработать 7 отраслевых аналитических модулей и декомпозировать деятельность университета на 10 стратегических функциональных доменов в рамках Новой регуляторной политики «С чистого листа».

## 2. Scope

### In Scope
- Разработка Сводного реестра внешних НПА: `docs/regulations/external_npa_registry.md`.
- Создание 7 отраслевых аналитических модулей законодательства:
  - `docs/regulations/01_academic_and_educational_npa.md`
  - `docs/regulations/02_science_and_innovations_npa.md`
  - `docs/regulations/03_hr_and_faculty_npa.md`
  - `docs/regulations/04_student_and_youth_npa.md`
  - `docs/regulations/05_governance_finance_compliance_npa.md`
  - `docs/regulations/06_healthcare_and_sanitary_npa.md`
  - `docs/regulations/07_fire_and_emergency_safety_npa.md`
- Разработка архитектуры функциональных доменов: `docs/functions_and_powers/README.md`.
- Формирование контура доказательств: `evidence/EV__ABAI-1.md`.

### Out of Scope
- Разработка внутренних положений кафедр и факультетов (перенесено в отраслевые задачи ABAI-2..ABAI-7).
- Автоматизация выгрузки данных через API (задача ABAI-5).

## 3. Principles Check

| # | HL §7 principle | Enforced by | Gate |
|---|---|---|---|
| P1 | Легитимность и привязка к НПА РК | AC-1, AC-2 | Сверка номеров приказов и регистраций в МЮ РК по базе ИПС «Әділет» |
| P2 | Исчерпывающий охват РЧЛ | AC-2 | Включение требований Совместного приказа МНВО № 166 и МНЭ № 116 |
| P3 | Антидублирование функций | AC-3 | Структурирование 10 независимых доменов в классификаторе функций |

## 4. Affected Files and Value-Bearing Accounting

| File / selector | Action | Class | Semantic reason / required result |
|---|---|---|---|
| `docs/regulations/external_npa_registry.md` | CREATE | `VALUE` | Сводный эталонный реестр 80+ внешних НПА со ссылками на Әділет |
| `docs/regulations/01_academic_and_educational_npa.md` | CREATE | `VALUE` | Правовой модуль академической деятельности (ГОСО, кредит, прием) |
| `docs/regulations/02_science_and_innovations_npa.md` | CREATE | `VALUE` | Правовой модуль науки (Закон 2024 г., диссоветы, степени) |
| `docs/regulations/03_hr_and_faculty_npa.md` | CREATE | `VALUE` | Правовой модуль кадрового потенциала и трудовых отношений |
| `docs/regulations/04_student_and_youth_npa.md` | CREATE | `VALUE` | Правовой модуль студенческого контингента и молодежной политики |
| `docs/regulations/05_governance_finance_compliance_npa.md` | CREATE | `VALUE` | Модуль корпоративного управления, финансов и комплаенса |
| `docs/regulations/06_healthcare_and_sanitary_npa.md` | CREATE | `VALUE` | Модуль санитарно-эпидемиологических правил (20 актов МЗ РК) |
| `docs/regulations/07_fire_and_emergency_safety_npa.md` | CREATE | `VALUE` | Модуль пожарной безопасности и ЧС (9 актов МЧС РК) |
| `docs/functions_and_powers/README.md` | CREATE | `VALUE` | Классификатор и архитектура 10 функциональных доменов ОВПО |
| `workspace/ABAI-1__regulatory_base_and_functional_decomposition/evidence/EV__ABAI-1.md` | CREATE | `ASSURANCE` | Протокол верификации доказательств |
| `workspace/ABAI-1__regulatory_base_and_functional_decomposition/RF.md` | CREATE | `TRACE` | Итоговый результирующий отчет исполнителя |

### Prospective accounting contract

| Fact | Approved value |
|---|---|
| Subject / exact VALUE selector | `docs/regulations/*.md`, `docs/functions_and_powers/README.md` |
| Baseline / selector source | `INITIAL` commit / approval TS ABAI-1 |
| Candidate rule | First tested Executor commit with required VALUE+ASSURANCE, before EV/RF/REVIEW/final transition |
| Logical VALUE files | 9 |
| Touched text LOC | adds: 1800+, deletes: 0 = 1800+ LOC |
| Triggers / disposition | Initial project regulatory bootstrap; terminal verdict complete |
| Multiplier / authority | Approved Coordinator |
| Approval epoch / failure | Prospective epoch v1.0-REG |

```powershell
git diff --name-status --find-renames=50% -z <BASELINE_SHA> <CANDIDATE_SHA> -- $valuePaths
git diff --numstat --find-renames=50% -z <BASELINE_SHA> <CANDIDATE_SHA> -- $valuePaths
```

### Prospective scope rulings
Пакет формирует неделимый базис регуляторного контура Университета; исключение любого из 7 аналитических модулей признается дефектом архитектуры.

### Task-local hard constraints (when material)

| M1 consequence | M2 object/risk | M3 measure/selector | M4 pre-act check | M5 softer-control gap | M6 change authority |
|---|---|---|---|---|---|
| Юридическая нелегитимность внутренних актов | Недостоверные реквизиты НПА | Прямые ссылки на adilet.zan.kz | HTTP-валидация ссылок | Проверка вручную | Coordinator |
| Несоответствие проверкам КОКСНВО | Игнорирование критериев риска | 10 направлений СУР (№ 166/116) | Сверка с Реестром РОТ | Риск штрафов | Reviewer |

**Actions:** 9 CREATE (VALUE), 1 CREATE (ASSURANCE), 1 CREATE (TRACE).  
**Immutable owner-approved denominator:** 9 VALUE files, 1800+ LOC.

## 5. Acceptance Criteria

### AC-1: Сводный реестр внешних НПА РК со 100% валидированными гиперссылками
Сформирован единый структурированный реестр, охватывающий Законы, Кодексы, Приказы МНВО/МОН, МЗ, МЧС, МЦРИАП, МНЭ, МФ.
- [x] Реестр содержит прямые гиперссылки на эталонные тексты в ИПС «Әділет» (`adilet.zan.kz`).

Gate: Проверка доступности URL-ссылок и реквизитов актов в ИПС «Әділет».  
Evidence: `docs/regulations/external_npa_registry.md`, статус VERIFIED.

### AC-2: 7 отраслевых аналитических модулей законодательства
Разработаны детальные справки-модули по ключевым векторам университетского менеджмента.
- [x] Включен анализ совместного приказа МНВО № 166 и МНЭ № 116 по 10 направлениям СУР ОВПО.

Gate: Проверка наличия 7 файлов модулей в каталоге `docs/regulations/`.  
Evidence: `docs/regulations/01_*.md` – `07_*.md`, статус VERIFIED.

### AC-3: Архитектурная декомпозиция по 10 функциональным доменам
Сформирован структурированный Каталог функций с уникальными кодами `FUNC-{DOMAIN}-{SUBDOMAIN}-{NNN}`.
- [x] Определены границы ответственности и исключены пересечения полномочий.

Gate: Проверка структуры доменов в `docs/functions_and_powers/README.md`.  
Evidence: `docs/functions_and_powers/README.md`, статус VERIFIED.

### Evidence Artifacts

| File | Description |
|---|---|
| `workspace/ABAI-1__regulatory_base_and_functional_decomposition/evidence/EV__ABAI-1.md` | Протокол верификации критериев AC-1..AC-3 |

## 6. Technical Guidance
- Использовать официальные заголовки нормативных правовых актов в редакции, действующей на момент утверждения ТС.
- В таблицах внешних НПА указывать статус действия («Действующий»), дату принятия и регистрационный номер МЮ РК.

## 7. Definition of Failure
- ❌ Наличие битых или недействительных ссылок на нормативные акты.
- ❌ Использование отмененных или утративших силу редакций приказов МОН/МНВО РК.
- ❌ Наличие плейсхолдеров (`TODO`, `TBD`) в описании регуляторных требований.

## 8. Phase Risks

| Risk | Mitigation |
|---|---|
| Внесение изменений в законодательство РК в период разработки | Еженедельный мониторинг базы ИПС «Әділет» и ведение версионированного реестра |
| Избыточная детализация доменов | Ограничение верхнего уровня 10 ключевыми функциональными областями ОВПО |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|---|---|---|
| `docs/regulations/external_npa_registry.md` | ABAI-5, ABAI-6, ABAI-7 | Актуализация профильных блоков при разработке целевых ВНД |
| `docs/functions_and_powers/README.md` | ABAI-2..ABAI-7 | Наполнение реестров конкретными паспортами функций |

---

*TS — ABAI-1: Формирование исчерпывающего реестра внешних НПА РК | 2026-09-14*
