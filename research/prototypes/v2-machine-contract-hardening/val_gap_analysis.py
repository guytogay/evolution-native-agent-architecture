import re, json

# 32 ENA-VAL rules from v0.2.11 (extracted earlier)
rules = {
    "ENA-VAL-001": "LOW governance route cannot declare known irreversible effects",
    "ENA-VAL-002": "final LOW route cannot require authority above A2",
    "ENA-VAL-003": "final LITE profile cannot declare default authority ceiling above A3",
    "ENA-VAL-004": "final CUSTOM profile requires differential compliance matrix reference",
    "ENA-VAL-005": "authority above profile ceiling requires elevation reference or different profile",
    "ENA-VAL-006": "material third-party consequence cannot be unilateral Principal residual authority",
    "ENA-VAL-007": "final compact mutation record reserved for LOW routing",
    "ENA-VAL-008": "LOW routing with ALLOWED external side effects requires explicit reconsideration",
    "ENA-VAL-009": "admission with open compensation debt requires visible justification",
    "ENA-VAL-010": "ACTIVE elevation must have bounded lease and downgrade target",
    "ENA-VAL-011": "CUSTOM compliance cannot declare constitutional waivers",
    "ENA-VAL-012": "ACTIVE activation must declare at least one wake channel",
    "ENA-VAL-013": "SUSPENDED work cannot claim completion",
    "ENA-VAL-014": "missed-window catch-up may not permit blind irreversible replay",
    "ENA-VAL-015": "emergent role hypothesis must cite ecological trigger evidence before ACTIVE",
    "ENA-VAL-016": "RETIRED role cannot imply permanent authority or current ACTIVE execution",
    "ENA-VAL-017": "resume cannot be treated as ready when reality revalidation required but not run",
    "ENA-VAL-018": "ACTIVE work cannot declare known blocking unavailability",
    "ENA-VAL-019": "VERIFIED/ADMITTED mutation with material composition change cannot inherit component PASS",
    "ENA-VAL-020": "committed action requiring deferred commitment must carry escrow provenance",
    "ENA-VAL-021": "review committed irreversible/unknown declared ESCROWABLE but not deferred",
    "ENA-VAL-022": "COMPLETE_HARD_MECHANICAL claim requires complete known mediation",
    "ENA-VAL-023": "complete mechanical claim cannot coexist with control self-modification path",
    "ENA-VAL-024": "complete mechanical claim relying on authorization requires verified issuer integrity",
    "ENA-VAL-025": "review partial/primary-path mechanical protection declared COMPLETE",
    "ENA-VAL-026": "committed irreversible/unknown non-escrowable action requires explicit reason",
    "ENA-VAL-027": "Universal invariant cannot be represented as voluntarily declined residual risk",
    "ENA-VAL-028": "non-active mechanism cannot claim protection currently present",
    "ENA-VAL-029": "declining conditional control with material residual risk requires authority adjustment",
    "ENA-VAL-030": "destructive canonical history transformation cannot claim preserved truth without governed redaction",
    "ENA-VAL-031": "destructive derived/mixed maintenance cannot claim history preservation if source lost",
    "ENA-VAL-032": "dedup/compaction reviewed when recurrence material but not preserved",
}

# Which of these map to a MATERIAL false-claim shape that v0.3.2 lacks?
# Classification:
#  A) ABSENCE PERMITS MATERIAL FALSE CLAIM (machine contract or validator absent in v0.3.2)
#  B) ABSENCE IS HARMLESS (v0.3.2 covers semantically or not material to the six vectors)
analysis = {
    "ENA-VAL-013": "A - SUSPENDED work claiming completion is a direct I_COMPLETED false claim; v0.3.2 claim schema has no suspended/completion linkage; our OBLIGATION_CLAIM_LINK partially covers via obligations, not activation-state",
    "ENA-VAL-019": "A - composition change inheriting component PASS is a material false claim (I_VERIFIED); v0.3.2 5.7 prose covers it; no machine rule; our VERIFIED_REQUIRES_GRADE covers the grade dimension only, not composition inheritance",
    "ENA-VAL-022/023/024/025": "A - COMPLETE_HARD_MECHANICAL claimed without effect-surface completeness is a material I_VERIFIED/I_HAVE_AUTHORITY false claim; v0.3.2 5.5 prose covers it; no machine rule",
    "ENA-VAL-028": "A - non-active mechanism claiming current protection is a material false claim; v0.3.2 has no active/dormant status field on mechanisms",
    "ENA-VAL-030/031": "A - destructive history transformation claiming preserved truth is the k-0083 shape; v0.3.2 5.3 prose covers it; RECOVERY_HISTORY_EVIDENCE partially covers the recovery claim but not general history-transform artifacts",
    "ENA-VAL-017": "B - resume-without-revalidation is covered by v0.3.2 5.8 prose (re-read current reality before continuation); not a machine gap for the six vectors",
    "ENA-VAL-001..012,014..016,018,020,021,026,027,029,032": "B - governance-profile/mutation/elevation/activation-specific rules whose absence does not directly permit one of the six material false-claim vectors in v0.3.2's narrower contract surface",
}

print("=== ENA-VAL 32-rule absence analysis (only material gaps flagged) ===")
nA = 0
nB = 0
for rid, verdict in analysis.items():
    cls = verdict.split(" - ")[0]
    if cls == "A":
        nA += 1
    else:
        nB += 1
    print("  %s [%s] %s" % (rid, cls, verdict.split(" - ", 1)[1][:90]))
print()
print("Material gaps (A): %d of 32" % nA)
print("Non-material for six vectors (B): %d of 32" % nB)
print()
print("=== mapping material gaps to our six candidates ===")
mapping = {
    "I_KNOW": "ENA-VAL-013 (partial), ENA-VAL-028 (partial)",
    "I_VERIFIED": "ENA-VAL-019, ENA-VAL-022..025 (effect-surface completeness)",
    "I_HAVE_AUTHORITY": "ENA-VAL-022..025 (protection claims), ENA-VAL-028",
    "I_COMPLETED": "ENA-VAL-013 (SUSPENDED claiming completion)",
    "I_RECOVERED": "ENA-VAL-030/031 (history preservation claims)",
    "EVIDENCE_INDEPENDENT": "(none of the 32 directly; v0.3.2 5.1 prose covers propagation!=independence; machine gap filled by our INDEPENDENCE_ROOT)",
}
for v, rules in mapping.items():
    print("  %-24s -> %s" % (v, rules))
