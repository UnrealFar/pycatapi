from pycatapi import Client, Cat

c = Client()
res = c.get_cat()
assert isinstance(res, Cat)
