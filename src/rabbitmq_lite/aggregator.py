# from messaging.rabbitmq import get_channel
# from agents.account_agent import AccountAgent
# from agents.billing_agent import BillingAgent
# from agents.document_agent import DocumentAgent
# from agents.support_agent import SupportAgent

# def start_consumer(agent, queue_name):
#     channel = get_channel()

#     channel.basic_consume(
#         queue=queue_name,
#         on_message_callback=agent.callback
#     )

#     print(f"🚀 Listening on {queue_name}")
#     channel.start_consuming()
#     print(f"Registered consumer for {queue_name}")
#     channel.start_consuming()

# if __name__ == "__main__":

#     agents = [
#         AccountAgent(),
#         BillingAgent(),
#         DocumentAgent(),
#         SupportAgent()
#     ]

#     queues = [
#         "account_queue",
#         "billing_queue",
#         "document_queue",
#         "support_queue"
#     ]

#     for agent, queue in zip(agents, queues):
#         start_consumer(agent, queue)
 


import threading

from messaging.rabbitmq import get_channel
from agents.account_agent import AccountAgent
from agents.billing_agent import BillingAgent
from agents.document_agent import DocumentAgent
from agents.support_agent import SupportAgent


def start_consumer(agent, queue_name):
    channel = get_channel()

    channel.basic_consume(
        queue=queue_name,
        on_message_callback=agent.callback
    )

    print(f"🚀 Listening on {queue_name}")
    channel.start_consuming()


agents = [
    (AccountAgent(), "account_queue"),
    (BillingAgent(), "billing_queue"),
    (DocumentAgent(), "document_queue"),
    (SupportAgent(), "support_queue"),
]

for agent, queue in agents:
    threading.Thread(
        target=start_consumer,
        args=(agent, queue),
        daemon=True
    ).start()

while True:
    pass