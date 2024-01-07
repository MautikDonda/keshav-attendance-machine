from loguru import logger

logger.add(
    "logs/file.log", rotation="5 MB", backtrace=True, diagnose=True, level="DEBUG", retention="10 days",
    format="[{time}] | {level} | {message}")