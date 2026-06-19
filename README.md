# RabbitMQ Messaging Application

##  Overview

The **RabbitMQ Messaging Application** is a scalable and fault-tolerant messaging system that demonstrates asynchronous communication between distributed components using a message broker architecture.

This project implements **producer-consumer messaging patterns** using RabbitMQ, enabling reliable, decoupled, and high-performance data exchange between services.

---

##  Key Features

- Asynchronous message publishing (Producer)
- Reliable message consumption (Consumer)
- Queue-based messaging using RabbitMQ (AMQP protocol)
- Guaranteed message delivery with acknowledgments
- Scalable architecture for distributed systems
- Robust error handling and logging mechanisms
- Easily extensible for microservices integration

---

##  Technology Stack

- **Message Broker:** RabbitMQ
- **Protocol:** AMQP 0-9-1
- **Programming Language:** Java / Python / Node.js / .NET *(as applicable)*
- **Frameworks:** (Spring Boot / Express / Flask / .NET Core) *(if applicable)*
- **Build Tools:** Maven / npm / pip
- **Logging:** Built-in logging framework / Log4j / Winston / etc.

---

##  Prerequisites

Before running this project, ensure the following are installed:

- RabbitMQ Server
- Erlang (dependency for RabbitMQ)
- Language runtime (JDK / Python / Node.js / .NET SDK)
- Package manager (Maven / npm / pip)

---

##  Installation & Setup

### 1. Clone the Repository
```bash
git clone:https://github.com/vigneshAnnadurai01/rabbitmq-lite.git
cd rabbitmq-lite

# 📩 RabbitMQ Multi-Agent Messaging System

A Python-based message-driven system using RabbitMQ where a single publisher sends messages to multiple queues and different agents process them concurrently.

## 🛠 Installation & Setup
1️⃣ Prerequisites
Install Python

Make sure Python 3.10+ is installed

python --version
Install RabbitMQ
Windows Setup
Install Erlang
https://www.erlang.org/downloads
Install RabbitMQ Server
https://www.rabbitmq.com/download.html
Enable management plugin:
rabbitmq-plugins enable rabbitmq_management
Start RabbitMQ:
rabbitmq-server

👉 Dashboard:

http://localhost:15672
Username: guest
Password: guest
Ubuntu/Linux
sudo apt update
sudo apt install rabbitmq-server -y
sudo systemctl start rabbitmq-server
sudo systemctl enable rabbitmq-server
2️⃣ Project Setup
Clone / Navigate project
cd F:\rabbit\src\rabbitmq_lite
Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
Install dependencies
pip install pika
## 📌 Project Architecture
main.py (Publisher)
        ↓
RabbitMQ Queues
        ↓
aggregator.py (Consumer Manager)
        ↓
Agents:
   ├── AccountAgent
   ├── BillingAgent
   ├── DocumentAgent
   └── SupportAgent
##  How to Run (IMPORTANT)
 STEP 1: Start RabbitMQ Server
rabbitmq-server
 STEP 2: Start Consumers

Open new terminal:

python aggregator.py

👉 You should see:

📌 Listening on account_queue
📌 Listening on billing_queue
📌 Listening on document_queue
📌 Listening on support_queue
 STEP 3: Send Messages (Publisher)

Open another terminal:

python main.py
## 📤 Message Flow
main.py sends payload
        ↓
4 queues receive message
        ↓
Each Agent processes independently
## 🧾 Sample Payload
{
    "user_id": 1000,
    "name": "Vignesh",
    "amount": 500,
    "doc_id": "DOC001",
    "ticket_id": "TKT001"
}
##  Agents Responsibilities
AccountAgent → User/account processing
BillingAgent → Payment & billing logic
DocumentAgent → Document handling
SupportAgent → Ticket management
## 📌 Expected Output
aggregator.py
📌 Listening on account_queue
📌 Listening on billing_queue
📌 Listening on document_queue
📌 Listening on support_queue
main.py
Message sent to all queues
## ⚠️ Common Issues
❌ RabbitMQ not connecting

✔ Ensure server is running:

rabbitmq-server
❌ No message received

✔ aggregator.py must be running before main.py

❌ Queue not found

✔ Run publisher once → queues auto-create

## 🔥 Run Order (VERY IMPORTANT)
1. Start RabbitMQ Server
2. Run aggregator.py
3. Run main.py