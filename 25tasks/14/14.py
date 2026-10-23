class LogOperation:
    def __init__(self, filename, operation):
        self.filename = filename
        self.operation = operation

    def __enter__(self):
        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(f"START: {self.operation}\n")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        with open(self.filename, "a", encoding="utf-8") as file:
            if exc_type is not None:
                file.write(f"ERROR: {self.operation}\n")
            else:
                file.write(f"END: {self.operation}\n")

        return False


def log_operation(filename, operation):
    return LogOperation(filename, operation)