"""
Modelo de Preguntas
"""

import json
import os

class Question:
    """Representa una pregunta del quiz."""
    
    def __init__(self, text, options, correct_answer, category="General"):
        self.text = text
        self.options = options  # Lista de 4 opciones
        self.correct_answer = correct_answer  # Índice (0-3)
        self.category = category
    
    def to_dict(self):
        """Convierte a diccionario (sin revelar la respuesta)."""
        return {
            'text': self.text,
            'options': self.options,
            'category': self.category
        }


class QuestionBank:
    """Banco de preguntas del quiz."""
    
    def __init__(self):
        self.questions = self._load_questions()
    
    def _load_questions(self):
        """Carga preguntas desde archivo JSON."""
        filepath = os.path.join(
            os.path.dirname(__file__), '..', 'data', 'questions.json'
        )
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [
                    Question(
                        text=q['text'],
                        options=q['options'],
                        correct_answer=q['answer'],
                        category=q.get('category', 'General')
                    )
                    for q in data
                ]
        except FileNotFoundError:
            return self._default_questions()
    
    def _default_questions(self):
        """Preguntas por defecto si no se encuentra el JSON."""
        return [
            Question(
                "¿Cuál es la PRIMERA etapa de la metodología según Cairo?",
                ["Codificación", "Análisis del problema", "Pruebas", "Documentación"],
                1,
                "Metodología (Angel)"
            ),
            Question(
                "¿Qué estructura se usa cuando las iteraciones son CONOCIDAS?",
                ["MIENTRAS (WHILE)", "REPETIR (FOR)", "SI...ENTONCES", "HACER-MIENTRAS"],
                1,
                "Estructuras (Andriy)"
            ),
            Question(
                "¿Qué símbolo de diagrama de flujo representa una DECISIÓN?",
                ["Rectángulo", "Paralelogramo", "Rombo", "Óvalo"],
                2,
                "Representación (David)"
            ),
            Question(
                "En Python, ¿cómo se traduce 'Leer NUM' de Cairo?",
                ["print(NUM)", "NUM = input()", "NUM <- input()", "read(NUM)"],
                1,
                "Codificación (David)"
            ),
            Question(
                "¿Cuál es el error MÁS PELIGROSO porque no muestra aviso?",
                ["Error de sintaxis", "Error de ejecución", "Error lógico", "Error de compilación"],
                2,
                "Pruebas (Kendrick)"
            ),
            Question(
                "¿Qué delimitador usa Cairo para comentarios?",
                ["// comentario", "<!-- -->", "{ comentario }", "# comentario"],
                2,
                "Documentación (Kendrick)"
            ),
            Question(
                "¿Qué tipo de mantenimiento aplica cuando cambian requerimientos?",
                ["Correctivo", "Adaptativo", "Perfectivo", "Preventivo"],
                1,
                "Mantenimiento (Carlos)"
            ),
        ]
    
    def get_question(self, index):
        """Obtiene una pregunta por índice."""
        if 0 <= index < len(self.questions):
            return self.questions[index]
        return None
    
    def total(self):
        """Retorna el total de preguntas."""
        return len(self.questions)