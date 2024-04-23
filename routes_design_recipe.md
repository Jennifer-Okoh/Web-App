
# {{ Add-Name }} Route Design Recipe
Use this Design Recipe to test-drive a new route POST /sort-names which receives a list of names (as a comma-separated string) and return the same list, sorted in alphabetical order.

## 1. Design the Route Signature

# Request:
GET http://localhost:5001/names?add=Eddie

# With query parameters:
names=Julia, Alic, Karim

# Expected response (new list of names):
Julia, Alic, Karim, Eddie

```
# EXAMPLE

GET /add-names
    names: a string of comma separated names with spaces

```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# GET /add-names
# With names=Julia, Alice, Karim
# Expected respons (200 OK)
"""
Julia, Alice, Karim, Eddie
"""

# GET /add-names
# With no new names
# Expected response Invalid Request code
"""
No new name added!!
"""
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /add-name
  Expected response (200 OK):
  "Julia, Alice, Karim, Eddie"
"""
def test_add_name(web_client):
    response = web_client.get("/add-name", data=[
        'names': 'Julia,Alice, Karim'
    ])
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ['Julia, Alice, Karim, Eddie']

"""
POST /submit
  Parameters:
    name: Leo
    message: Hello world
  Expected response (200 OK):
  "Thanks Leo, you sent this message: "Hello world""
"""
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Leo', 'message': 'Hello world'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Leo, you sent this message: "Hello world"'
```

