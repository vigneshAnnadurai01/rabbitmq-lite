from agents.base_agent import BaseAgent

class BillingAgent(BaseAgent):

    def __init__(self):
        super().__init__("billing_queue")

    def process(self, message):
        return f"Billing processed: {message.get('amount', 0)}"