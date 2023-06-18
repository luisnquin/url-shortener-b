"""
- '/all': Endpoint to get all stored URLs.
- '/create': Endpoint to create a short URL.
- '/{short_url}': Endpoint to redirect to the original URL based on the provided short URL.
"""

from typing import List

from fastapi import FastAPI, Response, status
from fastapi.responses import RedirectResponse
from nanoid import generate as generate_nanoid

from url_shortener_b.models import StandardResponse, URLItem, URLPayload


app = FastAPI()

url_store: List[URLItem] = []


@app.get('/all')
def get_all():
    """Get all stored URLs."""
    return StandardResponse(url_store)


@app.post('/create', status_code=status.HTTP_201_CREATED)
def create(payload: URLPayload):
    """Create a short URL for the given payload URL."""

    for item in url_store:
        if item.url == payload.url:
            return StandardResponse(item)

    item_id = generate_nanoid(size=20)
    new_item = URLItem(id=item_id, url=payload.url)

    url_store.append(new_item)

    return StandardResponse(new_item)


@app.get('/{short_url}')
def redirect(response: Response, short_url: str):
    """Redirect to the original URL based on the provided short URL."""

    url: str

    for item in url_store:
        if item.id == short_url:
            url = item.url

            break
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return StandardResponse(None, 'URL not found')

    return RedirectResponse(url)
