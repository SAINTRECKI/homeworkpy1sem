import re
import json
import logging
from collections import Counter

logging.basicConfig(
    filename="processing.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

def analyze_log(path):
    methods = Counter()
    urls = Counter()
    errors_4xx = 0

    pattern = re.compile(
        r"^\S+\s+\S+\s+(\d{1,3}(?:\.\d{1,3}){3})\s+"
        r"(GET|POST|PUT|DELETE|PATCH|HEAD|OPTIONS)\s+"
        r"(\S+)\s+(\d{3})$"
    )

    try:
        logging.info("Начало обработки файла")

        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                match = pattern.search(line.strip())

                if not match:
                    logging.warning("Некорректная строка")
                    continue

                ip, method, url, status = match.groups()

                methods[method] += 1
                urls[url] += 1

                if 400 <= int(status) < 500:
                    errors_4xx += 1

        most_common_url = (
            urls.most_common(1)[0][0] if urls else None
        )

        stats = {
            "methods": dict(methods),
            "errors_4xx": errors_4xx,
            "most_common_url": most_common_url
        }

        with open("statistics.json", "w", encoding="utf-8") as file:
            json.dump(stats, file, indent=4, ensure_ascii=False)

        logging.info("Обработка завершена успешно")
        print(stats)

    except FileNotFoundError:
        logging.error("Файл не найден")
        print("Ошибка: файл не найден")

    except PermissionError:
        logging.error("Недостаточно прав доступа")
        print("Ошибка: недостаточно прав доступа")

    except UnicodeError as e:
        logging.error("Ошибка декодирования: %s", e)
        print("Ошибка чтения содержимого файла")

    except OSError as e:
        logging.error("Ошибка работы с файлом: %s", e)
        print("Ошибка операционной системы")


analyze_log("access.log")