from pycatapi import Client

#Define our client here
c = Client()


"""Lets get a random cat image UwU"""

img = c.get_cat()
print(f"Cat\n{img}")

"""Get an image of a cat belonging to a specific breed"""

breedimg = c.get_breed("beng")
print(f"\nCat by breed\n{img}")

