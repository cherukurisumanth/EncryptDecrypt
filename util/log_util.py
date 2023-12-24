import sys, logging, re, uuid, os
from common import constants
from util.environment_util import get_environment_variable
from util.custom_stream_logger import CustomStreamToLogger
from util.log_util_masked_expressions import REGEX_EXPRESSIONS_TO_MASK

ID_STR:str = "<is_str>"
APP_ID_STR:str = "<app_id_str>"
LOG_FORMAT:str = f"%(asctime)s | %(levelname)s | {APP_ID_STR} | %(name)s | {ID_STR} | %(threadName)s | %(message)s"
MASKED_STR:str = "*****<MASKED>*****"

class MaskedFilter(logging.Filter):

    def filter(self, record:logging.LogRecord) -> bool:
        try:

            result_str = self._mask_line(record.getMessage())
            record.msg = result_str
            record.args = None
            return True
        except Exception as e:
            return False
        
    
    def _mask_line(self, message:str) -> str:
        result_str = message.rstrip()
        for key in REGEX_EXPRESSIONS_TO_MASK.keys():
            for regex_exp_str in REGEX_EXPRESSIONS_TO_MASK[key]:
                str_to_print = f"{key}:{MASKED_STR}"
                result_str = re.sub(regex_exp_str, str_to_print, result_str, flags=re.IGNORECASE)
        return result_str
    

def _get_new_uuid():
    return uuid.uuid4()


def _get_handlers(log_location:str, print_to_console:bool=True) -> list:
    handlers = []
    # File logger as standard
    fh = logging.FileHandler(filename=log_location, mode='a')
    handlers.append(fh)

    #Print to stdout only if needed
    if print_to_console:
        sh = logging.StreamHandler()
        handlers.append(sh)
    
    for handler in handlers:
        handler.addFilter(MaskedFilter())

    return handlers


def _initialize():
    log_level = get_environment_variable('LOG_LEVEL', constants.DEFAULT_LOG_LEVEL)
    log_location = get_environment_variable('LOG_FILE', constants.DEFAULT_LOG_FILE)
    print_to_console = get_environment_variable('PRINT_TO_CONSOLE', constants.DEFAULT_PRINT_TO_CONSOLE).lower() in ('true', '1', 't')
    log_format = LOG_FORMAT.replace(ID_STR, f"{constants.DEFAULT_HANDLER_TRACE_ID_FIELD}={str(_get_new_uuid())}")
    log_format = log_format.replace(APP_ID_STR, f"{constants.DEFAULT_APP_ID_FIELD}={constants.APP_NAME}")

    handlers = _get_handlers(log_location=log_location, print_to_console=print_to_console)

    logging.basicConfig(
        level=getattr(logging, log_level),
        format=log_format,
        handlers=handlers
    )


def configure_standard_loggers():
    _initialize()
    stdout_logger = logging.getLogger('STDOUT')
    sl = CustomStreamToLogger(stdout_logger)
    sys.stdout = sl

    stderr_logger = logging.getLogger('STDERR')
    sl = CustomStreamToLogger(stderr_logger)
    sys.stderr = sl