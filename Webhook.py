import requests


user_message = "Can you tell me about black holes in 3 to 4 lines?"

request_message = {"message": user_message}

url = "http://localhost:5678/webhook-test/c978d29e-b7cb-42a5-88f0-ab228f8e3b50"

response = requests.post(url, json=request_message)

print(response.status_code)

print(response.text)

print(response.json()[0]["output"])