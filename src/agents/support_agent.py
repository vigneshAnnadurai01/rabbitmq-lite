from agents.base_agent import BaseAgent

class SupportAgent(BaseAgent):

    def __init__(self):
        super().__init__("support_queue")

    def process(self, message):
        return f"Support ticket solved: {message.get('ticket_id')}"