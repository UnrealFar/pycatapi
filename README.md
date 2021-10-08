# PyCatApi
PyCatApi is a Python wrapper for [TheCatApi](https://thecatapi.com/) written by [TheFarGG](https://github.com/TheFarGG/)

## Example usage
```py
from pycatapi import Client

#Define our client here
c = Client()

img = c.get_cat()
print(f"Cat\n{img}")
```

### This will give us the url to a cat image 🐈