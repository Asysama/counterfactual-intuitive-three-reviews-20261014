# Generator contributor review — cam_cleat_load_induced_opening

**Decision: PASS (contributor self-check; Sara review pending).**
Reviewed head: `7b30f6188103dbe5afdbced8bb7d924e3b3dc14a`. [Source PR](https://github.com/hipo-dev/counterfactual-data/pull/673). [Review HTML](https://asysama.github.io/counterfactual-intuitive-three-reviews-20261014/cam_cleat_load_induced_opening/7b30f6188103dbe5afdbced8bb7d924e3b3dc14a/index.html).
Generator correctness: PASS. Runtime-provenance scope: NEW/REPLACEMENT. Runtime provenance: PASS.
Declared-target scale readiness: PASS for 100,000 accepted static profiles. Production readiness: PRODUCTION READY under the declared reduced model and tested parameter domain.
Exactly two accepted native rendered cases, seeds 42 and 98, were audited completely; this is not a claim that 100,000 videos have been rendered.

## Blocking findings

None outstanding at this exact head. Any source or evidence change invalidates this decision until re-audited. The current source fixes supersede earlier candidate renders; only the head-bound formal material linked here is accepted.

## Six-gate result

| Check | Result | Evidence |
|---|---|---|
| Output contract | PASS | Native 2048×2048, H.264, 24 fps, 120 frames, 5 s; all eight streams independently decoded. Exact RGB {0,255} binary masks. |
| Violating-object-only mask | PASS | Target: cam contacts and attached grip markers. Explicit identity whitelist and independently rerendered masks; shadows excluded. |
| Real scaling | PASS | Six independent axes, 13 controlled recipes × four 768² probe images; two diverse native cases; canonical 100k audit. |
| Official unpatched environment | PASS | Clean committed standalone generator; official Python3.11/bpy4.5.3/numpy1.26.4/Pillow11.3/imageio-ffmpeg0.6/pytest8.4.2/scipy1.16.2. |
| Decoded matched control | PASS | Every native RGB frame preceding intervention is exactly equal; mask begins at the first changed frame. |
| Semantic consistency | PASS | 负载使偏心夹轮夹紧绳索，重物停住；CF 仅反转绳索接触力矩，夹轮张开，重物落到托盘 |

## Production-quality behavioral baseline

| Check | Result | Evidence |
|---|---|---|
| True completes its prompt | PASS | 负载使偏心夹轮夹紧绳索，重物停住 |
| Exactly one CF error | PASS | 仅反转绳索接触力矩，夹轮张开，重物落到托盘 |
| Both prompts independently align | PASS | Each repeats the objects, setup and event; sampled nuisance details are omitted. Prompt files and metadata match. |
| Matched setup and correct branch roles | PASS | Independent physical trajectory witnesses, exact decoded prefix and visual review of both cases. |
| Geometry, continuity, contacts and final visibility | PASS | Native identity/projection and geometry checks plus actual-browser playback and first/evidence/final seeking; connected supports remain continuous. |
| Completion and observation tail | PASS | Both five-second clips show their completed outcomes and retain targets in view. |
| Source and guides | PASS | Mechanical supports/heater/rope are named accurately. No detached arrows, beams or floating guides. |
| Independent phenomenon checks | PASS | Measurements below; boundary physics independently tested over 13 recipes; 112 runtime profiles checked. |

## Timebase and playback integrity

| Check | Result | Evidence |
|---|---|---|
| Time mapping | PASS | Outer solver steps per recorded frame=120; dt=1/(24×120) s, physical seconds per video second=1.0, identical in both branches. RK4 internal stages do not add time. |
| Event and completion timing | PASS | Independent first-change/mask/evidence checks and full decoded final frames; actual Chrome playback and seeking pass. |
| Simulator claim | NOT APPLICABLE | Blender is the renderer. Dynamics use a disclosed custom reduced physical model; no native-contact/material-engine claim. |

## Semantic matrix

| Title/directory | README | True prompt | CF prompt | Scoring | Operator | Rendered behavior | Result |
|---|---|---|---|---|---|---|---|
| `cam_cleat_load_induced_opening` | Declared reduced model | 负载使偏心夹轮夹紧绳索，重物停住 | 仅反转绳索接触力矩，夹轮张开，重物落到托盘 | Independent trajectory and visible event predicates | Exactly the term stated above | Both accepted cases and their final frames agree | PASS |

## Visual geometry revision

Cam: machined beveled faces, matched restrained finish and cylindrical weight. Books: pale warm/cool individual leaves, staggered fore-edges and elevated view; actual mesh intersection audit covers all accepted frames with a forced-overlap negative control. Rubber: closed tan loop with an open center and constant material volume; its aggregate axial model is declared explicitly.

## Independent measurements

- `cam_cleat_load_induced_opening_00000042`: first changed frame 24, minimum target border 651 px; physical witnesses: `{"true_energy_max_increase_J": 0.0, "true_final_drop_m": 0.08617377639240734, "true_final_velocity": -0.00016707875374167127, "cf_final_drop_m": 0.44799999999999995, "cf_max_opening_degrees": 3.3575926530457383, "evidence_frame": 28}`.
- `cam_cleat_load_induced_opening_00000098`: first changed frame 28, minimum target border 656 px; physical witnesses: `{"true_energy_max_increase_J": 0.0, "true_final_drop_m": 0.1992254172934545, "true_final_velocity": 0.0, "cf_final_drop_m": 0.3640000000000001, "cf_max_opening_degrees": 4.465432127193034, "evidence_frame": 31}`.

## Successful-render runtime provenance

| Check | Result | Evidence |
|---|---|---|
| Case-to-witness mapping | PASS | Each of the two cases maps exactly once to a successful clean-head witness; expected count=2. |
| Runtime completeness | PASS | Actual interpreter/packages, dependency-lock hashes, Linux/driver/TeslaT4 headless NVIDIA OpenGL renderer and FFmpeg are retained in the successful witness and component records. |
| Artifact inventory | PASS | Every delivered formal manifest size and SHA-256 checked locally and against the runtime inventory; native release asset digests match. |
| Independent reproduction | PASS | Seed42 rerendered at this exact head through a new successful witness. Recipe/trajectories and masks are exact. All 120 decoded frame hashes of all four streams are identical. |
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

- Official `pytest`: 18 passed; compile and generate `--help` passed.
- Canonical `standards/cgc_v1/audit_scaling_contract.py`, 100000 profiles: PASS.
- Runtime witness audit and accepted index (2 cases), decoded independent native and browser-media audits: PASS.
- Reproduce/compare seed42, independent decoded comparison under the recorded tolerance: PASS.
- [Successful witness](https://asysama.github.io/counterfactual-intuitive-three-reviews-20261014/cam_cleat_load_induced_opening/7b30f6188103dbe5afdbced8bb7d924e3b3dc14a/runtime-witness.json), [accepted index](https://asysama.github.io/counterfactual-intuitive-three-reviews-20261014/cam_cleat_load_induced_opening/7b30f6188103dbe5afdbced8bb7d924e3b3dc14a/runtime-witness-index.json).
- [Independent native audit](https://asysama.github.io/counterfactual-intuitive-three-reviews-20261014/cam_cleat_load_induced_opening/7b30f6188103dbe5afdbced8bb7d924e3b3dc14a/review-evidence/independent-audit-v9.json), [geometry/identity audit](https://asysama.github.io/counterfactual-intuitive-three-reviews-20261014/cam_cleat_load_induced_opening/7b30f6188103dbe5afdbced8bb7d924e3b3dc14a/review-evidence/native-inspection/identity-projection-audit.json).
- [Reproduction audit](https://asysama.github.io/counterfactual-intuitive-three-reviews-20261014/cam_cleat_load_induced_opening/7b30f6188103dbe5afdbced8bb7d924e3b3dc14a/review-evidence/reproduction-independent-v9.json), [actual Chrome receipt](https://asysama.github.io/counterfactual-intuitive-three-reviews-20261014/cam_cleat_load_induced_opening/7b30f6188103dbe5afdbced8bb7d924e3b3dc14a/review-evidence/cam_cleat_load_induced_opening-chrome-playback-v9.json).
- [All native URLs and SHA-256](https://asysama.github.io/counterfactual-intuitive-three-reviews-20261014/cam_cleat_load_induced_opening/7b30f6188103dbe5afdbced8bb7d924e3b3dc14a/external-native-media.json), [packet manifest](https://asysama.github.io/counterfactual-intuitive-three-reviews-20261014/cam_cleat_load_induced_opening/7b30f6188103dbe5afdbced8bb7d924e3b3dc14a/packet-manifest.json).

## Re-review requirements

Sara's independent review remains pending. Do not infer Sara approval from contributor PASS. Any head change requires updated renders/provenance, independent checks and review packet. This review does not authorize merge or submit an application. No Sara form has been filled or submitted.
