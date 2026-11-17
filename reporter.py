import json
from pathlib import Path

def build_report(users, posts):
    counts = {user["id"]: 0 for user in users}
    for post in posts:
        user_id = post["userId"]
        if user_id in counts:
            counts[user_id] = counts[user_id] + 1
    rows = []
    for user in users:
        rows.append({
            "userId": user["id"],
            "name": user["name"],
            "city": user["address"]["city"],
            "postCount": counts[user["id"]],
        })
    rows.sort(key=lambda row: (-row["postCount"], row["name"]))
    return rows

def save_report(rows, path):
    text = json.dumps(rows, indent=2)
    Path(path).write_text(text, encoding="utf-8")

def format_table(rows):
    header = f"{'Name':<24}{'City':<16}{'Posts':>5}"
    lines = [header]
    for row in rows:
        lines.append(f"{row['name']:<24}{row['city']:<16}{row['postCount']:>5}")
    return "\n".join(lines)
