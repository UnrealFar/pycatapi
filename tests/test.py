from pycatapi import Client

c = Client()

cat = c.get_cat()
print(cat)
# Should print something similar to
# Cat(breed=[], id="fghf", url="https://something", width=1000, height=250)
