# ECE 449 — Intelligent Systems Engineering  
## Group Project: Kessler Fuzzy Control Agent (Fall 2026)

**Due (final):** Monday Dec. 7, 2026, 11:59:59pm (confirm on Canvas — assignment text also mentions Dec. 8)  
**Competition agent freeze (optional):** Friday Nov. 27 / Nov. 28 — use the Canvas “competition” link  
**Teams:** 3 people  
**Submit:** one Python file (`.py`, not a notebook) on Canvas

---

## What you are building

A **fuzzy control agent** for [Kessler](https://github.com/ThalesGroup/kessler-game) (Asteroids), version **2.4.0**, used in the Explainable Fuzzy Challenge (XFC).

Every frame, your controller’s `actions()` method receives the ship state and game state and must return:

| Output | Type | Meaning |
|--------|------|---------|
| `thrust` | float | Acceleration along current heading (m/s²) |
| `turn_rate` | float | Turn rate (degrees/s) |
| `fire` | bool | Shoot a bullet |
| `drop_mine` | bool | Drop a mine |

You must use a **declarative fuzzy controller** for these outputs. There must be rules that can produce non-zero / meaningful actions for **all four** (not necessarily every frame).

---

## Grading

| Weight | Requirement |
|--------|-------------|
| **75%** | Fuzzy controller that can play the game |
| **15%** | Optimize with a **genetic fuzzy tree** (GA tunes the fuzzy system) |
| **10%** | Defeat `test_controller.py` from Kessler examples |

**Beat-baseline rules (same as optional tournament):** 5 games, unlimited bullets, 3 lives. Winner = higher total score across 5 games; ties broken by average accuracy.

Your agent will be tested on the teaching team’s Kessler install with **scenarios different from the examples**.

---

## Resources (from the assignment)

- Kessler Game GitHub: https://github.com/ThalesGroup/kessler-game/tree/main  
- XFC YouTube: https://www.youtube.com/@fuzzycompetition8326  
- Calculating intercepts in 2D: https://www.youtube.com/watch?v=MpUUsDDE1sI  
- Another Kessler example: https://github.com/xfuzzycomp/KesslerGameExample  
- **Kessler Game Development Manual by Dr. Dick** (Canvas)  
- **Dr. Dick’s Kessler Game Agent** (Canvas)  
- Official fuzzy example in repo: `examples/scott_dick_controller.py`, `examples/test_controller_fuzzy.py`

---

## Step-by-step (how to actually do this)

### 1. Install Kessler 2.4.0

```bash
pip install KesslerGame==2.4.0
```

Or download the wheel from PyPI / GitHub releases and `pip install` that file. Details are in Dr. Dick’s development manual on Canvas.

### 2. Get the official examples running

From the Kessler GitHub `examples/` directory, download at least:

- `test_controller.py` — trivial spinner/shooter (the agent you must beat)
- `scenario_test.py` — runs the game
- `graphics_both.py` — graphics helper used by the example (or use Tkinter-only settings)

Run the example until you see the spinner ship working. **This is step one in the assignment — do this before designing fuzzy rules.**

### 3. Study Dr. Dick’s agent

On Canvas: development manual + his sample agent.  
It uses fuzzy logic for **turn_rate** and **fire** toward the closest asteroid. It is **not** a full solution:

- thrust is always zero (ship never moves)  
- no mines  

Your project must control **thrust, turn_rate, fire, and drop_mine**.

Also look at `examples/scott_dick_controller.py` / `test_controller_fuzzy.py` on GitHub.

### 4. Write your controller

Subclass `KesslerController` and implement `actions(ship_state, game_state)` so it returns the four controls from a **fuzzy inference system** (e.g. scikit-fuzzy).

Suggested build order:

1. Fuzzy aim + fire (extend Dick’s approach)  
2. Fuzzy thrust (move / dodge — needed to survive)  
3. Fuzzy mines (rules that can drop mines when appropriate)  
4. Optional: lead/intercept aiming (see the YouTube link)

Keep `actions()` fast — it is called every simulation step.

### 5. Genetic optimization (for the 15%)

Encode fuzzy parameters (membership function edges, gains, thresholds, etc.) as a genome. Evolve them with a GA (e.g. DEAP). Fitness = performance in Kessler with graphics off / trainer environment (score, deaths, etc.).

Bake the best parameters into the controller you submit.

### 6. Verify you beat `test_controller.py`

Run head-to-head under tournament-style settings: 5 games, unlimited ammo, 3 lives. Win on total score (accuracy breaks ties).

Do **not** only test the single 10-asteroid example map — graders use different scenarios.

### 7. Submit

- **Final:** one `.py` controller on the Canvas lecture submission before the deadline  
- **Competition (optional):** separate Canvas link; freeze by the competition deadline. You may keep improving for final submit, but competition agents cannot be updated after the freeze  

---

## Optional competition

- Offline round-robin (pools), then live Round of 16  
- Live event: Friday Dec. 4 / Dec. 5, 5–9pm (assignment text varies — check Canvas/room)  
- Format: 5 games head-to-head, Thales test scenarios, unlimited bullets, 3 lives  
- Extra credit: 1st = 3 pts, 2nd = 2 pts, 3rd = 1 pt on final grade  

---

## Team tips (lightweight)

- One shared controller file is enough; Canvas only wants one `.py`  
- One person: aim/fire fuzzy; one: thrust/mines; one: GA + eval vs baseline  
- Trust **Canvas** for exact dates if the PDF conflicts with itself  

---

## Checklist before submit

- [ ] Fuzzy (declarative) control — not only hard-coded if/else  
- [ ] Rules exist for thrust, turn_rate, fire, drop_mine  
- [ ] GA optimization done and best params in the submitted agent  
- [ ] Beats `test_controller.py` under 5-game tournament rules  
- [ ] Single `.py` uploaded to Canvas (competition copy uploaded separately if entering)
