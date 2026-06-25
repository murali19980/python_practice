"""
Practice: API Requests
"""
import requests

def fetch_post():
    try:
        resp = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=5)
        print(f"Status Code: {resp.status_code}")
        if resp.status_code == 200:
            data = resp.json()
            print(f"Title: {data.get('title')}")
        else:
            print("Request failed with status:", resp.status_code)
    except requests.exceptions.ConnectionError:
        print("Connection error: Please check your internet.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    fetch_post()
