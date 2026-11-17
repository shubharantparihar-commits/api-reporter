import requests

def main():
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        print("The server did not answer within 10 seconds.")
        return
    except requests.exceptions.ConnectionError:
        print("Could not connect to the server.")
        return
    except requests.exceptions.HTTPError as error:
        print(f"The server returned {error.response.status_code}.")
        return
    except requests.exceptions.RequestException:
        print("The request failed.")
        return
    users = response.json()
    print(type(users).__name__, len(users))
    for user in users:
        print(user["name"]+",", user["address"]["city"])
    

if __name__ == "__main__":
    main()
