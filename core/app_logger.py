import logging

from core import Settings

config = Settings()
config.configure()

log_format = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"

logging.basicConfig(
    handlers=[
        logging.FileHandler(
            filename=config.log_path,
            mode=config.log_mode
        ),
    ],
    format=log_format,
    level=config.verbosity
)
logging.getLogger('faker').setLevel(logging.ERROR)


def get_logger(name='logger'):
    logger = logging.getLogger(name)
    return logger
