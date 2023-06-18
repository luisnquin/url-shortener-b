from pydantic import BaseModel


class StandardResponse:
    """Standard response format for API endpoints."""
    message: str
    data: any

    def __init__(self, data, message='Success'):
        self.message = message
        self.data = data


class URLItem(BaseModel):
    """Data model for individual URL items."""
    id: str
    url: str


class URLPayload(BaseModel):
    """Payload model for creating a short URL."""
    url: str
