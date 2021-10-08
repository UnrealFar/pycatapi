from pycatapi import Client

#Define our client here
c = Client()


"""Lets get a random cat image UwU"""

img = c.get_cat()
print(f"Cat\n{img}")

"""Get an image of a cat belonging to a specific breed"""

breedimg = c.get_cat_by_breed("beng")
print(f"\nCat by breed\n{img}")


"""Now, lets get information about a specific cat breed"""

info = c.get_breed_desc("beng")
print(f"Breed description\n{info}")

"""
NOTE: Breed is the breed id, for more information
on breed id of a specified breed, please go to
the official documentation of TheCatApi
"""