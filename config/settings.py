"""
═══════════════════════════════════════════════════════════════
CONFIGURACIÓN GENERAL DEL SERVIDOR
Kahoot Offline - Equipo 6 FCFM
═══════════════════════════════════════════════════════════════
"""

import os

class Config:
    """Configuración base del servidor."""
    
    # Servidor
    HOST = '0.0.0.0'          # Escuchar en todas las interfaces
    PORT = 5000               # Puerto del servidor
    DEBUG = False             # Modo debug (False en producción)
    
    # Seguridad
    SECRET_KEY = os.environ.get('SECRET_KEY', 'fcfm_equipo6_z04_2024_secure')
    
    # Juego
    MAX_PLAYERS = 50          # Máximo de jugadores simultáneos
    TIME_PER_QUESTION = 30    # Segundos por pregunta
    POINTS_PER_CORRECT = 10   # Puntos por respuesta correcta
    POINTS_BONUS_SPEED = 5    # Puntos extra por velocidad
    
    # Red
    HOTSPOT_NAME = 'FCFM_Equipo6_SECURE'
    
    # Preguntas
    QUESTIONS_FILE = 'backend/data/questions.json'
    
    # Categorias de preguntas (temas del Equipo 6)
    CATEGORIES = [
        "Metodología (Angel)",
        "Estructuras (Andriy)",
        "Representación (David)",
        "Codificación (David)",
        "Pruebas (Kendrick)",
        "Documentación (Kendrick)",
        "Mantenimiento (Carlos)"
    ]