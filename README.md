# pantry_api

an library i made for short pantry api code

install by

- putting `pantry_api.py` file in your code directory
- or putting it in `site-packages`

after you done that you can code

## Example code

### New basket

```python
import pantry_api as api

pantry = api.Pantry("PANTRY-ID")

pantry.new_basket("name", {"content": "here"})
```

### Getting data from a basket

```python
import pantry_api as api

pantry = api.Pantry("PANTRY-ID", _default_basket = "default")

print(pantry.pull(basket = "another basket"))

#default basket
print(pantry.pull())

```

### Putting data in a basket

```python
import pantry_api as api

pantry = api.Pantry("PANTRY-ID", _default_basket = "default")

print(pantry.push(basket = "another basket", content = {"something": "a thing here", "dict": {"the": "end"}}))

#default basket
print(pantry.push(content = {"something": "a thing here", "dict": {"the": "end"}}))
```

### Using with statements

```python
import pantry_api as api

pantry = api.Pantry("PANTRY-ID", "default_basket") # you HAVE to put default basket here

with pantry as db:
    db["something"] = "This is a string"

#in IDLE
>>> import pantry_api as api
>>> pantry = api.Pantry("PANTRY-ID", "default_basket")
>>> with pantry as db:
...     db["something"] = "This is a string"
...     print(db)
...
{"something": "This is a string"}
```
