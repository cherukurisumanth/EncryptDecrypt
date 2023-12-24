import sys, logging
from common import constants
from util.environment_util import get_environment_variable

class CustomStreamToLogger(object):

    def __init__(self, logger, log_level=get_environment_variable('LOG_LEVEL', constants.DEFAULT_LOG_LEVEL)) -> None:
        self.logger = logger
        self.log_level = log_level
        self.linebuf = ''
        self.terminal_std_out = sys.stdout
        self.terminal_std_err = sys.stderr

    def write(self, buf) -> None:
        for line in buf.rstrip().splitlines():
            self.logger.log(getattr(logging, self.log_level), line.rstrip())

    def flush(self) -> None:
        self.terminal_std_out.flush()
        self.terminal_std_err.flush()