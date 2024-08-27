import keyboard

class HotkeyManager:
    def __init__(self, overlay):
        self.overlay = overlay

    def start(self):
        keyboard.add_hotkey('F7', self.toggle_timer)
        keyboard.add_hotkey('F8', self.reset_timer)

    def toggle_timer(self):
        if self.overlay.timer.running:
            self.overlay.timer.pause()
        else:
            self.overlay.timer.start()
        self.overlay.update_display()

    def reset_timer(self):
        self.overlay.timer.reset()
        self.overlay.update_display()
