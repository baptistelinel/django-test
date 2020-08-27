import os

import requests
from dotenv import load_dotenv


class RequestsAdapter:
    def __init__(self):
        load_dotenv()

    def http_get(self, uri: str, headers=None) -> dict:
        request = requests.get(f"{os.getenv('API_BASE_URL')}{uri}",
                               headers=headers)
        return {
            'headers': request.headers,
            'url': request.url,
            'status_code': request.status_code,
            'json': request.json()
        }
