# import json
# import pika

# connection = pika.BlockingConnection(
# 
# pika.ConnectionParameters("localhost")
# )

# channel = connection.channel()

# channel.queue_declare(
#     queue="billing_queue",
#     durable=True
# )


# def callback(ch, method, properties, body):

#     data = json.loads(body)

#     result = {
#         "event_id": data["event_id"],
#         "agent": "billing",
#         "response": f"Billing processed: {data['query']}"
#     }

#     channel.basic_publish(
#         exchange="",
#         routing_key="response_queue",
#         body=json.dumps(result)
#     )

#     ch.basic_ack(
#         delivery_tag=method.delivery_tag
#     )


# channel.basic_consume(
#     queue="billing_queue",
#     on_message_callback=callback
# )

# channel.start_consuming()

from agents.base_agent import BaseAgent

class DocumentAgent(BaseAgent):

    def __init__(self):
        super().__init__("document_queue")

    def process(self, message):
        return f"Document processed: {message.get('doc_id')}"