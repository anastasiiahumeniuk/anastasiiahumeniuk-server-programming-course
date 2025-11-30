import requests
import json

TOKEN = "5b6b3f2d7f4b4cc4ef214fa5f72e9dd8b76dca76"

headers = {
    "Authorization": f"Token {TOKEN}",
    "Content-Type": "application/json"
}


def get_list(base_url):
    print("\n--- GET LIST ---")
    resp = requests.get(base_url, headers=headers)
    print("Status:", resp.status_code)
    print(json.dumps(resp.json(), indent=2, ensure_ascii=False))


def get_item(base_url, item_id):
    print("\n--- GET ITEM ---")
    resp = requests.get(f"{base_url}{item_id}/", headers=headers)
    print("Status:", resp.status_code)
    print(json.dumps(resp.json(), indent=2, ensure_ascii=False))


def create_item(base_url, data):
    print("\n--- CREATE ITEM ---")
    resp = requests.post(base_url, json=data, headers=headers)
    print("Status:", resp.status_code)
    print(json.dumps(resp.json(), indent=2, ensure_ascii=False))


def update_item(base_url, item_id, data):
    print("\n--- UPDATE ITEM ---")
    resp = requests.put(f"{base_url}{item_id}/", json=data, headers=headers)
    print("Status:", resp.status_code)
    print(json.dumps(resp.json(), indent=2, ensure_ascii=False))


def delete_item(base_url, item_id):
    print("\n--- DELETE ITEM ---")
    resp = requests.delete(f"{base_url}{item_id}/", headers=headers)
    print("Status:", resp.status_code)
    if resp.text:
        print(resp.text)


if __name__ == "__main__":
    BASE_URL = "http://127.0.0.1:8000/api/customers/"

    get_list(BASE_URL)

    get_item(BASE_URL, 1)

    create_item(BASE_URL, {
        "first_name": "Test1",
        "last_name": "User1",
        "email": "test1.user1@example.com"
    })

    update_item(BASE_URL, 2, {
        "first_name": "Updated",
        "last_name": "Name",
        "email": "nastia@example.com"
    })

    delete_item(BASE_URL, 4)

"""from rest_framework.authtoken.models import Token
token = Token.objects.create(user=user)
print(token.key)
"""
