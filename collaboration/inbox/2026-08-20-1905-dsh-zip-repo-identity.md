# Persistent Project Contribution

Project: Evolution-Native Agent Architecture (ENA)
Contribution status: `UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED`
Date/time: `2026-08-20T19:05:00+08:00`
Target area: `evidence / field validation / release discipline / distribution channel`
Relationship to existing work: `COUNTEREXAMPLE + PORTABILITY_FINDING`

## Participant provenance

```yaml
participant:
  kind: "DeepSeek Harness"
  runtime_or_model: "deepseek-v4-flash via DeepSeek Harness Web GUI (DSH 0.x local runtime)"
  session_or_run_ref: "session-3b3cd6d7-9ccc-4523-8203-41be2c8b32fb"
  access_surfaces:
    github: "WRITE"
    google_drive: "NONE"
    other: ["Anytype MCP (knowledge base write)"]
  role_this_contribution: "EXPERIMENTER"
```

These fields describe provenance and technical capability, **not project authority**.

Tool access does not authorize Mainline modification, release, deployment, remediation, or scope expansion.

## Observed facts

- Host: `DESKTOP-AI`, Windows 11 (10.0.26200), PowerShell 7.6.5, Python 3.14.7, Node v24.19.0; route: DSH Web GUI → local runtime → pwsh adapters → gh CLI 2.97.0 (authenticated as `guytogay`, scopes gist/read:org/repo/workflow).
- Baseline: ENA v0.3.1-BETA.1, canonical source `releases/current/` @ main `ae3e2958` (user ruling 2026-08-20: repo is canonical; ZIP superseded).
- Anonymous GitHub REST API returns **404** for `guytogay/evolution-native-agent-architecture`. The repo **exists and is PRIVATE** (visibility=PRIVATE; branches `main` and `ena/v0.3.1-beta.1-flat-current` are identical). Authenticated `gh` reads it fully.
- User-provided `ENA-v0.3.1-BETA.1-CURRENT.zip` (SHA256 `A3386425B8F448D5DD32BD4EAE47D4FA1AF4BFE586CA3CEF3E81276205B7C2BD`) was compared against repo `releases/current/` via git blob SHA (git hash-object vs GitHub tree API): **21 corresponding files → 5 BLOB-MATCH, 16 BLOB-DIFF**; repo has **no MANIFEST.sha256** (22 files vs ZIP's 23).
- All 5 schemas are **SEMANTIC-EQUAL** (json.load deep equality; repo = compact formatting, ZIP = expanded formatting). `tools/validate_contracts.py` is behaviorally equal (same input → same output).
- `.md` files differ substantively: repo carries "low-ambiguity" revisions (e.g., `AGENT-ADOPTION-INSTRUCTION.md` gains `## Minimal instruction` + principle blockquote; `05-CORE-OPERATIONAL-CONTRACTS.md` expands bullets; `00-READ-ME-FIRST.md` "This package" → "This document").
- Timeline anomaly: ZIP mtime `2026-08-20T18:46:04+08:00` (=10:46Z) is **later** than repo last commit `10:22:26Z`, yet ZIP content is **older** (no low-ambiguity edits) → ZIP was not built from current main (or its mtime reflects copy/download time).
- `MANIFEST.sha256` shipped inside the ZIP verified 22/22 — yet the ZIP still differs from repo in 16/21 files. The bundled manifest is self-referential: it proves internal consistency, not authority/origin.

## Inference

- **Anonymous 404 on a private repo is an auth-boundary signal, not an existence/access verdict.** A participant using only anonymous probes can wrongly conclude "repo inaccessible / baseline unobtainable" when in fact authenticated access exists on the same host. This is a real near-miss: I initially reported "cannot access" and was corrected by the user pointing at the local authenticated `gh`.
- **A bundled MANIFEST.sha256 does not establish authority.** Our verification is a direct counterexample: manifest PASS (22/22) coexists with 16/21 files differing from the canonical source. The manifest only proves package-internal consistency; authority requires an independent trust anchor (git blob/tree/commit SHAs in-repo, or a manifest published via a separate trusted channel).
- **Two renderings of the same release can silently drift**: the ZIP and the repo directory share `CURRENT-BASELINE.yaml` and version identity yet differ in content. Release discipline should treat "same version number" and "byte-identical artifact" as different claims.

## Suggestion / question

- For distribution-channel robustness: consider whether `releases/current/` should note that anonymous access is impossible (private repo) so adopters know to use authenticated tooling or the user-mediated ZIP path.
- Consider whether the ENA project wants a machine-checkable canonical pointer (e.g., a pinned commit SHA in `CURRENT-BASELINE.yaml` or `PROJECT-HUB.md`) so "current" is resolvable without cloning history.
- No recommendation to add MANIFEST.sha256 to the repo: git SHAs already provide stronger, immutable, independently verifiable integrity + provenance. Bundled manifests add self-referential noise. (Residual value only for transport-corruption detection with a separately-obtained manifest.)

## Evidence references

- `adoption/claims/claim-adopt-001.json` + `support-adopt-001.json` (validator PASS: `SUPPORT_SCOPE_DIRECT_MATCH`) — host workspace `C:\Users\PC\Documents\Deepseek Harness\ENA-v0.3.1-BETA.1\`
- Per-file blob comparison table (git hash-object vs GitHub tree API) — session log
- json.load deep-equality outputs: 5× `SEMANTIC-EQUAL`
- validator behavioral comparison: identical outputs on both copies
- `git diff --no-index` outputs for md files
- Local landing `baseline-repo/` (22 files, 22/22 blob SHA match) — workspace

## Known limitations / unknowns

- Single host, single session, single model binding; no independent replication yet.
- ZIP's true provenance (which commit/source it was built from) is undetermined; history-tree API calls for older SHAs failed on this host.
- Whether the private-repo state is intentional (e.g., pre-release) or incidental is unknown to this participant.

## Triggered follow-up obligations

```yaml
triggered_obligations:
  - obligation_id: "DSH-2026-08-20-OB-01"
    rule_ref: "ENA-CON-004 / 5.1 claim-evidence envelope"
    applicability: "APPLICABLE"
    materiality: "MATERIAL_TO_COMPLETION"
    status: "SATISFIED"
    required_before_claim: "none (adoption claim already validated)"
    evidence_refs: ["support-adopt-001.json"]
    resolution_reason: "Identity claim verified against blob SHAs; user ruling resolved canonical source."
```

## Requested reconciliation

- `ACCEPT_AS_EVIDENCE` of (a) private-repo 404 semantics and (b) bundled-manifest non-authority.
- `ACCEPT_AS_CLARIFICATION` for the distribution-channel note suggestion.

## Authority / implementation note

- `advice only / evidence contributed`. No implementation performed on the repo; no baseline modification; no promotion request.

## Notes

Do not present this contribution as accepted ENA truth merely because it is committed to GitHub.

Preserve the original contribution even after reconciliation.
