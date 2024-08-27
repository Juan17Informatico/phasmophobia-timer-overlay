from ui import OverlayUI
from hotkeys import HotkeyManager

def main():
    # Iniciar la interfaz de usuario
    overlay = OverlayUI()

    # Configurar y activar las teclas de acceso rápido
    hotkeys = HotkeyManager(overlay)
    hotkeys.start()

    # Iniciar el loop de la interfaz gráfica
    overlay.run()

if __name__ == "__main__":
    main()
