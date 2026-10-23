import re

text = ("Полезные сайты: https://python.org, "
        "http://example.com/page, "
        "https://example.com/docs/index.html "
        "и ftp://files.example.com/data.")

pattern = r"https?://[^\s,]+"

urls = re.findall(pattern, text)

for url in urls:
    print(url)