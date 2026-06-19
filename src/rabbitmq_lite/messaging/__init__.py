"""
Messaging Package
Handles RabbitMQ publishing and communication layer.
"""

from .publisher import publish

__all__ = ["publish"]