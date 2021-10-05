import requests

class Cat():
    def get_cat():
        """Get a random cat pic UwU"""
        catraw = requests.get("https://api.thecatapi.com/v1/images/search").json()
        cat = catraw[0]["url"]
        return cat
        