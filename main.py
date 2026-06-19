from messaging.publisher import publish

payload = {
    "user_id": 1000,
    "name": "Vignesh",
    "amount": 500,
    "doc_id": "DOC001",
    "ticket_id": "TKT001"
     
}

queues = [
    "account_queue",
    "billing_queue",
    "document_queue",
    "support_queue"
]

for queue in queues:
    publish(queue, payload)

print("Message sent to all queues")



# from messaging.publisher import publish

# publish("account_queue", {"user_id": 1})
# publish("billing_queue", {"invoice_id": 101})
# publish("document_queue", {"doc_id": 501})
# publish("support_queue", {"ticket_id": 9001})