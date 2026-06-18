# import json
# import pika

# connection = pika.BlockingConnection(
#     pika.ConnectionParameters("localhost")
# )

# channel = connection.channel()

# channel.queue_declare(
#     queue="response_queue",
#     durable=True
# )


# def callback(ch, method, properties, body):

#     result = json.loads(body)

#     print("\n========= FINAL RESPONSE =========")
#     print(result)
#     print("==================================\n")

#     ch.basic_ack(
#         delivery_tag=method.delivery_tag
#     )


# channel.basic_consume(
#     queue="response_queue",
#     on_message_callback=callback
# )

# print("Aggregator Running")

# channel.start_consuming()



from agents.base_agent import BaseAgent

class BillingAgent(BaseAgent):

    def __init__(self):
        super().__init__("billing_queue")

    def process(self, message):
        return f"Billing processed: {message.get('amount', 0)}"