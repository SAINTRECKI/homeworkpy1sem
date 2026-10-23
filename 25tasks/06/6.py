from pathlib import Path
path = Path(input())
countFiles = countDir = 0
pyFiles = []
size = 0

for child in path.iterdir():
    if child.is_file():
        countFiles += 1
        size += child.stat().st_size
        if child.suffix == '.py':
            pyFiles.append(child.name)
    elif child.is_dir():
        countDir += 1

print("Количество файлов: ", countFiles)
print("Количество подкаталогов: ", countDir)
print("Python Файлы: ")
for temp in pyFiles:
    print(temp)
print(f"Суммарный размер всех файлов: {size} байт")