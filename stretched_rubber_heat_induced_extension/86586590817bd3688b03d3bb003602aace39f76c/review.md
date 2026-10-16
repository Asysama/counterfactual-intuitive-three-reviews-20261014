# Generator contributor review — stretched_rubber_heat_induced_extension

**Decision: PASS (contributor self-check; Sara review pending).**
Reviewed head: `86586590817bd3688b03d3bb003602aace39f76c`. [Source PR](https://github.com/hipo-dev/counterfactual-data/pull/675). [Review HTML](https://asysama.github.io/counterfactual-intuitive-three-reviews-20261014/stretched_rubber_heat_induced_extension/86586590817bd3688b03d3bb003602aace39f76c/index.html).
Generator correctness: PASS. Runtime-provenance scope: NEW/REPLACEMENT. Runtime provenance: PASS.
Declared-target scale readiness: PASS for 100,000 accepted static profiles. Production readiness: PRODUCTION READY under the declared reduced model and tested parameter domain.
Exactly two accepted native rendered cases, seeds 42 and 98, were audited completely; this is not a claim that 100,000 videos have been rendered.

## Blocking findings

None outstanding at this exact head. Any source or evidence change invalidates this decision until re-audited. The current source fixes supersede earlier candidate renders; only the head-bound formal material linked here is accepted.

## Six-gate result

| Check | Result | Evidence |
|---|---|---|
| Output contract | PASS | Native 2048×2048, H.264, 24 fps, 120 frames, 5 s; all eight streams independently decoded. Exact RGB {0,255} binary masks. |
| Violating-object-only mask | PASS | Target: closed rubber loop only. Explicit identity whitelist and independently rerendered masks; shadows excluded. |
| Real scaling | PASS | Six independent axes, 13 controlled recipes × four 768² probe images; two diverse native cases; canonical 100k audit. |
| Official unpatched environment | PASS | Clean committed standalone generator; official Python3.11/bpy4.5.3/numpy1.26.4/Pillow11.3/imageio-ffmpeg0.6/pytest8.4.2/scipy1.16.2. |
| Decoded matched control | PASS | Every native RGB frame preceding intervention is exactly equal; mask begins at the first changed frame. |
| Semantic consistency | PASS | 恒定重物拉伸的闭环橡皮筋均匀受热后收缩并提起重物；CF 仅将熵弹性温度因子 T 改为 T0²/T，闭环橡皮筋伸长、重物下降 |

## Production-quality behavioral baseline

| Check | Result | Evidence |
|---|---|---|
| True completes its prompt | PASS | 恒定重物拉伸的闭环橡皮筋均匀受热后收缩并提起重物 |
| Exactly one CF error | PASS | 仅将熵弹性温度因子 T 改为 T0²/T，闭环橡皮筋伸长、重物下降 |
| Both prompts independently align | PASS | Each repeats the objects, setup and event; sampled nuisance details are omitted. Prompt files and metadata match. |
| Matched setup and correct branch roles | PASS | Independent physical trajectory witnesses, exact decoded prefix and visual review of both cases. |
| Geometry, continuity, contacts and final visibility | PASS | Native identity/projection and geometry checks plus actual-browser playback and first/evidence/final seeking; connected supports remain continuous. |
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
| `stretched_rubber_heat_induced_extension` | Declared reduced model | 恒定重物拉伸的闭环橡皮筋均匀受热后收缩并提起重物 | 仅将熵弹性温度因子 T 改为 T0²/T，闭环橡皮筋伸长、重物下降 | Independent trajectory and visible event predicates | Exactly the term stated above | Both accepted cases and their final frames agree | PASS |

## Visual geometry revision

Cam: machined beveled faces, matched restrained finish and cylindrical weight. Books: pale warm/cool individual leaves, staggered fore-edges and elevated view; actual mesh intersection audit covers all accepted frames with a forced-overlap negative control. Rubber: closed tan loop with an open center and constant material volume; its aggregate axial model is declared explicitly.

## Independent measurements

- `stretched_rubber_heat_induced_extension_00000042`: first changed frame 24, minimum target border 430 px; physical witnesses: `{"independent_ode_errors_m": [2.5912605394751154e-12, 1.4235279621743757e-12], "true_final_length": 1.0978889988139606, "cf_final_length": 1.4196316187397173, "initial_length": 1.2427614814814814, "final_temperature_kelvin": 343.64121684671, "evidence_frame": 35}`.
- `stretched_rubber_heat_induced_extension_00000098`: first changed frame 28, minimum target border 433 px; physical witnesses: `{"independent_ode_errors_m": [5.513256517986065e-12, 3.055555808373356e-12], "true_final_length": 0.6298208443220215, "cf_final_length": 0.8660088895015624, "initial_length": 0.7307993333333334, "final_temperature_kelvin": 363.03239146232073, "evidence_frame": 37}`.

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

- Official `pytest`: 19 passed; compile and generate `--help` passed.
- Canonical `standards/cgc_v1/audit_scaling_contract.py`, 100000 profiles: PASS.
- Runtime witness audit and accepted index (2 cases), decoded independent native and browser-media audits: PASS.
- Reproduce/compare seed42, independent decoded comparison under the recorded tolerance: PASS.
- [Successful witness](https://asysama.github.io/counterfactual-intuitive-three-reviews-20261014/stretched_rubber_heat_induced_extension/86586590817bd3688b03d3bb003602aace39f76c/runtime-witness.json), [accepted index](https://asysama.github.io/counterfactual-intuitive-three-reviews-20261014/stretched_rubber_heat_induced_extension/86586590817bd3688b03d3bb003602aace39f76c/runtime-witness-index.json).
- [Independent native audit](https://asysama.github.io/counterfactual-intuitive-three-reviews-20261014/stretched_rubber_heat_induced_extension/86586590817bd3688b03d3bb003602aace39f76c/review-evidence/independent-audit-v9.json), [geometry/identity audit](https://asysama.github.io/counterfactual-intuitive-three-reviews-20261014/stretched_rubber_heat_induced_extension/86586590817bd3688b03d3bb003602aace39f76c/review-evidence/native-inspection/identity-projection-audit.json).
- [Reproduction audit](https://asysama.github.io/counterfactual-intuitive-three-reviews-20261014/stretched_rubber_heat_induced_extension/86586590817bd3688b03d3bb003602aace39f76c/review-evidence/reproduction-independent-v9.json), [actual Chrome receipt](https://asysama.github.io/counterfactual-intuitive-three-reviews-20261014/stretched_rubber_heat_induced_extension/86586590817bd3688b03d3bb003602aace39f76c/review-evidence/stretched_rubber_heat_induced_extension-chrome-playback-v9.json).
- [All native URLs and SHA-256](https://asysama.github.io/counterfactual-intuitive-three-reviews-20261014/stretched_rubber_heat_induced_extension/86586590817bd3688b03d3bb003602aace39f76c/external-native-media.json), [packet manifest](https://asysama.github.io/counterfactual-intuitive-three-reviews-20261014/stretched_rubber_heat_induced_extension/86586590817bd3688b03d3bb003602aace39f76c/packet-manifest.json).

## Re-review requirements

Sara's independent review remains pending. Do not infer Sara approval from contributor PASS. Any head change requires updated renders/provenance, independent checks and review packet. This review does not authorize merge or submit an application. No Sara form has been filled or submitted.
