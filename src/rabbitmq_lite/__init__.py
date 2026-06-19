"""
rabbitmq_lite

RabbitMQ-based microservice messaging framework.
"""

__version__ = "0.1.2"

from .messaging.rabbitmq import RabbitMQClient
from .messaging.publisher import Publisher

__all__ = [
    "RabbitMQClient",
    "Publisher",
]