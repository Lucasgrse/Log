class LoggerFactory:
    def get_logger(self, type):
        if type == "file":
            return FileLogger()
        elif type == "console":
            return ConsoleLogger()

class FileLogger:
    def log(self, message):
        with open("log.txt", "a") as f:
            f.write(message + "\n")

class ConsoleLogger:
    def log(self, message):
        print(message)

if __name__ == "__main__":
    import sys

    log_type = sys.argv[1] if len(sys.argv) > 1 else "console"
    factory = LoggerFactory()
    logger = factory.get_logger(log_type)

    for i in range(1, 11):
        logger.log(str(i))


