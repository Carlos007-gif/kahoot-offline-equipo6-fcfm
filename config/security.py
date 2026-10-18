"""
═══════════════════════════════════════════════════════════════
CONFIGURACIÓN DE SEGURIDAD
Red local aislada - Sin exposición a internet
═══════════════════════════════════════════════════════════════
"""

class SecurityConfig:
    """Configuración de seguridad del servidor."""
    
    # Red local aislada (air-gapped)
    ALLOWED_NETWORKS = [
        '192.168.0.0/16',    # Red local clase C
        '10.0.0.0/8',        # Red local clase A
        '172.16.0.0/12',     # Red local clase B
    ]
    
    # Límite de conexiones por IP
    MAX_CONNECTIONS_PER_IP = 1
    
    # Rate limiting (peticiones por segundo)
    RATE_LIMIT = '10 per second'
    
    # Validación de nombres de usuario
    MAX_USERNAME_LENGTH = 20
    MIN_USERNAME_LENGTH = 3
    
    # Caracteres permitidos en nombres
    ALLOWED_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 _-'
    
    # Headers de seguridad
    SECURITY_HEADERS = {
        'X-Content-Type-Options': 'nosniff',
        'X-Frame-Options': 'DENY',
        'X-XSS-Protection': '1; mode=block',
    }