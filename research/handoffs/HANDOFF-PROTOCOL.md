# ENA Project Handoff Protocol

Status: `CANONICAL_HANDOFF_FRAMEWORK / MAIN_VISIBLE / NOT_ENA_CURRENT`

ENA must survive replacement of the current conversational Agent without forcing the human to reconstruct project state or method.

The important correction from recent use is that **not every continuation deserves the same amount of handoff machinery**.

```text
PROJECT_CONTINUITY > SESSION_CONTINUITY
HANDOFF_DEPTH SHOULD MATCH CONTINUITY RISK
FRESH_VALIDATION != PROJECT_MANAGER_SUCCESSION
```

## 1. Three transfer modes

### A. Normal continuation — default

Use when `NOW.md` plus the directly relevant artifact/Issue is enough to continue correctly.

Receiver normally:

1. reads `NOW.md`;
2. reads the task-relevant Issue/file;
3. verifies Current only if the decision depends on Current identity;
4. retrieves deeper history only when it can change the decision;
5. starts useful work.

Do **not** require a full handoff record, branch census, master-plan reread, or repository audit merely because a session changed.

### B. Deep project/session succession

Use when losing the current session would materially risk losing:

- a long decision chain;
- active experimental design/oracle;
- important rejected approaches;
- repo-ecosystem boundaries;
- unresolved branches of reasoning;
- project method learned during the session;
- a complex next action that cannot be reconstructed cheaply.

This is the mode used by the 2026-09-03 succession because the session contains several rounds of evolutionary-memory research, cleanroom experiments, branch cleanup, and cross-repo method work.

A deep handoff should be detailed enough that the next Agent can continue without asking the user to replay the session, but it should still link to durable source artifacts instead of copying the whole repository.

### C. Fresh independent validation

Optimize in the opposite direction.

The validator should receive a structurally isolated target/task surface with minimal author-shaped context.

Do **not** give the validator the deep project-manager handoff before its independent first response.

```text
PROJECT_MANAGER_SUCCESSION -> PRESERVE RELEVANT CONTEXT
FRESH_VALIDATOR -> REMOVE CONTAMINATING CONTEXT
```

## 2. Handoff framework vs occurrence record

Reusable succession rules live under `research/handoffs/`.

One deep succession occurrence lives under:

`research/handoffs/records/<handoff-id>/`

Reusable method discovered during the occurrence must be promoted to:

- this protocol;
- `PROJECT-MANAGEMENT-DISCIPLINE.md`; or
- `research/methodology/`.

Do not make every dated record another permanent policy layer.

## 3. Deep outgoing protocol

Before declaring a deep succession ready:

1. **Persist material work**
   - conclusions;
   - negative/null results;
   - active hypotheses;
   - experimental oracle/design;
   - rejected approaches likely to be retried;
   - unmerged unique artifacts.

2. **Reverify live reality**
   - `main`;
   - Current if relevant;
   - open PRs that matter;
   - branch uniqueness/cleanup if branch topology is part of the handoff.

3. **Preserve exact immutable identities where they matter**
   - frozen/released objects use exact source/tree/content identity;
   - a mutable branch head is not a frozen identity.

4. **Preserve unresolved variation**
   - compress prose;
   - do not silently delete competing hypotheses, negative results, Host differences, or falsification conditions.

5. **Write the deep record**
   A material record normally contains:
   - `HANDOFF-START-HERE.md`;
   - `HANDOFF-MANIFEST.yaml`;
   - `PROJECT-STATE.md`;
   - `RECENT-THREE-ROUNDS.md`;
   - `FILE-CATALOG.md`;
   - `HANDOFF-READBACK.md`.

   Add focused files such as `LESSONS-AND-REMINDERS.md` or `REPO-ECOSYSTEM.md` when they materially reduce successor error.

6. **Update `CURRENT-HANDOFF.yaml`**
   - point to the latest intended deep record;
   - keep it a router, not a duplicated project encyclopedia.

7. **Integrate and read back**
   - merge via normal PR/review;
   - read the resulting main surfaces as a successor would;
   - correct contradictions that would change the next action.

## 4. Deep incoming protocol

A receiver of a deep handoff should:

1. start from current `main`;
2. read `NOW.md`;
3. read `research/handoffs/CURRENT-HANDOFF.yaml`;
4. follow its `start_here` and manifest;
5. read the project state, recent rounds, repo map, lessons, and file catalog actually linked by that record;
6. reverify mutable live facts before writing;
7. read only the deeper research/method/evidence files needed by the next consequential action;
8. continue without asking the user to repeat durably available project context.

The receiver does **not** need to reread every old handoff record, release reconciliation file, branch inventory generation, or master-plan version.

## 5. Authority hierarchy

When surfaces disagree:

```text
Current identity
  -> releases/current/CURRENT-BASELINE.yaml

Live project/research status
  -> NOW.md on main

Research method
  -> research/methodology/ canonical files

Handoff method
  -> research/handoffs/HANDOFF-PROTOCOL.md

Deep succession router
  -> research/handoffs/CURRENT-HANDOFF.yaml

Handoff record
  -> occurrence projection / bootstrap

Historical plan/progress/branch records
  -> lineage unless current live routing explicitly depends on them

Chat
  -> useful but non-authoritative context
```

## 6. Independent-validation information boundary

A different session/model is not automatically independent if it receives the author's answer shape first.

For fresh cleanroom experiments:

```text
structural isolation
+ identical common substrate across arms
+ only intended treatment/task difference
+ preregistered oracle
+ first complete response captured
-> then author context/adjudication
```

Do not tell a fresh Agent “do not inspect the source repo/research/oracle” when the cleaner design is to make those surfaces absent.

## 7. Completeness test for deep succession

A deep handoff is sufficient when the receiver can answer:

- What is ENA and what is not ENA Current?
- What project phase is active now?
- What did the last experimental rounds actually show, including null/negative results?
- Which hypotheses were narrowed rather than supported?
- What earlier research branches remain validation obligations?
- What is the next falsifiable experiment and what design mistakes must it avoid?
- Which related repositories exist and what are their boundaries?
- Which branches are historical/delete-safe and which unique material had to be rescued?
- What should the receiver **not** redo?

If the receiver must ask the user to reconstruct these, the deep succession failed.

## 8. Normal lifecycle rule

Session replacement is normal maintenance.

> A healthy project can use a tiny handoff most of the time and a deep handoff when continuity risk genuinely warrants it.

The goal is continuity, not handoff document production.
