"""
═══════════════════════════════════════════════════════════════
EVENTOS WEBSOCKET (TIEMPO REAL)
Kahoot Offline - Equipo 6 FCFM
═══════════════════════════════════════════════════════════════
"""

import json
import time
from flask_socketio import emit, broadcast
from backend.models.player import Player
from backend.models.question import QuestionBank

# Estado global del juego
players = {}
question_bank = QuestionBank()
current_question_index = -1
game_active = False
question_start_time = 0


def register_events(socketio):
    """Registra todos los eventos de SocketIO."""
    
    # ═══════════════════════════════════════════════════════
    # EVENTO: Jugador se une
    # ═══════════════════════════════════════════════════════
    @socketio.on('join')
    def on_join(data):
        global players
        
        username = data.get('username', '').strip()
        
        # Validar nombre
        if len(username) < 3 or len(username) > 20:
            emit('error', {'message': 'Nombre debe tener 3-20 caracteres'})
            return
        
        if username in players:
            emit('error', {'message': 'Ese nombre ya está en uso'})
            return
        
        # Crear jugador
        players[username] = Player(username)
        
        # Notificar a todos
        emit('player_joined', {'username': username}, broadcast=True)
        emit('player_count', len(players), broadcast=True)
        emit('player_list', list(players.keys()), broadcast=True)
    
    # ═══════════════════════════════════════════════════════
    # EVENTO: Iniciar juego (solo el host)
    # ═══════════════════════════════════════════════════════
    @socketio.on('start_game')
    def on_start_game():
        global game_active, current_question_index, question_start_time
        
        if len(players) == 0:
            emit('error', {'message': 'No hay jugadores conectados'})
            return
        
        game_active = True
        current_question_index = 0
        question_start_time = time.time()
        
        # Enviar primera pregunta a TODOS
        question = question_bank.get_question(0)
        emit('game_started', {
            'question': question.to_dict(),
            'q_number': 1,
            'total': question_bank.total(),
            'time_limit': 30
        }, broadcast=True)
    
    # ═══════════════════════════════════════════════════════
    # EVENTO: Jugador responde
    # ═══════════════════════════════════════════════════════
    @socketio.on('vote')
    def on_vote(data):
        global players, question_start_time
        
        username = data.get('player')
        choice = data.get('choice')
        
        if username not in players or not game_active:
            return
        
        # Evitar doble voto
        if players[username].has_voted:
            return
        
        # Calcular tiempo de respuesta
        response_time = time.time() - question_start_time
        
        # Verificar respuesta
        question = question_bank.get_question(current_question_index)
        is_correct = (choice == question.correct_answer)
        
        # Actualizar puntuación
        if is_correct:
            points = 10  # Puntos base
            # Bonus por velocidad (máx 5 puntos extra)
            speed_bonus = max(0, int(5 - (response_time / 6)))
            points += speed_bonus
            players[username].add_points(points)
        
        players[username].mark_voted()
        
        # Confirmar al jugador
        emit('vote_confirmed', {
            'correct': is_correct,
            'points': points if is_correct else 0
        })
        
        # Actualizar scores en tiempo real (solo para el host)
        sorted_scores = get_sorted_scores()
        emit('live_scores', {'scores': sorted_scores}, broadcast=True)
    
    # ═══════════════════════════════════════════════════════
    # EVENTO: Siguiente pregunta (solo el host)
    # ═══════════════════════════════════════════════════════
    @socketio.on('next_question')
    def on_next_question():
        global current_question_index, question_start_time
        
        current_question_index += 1
        
        # Resetear votos
        for player in players.values():
            player.reset_vote()
        
        if current_question_index < question_bank.total():
            question_start_time = time.time()
            question = question_bank.get_question(current_question_index)
            
            emit('new_question', {
                'question': question.to_dict(),
                'q_number': current_question_index + 1,
                'total': question_bank.total(),
                'time_limit': 30
            }, broadcast=True)
        else:
            # Juego terminado
            end_game()
    
    # ═══════════════════════════════════════════════════════
    # EVENTO: Terminar juego
    # ═══════════════════════════════════════════════════════
    @socketio.on('end_game')
    def on_end_game():
        end_game()
    
    # ═══════════════════════════════════════════════════════
    # EVENTO: Jugador se desconecta
    # ═══════════════════════════════════════════════════════
    @socketio.on('disconnect')
    def on_disconnect():
        pass  # Se maneja en el cliente


def end_game():
    """Termina el juego y muestra el podio."""
    global game_active
    game_active = False
    
    podium = get_sorted_scores()[:3]  # Top 3
    
    emit('game_over', {
        'podium': podium,
        'total_players': len(players)
    }, broadcast=True)


def get_sorted_scores():
    """Retorna lista de jugadores ordenados por puntuación."""
    return [
        {'username': p.username, 'score': p.score}
        for p in sorted(players.values(), key=lambda x: x.score, reverse=True)
    ]