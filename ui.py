import tkinter as tk
from timer import Timer

class OverlayUI:
    def __init__(self):
        self.timer = Timer()
        self.root = tk.Tk()
        self.root.title("Phasmophobia Timer")
        
        # Configurar la ventana
        self.root.geometry("300x100")  # Tamaño aumentado para la nueva fuente
        self.root.attributes("-topmost", True)
        self.root.overrideredirect(True)
        self.root.configure(bg='black')
        self.root.attributes("-alpha", 0.8)
        
        # Centrar la ventana en la parte superior de la pantalla
        self.center_window()

        # Ajustar la fuente a "italic" y "bold" con un peso menor
        self.label = tk.Label(self.root, text="00:00", font=("Arial", 48, "italic bold"), fg="#d3d3d3", bg="black")
        self.label.pack(expand=True)

        # Llamar al método de actualización de tiempo cada 100ms
        self.update_clock()

    def center_window(self):
        # Obtener el tamaño de la ventana
        window_width = 300
        window_height = 100

        # Obtener el tamaño de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calcular la posición de la ventana para que esté centrada horizontalmente y en la parte superior verticalmente
        x = (screen_width // 2) - (window_width // 2)
        y = 0  # Posición vertical en la parte superior de la pantalla

        # Configurar la geometría de la ventana
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def update_clock(self):
        self.label.config(text=self.timer.format_time())
        self.root.update_idletasks()
        # Llama a sí misma después de 100 ms
        self.root.after(100, self.update_clock)

    def update_display(self):
        self.label.config(text=self.timer.format_time())
        self.root.update_idletasks()

    def close(self):
        self.root.quit()  # Cierra el mainloop y termina la aplicación

    def run(self):
        self.root.mainloop()
