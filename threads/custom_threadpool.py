import logging
from concurrent.futures import ThreadPoolExecutor

audit_logger = logging.getLogger('audit')
app_logger = logging.getLogger('app')

class CustomThreadPool:

    def __init__(self, workers:int=10) -> None:
        app_logger.info(f"Initializing with {workers} workers.")
        self.threadpool = ThreadPoolExecutor(max_workers=workers)

    def get_threadpool(self):
        return self.threadpool
    
    def execute_thread(self, function, *argv):
        app_logger.info(f"Executing with {function}.")
        self.threadpool.submit(function, argv)