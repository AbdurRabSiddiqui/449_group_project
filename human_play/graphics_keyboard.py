# Tkinter graphics wrapper that routes keyboard events to KeyboardController.

from kesslergame.graphics.graphics_tk import GraphicsTK

from keyboard_controller import KeyboardController


class KeyboardGraphics(GraphicsTK):
    def __init__(self, controller: KeyboardController, UI_settings=None) -> None:
        super().__init__(UI_settings)
        self.controller = controller

    def start(self, scenario) -> None:
        super().start(scenario)
        self.window.title("Kessler — Keyboard Play")
        self.window.bind("<KeyPress>", self.controller.on_key_press)
        self.window.bind("<KeyRelease>", self.controller.on_key_release)
        self.window.bind("<FocusOut>", self.controller.clear_keys)
        self.window.focus_force()
