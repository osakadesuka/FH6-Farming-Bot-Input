import time
import config
from controller import VirtualController

class FarmSequence:
    def __init__(self, controller: VirtualController):
        self.pad = controller

    def step_open_menu_and_start_race(self):
        """
        1. Abre el menú de pausa desde el mundo libre.
        2. Navega al evento en EventLab (Favoritos).
        3. Entra a la carrera e inicia la carga.
        
        NOTA: Puedes ajustar esta secuencia de botones según la pestaña
        donde tengas guardado tu mapa.
        """
        print("[1/5] Abriendo menú de pausa...")
        self.pad.press_button('START', duration=0.15, post_delay=1.5)

        print("[2/5] Navegando al evento en EventLab / Favoritos...")
        # Ejemplo: Cambiar de pestaña al Hub Creativo / EventLab
        # Ajusta estos toques según tu menú exacto en Forza:
        self.pad.press_button('RB', post_delay=0.8)
        self.pad.press_button('RB', post_delay=0.8)
        self.pad.press_button('A', post_delay=1.2)   # Entra a EventLab
        self.pad.press_button('A', post_delay=1.5)   # Selecciona la primera carrera guardada

        print("[3/5] Confirmando inicio de carrera...")
        # Confirmar en solitario (Solo) e iniciar carrera
        self.pad.press_button('A', post_delay=1.0)
        self.pad.press_button('A', post_delay=1.0)

        # Espera de pantalla de carga y cuenta regresiva
        print(f"      Esperando carga de la carrera ({config.RACE_LOADING_DELAY}s)...")
        time.sleep(config.RACE_LOADING_DELAY)
        
        print(f"      Esperando cuenta regresiva de inicio ({config.RACE_COUNTDOWN_DELAY}s)...")
        time.sleep(config.RACE_COUNTDOWN_DELAY)

    def step_drive_and_ebrake(self):
        """
        4. El coche avanza lentamente hacia el obstáculo / rampa.
        5. Al chocar contra la pendiente, mantiene presionado el freno de mano por 30s.
        """
        print(f"[4/5] Avanzando despacio hacia el obstáculo ({config.DRIVE_FORWARD_SECONDS}s)...")
        self.pad.set_throttle(config.THROTTLE_PERCENT)
        time.sleep(config.DRIVE_FORWARD_SECONDS)

        # Suelta el acelerador
        self.pad.set_throttle(0.0)

        print(f"      Manteniendo freno de mano ({config.EBRAKE_BUTTON}) durante {config.EBRAKE_HOLD_SECONDS}s...")
        self.pad.hold_button(config.EBRAKE_BUTTON)
        time.sleep(config.EBRAKE_HOLD_SECONDS)
        self.pad.release_button(config.EBRAKE_BUTTON)
        print("      Freno de mano liberado.")

    def step_accept_rewards_and_exit(self):
        """
        6. Acepta las pantallas de recompensas, XP y podio.
        7. Espera la pantalla de carga para regresar al mundo libre.
        """
        print("[5/5] Aceptando recompensas y saliendo al mundo libre...")
        
        # Secuencia de pulsar 'A' con pausas para avanzar los menús de fin de carrera
        for i in range(4):
            time.sleep(1.2)
            self.pad.press_button('A', post_delay=1.0)

        print(f"      Esperando carga de regreso al Mundo Libre ({config.FREEROAM_LOADING_DELAY}s)...")
        time.sleep(config.FREEROAM_LOADING_DELAY)
        print("      ¡Ciclo completado con éxito! Listo para la siguiente vuelta.\n")

    def run_one_cycle(self):
        """Ejecuta una vuelta completa del proceso."""
        self.step_open_menu_and_start_race()
        self.step_drive_and_ebrake()
        self.step_accept_rewards_and_exit()
