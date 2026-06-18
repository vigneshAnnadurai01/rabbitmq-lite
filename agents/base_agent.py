import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("agent")


class BaseAgent:

    def __init__(self, queue_name):
        self.queue_name = queue_name

    def process(self, message):
        raise NotImplementedError("Override this method")

    def callback(self, ch, method, properties, body):
        message = json.loads(body)

        logger.info(f"[{self.queue_name}] Received: {message}")
        logger.info(f"RAW MESSAGE: {message}")
        logger.info(f"DOC_ID: {message.get('doc_id')}")
        try:
            result = self.process(message)
            logger.info(f"[{self.queue_name}] Processed result: {result}")

            ch.basic_ack(delivery_tag=method.delivery_tag)

        except Exception as e:
            logger.error(f"[{self.queue_name}] Error: {str(e)}")
            ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)