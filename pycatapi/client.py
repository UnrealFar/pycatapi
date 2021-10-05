import requests

from .cat import Cat

class Client:

    def __init__(self) -> None:
        self.session = requests.Session()

    @staticmethod
    def request(session: requests.Session):
        r = session.get("https://api.thecatapi.com/v1/images/search")
        json: list[dict] = r.json()
        return json[0]

    def get_cat(self) -> Cat:
        """Get a random cat pic UwU"""
        data = self.request(self.session)
        return Cat(**data)
