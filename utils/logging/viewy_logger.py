import time

class VLogger:

    @staticmethod
    def log(level: str, message: str) -> None:
        with open("utils/logging/logs", "a") as file:
            file.write(f"{level} <{time.ctime()}> {message}\n")

    @staticmethod
    def info(message: str) -> None:
        VLogger.log("[INFO]", message)

    @staticmethod
    def debug(message: str) -> None:
        VLogger.log("[DEBUG]", message)

    @staticmethod
    def warning(message: str) -> None:
        VLogger.log("[WARNING]", message)

    @staticmethod
    def error(message: str) -> None:
        VLogger.log("[ERROR]", message)
