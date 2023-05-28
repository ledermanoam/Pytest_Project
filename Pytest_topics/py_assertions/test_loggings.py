import logging
LOGGER = logging.getLogger(__name__)

def test_myloggings():
    logging.warning("warning Logs")
    logging.error("Error Logs")
    LOGGER.critical("critical Logs")
    assert True

