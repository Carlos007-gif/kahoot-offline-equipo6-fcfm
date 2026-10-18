"""
═══════════════════════════════════════════════════════════════
APLICACIÓN PRINCIPAL - FLASK + SOCKETIO
Kahoot Offline - Equipo 6 FCFM
═══════════════════════════════════════════════════════════════
"""

from flask import Flask, render_template
from flask_socketio import SocketIO
from config.settings import Config

def create_app():
    """
    Crea y configura la aplicación Flask.
    
    Retorna:
        tuple: (app, socketio)
    """
    # Crear app Flask
    app = Flask(
        __name__,
        template_folder='../frontend/templates',
        static_folder='../frontend/static'
    )
    
    # Configuración
    app.config['SECRET_KEY'] = Config.SECRET_KEY
    
    # Crear SocketIO
    socketio = SocketIO(
        app,
        cors_allowed_origins="*",  # Permitir conexiones locales
        async_mode='eventlet'
    )
    
    # ═══════════════════════════════════════════════════════
    # RUTAS HTTP
    # ═══════════════════════════════════════════════════════
    
    @app.route('/')
    def host_panel():
        """Panel de control del presentador (host)."""
        return render_template('index.html')
    
    @app.route('/play')
    def player_lobby():
        """Sala de espera para jugadores."""
        return render_template('lobby.html')
    
    @app.route('/game')
    def game_screen():
        """Pantalla de juego para jugadores."""
        return render_template('game.html')
    
    @app.route('/results')
    def results_screen():
        """Pantalla de resultados."""
        return render_template('results.html')
    
    return app, socketio