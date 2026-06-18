 
    
# from messaging.rabbitmq import get_channel
# import json
# event = {
#     "user_id": 101,
#     "action": "create_account"
# }
# payload = {
#     "data": event,
#     "retry_count": 0
# }
# def publish(queue_name, payload):
#     channel = get_channel()

#     channel.basic_publish(
#         exchange="",
#         routing_key=queue_name,
#         body=json.dumps(payload),
#         properties=None
#     )

#     print(f"Published --> {queue_name}")


import json
import logging
from messaging.rabbitmq import get_channel

logger = logging.getLogger("publisher")

def publish(queue_name, message: dict):
    try:
        channel = get_channel()

        channel.basic_publish(
            exchange="",
            routing_key=queue_name,
            body=json.dumps(message),
            properties=None
        )

        logger.info(f"Message sent → {queue_name} | {message}")

    except Exception as e:
        logger.error(f"Publish failed: {str(e)}")