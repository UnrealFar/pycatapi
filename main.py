from pycatapi import Client
from pprint import pprint
import asyncio

#Define our client here
c = Client()

#Lets get a random cat image UwU

img = asyncio.run(c.get_cat())
print(f"Cat\n{img}")

#Get an image of a cat belonging to a specific breed

breedimg = asyncio.run(c.get_breed("beng"))
print(f"Cat by breed\n{breedimg}")
