import logging
from market_maker.utils.Colorer import ColoredFormatter
from market_maker.settings import settings


def setup_custom_logger(name, log_level=settings.LOG_LEVEL):
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(levelname)s - %(module)s - %(message)s"
    )

    cf = ColoredFormatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s")

    handler = logging.StreamHandler()

    handler.setFormatter(formatter)
    # handler.setFormatter(cf)

    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    logger.addHandler(handler)
    return logger
