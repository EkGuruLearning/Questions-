# Exam Profiles & Syllabus Mappings

**Bank build ID:** `cn-014b0aa51c0651e7`<br>
**Canonical SHA-256:** `014b0aa51c0651e77ee8166a9f81a4daeeb0574b75b7abf6e5d72050c46feef0`<br>
**Snapshot date:** 2026-10-14

No exam profile is published as an exact simulation in this build. Official links in the catalog are references, not a release-gate pass; timing and marking fields are deliberately not treated as verified. The UGC-NET syllabus index was checked and labels its syllabi as applicable from June 2019; the NTA homepage served June 2025 materials during this audit, so no current-cycle 2026 pattern is claimed. The draft `AnswerKey.html` URL was removed from the UGC pattern field.

| Profile | Status | Scope | Pattern status | Tag records | Time / marking |
|---|---|---|---|---:|---|
| General Computer Networks practice | `available` | `practice_only` | `not_an_exam_blueprint` | 1556 | Practice default; not an official exam rule |
| GATE CS/IT — syllabus-based CN practice | `review` | `syllabus_based_practice` | `official_pattern_not_reverified_in_this_build` | 457 | User-configured mock only; full GATE MCQ/MSQ/NAT rules are not implemented |
| UGC-NET Computer Science & Applications (087) — CN practice | `review` | `syllabus_based_practice` | `current_cycle_pattern_not_reverified` | 426 | User-configured mock only; this is not a complete Paper 1 + Paper 2 test |
| RPSC Programmer — CN syllabus-based practice | `review` | `syllabus_based_practice` | `official_notice_and_pattern_not_reverified_in_this_build` | 1379 | User-configured mock only; notification-specific rules are not configured |
| Rajasthan Informatics Assistant — syllabus-based practice | `review` | `syllabus_based_practice` | `authority_and_current_pattern_not_reverified_in_this_build` | 997 | User-configured mock only; current notification must be checked |
| SSC Computer Awareness — practice segment | `review` | `syllabus_based_practice` | `exam_and_year_specific_pattern_not_reverified_in_this_build` | 1020 | User-configured mock only; section coverage and marking vary by exam/year |

## Official references (links are not current-cycle pattern approval)

- **GATE CS/IT — syllabus-based CN practice** — https://gate2026.iitg.ac.in/exam-papers-and-syllabus.html, https://gate2026.iitg.ac.in/question-paper-pattern.html
- **UGC-NET Computer Science & Applications (087) — CN practice** — https://www.ugcnetonline.in/syllabus-new.php
- **RPSC Programmer — CN syllabus-based practice** — https://rpsc.rajasthan.gov.in/Syllabus.aspx

## Mapping status

| Exam profile | Subject | Topics | Mapping status | Reference |
|---|---|---|---|---|
| `general-cn-practice` | `cn` | T01, T02, T03, T04, T05, T06, T07 | `subject_scope` | Computer Network/data/cn_questions.json |
| `gate-cs` | `cn` | T01, T02, T03, T04, T05, T06, T07 | `suggested_practice_fit` | Computer Network/Reports/EXAM_BLUEPRINTS.md (historic secondary-source snapshot; official pattern not reverified) |
| `ugc-net-cs-087` | `cn` | T01, T02, T03, T04, T05, T06, T07 | `suggested_practice_fit` | Computer Network/Reports/EXAM_BLUEPRINTS.md (historic secondary-source snapshot; official syllabus/pattern not reverified) |
| `rpsc-programmer` | `cn` | T01, T02, T03, T04, T05, T06, T07 | `suggested_practice_fit` | Computer Network/Past Papers/RPSC Programmer 2024 Paper-1/README-source.md (community-maintained source; not an official key) |
| `rsmssb-informatics-assistant` | `cn` | T01, T02, T03, T04, T05, T06, T07 | `suggested_practice_fit` | Computer Network/Reports/SOURCE_REGISTER.md (source labels/difficulty-derived tags; not official syllabus mapping) |
| `ssc-computer-awareness` | `cn` | T01, T02, T03, T04, T05, T06, T07 | `suggested_practice_fit` | Computer Network/Reports/SOURCE_REGISTER.md (source labels/difficulty-derived tags; not official syllabus mapping) |

GATE CN practice does not implement MSQ/NAT or a complete paper. UGC-NET, RPSC Programmer, Informatics Assistant and SSC rows are subject/segment practice only. Do not infer an exam's duration, section splits, negative marking or official PYQ coverage from these profiles.
