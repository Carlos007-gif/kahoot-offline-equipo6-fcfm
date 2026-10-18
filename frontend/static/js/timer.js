/**
 * TEMPORIZADOR DE PREGUNTAS
 * Kahoot Offline - Equipo 6 FCFM
 */

let timerInterval = null;
let timeRemaining = 30;

function startTimer(seconds) {
    clearInterval(timerInterval);
    timeRemaining = seconds;
    
    const timerEl = document.getElementById('timer-display') || 
                    document.getElementById('game-timer');
    
    if (!timerEl) return;
    
    timerInterval = setInterval(() => {
        timeRemaining--;
        timerEl.textContent = `⏱️ ${timeRemaining}s`;
        
        if (timeRemaining <= 5) {
            timerEl.style.color = '#e74c3c';
        }
        
        if (timeRemaining <= 0) {
            clearInterval(timerInterval);
            timerEl.textContent = '⏱️ ¡TIEMPO!';
        }
    }, 1000);
}

function stopTimer() {
    clearInterval(timerInterval);
}