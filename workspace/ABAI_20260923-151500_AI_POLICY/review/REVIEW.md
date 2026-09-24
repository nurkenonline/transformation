# REVIEW — ABAI-26: Институциональная политика этичного использования искусственного интеллекта (GenAI), академическая честность, аутентичное оценивание и публикационная этика по COPE (Фазы A и B)

> **Date**: 2026-09-23  
> **Author**: Reviewer / Academic Integrity & AI Governance Auditor  
> **Verdict**: ✅ **APPROVE (Full Task Approved: Phases A & B Completed)**  
> **Target Lifecycle**: `DONE`  
> **Parent HL**: [HL-ABAI_20260923-151500_AI_POLICY](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260923-151500_AI_POLICY/HL.md)  
> **Phase A Review**: [REVIEW_PHASE_A.md](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260923-151500_AI_POLICY/review/REVIEW_PHASE_A.md) (`✅ APPROVE`)  
> **Phase B Review**: [REVIEW_PHASE_B.md](file:///g:/Мой%20диск/Google%20AI%20Studio/Abai%20Unviersity%20Transformation/workspace/ABAI_20260923-151500_AI_POLICY/review/REVIEW_PHASE_B.md) (`✅ APPROVE`)  
> **Stage files**: `1_map.md`, `2_verify.md`, `3_judge.md`, `map_phase_b.md`, `verify_phase_b.md`, `judge_phase_b.md`  

---

## 1. Executive Summary & Architecture Map

В рамках задачи ABAI-26 Университет сформировал целостную институциональную систему управления и этичного применения технологий искусственного интеллекта (GenAI/LLM), охватывающую нормативный, дидактический, исследовательский и контрольно-надзорный контуры:

```text
┌────────────────────────────────────────────────────────────────────────────┐
│         ИНСТИТУЦИОНАЛЬНЫЙ ЛАНДШАФТ ИСКУССТВЕННОГО ИНТЕЛЛЕКТА В ОВПО РК    │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  1. НОРМАТИВНЫЙ ФУНДАМЕНТ (ФАЗА A)                                         │
│     ├── Институциональная политика POL-AI-INTEGRITY-001 (ПП РК № 604)      │
│     ├── 4-уровневая шкала AI Disclosure Scale (0, 1, 2, 3)                 │
│     ├── Стандартизированный формуляр AI Statement Form                     │
│     └── Презумпция невиновности и процессуальный регламент Viva Voce       │
│                                                                            │
│  2. ДИДАКТИКА И АУТЕНТИЧНОЕ ОЦЕНИВАНИЕ (ФАЗА B)                            │
│     ├── Методические указания GUIDE-ACAD-AI-001 (Блум в эпоху GenAI)       │
│     ├── 4 модели аутентичных заданий (казахстанский контекст, PBL)        │
│     ├── Оценивание процесса создания (черновики, Git, лог промптов)        │
│     └── Чек-лист вопросов для преподавателей при собеседовании Viva Voce   │
│                                                                            │
│  3. НАУЧНАЯ ЭТИКА И ПАТЕНТНЫЙ БАРЬЕР (ФАЗА B)                              │
│     ├── Регламент этики научных публикаций SOP-SCI-AI-ETHICS-001 (COPE)    │
│     ├── Категорический запрет авторства ИИ в научных публикациях           │
│     ├── Защита патентной чистоты от утечек данных в публичные LLM          │
│     ├── Тайна научного рецензирования (Peer Review Confidentiality)        │
│     └── Синхронизация требований оригинальности диссертаций PhD (75–80%)   │
│                                                                            │
│  4. ИНСТИТУЦИОНАЛИЗАЦИЯ В КАТАЛОГЕ ФУНКЦИЙ (ФАЗА B)                        │
│     ├── Домен 01 (Academic Affairs): FUNC-ACAD-AI-011 (Директор ДАВ)       │
│     ├── Домен 02 (Science & Tech):   FUNC-SCI-ETHIC-AI-010 (Наука / REC)   │
│     └── Домен 05 (QA & Compliance):  FUNC-QA-AI-AUDIT-009 (QA Committee)   │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Сводная верификация результатов (Phases A & B)

| Фаза | Результаты и ключевые артефакты | Статус верификации | Вердикт |
|:---:|---|:---:|:---:|
| **Phase A** | `POL-AI-INTEGRITY-001`, `ai_usage_statement_form.md`, модернизация `academic_integrity_policy.md`, актуализация `README.md`. | 100% файлов верифицировано, 7/7 доказательств `VERIFIED`. | ✅ **APPROVE** |
| **Phase B** | `GUIDE-ACAD-AI-001` (аутентичное оценивание), `SOP-SCI-AI-ETHICS-001` (COPE), Каталог функций: Домены 01, 02, 05, актуализация `README.md`. | 100% файлов верифицировано, 8/8 доказательств `VERIFIED`. | ✅ **APPROVE** |

---

## 3. Соблюдение лимитов Scope Budget

- **Всего создано новых файлов VALUE:** 4 файла (`ai_governance_and_integrity_policy.md`, `ai_usage_statement_form.md`, `guidelines_ai_authentic_assessment_for_faculty.md`, `sop_scientific_ai_ethics_and_publishing.md`) при лимите $\le 8$ новых файлов на фазу;
- **Всего модифицировано файлов VALUE:** 4 файла (`academic_integrity_policy.md`, `01_academic_affairs.md`, `02_science_and_technology.md`, `05_quality_assurance_and_compliance.md`, `docs/internal_acts/README.md`);
- **Суммарный объем изменений:** $\approx 660$ LOC за обе фазы (при нормативе $\le 1200$ LOC на одну фазу);
- **Чистота кода:** 0 плейсхолдеров `TODO`/`TBD`/`FIXME`, системные макропеременные `[V_*]` соблюдены на 100%.

---

## 4. Консолидированные факты в KNOWLEDGE.md

1. **`FACT-051`** — *AI Policy, AI Disclosure Scale & Viva Voce Protection (ABAI-26 Phase A)*: Институциональная политика `POL-AI-INTEGRITY-001`, 4-уровневая шкала силлабусов (0–3), запрет выгрузки ПДн (ст. 52 ТК РК, ст. 79 КоАП РК), формуляр AI Statement Form, презумпция невиновности студента и устное собеседование Viva Voce.
2. **`FACT-052`** — *AI Authentic Assessment, Scientific AI Ethics (COPE) & Domain Functions (ABAI-26 Phase B)*: Методические указания для ППС `GUIDE-ACAD-AI-001`, регламент публикационной этики `SOP-SCI-AI-ETHICS-001` по стандартам COPE (2024), патентный барьер для открытых LLM, тайна рецензирования Peer Review, гармонизация функций Доменов 01, 02, 05.

---

## 5. Итоговый вердикт

### **✅ APPROVE (DONE)**

Задача **ABAI-26 (`ABAI_20260923-151500_AI_POLICY`)** полностью выполнена по обеим фазам A и B в строгом соответствии с каноническими правилами **Trace-First Workflow (TFW v3.4.0)**, законодательством Республики Казахстан и международными академическими стандартами. Задача закрыта в статусе **`DONE`**.

---

*REVIEW — ABAI-26: Институциональная политика этичного использования искусственного интеллекта (GenAI) в ОВПО РК | 2026-09-23*
