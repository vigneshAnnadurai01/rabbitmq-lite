 
from agents.base_agent import BaseAgent

class DocumentAgent(BaseAgent):

    def __init__(self):
        super().__init__("document_queue")

    def process(self, message):
        return f"Document processed: {message.get('doc_id')}"