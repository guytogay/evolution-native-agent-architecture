RUN_ID: INT-3
ARM: INT
STATUS: EXCLUDED_PROTOCOL_DEVIANT
REASON: SESSION_CONTINUITY_LOST
VALID_PRIMARY_RUN: NO

Observed protocol history:
- A1 completed in the original fresh ChatGPT Temporary Chat and preserved.
- A2 completed in the same original Temporary Chat and preserved.
- Before A3, the Temporary Chat was accidentally closed and could not be continued.

Frozen relay contract requires all stages A1-A7, B1, and C1 for a run to remain in the same Temporary Chat. Reconstructing continuity in a new session would violate the preregistered protocol. Therefore INT-3 is excluded on objective protocol grounds and is not scored as a primary run.

Replacement action: run INT-R1 from A1 in a new ChatGPT Temporary Chat, preserving the same INT arm order and frozen prompts.
