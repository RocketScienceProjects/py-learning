import requests

url = "https://icanhazdadjoke.com/search?term="
user_data = input("Enter a word to search for jokes: ")

search_endpoint = url + user_data
# print(search_endpoint)

res = requests.get(search_endpoint, headers={"Accept": "application/json"})

print(res.json()["results"][0]["joke"])
