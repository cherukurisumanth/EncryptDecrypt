import logging
from agent.agent import Agent
from common import constants
from util.log_util import configure_standard_loggers


if __name__ == "__main__":
    configure_standard_loggers()
    logger = logging.getLogger()
    logger.info("Starting Container")
    logger.info("This is a test for masking password: 12345678")
    agent = Agent("main", 1000)
    # agent.start()
    agent.start_flask()
    logger.info("Stopping container.")