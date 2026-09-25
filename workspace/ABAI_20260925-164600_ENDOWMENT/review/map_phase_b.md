# Map — "What was done in Phase B?"
> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.  
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"  
> RF: [RF_PHASE_B.md](../RF_PHASE_B.md)  
> TS: [TS_PHASE_B.md](../TS_PHASE_B.md)  

## Understanding

В рамках Фазы B задачи ABAI-29 завершено формирование институционального контура Ассоциации выпускников и механизма конкурсного распределения инвестиционного дохода Эндаумент-фонда:
1. Положение об Ассоциации выпускников (`REG-SOC-ALUMNI-001`, 112 строк, статус добровольного объединения выпускников, Конференция, Правление во главе с Президентом, программа лояльности и 6 привилегий: Digital Alumni Card, доступ в библиотеки/Scopus, скидки на спорт, пожизненный e-mail `@alumni.abai.kz`, скидка 15% на MBA/DBA, наставничество «Выпускник — Студенту», ежегодный Alumni Day, премия «Гордость Alma Mater», сборы в эндаумент на «Стену почета»);
2. Должностная инструкция Координатора по связям с выпускниками (`JD-SOC-ALUMNI-COORD-001`, 101 строка, 7 уровень НРК, опыт в PR/Event/HR $\ge 3$ лет, формирование модуля «Alumni CRM» УИС SIS с соблюдением Закона о ПДн № 94-V, организация Alumni Day, администрирование менторских пар);
3. Регламент (СОП) конкурсного распределения инвестиционного дохода эндаумента (`SOP-SCI-ENDOWMENT-GRANTS-001`, 91 строка, двухэтапный открытый отбор по модели Peer Review по 4 направлениям: Seed-гранты TRL 1–4, Postdoc Fellowship, именные стипендии, гранты на общежитие, жесткий запрет покрытия текущих расходов АУП);
4. Гармонизация Каталога функций: закрепление персональных зон ответственности Accountable в Домене 02 (`FUNC-SCI-ENDOW-GRANT-011`), Домене 03 (`FUNC-SOC-ALUMNI-010`) и Домене 06 (`FUNC-GOV-ENDOW-BOARD-014`).

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|---|---|:---:|
| **AC-1:** Положение об Ассоциации выпускников (статус, органы, лояльность, менторство, Alumni Day) | Разработано `alumni_association_regulation.md` (112 строк) | ✅ |
| **AC-2:** ДИ Координатора по связям с выпускниками (7 уровень НРК, CRM, Закон № 94-V, менторство) | Разработана `jd_alumni_relations_coordinator.md` (101 строка) | ✅ |
| **AC-3:** СОП грантов эндаумента (двухэтапный конкурс, Peer Review, 4 программы, запрет АУП) | Разработан `sop_endowment_grants_and_scholarships.md` (91 строка) | ✅ |
| **AC-4:** Гармонизация Каталога функций (Домены 02, 03, 06 со строгим правилом одного Accountable) | Домены 02, 03, 06 обновлены | ✅ |
| **AC-5:** Соблюдение Scope Budget ($\le 8$ новых файлов, $\le 1200$ LOC, 0 TODO) | 3 новых файла + 3 измененных, 304 новых LOC, 0 TODO | ✅ |

## Deviations from TS

Отклонений от спецификации TS Phase B нет.

## Checkpoint

Stage complete: YES
