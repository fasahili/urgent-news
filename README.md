# Urgent News - Dockerized Web Application

## Overview
Urgent News is a web-based one-page platform that displays the ten most recent urgent news articles. The application is fully containerized using Docker and consists of three main services:

1. **Database Service (PostgreSQL)** - Stores the news articles.
2. **Backend Service (Flask API)** - Fetches the latest news from the database.
3. **Frontend Service (Apache Server)** - Displays the news to users.

---

## Project Structure
```
urgentNews/
│── backend/
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│── db/
│   ├── Dockerfile
│   ├── init.sql
│── frontend/
│   ├── Dockerfile
│   ├── index.html
│   ├── styles.css
│── docker-compose.yml
│── README.md
```

---

## Docker Images
The project consists of the following Docker images:

| Service   | Image Name                           |
|-----------|------------------------------------|
| Database  | [DB link](https://hub.docker.com/repository/docker/fasahili/postgres-urgentnews/general)    |
| Backend   | [BE link](https://hub.docker.com/repository/docker/fasahili/backend-urgentnews/general)     |
| Frontend  | [FE link](https://hub.docker.com/repository/docker/fasahili/frontend-urgentnews/general)    |

All images are publicly available on Docker Hub.

---

## Running the Application
You can run the project using Docker Compose.

### **Step 1: Clone the Repository**
```sh
git clone https://github.com/yourusername/urgentNews.git
cd urgentNews
```

### **Step 2: Run the Application**
```sh
docker-compose up --build
```

### **Step 3: Access the Services**
- **Frontend:** `http://localhost`
- **Backend API:** `http://localhost:5000/getUrgentNews`
---

## Loom Video (Project Demo)
🎥 **Watch the full setup and demo here:** [Loom Video](https://www.loom.com/share/f821ce16f38c445489355087cb76acee?sid=30d690dc-7bf7-4207-b01e-212f9dee5a0f)

---
