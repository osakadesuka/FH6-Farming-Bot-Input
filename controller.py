import time
import random
import config

try:
    import vgamepad as vg
except ImportError:
    vg = None

class VirtualController:
    def __init__(self):
        if vg is None:
            raise RuntimeError(
                "La librería 'vgamepad' no está instalada o el driver ViGEmBus no ha finalizado. "
                "Asegúrate de completar la instalación."
            )
        self.gamepad = vg.VX360Gamepad()
        
        self.BUTTON_MAP = {
            'A': vg.XUSB_BUTTON.XUSB_GAMEPAD_A,
            'B': vg.XUSB_BUTTON.XUSB_GAMEPAD_B,
            'X': vg.XUSB_BUTTON.XUSB_GAMEPAD_X,
            'Y': vg.XUSB_BUTTON.XUSB_GAMEPAD_Y,
            'START': vg.XUSB_BUTTON.XUSB_GAMEPAD_START,
            'BACK': vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK,
            'LB': vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER,
            'RB': vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER,
            'UP': vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP,
            'DOWN': vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN,
            'LEFT': vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT,
            'RIGHT': vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT,
        }

    def _apply_jitter(self, base_delay: float) -> float:
        """Añade una micro-variación humana a los tiempos de espera."""
        if config.ENABLE_HUMAN_JITTER:
            jitter = random.uniform(config.JITTER_MIN, config.JITTER_MAX)
            return max(0.05, base_delay + jitter)
        return base_delay

    def press_button(self, button_name: str, duration: float = 0.12, post_delay: float = None):
        """Presiona y suelta un botón con duración controlada."""
        btn = self.BUTTON_MAP.get(button_name.upper())
        if not btn:
            raise ValueError(f"Botón desconocido: {button_name}")
        
        self.gamepad.press_button(button=btn)
        self.gamepad.update()
        time.sleep(duration)
        
        self.gamepad.release_button(button=btn)
        self.gamepad.update()
        
        delay = post_delay if post_delay is not None else config.MENU_STEP_DELAY
        time.sleep(self._apply_jitter(delay))

    def hold_button(self, button_name: str):
        """Mantiene presionado un botón."""
        btn = self.BUTTON_MAP.get(button_name.upper())
        if not btn:
            raise ValueError(f"Botón desconocido: {button_name}")
        self.gamepad.press_button(button=btn)
        self.gamepad.update()

    def release_button(self, button_name: str):
        """Suelta un botón."""
        btn = self.BUTTON_MAP.get(button_name.upper())
        if not btn:
            raise ValueError(f"Botón desconocido: {button_name}")
        self.gamepad.release_button(button=btn)
        self.gamepad.update()

    def set_throttle(self, value: float):
        """Aplica acelerador con el gatillo derecho (RT) de 0.0 a 1.0."""
        clamped = max(0.0, min(1.0, value))
        self.gamepad.right_trigger_float(value_float=clamped)
        self.gamepad.update()

    def reset_all(self):
        """Libera todos los botones y gatillos a su estado neutro."""
        self.gamepad.reset()
        self.gamepad.update()
