import aiohttp

class Client:
    def __init__(self):
        self._base_url = "https://api.thecatapi.com/v1"

    async def get_cat(self):
        """Get a random cat pic UwU"""
        url = f"{self._base_url}/images/search"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as data:
                cat = await data.json()
        return cat[0]["url"]

    async def get_breed(self, breed: str):
        """Get information on a breed!"""
        url = f"{self._base_url}/breeds?q={breed}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as data:
                breedinfo = await data.json()
        return breedinfo[0]