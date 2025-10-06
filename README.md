# PyCatApi
PyCatApi is a Python wrapper for [TheCatApi](https://thecatapi.com/) written by [UnrealFar](https://github.com/UnrealFar)

## Example usage
```py
#Define our client here
c = Client()

#Lets get a random cat image UwU

img = asyncio.run(c.get_cat())
pprint(f"Cat\n{img}")

#Get an image of a cat belonging to a specific breed

breedimg = asyncio.run(c.get_breed("beng"))
pprint(f"Cat by breed\n{breedimg}")

```

### This will give us the url to a cat image 🐈
