import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url)

print("----------------Status------------")
print(response.status_code)

print("----------------JSON---------------")
print(response.json())

print("-----------------Headers-----------")
print(response.headers)
