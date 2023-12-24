import queue

class CustomQueue:

    def __init__(self, maxsize:int=0) -> None:
        self.task_queue = queue.Queue(maxsize=maxsize)

    def initialize_queue(self) -> None:
        self.task_queue = queue.Queue()

    def add_to_queue(self, job:object) -> None:
        self.task_queue.put(job)

    def get_queue_size(self) -> int:
        self.task_queue.qsize()

    def get_from_queue(self) -> any:
        try:
            return self.task_queue.get(block=False)
        except queue.Empty:
            return None
