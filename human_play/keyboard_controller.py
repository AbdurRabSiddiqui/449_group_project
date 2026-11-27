# Keyboard controller for manually playing Kessler.

from typing import Dict, Tuple, Set

from kesslergame import KesslerController


class KeyboardController(KesslerController):
    """
    Controls:
      W / Up arrow     - thrust forward
      S / Down arrow   - thrust reverse
      A / Left arrow   - turn left
      D / Right arrow  - turn right
      Space            - fire
      M / Shift_L      - drop mine
    """

    THRUST = 240.0
    TURN_RATE = 120.0

    def __init__(self) -> None:
        self._pressed: Set[str] = set()

    def on_key_press(self, event) -> None:
        key = event.keysym
        self._pressed.add(key)

    def on_key_release(self, event) -> None:
        key = event.keysym
        self._pressed.discard(key)

    def clear_keys(self, _event=None) -> None:
        self._pressed.clear()

    def actions(self, ship_state: Dict, game_state: Dict) -> Tuple[float, float, bool, bool]:
        thrust = 0.0
        turn_rate = 0.0

        if self._pressed & {"w", "W", "Up"}:
            thrust += self.THRUST
        if self._pressed & {"s", "S", "Down"}:
            thrust -= self.THRUST
        if self._pressed & {"a", "A", "Left"}:
            turn_rate += self.TURN_RATE
        if self._pressed & {"d", "D", "Right"}:
            turn_rate -= self.TURN_RATE

        fire = "space" in self._pressed
        drop_mine = bool(self._pressed & {"m", "M", "Shift_L", "Shift_R"})

        return thrust, turn_rate, fire, drop_mine

    @property
    def name(self) -> str:
        return "Keyboard"
