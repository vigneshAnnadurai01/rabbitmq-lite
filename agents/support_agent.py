# import json
# import pika

# connection = pika.BlockingConnection(
#     pika.ConnectionParameters("localhost")
# )

# channel = connection.channel()

# channel.queue_declare(
#     queue="document_queue",
#     durable=True
# )


# def callback(ch, method, properties, body):

#     data = json.loads(body)

#     result = {
#         "event_id": data["event_id"],
#         "agent": "document",
#         "response": f"Document analyzed: {data['query']}"
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
#     queue="document_queue",
#     on_message_callback=callback
# )

# channel.start_consuming()

from agents.base_agent import BaseAgent

class SupportAgent(BaseAgent):

    def __init__(self):
        super().__init__("support_queue")

    def process(self, message):
        return f"Support ticket solved: {message.get('ticket_id')}"