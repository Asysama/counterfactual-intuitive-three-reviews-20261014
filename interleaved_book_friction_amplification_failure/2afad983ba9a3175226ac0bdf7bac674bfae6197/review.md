# Generator contributor review — interleaved_book_friction_amplification_failure

**Decision: PASS (contributor self-check; Sara review pending).**
Reviewed head: `2afad983ba9a3175226ac0bdf7bac674bfae6197`. [Source PR](https://github.com/hipo-dev/counterfactual-data/pull/674). [Review HTML](https://asysama.github.io/counterfactual-intuitive-three-reviews-20261014/interleaved_book_friction_amplification_failure/2afad983ba9a3175226ac0bdf7bac674bfae6197/index.html).
Generator correctness: PASS. Runtime-provenance scope: NEW/REPLACEMENT. Runtime provenance: PASS.
Declared-target scale readiness: PASS for 100,000 accepted static profiles. Production readiness: PRODUCTION READY under the declared reduced model and tested parameter domain.
Exactly two accepted native rendered cases, seeds 42 and 98, were audited completely; this is not a claim that 100,000 videos have been rendered.

## Blocking findings

None outstanding at this exact head. Any source or evidence change invalidates this decision until re-audited. The current source fixes supersede earlier candidate renders; only the head-bound formal material linked here is accepted.

## Six-gate result

| Check | Result | Evidence |
|---|---|---|
| Output contract | PASS | Native 2048×2048, H.264, 24 fps, 120 frames, 5 s; all eight streams independently decoded. Exact RGB {0,255} binary masks. |
| Violating-object-only mask | PASS | Target: right booklet, spine, shoes and eyelet. Explicit identity whitelist and independently rerendered masks; shadows excluded. |
| Real scaling | PASS | Six independent axes, 13 controlled recipes × four 768² probe images; two diverse native cases; canonical 100k audit. |
| Official unpatched environment | PASS | Clean committed standalone generator; official Python3.11/bpy4.5.3/numpy1.26.4/Pillow11.3/imageio-ffmpeg0.6/pytest8.4.2/scipy1.16.2. |
| Decoded matched control | PASS | Every native RGB frame preceding intervention is exactly equal; mask begins at the first changed frame. |
| Semantic consistency | PASS | 交错纸页的张力诱导法向力放大阻止抽离；CF 仅移除法向力放大，保留边界库仑摩擦，右侧纸册滑出并由挡块停止 |

## Production-quality behavioral baseline

| Check | Result | Evidence |
|---|---|---|
| True completes its prompt | PASS | 交错纸页的张力诱导法向力放大阻止抽离 |
| Exactly one CF error | PASS | 仅移除法向力放大，保留边界库仑摩擦，右侧纸册滑出并由挡块停止 |
| Both prompts independently align | PASS | Each repeats the objects, setup and event; sampled nuisance details are omitted. Prompt files and metadata match. |
| Matched setup and correct branch roles | PASS | Independent physical trajectory witnesses, exact decoded prefix and visual review of both cases. |
| Geometry, continuity, contacts and final visibility | PASS | Native identity/projection and geometry checks plus actual-browser first/evidence/final inspection; connected supports remain continuous. |
| Completion and observation tail | PASS | Both five-second clips show their completed outcomes and retain targets in view. |
| Source and guides | PASS | Mechanical supports/heater/rope are named accurately. No detached arrows, beams or floating guides. |
| Independent phenomenon checks | PASS | Measurements below; boundary physics independently tested over 13 recipes; 112 runtime profiles checked. |

## Timebase and playback integrity

| Check | Result | Evidence |
|---|---|---|
| Time mapping | PASS | Outer solver steps per recorded frame=40; dt=1/(24×40) s, physical seconds per video second=1.0, identical in both branches. RK4 internal stages do not add time. |
| Event and completion timing | PASS | Independent first-change/mask/evidence checks and full decoded final frames; actual Chrome playback and seeking pass. |
| Simulator claim | NOT APPLICABLE | Blender is the renderer. Dynamics use a disclosed custom reduced physical model; no native-contact/material-engine claim. |

## Semantic matrix

| Title/directory | README | True prompt | CF prompt | Scoring | Operator | Rendered behavior | Result |
|---|---|---|---|---|---|---|---|
| `interleaved_book_friction_amplification_failure` | Declared reduced model | 交错纸页的张力诱导法向力放大阻止抽离 | 仅移除法向力放大，保留边界库仑摩擦，右侧纸册滑出并由挡块停止 | Independent trajectory and visible event predicates | Exactly the term stated above | Both accepted cases and their final frames agree | PASS |

## Independent measurements

- `interleaved_book_friction_amplification_failure_00000042`: first changed frame 24, minimum target border 569 px; physical witnesses: `{"independent_integral_amplification": 8.185080088713132, "normal_force_parameter": 2.747733333333333, "load_N": 6.089699586002569, "threshold_N": 9.822096106455756, "true_final_displacement": 0.0, "cf_final_displacement": 0.3008, "minimum_leaf_gap_m": 3.072e-05, "evidence_frame": 37}`.
- `interleaved_book_friction_amplification_failure_00000098`: first changed frame 28, minimum target border 601 px; physical witnesses: `{"independent_integral_amplification": 2.963526858523965, "normal_force_parameter": 1.4959304347826086, "load_N": 2.2048639827418297, "threshold_N": 3.556232230228758, "true_final_displacement": 0.0, "cf_final_displacement": 0.2444, "minimum_leaf_gap_m": 2.496e-05, "evidence_frame": 52}`.

## Successful-render runtime provenance

| Check | Result | Evidence |
|---|---|---|
| Case-to-witness mapping | PASS | Each of the two cases maps exactly once to a successful clean-head witness; expected count=2. |
| Runtime completeness | PASS | Actual interpreter/packages, dependency-lock hashes, Linux/driver/TeslaT4 headless NVIDIA OpenGL renderer and FFmpeg are retained in the successful witness and component records. |
| Artifact inventory | PASS | Every delivered formal manifest size and SHA-256 checked locally and against the runtime inventory; native release asset digests match. |
| Independent reproduction | PASS | Seed42 rerendered at this exact head through a new successful witness. Recipe/trajectories and all 120 decoded frame hashes of all four streams are identical. |
| Failed runs | PASS | Failed software-render attempts and superseded candidates preserved separately; excluded from accepted mapping. |

## Client-facing artifact consistency

| Check | Result | Evidence |
|---|---|---|
| Browser playback and seek | PASS | All eight delivered streams played to ended in actual Chrome. Start, evidence and frame119 seeking checked; no media errors, blank/channel-swapped/green or magenta output. |
| Mask and overlay presentation | PASS | Browser mask: white object on black. Single red overlay convention. Native off-mask pixels exactly match CF and no target shadows are included. |
| Derivative disclosure | PASS | 1024² H.264 browser derivatives explicitly review-only. RGB/overlay are lossy; grayscale browser mask independently decoded binary. Native lossless RGB originals remain authoritative. |

## Scale-readiness result

| Check | Result | Evidence |
|---|---|---|
| Declared population | PASS | 100,000 static seeds accepted (100%); 100,000 distinct effective signatures/profile IDs; 1,000,000 profile space. No smaller-target exception. |
| Axes and bucket coverage | PASS | length, response, onset, depth, appearance, view; all buckets covered (1.0 per axis), no static rejections or rejection collapse. Gravity fixed at9.81. |
| Rendered axis wiring | PASS | 13 controlled baseline/low/high recipes; 52 actual768² rendered probe frames trace final specs and per-axis pixel effects. These are diversity probes, not formal2048 acceptance. |
| Runtime boundaries | PASS | 16 physical corners +96 distributed profiles pass; independent13-boundary physical audit. |
| Pair nuisance sharing and prompts | PASS | Setup/material/camera/time mapping shared within a pair; no seed/profile labels in prompts. |
| Sharding, quota and safe resume | PASS | Eight shard streams tested disjoint; accepted quota and rejection logging; complete manifest-backed resume succeeds and incompatible quota refuses. |
| Fail-closed validation | PASS | Runtime trajectory and decoded audits run before acceptance; formal two-case output and independent audits pass. |

## Commands and artifacts checked

- Official `pytest`: 19 passed; compile and generate `--help` passed.
- Canonical `standards/cgc_v1/audit_scaling_contract.py`, 100000 profiles: PASS.
- Runtime witness audit and accepted index (2 cases), decoded independent native and browser-media audits: PASS.
- Reproduce/compare seed42, decoded exact-frame independent comparison: PASS.
- [Successful witness](https://asysama.github.io/counterfactual-intuitive-three-reviews-20261014/interleaved_book_friction_amplification_failure/2afad983ba9a3175226ac0bdf7bac674bfae6197/runtime-witness.json), [accepted index](https://asysama.github.io/counterfactual-intuitive-three-reviews-20261014/interleaved_book_friction_amplification_failure/2afad983ba9a3175226ac0bdf7bac674bfae6197/runtime-witness-index.json).
- [Independent native audit](https://asysama.github.io/counterfactual-intuitive-three-reviews-20261014/interleaved_book_friction_amplification_failure/2afad983ba9a3175226ac0bdf7bac674bfae6197/review-evidence/independent-audit-final.json), [geometry/identity audit](https://asysama.github.io/counterfactual-intuitive-three-reviews-20261014/interleaved_book_friction_amplification_failure/2afad983ba9a3175226ac0bdf7bac674bfae6197/review-evidence/native-inspection/identity-projection-audit.json).
- [Reproduction audit](https://asysama.github.io/counterfactual-intuitive-three-reviews-20261014/interleaved_book_friction_amplification_failure/2afad983ba9a3175226ac0bdf7bac674bfae6197/review-evidence/reproduction-independent-final.json), [actual Chrome receipt](https://asysama.github.io/counterfactual-intuitive-three-reviews-20261014/interleaved_book_friction_amplification_failure/2afad983ba9a3175226ac0bdf7bac674bfae6197/review-evidence/interleaved_book_friction_amplification_failure-chrome-playback.json).
- [All native URLs and SHA-256](https://asysama.github.io/counterfactual-intuitive-three-reviews-20261014/interleaved_book_friction_amplification_failure/2afad983ba9a3175226ac0bdf7bac674bfae6197/external-native-media.json), [packet manifest](https://asysama.github.io/counterfactual-intuitive-three-reviews-20261014/interleaved_book_friction_amplification_failure/2afad983ba9a3175226ac0bdf7bac674bfae6197/packet-manifest.json).

## Re-review requirements

Sara's independent review remains pending. Do not infer Sara approval from contributor PASS. Any head change requires updated renders/provenance, independent checks and review packet. This review does not authorize merge or submit an application. No Sara form has been filled or submitted.
