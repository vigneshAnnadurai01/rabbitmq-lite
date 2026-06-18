 

# import pika

# RABBITMQ_HOST = "localhost"

# def get_channel():
#     connection = pika.BlockingConnection(
#         pika.ConnectionParameters(RABBITMQ_HOST)
#     )

#     channel = connection.channel()

#     # =========================
#     # MAIN QUEUE
#     # =========================
#     channel.queue_declare(queue="account_queue", durable=True)

#     # =========================
#     # RETRY QUEUE (DELAY LOGIC)
#     # =========================
#     channel.queue_declare(
#         queue="account_retry_queue",
#         durable=True,
#         arguments={
#             "x-message-ttl": 5000,  # 5 sec delay
#             "x-dead-letter-exchange": "",
#             "x-dead-letter-routing-key": "account_queue"
#         }
#     )

#     # =========================
#     # DEAD LETTER QUEUE
#     # =========================
#     channel.queue_declare(queue="account_dlq", durable=True)

#     return channel


import pika
import logging

RABBITMQ_HOST = "localhost"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("rabbitmq")

def get_connection():
    params = pika.ConnectionParameters(
        host=RABBITMQ_HOST,
        heartbeat=600,
        blocked_connection_timeout=300
    )
    return pika.BlockingConnection(params)


def get_channel():
    connection = get_connection()
    channel = connection.channel()

    queues = [
        "account_queue",
        "billing_queue",
        "document_queue",
        "support_queue"
    ]

    for q in queues:
        channel.queue_declare(queue=q, durable=True)
        logger.info(f"Queue ready: {q}")

    return channel