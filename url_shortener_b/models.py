"""All theAPI models here"""

# pylint: disable=no-name-in-module
from pydantic import BaseModel


class StandardResponse:  # pylint: disable=too-few-public-methods
    """Standard response format for API endpoints."""
    message: str
    data: any

    def __init__(self, data, message='Success'):
        self.message = message
        self.data = data


class URLItem(BaseModel):  # pylint: disable=too-few-public-methods
    """Data model for individual URL items."""
    id: str
    url: str


class URLPayload(BaseModel):  # pylint: disable=too-few-public-methods
    """Payload model for creating a short URL."""
    url: str
