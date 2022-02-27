import logging

logger= logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s [%(levelname)-5.5s] %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
