from pycatapi import Client

c = Client()
res = c.get_cat()

print(res)

c.close()