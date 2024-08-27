import keyboard

class HotkeyManager:
    def __init__(self, overlay):
        self.overlay = overlay

    def start(self):
        keyboard.add_hotkey('ctrl+e', self.toggle_timer)
        keyboard.add_hotkey('ctrl+r', self.reset_timer)
        keyboard.add_hotkey('ctrl+q', self.close_program)  # Nueva tecla para cerrar el programa

    def toggle_timer(self):
        if self.overlay.timer.running:
            self.overlay.timer.pause()
        else:
            self.overlay.timer.start()
        self.overlay.update_display()

    def reset_timer(self):
        self.overlay.timer.reset()
        self.overlay.update_display()

    def close_program(self):
        self.overlay.close()  # Llama al método close del OverlayUI
