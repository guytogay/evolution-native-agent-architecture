# Operational Cue Index — Current

Status: `CURRENT / OPERATIONAL_ROUTER`

Use this when the Agent knows the problem but not the ENA mechanism.

| Cue / failure | Route first |
|---|---|
| stored knowledge cannot be found/trusted | `OA-RET-01` Retrieval |
| raw incidents accumulate without competence | `OA-MEM-01` Memory Metabolism |
| compaction may omit decision-material lineage | `OA-PROJ-01` Projection |
| silence/timeout/unknown callback | `OA-WAIT-01` WAIT / `OA-EFF-01` Effect |
| consequential permission/mandate | `OA-AUTH-01` Authority |
| external retry/restart may duplicate effect | `OA-EFF-01` Effect Lifecycle |
| restore/checkpoint then resume | `OA-REC-01` Recovery |
| worker changed but obligation remains | `OA-COM-01` Commitment/Settlement |
| same-Agent question | `OA-ID-01` Purpose-relative continuity |
| durable purpose/value/refusal/self-definition changes | `OA-AUTHOR-01` Authorship |
| material objection/correction | `OA-STAND-01` Standing Input |
| correlated agreement/evidence applicability | `OA-EVID-01` Evidence |
| failure/success/discovery suggests change | `OA-EVO-01` Evolution |
| idea/correction may disappear with the session | `OA-EVO-01` Evolution -> `procedures/EVOLUTION-LOOP.md` signal/inbox |
| Agent asks "how do I improve/evolve myself?" | `OA-EVO-01` Evolution -> `procedures/EVOLUTION-LOOP.md` |
| self-change has no before/after measurement | `OA-EVO-01` Evolution -> baseline/evidence step |
| change was tried but no retain/reject/unknown decision exists | `OA-EVO-01` Evolution -> local selection step |
| latent candidates accumulate but are never revisited | `OA-EVO-01` Evolution -> wake/review step; `OA-ECO-01` if the loop itself is stale |
| adaptation sharing/import | `OA-MIG-01` Migration/Commons |
| safeguard may be stale | `OA-ECO-01` Ecology/Control Retirement |
| components/Agents interact and outcome may change | `OA-EVO-01` + composition check |
| rules exist but are not salient at runtime | `OA-RT-01` Runtime routing |
| adoption/language/package question | `OA-ADOPT-01` Adoption |
| ENA was adopted but no Host-local mechanisms were considered | `OA-ADOPT-01` Adoption -> bounded local operationalization pass; route concrete gaps to the relevant HOW |

After selecting a route:

`CUE-INDEX -> HOW-MAP -> REFERENCE-INDEX -> exact mechanism`

For evolution specifically:

`signal/idea -> OA-EVO-01 -> procedures/EVOLUTION-LOOP.md -> Host-native inbox/trial/baseline/selection/wake implementation`.

A cue match is not applicability proof. If another mechanism cannot plausibly change the decision, stop adding governance or evolution machinery.
