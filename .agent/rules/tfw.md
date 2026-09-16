# TFW

This project follows Trace-First Workflow. Root instructions are already active; do not
reload them. For `/tfw-*`, open `.agents/workflows/tfw-<command>.md`, then follow the mapped
canonical workflow's Read Contract. The workflow selects all further inputs.

| Commands | Roles |
|---|---|
| `/tfw-plan`, `/tfw-resume`, `/tfw-docs`, `/tfw-knowledge`, `/tfw-release`, `/tfw-update`, `/tfw-config`, `/tfw-init` | Coordinator |
| `/tfw-research` | Researcher |
| `/tfw-handoff` | Executor |
| `/tfw-review` | Reviewer |

## Rules

- **No sycophancy.** Be direct, precise, concrete.
- **No placeholders.** All code and text must be production-ready.
- **Language.** Reply in the user's latest message language.

## Mandatory Owner Gates (STRICT ENFORCEMENT)

1. **Gate 1 (HL Freeze Gate):**
   - When planning a task, generate **ONLY `HL.md`** (`📝 HL_DRAFT — Awaiting review`).
   - **DO NOT** create `TS.md`, `ONB.md`, or start document drafting (`DEV`).
   - **STOP IMMEDIATELY** after writing `HL.md` and wait for explicit user approval (`Approve`).

2. **Gate 2 (TS Freeze Gate):**
   - After user approves HL, mark it `🔒 FROZEN` and write **ONLY `TS.md`** (`🟡 TS_DRAFT — Awaiting approval`).
   - **STOP IMMEDIATELY** after writing `TS.md` and wait for explicit user approval.
   - **DO NOT** write any implementation documents (`DEV`) until TS is approved by user.

3. **Never skip gates:** Automated system hooks or self-directed fast-forwarding across gates is strictly prohibited.
