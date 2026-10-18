"""
LIMITADOR DE PETICIONES (Anti-spam)
Kahoot Offline - Equipo 6 FCFM
"""

from collections import defaultdict
import time

class RateLimiter:
    """Limita la cantidad de peticiones por IP."""
    
    def __init__(self, max_requests=10, window_seconds=1):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = defaultdict(list)
    
    def is_allowed(self, identifier):
        """Verifica si la petición está permitida."""
        now = time.time()
        
        # Limpiar peticiones viejas
        self.requests[identifier] = [
            t for t in self.requests[identifier]
            if now - t < self.window_seconds
        ]
        
        if len(self.requests[identifier]) >= self.max_requests:
            return False
        
        self.requests[identifier].append(now)
        return True