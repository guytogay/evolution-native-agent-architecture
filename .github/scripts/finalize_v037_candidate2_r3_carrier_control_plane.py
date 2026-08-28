#!/usr/bin/env python3
"""Finalize candidate.2 isolated-review carrier identity across research control surfaces.

This is a control-plane/method projection only. It must not modify frozen candidate
or Current cargo. It upgrades the active carrier identity from the superseded r3
build (33131665994) to the final manifest-corrected audited build (33131773164).
"""
from pathlib import Path

OLD_RUN = "33131665994"
NEW_RUN = "33131773164"
OLD_AS = "ee80ac827dedff7a8de9d10f0a9cbcd70c66f3b7b885296f9e2335af6ec92131"
NEW_AS = "dfe15a686668440138bfd624453059d61a0b28625bb9a5e0c185b33eccf9c2da"
OLD_AP = "b3e2222c591a2760b976e6791f18e2494c17063ddfe539291f1cd8799fd54bcd"
NEW_AP = "427a1776aea199f5f27c4bea2827d3c827cf82fab2c8cd403da0e8cc1dd97649"
OLD_ARTIFACT = "9670480727"
AS_ARTIFACT = "9670518379"
AP_ARTIFACT = "9670518708"
OLD_OUTER = "104005b329cc042721da76a38f8a41c282c278bca3d2c424ecd7288ceeb1c357"
AS_ACTIONS_DIGEST = "146c15bed53826fe8cce4738540c471127bda7c15cf5616cd20387f7e3567def"
AP_ACTIONS_DIGEST = "d5b2b1d67f300c087d3d3869e4a93148a89d75cb5d3860025bb340bcdc6c65f2"

FILES = [
    Path("research/ACTIVE-RESEARCH.yaml"),
    Path("research/plans/PROGRESS.yaml"),
    Path("research/handoffs/CURRENT-HANDOFF.yaml"),
    Path("research/handoffs/records/2026-08-28-v037-candidate2-isolated-as-capsule-ready/HANDOFF-START-HERE.md"),
    Path("research/handoffs/records/2026-08-28-v037-candidate2-isolated-as-capsule-ready/HANDOFF-MANIFEST.yaml"),
    Path("research/handoffs/records/2026-08-28-v037-candidate2-isolated-as-capsule-ready/PROJECT-STATE.md"),
    Path("research/handoffs/records/2026-08-28-v037-candidate2-isolated-as-capsule-ready/RECENT-THREE-ROUNDS.md"),
    Path("research/handoffs/records/2026-08-28-v037-candidate2-isolated-as-capsule-ready/FILE-CATALOG.md"),
    Path("research/handoffs/records/2026-08-28-v037-candidate2-isolated-as-capsule-ready/HANDOFF-READBACK.md"),
]


def replace_all(text: str, old: str, new: str) -> tuple[str, int]:
    n = text.count(old)
    return text.replace(old, new), n


def main() -> None:
    observed_old_run = 0
    observed_old_as = 0
    observed_old_ap = 0

    for path in FILES:
        if not path.exists():
            raise SystemExit(f"missing expected control-plane file: {path}")
        text = path.read_text(encoding="utf-8")
        text, n = replace_all(text, OLD_RUN, NEW_RUN); observed_old_run += n
        text, n = replace_all(text, OLD_AS, NEW_AS); observed_old_as += n
        text, n = replace_all(text, OLD_AP, NEW_AP); observed_old_ap += n

        # A former combined artifact is no longer the authority. Where a file
        # has a single carrier-artifact field, split it into the two final
        # independently uploaded carrier artifacts.
        text = text.replace(
            f"capsule_artifact_id: {OLD_ARTIFACT}",
            f"a_s_actions_artifact_id: {AS_ARTIFACT}\n  a_p_actions_artifact_id: {AP_ARTIFACT}",
        )
        text = text.replace(
            f"carrier_artifact_id: {OLD_ARTIFACT}",
            f"a_s_actions_artifact_id: {AS_ARTIFACT}\n  a_p_actions_artifact_id: {AP_ARTIFACT}",
        )
        text = text.replace(
            f"capsule_artifact_id: \"{OLD_ARTIFACT}\"",
            f"a_s_actions_artifact_id: \"{AS_ARTIFACT}\"\n  a_p_actions_artifact_id: \"{AP_ARTIFACT}\"",
        )
        text = text.replace(
            f"  artifact_id: {OLD_ARTIFACT}\n  outer_artifact_sha256: {OLD_OUTER}",
            f"  a_s_actions_artifact_id: {AS_ARTIFACT}\n  a_s_actions_artifact_digest: {AS_ACTIONS_DIGEST}\n  a_p_actions_artifact_id: {AP_ARTIFACT}\n  a_p_actions_artifact_digest: {AP_ACTIONS_DIGEST}",
        )
        text = text.replace(
            f"artifact id `{OLD_ARTIFACT}`",
            f"A-S artifact id `{AS_ARTIFACT}` and A-P artifact id `{AP_ARTIFACT}`",
        )
        text = text.replace(OLD_OUTER, f"A-S:{AS_ACTIONS_DIGEST} / A-P:{AP_ACTIONS_DIGEST}")

        # Method-index duplicate created during concurrent repair was reconciled
        # into the already-referenced canonical companion.
        text = text.replace(
            "research/methodology/PHYSICALLY-ISOLATED-INDEPENDENT-REVIEW-CARRIER.md",
            "research/methodology/INDEPENDENT-VALIDATION-CAPSULE-CARRIER.md",
        )
        text = text.replace(
            "collaboration/reconciliation/2026-08-28-v037-candidate2-isolated-review-capsule-r3.md",
            "collaboration/reconciliation/2026-08-28-v037-candidate2-isolated-capsule-intake-reconciliation.md",
        )
        text = text.replace(
            "research/methodology/incidents/2026-08-28-CANDIDATE2-BLIND-CARRIER-LEAK-INCIDENT.md",
            "research/methodology/incidents/2026-08-28-CANDIDATE2-GITHUB-NATURAL-NAVIGATION-PRIMING-INCIDENT.md",
        )

        if path.as_posix() == "research/ACTIVE-RESEARCH.yaml":
            text = text.replace(
                'event: "V0_3_7_CANDIDATE2_EXACT_PREFREEZE_PASS_EXTERNALLY_FROZEN_FRESH_BLIND_REVIEW_WARRANTED"',
                'event: "V0_3_7_CANDIDATE2_ISOLATED_REVIEW_CARRIER_R3_FINALIZED"',
            )
            text = text.replace(
                "  fresh_a_s_intake_ready: true",
                "  isolated_a_s_capsule_ready: true\n  a_s_manifest_payload_count: 78\n  a_p_manifest_payload_count: 119\n  manifest_self_hash_policy: EXCLUDED_BY_DEFINITION",
            )
            needle = "    - fresh independent intake Issue 137 created for validation/v037-c2-blind-semantic-primary"
            if needle in text and "final isolated carrier audit run 33131773164" not in text:
                text = text.replace(
                    needle,
                    needle
                    + "\n    - Issue 137 fresh reviewer correctly aborted before A-S seal after GitHub natural-navigation boundary crossing"
                    + "\n    - final isolated carrier audit run 33131773164 PASS after semantic-vocabulary detector and manifest-inventory corrections",
                )

        if path.as_posix() == "research/plans/PROGRESS.yaml":
            old_block = """current_method_transition:
  id: CANDIDATE_SELF_PRIMING_TO_BLIND_SEMANTIC_VIEW
  target: VALIDATION_INTERFACE_FOR_FROZEN_CANDIDATE1
  result: BLIND_SEMANTIC_VIEW_COMPLETED_A_S_A_P_SEALED_PHASE_B_NEEDS_REVISION
  method: research/methodology/INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md
  incident: research/methodology/incidents/2026-08-27-CANDIDATE-SELF-PRIMING-INCIDENT.md
  reconciliation: collaboration/reconciliation/2026-08-27-v037-candidate1-blind-view-repair.md
  invalid_issue: 128
  completed_issue: 131
  sealed_branch: validation/v037-c1-blind-semantic-primary
  candidate_bytes_changed: false
  candidate2_required_by_method_change: false
  candidate2_required_by_phase_b_defects: true
"""
            new_block = """current_method_transition:
  id: CANDIDATE2_SAME_REPO_BLIND_VIEW_TO_PHYSICALLY_ISOLATED_CARRIER_R3
  target: VALIDATION_INTERFACE_FOR_FROZEN_CANDIDATE2
  result: ISSUE137_ABORTED_INTERFACE_DEFECT_ISOLATED_A_S_CAPSULE_READY_A_P_WITHHELD
  information_boundary_method: research/methodology/INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md
  carrier_method: research/methodology/INDEPENDENT-VALIDATION-CAPSULE-CARRIER.md
  incident: research/methodology/incidents/2026-08-28-CANDIDATE2-GITHUB-NATURAL-NAVIGATION-PRIMING-INCIDENT.md
  reconciliation: collaboration/reconciliation/2026-08-28-v037-candidate2-isolated-capsule-intake-reconciliation.md
  invalidated_issue: 137
  authoritative_carrier_audit_run: 33131773164
  candidate_bytes_changed: false
  current_bytes_changed: false
  manifest_self_hash_policy: EXCLUDED_BY_DEFINITION
  attack_cardinality: OPEN
"""
            if old_block in text:
                text = text.replace(old_block, new_block)

            text = text.replace(
                "  capsule_build_run: 33131773164\n  a_s_capsule_sha256:",
                "  capsule_build_run: 33131773164\n  a_s_manifest_payload_count: 78\n  a_p_manifest_payload_count: 119\n  manifest_self_hash_policy: EXCLUDED_BY_DEFINITION\n  a_s_capsule_sha256:",
                1,
            )

        path.write_text(text, encoding="utf-8")

    if observed_old_run < 3 or observed_old_as < 3 or observed_old_ap < 3:
        raise SystemExit(
            f"expected superseded carrier identity not sufficiently present: "
            f"run={observed_old_run} as={observed_old_as} ap={observed_old_ap}"
        )

    # No superseded active carrier hashes may remain in aligned control surfaces.
    for path in FILES:
        text = path.read_text(encoding="utf-8")
        if OLD_AS in text or OLD_AP in text:
            raise SystemExit(f"superseded active carrier hash remains in {path}")

    print("CANDIDATE2_R3_CARRIER_CONTROL_PLANE_FINALIZATION=PASS")
    print(f"authoritative_run={NEW_RUN}")
    print(f"a_s_sha256={NEW_AS}")
    print(f"a_p_sha256={NEW_AP}")
    print("manifest_self_hash=EXCLUDED_BY_DEFINITION")
    print("attack_cardinality=OPEN")


if __name__ == "__main__":
    main()
