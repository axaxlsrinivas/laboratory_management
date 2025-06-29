import requests

def test_google_search_api():
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": "test",
        "key": "YOUR_API_KEY",
        "cx": "YOUR_SEARCH_ENGINE_ID"
    }
    response = requests.get(url, params=params)
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())

if __name__ == "__main__":
    test_google_search_api()
