def read_file(path):
    try:
        file = open(path)
        return file.read()
    except FileNotFoundError:
        print("Файл не найден")
    except PermissionError:
        print("Нет доступа к файлу")
    except UnicodeDecodeError:
        print("Ошибка чтения файла")
    except OSError:
        print("Ошибка операционной системы")
