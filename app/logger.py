import logging

from .enums import Enum
from .settings import LOG_LEVEL

LOG_FORMAT_INFO = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logger = logging.getLogger(__name__)


class LogLevels(Enum):
    info = "INFO"
    warn = "WARN"
    error = "ERROR"
    debug = "DEBUG"


def configure_logging():
    log_level = str(LOG_LEVEL).upper()  # cast to string\
    log_handler = logging.StreamHandler()
    log_handler.setFormatter(LOG_FORMAT_INFO)
    logger.addHandler(log_handler)
    log_levels = list(LogLevels)

    if log_level not in log_levels:
        # we use info as the default loglevel
        logging.basicConfig(level=LogLevels.info)
        return

    if log_level == LogLevels.debug:
        logging.basicConfig(level=log_level, format=LOG_FORMAT_INFO)
        return
    logging.getLogger().setLevel(log_level)
