import requests

from .cat import Cat

class Client:

    def __init__(self) -> None:
        self._session = requests.Session()

    @staticmethod
    def request(_session: requests.Session, endpoint: str):
        r = _session.get(f"https://api.thecatapi.com/v1/{endpoint}")
        json: list[dict] = r.json()
        return json[0]

    def get_cat(self) -> Cat:
        """Get a random cat pic UwU"""
        data = self.request(self._session, "images/search")
        return data["url"]

    def close(self):
        self._session.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self._session.close()
