"""
Configuración general del Bot de Farmeo para Forza Horizon
Modifica estos valores según tus preferencias y tiempos de carga.
"""

# Duración total de la sesión en horas (ej: 8.0 para 8 horas, 0.5 para media hora de prueba)
TOTAL_HOURS = 8.0

# Tiempo (en segundos) que se mantiene presionado el freno de mano (E-brake)
EBRAKE_HOLD_SECONDS = 30.0

# Botón del freno de mano en tu configuración de Forza:
# En Forza Horizon por defecto:
# - Configuración estándar: 'A'
# - Configuración alternativa: 'X' o 'B'
EBRAKE_BUTTON = 'A'

# Tiempo para avanzar lentamente hacia la pendiente/obstáculo antes del freno de mano
DRIVE_FORWARD_SECONDS = 3.5

# Intensidad del acelerador para ir despacio (0.0 a 1.0)
THROTTLE_PERCENT = 0.45

# --- TIEMPOS DE ESPERA Y CARGA (en segundos) ---
# Se recomienda usar números generosos para evitar desincronizaciones por lag de carga

# Tiempo entre cada pulsación de botón en los menús
MENU_STEP_DELAY = 0.8

# Tiempo de espera mientras carga la carrera de EventLab
RACE_LOADING_DELAY = 16.0

# Tiempo de espera para la cuenta regresiva antes de que empiece la carrera (3... 2... 1... YA)
RACE_COUNTDOWN_DELAY = 4.0

# Tiempo de espera mientras carga la salida de regreso al Mundo Libre
FREEROAM_LOADING_DELAY = 18.0

# Variación aleatoria de tiempo (segundos) para evitar detección por patrones idénticos
ENABLE_HUMAN_JITTER = True
JITTER_MIN = 0.1
JITTER_MAX = 0.4

# Tecla de emergencia en el teclado para detener el bot en cualquier momento
EMERGENCY_STOP_KEY = 'f10'
