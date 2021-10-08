import requests

class Client:
    def __init__(self):
        self._get = requests.get
        self._base_url = "https://api.thecatapi.com/v1/images/search"

    def get_cat(self):
        """Get a random cat pic UwU"""
        url = self._base_url
        data = self._get(url)
        cat = data.json()[0]
        return cat["url"]

    def get_cat_by_breed(self, breed: str):
        """Get a random cat pic of a specified breed!"""
        url = f"{self._base_url}?breed_ids={breed}"
        data = self._get(url)
        cat = data.json()[0]
        return cat["url"]

    def get_breed_desc(self, breed: str):
        """Get the description of a specified cat breed!"""
        url = f"{self._base_url}?breed_ids={breed}"
        data = self._get(url)
        catinfo = data.json()[0]["breeds"][0]["description"]
        return catinfo