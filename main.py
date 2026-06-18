 

# from messaging.publisher import publish
# import uuid

# print("\n🚀 RabbitMQ Unified Test System Started")

# while True:
#     print("\n==============================")
#     print("ACCOUNT / BILLING / DOCUMENT / SUPPORT TEST")
#     print("==============================")
#     print("Type keywords:")
#     print("account   → Account Queue")
#     print("billing   → Billing Queue")
#     print("document  → Document Queue")
#     print("support   → Support Queue")
#     print("custom    → Custom queue input")
#     print("exit      → Stop system")

#     choice = input("\nEnter your input: ").strip().lower()

#     # ❌ EXIT
#     if choice == "exit":
#         print("👋 Exiting system...")
#         break

#     # 👤 ACCOUNT
#     elif choice == "account":
#         query = input("Enter account query: ")
#         publish("account_queue", {
#             "event_id": str(uuid.uuid4()),
#             "user_id": 101,
#             "agent_type": "account",
#             "query": query
#         })
#         print("✅ Sent to account_queue")

#     # 💰 BILLING
#     elif choice == "billing":
#         query = input("Enter billing query: ")
#         amount = input("Enter amount: ")

#         publish("billing_queue", {
#             "event_id": str(uuid.uuid4()),
#             "user_id": 102,
#             "agent_type": "billing",
#             "query": query,
#             "amount": amount
#         })
#         print("✅ Sent to billing_queue")

#     # 📄 DOCUMENT
#     elif choice == "document":
#         doc = input("Enter document type: ")

#         publish("document_queue", {
#             "event_id": str(uuid.uuid4()),
#             "user_id": 103,
#             "agent_type": "document",
#             "doc_type": doc,
#             "query": "process document"
#         })
#         print("✅ Sent to document_queue")

#     # 🎧 SUPPORT
#     elif choice == "support":
#         issue = input("Enter issue: ")

#         publish("support_queue", {
#             "event_id": str(uuid.uuid4()),
#             "user_id": 104,
#             "agent_type": "support",
#             "issue": issue,
#             "query": "create ticket"
#         })
#         print("✅ Sent to support_queue")

#     # ⚙️ CUSTOM QUEUE
#     elif choice == "custom":
#         queue = input("Enter queue name: ")
#         msg = input("Enter message: ")

#         publish(queue, {
#             "event_id": str(uuid.uuid4()),
#             "user_id": 999,
#             "agent_type": queue.replace("_queue", ""),
#             "query": msg
#         })
#         print(f"✅ Sent to {queue}")

#     else:
#         print("❌ Invalid input. Try: account / billing / document / support / custom / exit")


# just qeue test



# from messaging.publisher import publish

# publish(
#     "account_queue",
#     {
#         "user_id": 1,
#         "action": "create_account"
#     }
# )

# print("Message published")


# load testing=====================================================================================================

# from messaging.publisher import publish

# for i in range(100):
#     publish(
#         "account_queue",
#         {
#             "user_id": i,
#             "action": "create_account"
#         }
#     )

# print("10,000 messages sent")

# # load testing=====================================================================================================

# from messaging.publisher import publish

# user_request = {
#     "user_id": 1000,
#     "name": "Vignesh",
#     "amount": 500,
#     "doc_id": "DOC001",
#     "ticket_id": "TKT001"
# }

# publish("account_queue", user_request)
# publish("billing_queue", user_request)
# publish("document_queue", user_request)
# publish("support_queue", user_request)

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