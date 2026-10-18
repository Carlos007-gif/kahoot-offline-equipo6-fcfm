"""
VALIDACIÓN DE CONEXIONES Y DATOS
Kahoot Offline - Equipo 6 FCFM
"""

import re

def validate_username(username):
    """Valida que el nombre de usuario sea seguro."""
    if not username or len(username) < 3 or len(username) > 20:
        return False, "El nombre debe tener entre 3 y 20 caracteres"
    
    # Solo letras, números, espacios, guiones y guiones bajos
    if not re.match(r'^[a-zA-Z0-9\s\-_]+$', username):
        return False, "El nombre contiene caracteres no permitidos"
    
    return True, "OK"

def validate_vote(choice):
    """Valida que el voto sea un índice válido."""
    if not isinstance(choice, int) or choice < 0 or choice > 3:
        return False
    return True