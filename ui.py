import tkinter as tk
from timer import Timer

class OverlayUI:
    def __init__(self):
        self.timer = Timer()
        self.root = tk.Tk()
        self.root.title("Phasmophobia Timer")
        self.root.geometry("200x50")
        self.root.attributes("-topmost", True)
        self.root.overrideredirect(True)
        self.root.configure(bg='black')
        self.root.attributes("-alpha", 0.7)

        self.label = tk.Label(self.root, text="00:00", font=("Helvetica", 24), fg="white", bg="black")
        self.label.pack(expand=True)

        # Llamar al método de actualización de tiempo cada 100ms
        self.update_clock()

    def update_clock(self):
        self.label.config(text=self.timer.format_time())
        self.root.update_idletasks()
        # Llama a sí misma después de 100 ms
        self.root.after(100, self.update_clock)

    def update_display(self):
        self.label.config(text=self.timer.format_time())
        self.root.update_idletasks()

    def run(self):
        self.root.mainloop()
