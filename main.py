import time
import sys
import threading
import config
from controller import VirtualController
from sequence import FarmSequence

# Bandera global para detener el bot inmediatamente
stop_requested = False

def emergency_listener():
    """Escucha la tecla de emergencia para detener el bot en cualquier momento."""
    global stop_requested
    try:
        import keyboard
        while not stop_requested:
            if keyboard.is_pressed(config.EMERGENCY_STOP_KEY):
                print(f"\n[ALERTA] ¡Tecla de emergencia '{config.EMERGENCY_STOP_KEY.upper()}' presionada! Deteniendo el bot...")
                stop_requested = True
                break
            time.sleep(0.1)
    except Exception:
        # Si no se tienen privilegios de hook de teclado, el usuario aún puede usar Ctrl+C
        pass

def main():
    global stop_requested
    print("=" * 65)
    print("      FORZA HORIZON - BOT AUTOMATIZADO DE FARMEO AFK")
    print("=" * 65)
    print(f" * Duración objetivo: {config.TOTAL_HOURS} hora(s)")
    print(f" * Freno de mano: botón '{config.EBRAKE_BUTTON}' durante {config.EBRAKE_HOLD_SECONDS}s")
    print(f" * Tecla de emergencia para parar: [{config.EMERGENCY_STOP_KEY.upper()}] o [Ctrl + C]")
    print("=" * 65)

    try:
        pad = VirtualController()
    except Exception as e:
        print(f"\n[ERROR] No se pudo inicializar el mando virtual:\n{e}")
        return

    # Iniciar hilo de tecla de emergencia
    listener_thread = threading.Thread(target=emergency_listener, daemon=True)
    listener_thread.start()

    sequence = FarmSequence(pad)

    print("\n[!] Tienes 5 segundos para pasar a la ventana de Forza Horizon...")
    for i in range(5, 0, -1):
        print(f"    Iniciando en {i}...")
        time.sleep(1.0)
    print("--> ¡BOT ACTIVO! <--\n")

    start_time = time.time()
    max_duration_seconds = config.TOTAL_HOURS * 3600.0
    cycle_count = 0

    try:
        while not stop_requested:
            elapsed = time.time() - start_time
            if elapsed >= max_duration_seconds:
                print(f"\n[TIEMPO CUMPLIDO] Se completaron las {config.TOTAL_HOURS} horas configuradas.")
                break

            cycle_count += 1
            remaining = max(0, max_duration_seconds - elapsed)
            hours_rem = int(remaining // 3600)
            mins_rem = int((remaining % 3600) // 60)
            
            print(f"--- [CICLO #{cycle_count}] (Tiempo restante: {hours_rem}h {mins_rem}m) ---")
            
            sequence.run_one_cycle()

    except KeyboardInterrupt:
        print("\n[INFO] Bot detenido manualmente por el usuario (Ctrl + C).")
    finally:
        # Asegurarse SIEMPRE de liberar todos los botones del mando virtual
        pad.reset_all()
        print("\n" + "=" * 65)
        print(f" Resumen de la sesión:")
        print(f" * Ciclos completados: {cycle_count}")
        elapsed_mins = (time.time() - start_time) / 60.0
        print(f" * Tiempo total ejecutado: {elapsed_mins:.1f} minutos")
        print(f" * Mando virtual restablecido a neutro.")
        print("=" * 65)

if __name__ == "__main__":
    main()
