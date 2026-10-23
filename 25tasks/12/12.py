from re import finditer
text = []
while True:
    line = input()
    if line == '':
        break
    text.append(line)

pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
emails = []
for line in text:
        for match in finditer(pattern, line):
            email = match.group()
            if email not in emails:
                emails.append(match.group())

for mail in emails:
    print(mail)