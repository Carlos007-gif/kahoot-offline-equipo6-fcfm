# 🎮 Kahoot Offline - Equipo 6 FCFM

> Sistema de quiz interactivo en tiempo real **100% OFFLINE** (sin internet)
> Desarrollado para la dinámica de 15 minutos - Metodologías de la Programación

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![Flask](https://img.shields.io/badge/Flask-3.0+-green)
![SocketIO](https://img.shields.io/badge/Socket.IO-RealTime-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📖 Descripción

Sistema de quiz interactivo en tiempo real diseñado para funcionar completamente
offline sin conexión a internet. Desarrollado por el **Equipo 6** de la materia
*"Metodologías de la Programación"* de la **Facultad de Ciencias Físico Matemáticas**
de la **Universidad Autónoma de Nuevo León (FCFM-UANL)**, Grupo Z04.

El proyecto implementa una dinámica tipo Kahoot donde un servidor local (laptop
del presentador) actúa como host y los participantes se conectan vía red WiFi
local usando sus dispositivos móviles.

---

## 🚀 Inicio Rápido

### Requisitos

- Python 3.11 o superior
- pip (gestor de paquetes de Python)
- Un dispositivo para cada participante (celular/tablet/laptop)

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/TU_USUARIO/kahoot-offline-equipo6-fcfm.git

# Entrar al directorio
cd kahoot-offline-equipo6-fcfm

# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual (Linux/Mac)
source venv/bin/activate

# Activar entorno virtual (Windows)
# venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el servidor
python run.py