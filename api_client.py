import requests

USERS_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_json(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.Timeout as error:
        raise RuntimeError("The server did not answer within 10 seconds.") from error
    except requests.exceptions.ConnectionError as error:
        raise RuntimeError("Could not connect to the server.") from error
    except requests.exceptions.HTTPError as error:
        status = error.response.status_code
        raise RuntimeError(f"The server returned status {status} for {url}.") from error
    except requests.exceptions.RequestException as error:
        raise RuntimeError("The request failed.") from error
    return response.json()
