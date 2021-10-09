import requests

class Client:
    def __init__(self):
        self._get = requests.get
        self._base_url = "https://api.thecatapi.com/v1"

    def get_cat(self):
        """Get a random cat pic UwU"""
        url = f"{self._base_url}/images/search"
        data = self._get(url)
        cat = data.json()[0]
        return cat["url"]

    def get_breed(self, breed: str):
        """Get information on a breed!"""
        url = f"{self._base_url}/breeds?q={breed}"
        data = self._get(url)
        breedinfo = data.json()[0]
        return breedinfo