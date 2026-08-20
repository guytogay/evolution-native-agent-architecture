# ADR-001 — Adopt Project-First Persistent Information Architecture

```yaml
project: ena
artifact_type: DECISION
status: ACCEPTED
created_at: "2026-08-20T11:45:00+08:00"
decision_authority: "User explicitly requested restructuring Google Drive and GitHub for multi-Agent/human project collaboration"
related_artifacts:
  - PROJECT-HUB.md
  - PROJECT-METADATA.yaml
  - PROJECT-STRUCTURE.md
  - research/evolution-inbox/README.md
  - "Google Drive: Persistent Project Structure and Naming Standard"
supersedes:
  - "flat ENA artifact placement under ChatGPT Knowledge"
```

## Context

ENA artifacts, collaboration protocols, release packages, research notes, and unrelated knowledge had accumulated in a flat `ChatGPT Knowledge` Drive folder. This caused poor discoverability and participant-specific assumptions. A concrete failure was that the user could not find the ENA Evolution Inbox by searching for `Inbox` because no obvious Drive path/artifact exposed that concept.

At the same time, ENA collaboration had expanded from multiple ChatGPT sessions to heterogeneous participants such as Gemini, OpenClaw, Hermes Agent, DeepSeek Harness, Codex, humans, and bots with access to GitHub, Google Drive, or both.

## Evidence / constraints

- Existing ENA Drive links/file IDs should remain valid where possible.
- GitHub already serves as diff-friendly engineering/research lineage from repository adoption onward.
- Drive is valuable for durable release artifacts, human-readable reports, discovery, Drive-only participants, and recovery anchors.
- Multiple writers should not depend on a single giant shared Inbox file.
- Persistence does not imply synchronization across disconnected surfaces.
- Tool write access must not be confused with project authority.
- Historical layout and old GitHub paths should not be rewritten out of existence merely to make the new structure look older than it is.

## Decision

Adopt a **project-first, participant-neutral Persistent Project Information Architecture**.

### Global Drive

```text
My Drive /
  00 Persistent Collaboration /
  10 Projects /
```

Global collaboration protocol, registry, naming/structure standard, and bootstrap templates live under `00 Persistent Collaboration`.

Long-lived projects live under `10 Projects`, not under folders named after specific Agents/apps.

### ENA Drive root

```text
10 Projects /
  ENA - Evolution-Native Agent Architecture /
    00 Project Hub /
    10 Mainline /
    20 Research /
      00 Evolution Inbox /
      10 Historical Adversarial Replay /
      20 Experiments /
      30 Prototypes /
    30 Evidence /
    40 Releases /
      10 Current /
      90 Archive /
    50 Collaboration /
      10 Inbox /
      20 Reconciliation /
      30 Templates /
    60 Decisions /
    90 Archive /
```

Critical searchable concepts are exposed literally in directory/index names.

### GitHub

- retain `PROJECT-HUB.md` as the stable human/Agent entrypoint;
- add `PROJECT-METADATA.yaml` for machine-readable navigation/state;
- canonical structured Evolution Inbox moves to `research/evolution-inbox/README.md`;
- retain `research/EVOLUTION-INBOX.md` as a compatibility pointer;
- add `CONTRIBUTING.md`, `PROJECT-STRUCTURE.md`, `decisions/`, and semantic Evidence/Release/Collaboration entrypoints.

## Rationale

The project—not a particular Agent/session—is the persistent coordination substrate.

Directory structure provides predictable coarse navigation; Project Hub and machine metadata provide explicit semantics. Independent contribution artifacts reduce multi-writer conflicts. Reconciliation remains separate from source contribution, preserving provenance and disagreement.

The design allows GitHub-only and Drive-only participants to join while exposing surface partition honestly and requiring a bridge/reconciliation participant before claiming cross-surface synchronization.

## Alternatives considered

### Keep `ChatGPT Knowledge` as project root

Benefits:
- no migration work.

Costs/risks:
- participant-specific naming;
- multiple projects become mixed;
- research/release/evidence boundaries remain unclear;
- poor searchability;
- future non-ChatGPT participants inherit misleading structure.

Rejected.

### Organize by participant (`ChatGPT/ENA`, `Gemini/ENA`, etc.)

Benefits:
- simple provenance by folder.

Costs/risks:
- fragments one project into multiple pseudo-projects;
- duplicates canonical state;
- makes reconciliation harder;
- participant replacement breaks continuity.

Rejected.

### Make GitHub and Drive identical mirrors

Benefits:
- superficial structural symmetry.

Costs/risks:
- duplicate living truth;
- binary/release and engineering-source needs differ;
- copy can be mistaken for synchronization;
- unnecessary maintenance cost.

Rejected. Semantic role alignment is preferred over byte-for-byte mirroring.

## Consequences

### Positive

- a participant who knows only `ENA` can discover the project through Registry/Project Hub;
- `Evolution Inbox` is explicitly searchable;
- Mainline, research, evidence, releases, collaboration, decisions, and archive are visually separated;
- Drive-only and GitHub-only participation has declared paths;
- machine-readable `PROJECT-METADATA.yaml` reduces reliance on directory guessing;
- old GitHub Inbox path remains non-breaking via pointer;
- moved Drive files keep existing IDs/links.

### Costs / risks

- some old prose may still reference legacy paths until found and repaired;
- two persistent surfaces require bridge discipline rather than assumed synchronization;
- a directory structure can itself become stale if Project Hub/metadata are not maintained;
- modular v0.2.11 GitHub source expansion remains separate unfinished adoption work (Issue #2).

## Migration / compatibility

- Existing Drive files were **moved rather than copied** where possible, preserving file IDs and links.
- `ChatGPT Knowledge` remains as legacy/general knowledge; it is no longer ENA's project root.
- Old ChatGPT-specific collaboration protocols are archived rather than deleted.
- `research/EVOLUTION-INBOX.md` is retained as a compatibility pointer.
- The migration is an information-architecture change, not an ENA normative semantic revision.

## Authority boundary

This decision authorizes organizing persistent project information and collaboration entrypoints.

It does **not** authorize:

- changing ENA v0.2.11 normative semantics;
- opening v0.2.12;
- promoting research candidates;
- remediating DSH host defects;
- changing evidence truth/status merely because files move;
- treating tool write access as Mainline authority.

## Validation / follow-up

- verify Drive Registry points to the new ENA root;
- verify literal search for `Evolution Inbox` resolves the new index;
- verify current release artifacts are in `40 Releases / 10 Current`;
- verify older/candidate releases are in `40 Releases / 90 Archive`;
- audit GitHub for stale `ChatGPT Knowledge` and old Evolution Inbox path references;
- maintain compatibility pointers where historical consumers may rely on old paths.

## Status history

- `2026-08-20T11:45:00+08:00` — ACCEPTED and migration initiated under explicit user request.
