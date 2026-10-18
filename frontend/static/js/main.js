/**
 * LÓGICA PRINCIPAL DEL HOST
 * Kahoot Offline - Equipo 6 FCFM
 */

// ═══════════════════════════════════════════════════════════
// VARIABLES GLOBALES
// ═══════════════════════════════════════════════════════════
let currentQuestion = 0;
let totalQuestions = 7;
let gameStarted = false;

// ═══════════════════════════════════════════════════════════
// EVENTOS SOCKET (HOST)
// ═══════════════════════════════════════════════════════════

socket.on('player_joined', function(data) {
    const list = document.getElementById('player-list');
    const li = document.createElement('li');
    li.textContent = `👤 ${data.username}`;
    list.appendChild(li);
});

socket.on('player_count', function(count) {
    document.getElementById('player-count').textContent = `👥 Jugadores: ${count}`;
});

socket.on('game_started', function(data) {
    gameStarted = true;
    displayQuestion(data);
    document.getElementById('btn-start').style.display = 'none';
    document.getElementById('btn-next').style.display = 'inline-block';
    document.getElementById('btn-end').style.display = 'inline-block';
    document.getElementById('game-status').textContent = '🎮 EN JUEGO';
    document.getElementById('question-section').style.display = 'block';
    document.getElementById('scores-section').style.display = 'block';
});

socket.on('new_question', function(data) {
    displayQuestion(data);
});

socket.on('live_scores', function(data) {
    displayScores(data.scores);
});

socket.on('game_over', function(data) {
    displayPodium(data.podium);
    document.getElementById('question-section').style.display = 'none';
    document.getElementById('scores-section').style.display = 'none';
    document.getElementById('podium-section').style.display = 'block';
    document.getElementById('game-status').textContent = '🏆 TERMINADO';
});

// ═══════════════════════════════════════════════════════════
// FUNCIONES DEL HOST
// ═══════════════════════════════════════════════════════════

function startGame() {
    socket.emit('start_game');
}

function nextQuestion() {
    socket.emit('next_question');
}

function endGame() {
    socket.emit('end_game');
}

// ═══════════════════════════════════════════════════════════
// FUNCIONES DE RENDERIZADO
// ═══════════════════════════════════════════════════════════

function displayQuestion(data) {
    document.getElementById('q-number').textContent = 
        `Pregunta ${data.q_number}/${data.total}`;
    document.getElementById('q-category').textContent = 
        data.question.category || '';
    document.getElementById('question-text').textContent = 
        data.question.text;
    
    const grid = document.getElementById('options-grid');
    grid.innerHTML = '';
    
    const colors = ['#e74c3c', '#3498db', '#f39c12', '#27ae60'];
    
    data.question.options.forEach((opt, i) => {
        const div = document.createElement('div');
        div.className = 'option-display';
        div.style.backgroundColor = colors[i];
        div.textContent = opt;
        grid.appendChild(div);
    });
    
    startTimer(data.time_limit);
}

function displayScores(scores) {
    const container = document.getElementById('live-scores');
    container.innerHTML = '';
    
    scores.forEach((player, i) => {
        const div = document.createElement('div');
        div.className = 'score-item';
        div.innerHTML = `<span>${i+1}. ${player.username}</span> <strong>${player.score} pts</strong>`;
        container.appendChild(div);
    });
}

function displayPodium(podium) {
    const container = document.getElementById('podium-display');
    const medals = ['🥇', '🥈', '🥉'];
    
    let html = '';
    podium.forEach((player, i) => {
        html += `
            <div class="podium-item position-${i+1}">
                <span class="medal">${medals[i]}</span>
                <span>${player.username} - ${player.score} pts</span>
            </div>
        `;
    });
    
    container.innerHTML = html;
}