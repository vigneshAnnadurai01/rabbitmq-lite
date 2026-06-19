from agents.base_agent import BaseAgent

class AccountAgent(BaseAgent):

    def __init__(self):
        super().__init__("account_queue")

    def process(self, message):
        return f"Account handled for user {message.get('user_id')}"