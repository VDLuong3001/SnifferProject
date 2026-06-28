# Network Packet Sniffer

A web-based Network Packet Sniffer built with Python, Flask, Scapy, MongoDB, and Vite. The application captures live network traffic from the host machine, stores packet metadata in MongoDB, and displays real-time packet information through a web dashboard.

---

## Features

- Capture live network packets
- Display source and destination IP addresses
- Identify network protocols (TCP, UDP, ICMP, etc.)
- Store captured packet metadata in MongoDB
- REST API for retrieving packet data
- Real-time frontend updates
- Simple and responsive web dashboard

---

## Technologies Used

**Languages**
- Python
- JavaScript
- HTML5
- CSS3

**Frameworks & Libraries**
- Flask
- Scapy
- Flask-CORS
- PyMongo
- Vite

**Database**
- MongoDB

**Tools**
- Git
- GitHub
- Visual Studio Code
- MongoDB Compass
- Npcap
- REST API
- ChatGPT

---

## Project Structure

```
Sniffer
│
├── backend
│   ├── app.py
│   ├── database.py
│   └── sniffer.py
│
└── frontend
    ├── src
    ├── public
    ├── package.json
    └── vite.config.js
```

---

## System Workflow

```
Internet / Local Network
          │
          ▼
   Scapy Packet Sniffer
          │
          ▼
      Flask Backend
          │
          ▼
        MongoDB
          │
          ▼
      REST API (/packets)
          │
          ▼
      Vite Frontend
```

---

## Core Functionality

### Packet Capture
Scapy continuously listens to the host machine's network interface and captures incoming and outgoing network packets.

### Packet Processing
For each captured packet, the application extracts:

- Source IP Address
- Destination IP Address
- Network Protocol

### Data Storage
Packet metadata is stored in a MongoDB database for later retrieval and visualization.

### REST API
The Flask backend provides REST API endpoints that allow the frontend to retrieve captured packet data.

### Real-Time Dashboard
The frontend periodically requests the latest packet information from the backend and updates the dashboard automatically.

---

## Database Structure

### Database

```
packet_sniffer
```

### Collection

```
packets
```

### Sample Document

```json
{
    "src_ip": "192.168.1.5",
    "dst_ip": "142.250.190.78",
    "protocol": 6
}
```

---

## Getting Started

### Clone Repository

```bash
git clone <repository-url>
cd Sniffer
```

### Backend

```bash
cd backend

pip install flask
pip install flask-cors
pip install scapy
pip install pymongo

python app.py
```

### Frontend

```bash
cd frontend

npm install
npm run dev
```

---

## Future Improvements

- Packet filtering
- Protocol name conversion (TCP/UDP/ICMP)
- Packet timestamps
- Packet size statistics
- Live traffic charts
- Search and filtering
- WebSocket-based real-time updates
- Network traffic analytics
- Suspicious traffic detection

---

## Author

Developed by **Võ Đại Lượng**
