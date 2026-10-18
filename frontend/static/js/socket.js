/**
 * CONEXIÓN WEBSOCKET
 * Kahoot Offline - Equipo 6 FCFM
 */

// Conectar al servidor Socket.IO
const socket = io();

// Almacenar nombre del jugador
let playerName = sessionStorage.getItem('username') || '';

console.log('🔌 Conectado al servidor Kahoot Offline');