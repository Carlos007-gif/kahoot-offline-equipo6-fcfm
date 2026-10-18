# 📁 ESTRUCTURA DEL PROYECTO

## Árbol de Directorios y Archivos
```text
kahoot-offline-equipo6-fcfm/
│
├── 📄 README.md → Documentación principal del proyecto
├── 📄 .gitignore → Archivos excluidos de Git
├── 📄 LICENSE → Licencia MIT
├── 📄 ESTRUCTURA.md → Este archivo (mapa del proyecto)
├── 📄 requirements.txt → Dependencias de Python
├── 📄 run.py → Punto de entrada del servidor
├── 📄 .env.example → Plantilla de variables de entorno
│
├── 📁 config/ → ARCHIVOS DE CONFIGURACIÓN
│   ├── 📄 init.py → Inicializador del paquete
│   ├── 📄 settings.py → Configuración general (puerto, host)
│   └── 📄 security.py → Configuración de seguridad
│
├── 📁 backend/ → ARCHIVOS DE BACKEND (Python/Flask)
│   ├── 📄 init.py → Inicializador del paquete
│   ├── 📄 app.py → Creación de la app Flask + SocketIO
│   ├── 📄 socketio_events.py → Eventos WebSocket (join, vote, etc.)
│   ├── 📁 models/ → Modelos de datos
│   │   ├── 📄 init.py
│   │   ├── 📄 player.py → Modelo del jugador
│   │   └── 📄 question.py → Modelo de pregunta
│   └── 📁 data/ → Datos estáticos
│       └── 📄 questions.json → Banco de preguntas (7 preguntas)
│
├── 📁 frontend/ → ARCHIVOS DE FRONTEND
│   ├── 📁 templates/ → Plantillas HTML (Jinja2)
│   │   ├── 📄 index.html → Página principal (host)
│   │   ├── 📄 lobby.html → Sala de espera (jugadores)
│   │   ├── 📄 game.html → Pantalla de juego (jugadores)
│   │   └── 📄 results.html → Pantalla de resultados/podio
│   └── 📁 static/ → Archivos estáticos
│       ├── 📁 css/
│       │   └── 📄 style.css → Estilos principales
│       ├── 📁 js/
│       │   ├── 📄 main.js → Lógica principal del juego
│       │   ├── 📄 socket.js → Conexión WebSocket
│       │   └── 📄 timer.js → Temporizador de preguntas
│       └── 📁 img/
│           └── 📄 qr_placeholder.png → Placeholder del QR
│
├── 📁 security/ → ARCHIVOS DE SEGURIDAD
│   ├── 📄 validate.py → Validación de conexiones
│   └── 📄 rate_limiter.py → Limitador de peticiones
│
└── 📁 docs/ → DOCUMENTACIÓN ADICIONAL
	├── 📄 MANUAL_USUARIO.md → Manual para el presentador
	└── 📄 MANUAL_TECNICO.md → Manual técnico de instalación
```

## Descripción de Carpetas

| Carpeta | Propósito |
|---------|-----------|
| `config/` | Configuración del servidor (puerto, seguridad) |
| `backend/` | Lógica del servidor (Flask + SocketIO) |
| `backend/models/` | Modelos de datos (Player, Question) |
| `backend/data/` | Datos estáticos (preguntas JSON) |
| `frontend/templates/` | Plantillas HTML renderizadas por Flask |
| `frontend/static/` | CSS, JS, imágenes |
| `security/` | Validaciones y protección |
| `docs/` | Manuales de usuario y técnico |

## Tecnologías Utilizadas

| Capa | Tecnología | Versión |
|------|-----------|---------|
| Backend | Python | 3.11+ |
| Framework Web | Flask | 3.0+ |
| WebSockets | Flask-SocketIO | 5.3+ |
| Motor WebSocket | python-socketio | 5.10+ |
| Frontend Markup | HTML5 | — |
| Estilos | CSS3 | — |
| Frontend Logic | JavaScript Vanilla | ES6+ |
| Control de versiones | Git + GitHub | — |