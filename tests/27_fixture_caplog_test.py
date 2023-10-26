from db_calculator import Calculator
import logging
import  pytest


# pytest tests/27_fixture_caplog_test.py -v
# pytest tests/27_fixture_caplog_test.py -vs --log-format="%(asctime)s %(levelname)s %(message)s" --log-date-format="%Y-%m-%d %H:%M:%S"


# loggin.NOTSET     0
# loggin.DEBUG      10
# loggin.INFO       20
# loggin.WARNING    30
# loggin.ERROR      40
# loggin.CRITICAL   50


# 1

def test_caplog(caplog):
    logger = logging.getLogger("my_logger")
    logger_2 = logging.getLogger("my_logger_2")
    logger.setLevel(logging.DEBUG)
    logger_2.setLevel(logging.DEBUG)
    MY_LOG_LEVEL = 51
    logging.addLevelName(MY_LOG_LEVEL, "STEP")

    # logger.setLevel(logging.WARNING)

    # Something is wrong with this !!!
    # caplog.set_level(logging.WARNING, logger=logger.name)
    # caplog.set_level(logging.WARNING, logger=logger_2.name)
    # with caplog.at_level(logging.WARNING, logger=logger_2.name):

    logger.debug("This is a debug message")
    logger.info("This is a info message")
    logger.warning("This is a warning message")
    logger.error("This is a error message")
    logger.critical("This is a critical message")
    logger.log(MY_LOG_LEVEL, "This is a step message")

    logger_2.debug("2 This is a debug message")
    logger_2.info("2 This is a info message")
    logger_2.warning("2 This is a warning message")
    logger_2.error("2 This is a error message")
    logger_2.critical("2 This is a critical message")
    logger_2.log(MY_LOG_LEVEL, "2 This is a step message")


    print('\n----caplog.messages----')
    for message in caplog.messages:
        print(message)

    print('\n----caplog.text----')
    print(caplog.text)

    print('\n----caplog.records----')
    for record in caplog.records:
        print(record)

    print('\n----caplog.record_tuples----')
    for record_tuple in caplog.record_tuples:
        print(record_tuple)

    # caplog.clear()

    assert "This is a debug message" in caplog.text
    assert "This is a info message" in caplog.text
    assert "This is a warning message" in caplog.text
    assert "This is a error message" in caplog.text
    assert "This is a critical message" in caplog.text
    assert "This is a step message" in caplog.text
    # assert "ERROR 33" in caplog.text
