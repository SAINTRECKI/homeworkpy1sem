import re
from collections import Counter

def analyze_logs(path):
    stats = Counter({"INFO": 0, "WARNING": 0, "ERROR": 0})
    error_users = set()

    level_pattern = r"\b(INFO|WARNING|ERROR)\b"
    user_pattern = r"\bUser\s+(\d+)\b"

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            level_match = re.search(level_pattern, line)

            if level_match:
                level = level_match.group(1)
                stats[level] += 1

                if level == "ERROR":
                    user_match = re.search(user_pattern, line)

                    if user_match:
                        error_users.add(user_match.group(1))

    for level in ("INFO", "WARNING", "ERROR"):
        print(f"{level}: {stats[level]}")

    print("Пользователи с ошибками:")
    for user in sorted(error_users, key=int):
        print(user)
