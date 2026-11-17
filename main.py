from api_client import fetch_json, POSTS_URL, USERS_URL
from reporter import build_report, format_table, save_report

def main():
    try:
        users = fetch_json(USERS_URL)
        posts = fetch_json(POSTS_URL)
    except RuntimeError as error:
        print(error)
        return
    rows = build_report(users, posts)
    print(format_table(rows))


if __name__ == "__main__":
    main()