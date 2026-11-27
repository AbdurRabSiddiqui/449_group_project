# Manual keyboard play session for learning Kessler mechanics.

import time

from kesslergame import Scenario, KesslerGame, GraphicsType
from kesslergame.graphics.graphics_base import KesslerGraphics
import kesslergame.graphics.graphics_handler as graphics_handler

# Kessler 2.4.0 bug: graphics_handler references KesslerGraphics at runtime
# but only imports it under TYPE_CHECKING. Patch before using graphics_obj.
graphics_handler.KesslerGraphics = KesslerGraphics

from keyboard_controller import KeyboardController
from graphics_keyboard import KeyboardGraphics


CONTROLS = """
========================================
  KESSLER — KEYBOARD PLAY
========================================
  Click the game window first, then:

  W / Up      thrust forward
  S / Down    thrust reverse
  A / Left    turn left
  D / Right   turn right
  Space       fire
  M / Shift   drop mine
========================================
"""


def main() -> None:
    print(CONTROLS)

    controller = KeyboardController()
    graphics = KeyboardGraphics(
        controller,
        UI_settings={
            "ships": True,
            "lives_remaining": True,
            "accuracy": True,
            "asteroids_hit": True,
            "shots_fired": True,
            "bullets_remaining": True,
            "mines_remaining": True,
            "controller_name": True,
        },
    )

    scenario = Scenario(
        name="Human Practice",
        num_asteroids=8,
        ship_states=[
            {
                "position": (500, 400),
                "angle": 90,
                "lives": 10,
                "team": 1,
                "mines_remaining": 10,
            },
        ],
        map_size=(1000, 800),
        time_limit=180,
        ammo_limit_multiplier=0,
        stop_if_no_ammo=False,
    )

    game_settings = {
        "perf_tracker": False,
        "graphics_type": GraphicsType.Tkinter,
        "realtime_multiplier": 1,
        "graphics_obj": graphics,
        "frequency": 30,
    }

    game = KesslerGame(settings=game_settings)
    pre = time.perf_counter()
    score, _ = game.run(scenario=scenario, controllers=[controller])

    print(f"Scenario eval time: {time.perf_counter() - pre:.2f}s")
    print(score.stop_reason)
    print("Asteroids hit:", [team.asteroids_hit for team in score.teams])
    print("Deaths:", [team.deaths for team in score.teams])
    print("Accuracy:", [team.accuracy for team in score.teams])


if __name__ == "__main__":
    main()
