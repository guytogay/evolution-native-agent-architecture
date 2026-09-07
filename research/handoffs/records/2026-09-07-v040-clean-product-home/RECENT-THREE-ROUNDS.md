# Recent Three Rounds

## Round 1 — Product/project contamination identified
The owner corrected the maintainer for copying build-quality instructions into ENA itself. The owner used the exam-paper analogy: instructions such as keeping the paper clean belong in how the student works, not in the answer. This exposed a broader boundary error between ENA product content and ENA-maintainer/session instructions.

## Round 2 — Legacy ENA recognized as structurally contaminated
The owner described legacy ENA as a tree that has grown around an inserted coin: project/session-management material may now be embedded inside terminology, distinctions, workflows, and architecture. The maintainer therefore stopped treating legacy ENA as the v0.4 design source. The correct order became clean derivation first, legacy regression checking second.

The legacy repository then received a first cleanup pass: obsolete root project-management files were removed or archived, the root README was shortened, collaboration machinery was demoted, and the legacy semantic coverage ledger was moved out of the active rebuild root.

## Round 3 — Clean product repository + Field Guide consolidation
The owner created `guytogay/ENA` as a new public empty repository. It was accepted as the clean product home for the next ENA and initialized only with a minimal README.

The owner and maintainer then re-evaluated `guytogay/ena-field-guide`. The old split between ENA theory and a separate practical HOW repository was judged unnecessary for the new product direction. Field Guide is to stop independent evolution; useful HOW/evidence such as PR #6 may be recovered into the new ENA after independent value judgment, then the repository can be archived.

The owner explicitly required this consensus to be thoroughly carried forward so later succession cannot silently drift back to the old structure.
