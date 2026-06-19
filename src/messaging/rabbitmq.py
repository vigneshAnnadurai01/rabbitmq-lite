
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