"""
═══════════════════════════════════════════════════════════════
PUNTO DE ENTRADA DEL SERVIDOR
Kahoot Offline - Equipo 6 FCFM UANL
═══════════════════════════════════════════════════════════════
Ejecutar: python run.py
═══════════════════════════════════════════════════════════════
"""

from backend.app import create_app
from backend.socketio_events import register_events
from config.settings import Config
import socket

def get_local_ip():
    """Obtiene la IP local del servidor."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def print_banner(local_ip):
    """Muestra el banner de inicio del servidor."""
    print()
    print("═" * 60)
    print("🎮 KAHOOT OFFLINE - EQUIPO 6 FCFM UANL")
    print("═" * 60)
    print(f"")
    print(f"   📡 Servidor activo en:")
    print(f"      Local:   http://localhost:{Config.PORT}")
    print(f"      Red:     http://{local_ip}:{Config.PORT}")
    print(f"      Jugadores: http://{local_ip}:{Config.PORT}/play")
    print(f"")
    print(f"   📶 Red WiFi: {Config.HOTSPOT_NAME}")
    print(f"   👥 Máximo jugadores: {Config.MAX_PLAYERS}")
    print(f"   ⏱️  Tiempo por pregunta: {Config.TIME_PER_QUESTION}s")
    print(f"")
    print(f"   🔒 MODO OFFLINE - Sin conexión a internet")
    print(f"   🛡️  Red local aislada (Air-gapped)")
    print(f"")
    print("═" * 60)
    print("   Presiona Ctrl+C para detener el servidor")
    print("═" * 60)
    print()

if __name__ == '__main__':
    # Crear aplicación
    app, socketio = create_app()
    
    # Registrar eventos WebSocket
    register_events(socketio)
    
    # Obtener IP local
    local_ip = get_local_ip()
    
    # Mostrar banner
    print_banner(local_ip)
    
    # Ejecutar servidor
    socketio.run(
        app,
        host=Config.HOST,
        port=Config.PORT,
        debug=Config.DEBUG
    )