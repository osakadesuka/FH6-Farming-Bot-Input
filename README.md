# Forza Horizon - Bot de Farmeo AFK

Este bot emula un mando de Xbox mediante software (driver ViGEmBus) para repetir el ciclo de farmeo de manera 100% desatendida.

---

## 📁 Estructura del Proyecto

* **`config.py`**: Todos los ajustes editables (horas de duración, botón del freno de mano, tiempos de carga, etc.).
* **`sequence.py`**: La lógica paso a paso (abrir menú, iniciar carrera, avanzar, mantener freno de mano 30s y salir).
* **`controller.py`**: El controlador virtual de Xbox que envía las señales al juego.
* **`main.py`**: El script principal que inicia el bucle, muestra el progreso en consola y gestiona la tecla de parada de emergencia.
* **`requirements.txt`**: Librerías necesarias de Python.

---

## 🚀 Cómo Usarlo

### 1. Ajustes Previos en el Juego:
* Pon el juego en **Horizon Solo** (Modo un jugador / Offline) para evitar desconexiones de red.
* Guarda el mapa de EventLab en tus **Favoritos**.

### 2. Calibración Inicial:
* Abre `config.py` y pon `TOTAL_HOURS = 0.05` para hacer una prueba corta de 1 o 2 ciclos.
* Verifica en `sequence.py` que los toques de menú (`RB`, `A`, etc.) coincidan exactamente con la posición de tu mapa en tus menús.

### 3. Ejecución:
En la terminal de VS Code en esta carpeta:
```bash
python main.py
```
* Tendrás **5 segundos** para hacer clic en la ventana de Forza Horizon.
* Para detener el bot en cualquier momento, presiona **`F10`** en tu teclado o **`Ctrl + C`** en la terminal.
