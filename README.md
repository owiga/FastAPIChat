# 💬 FastAPI Chat

A lightweight, real-time system monitor (CPU/RAM telemetry) and persistent multi-client chat built with FastAPI, WebSockets, and SQLite, fully containerized with Docker.


# 🚀 Real-Time System Monitor & Chat Dashboard

A lightweight, high-performance real-time web application featuring live server telemetry (CPU & RAM usage) and a persistent multi-client chat room. Built with **FastAPI**, **WebSockets**, and **SQLite**, and fully containerized using **Docker**.


## ✨ Key Features

- **Live System Telemetry**: Streams real-time CPU and RAM utilization metrics to clients using WebSockets and `psutil`.
- **Persistent Multi-Client Chat**: Broadcasts messages instantly to all connected peers while saving chat history securely to an SQLite database.
- **Asynchronous Architecture**: Leverages FastAPI and Python's `asyncio` for non-blocking concurrent connections.
- **Clean Modular Design**: Separates database concerns, WebSocket routing, and application entry points to prevent circular imports.
- **Docker Ready**: Fully containerized with `Dockerfile` and `Docker Compose` with volume mounting for local development and persistent storage.


## 🛠️ Tech Stack

- **Backend**: Python 3.11+, FastAPI, Uvicorn, WebSockets, asyncio
- **System Metrics**: `psutil`
- **Database**: SQLite (managed with custom context managers)
- **Containerization**: Docker, Docker Compose

## 📦 Project Structure

```text
CPUDashboard/
│
├── main.py             # FastAPI entry point & WebSocket routers
├── database.py         # SQLite database handler & context managers
├── requirements.txt    # Python dependencies
├── Dockerfile          # Container image specification
├── docker-compose.yml  # Multi-container orchestration & volumes
└── chat.db             # SQLite database (auto-generated)
```


## 🚀 Getting Started
Prerequisites
-- Python 3.11+ (if running locally without Docker)
-- Docker & Docker Compose (recommended)



## 🐋 Running with Docker (Recommended)
Clone the repository:
```Bash
git clone [https://github.com/your-username/CPUDashboard.git](https://github.com/your-username/CPUDashboard.git)
cd CPUDashboard
```

Build and run using Docker Compose:
```Bash
docker compose up --build
```

Open your browser and navigate to:
http://localhost:8000

## 📦 Running Locally (Without Docker)
Create and activate a virtual environment:

```Bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

Install dependencies:
```Bash
pip install -r requirements.txt
```

Run the application with Uvicorn:
```Bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

---

📄 License
This project is open-source and available under the MIT License.
