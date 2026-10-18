"""
Modelo del Jugador
"""

class Player:
    """Representa a un jugador en el quiz."""
    
    def __init__(self, username):
        self.username = username
        self.score = 0
        self.has_voted = False
        self.correct_answers = 0
        self.total_answers = 0
    
    def add_points(self, points):
        """Agrega puntos al jugador."""
        self.score += points
        self.correct_answers += 1
        self.total_answers += 1
    
    def mark_voted(self):
        """Marca que el jugador ya votó en esta pregunta."""
        self.has_voted = True
    
    def reset_vote(self):
        """Resetea el estado de voto para nueva pregunta."""
        self.has_voted = False
    
    def to_dict(self):
        """Convierte a diccionario."""
        return {
            'username': self.username,
            'score': self.score,
            'correct_answers': self.correct_answers,
            'total_answers': self.total_answers
        }