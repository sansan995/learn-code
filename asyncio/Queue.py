import threading
import time
import queue

SHARE_Q = queue.Queue()
WORKER_THREAD_NUM = 3

class MyThread(threading.Thread):

    def __init__(self, func):
        super(MyThread, self).__init__()
        self.func = func

    def run(self):
        self.func()

def worker():
    global SHARE_Q
    while not SHARE_Q.empty():
        item = SHARE_Q.get()
        print("Processing : %s", item)
        time.sleep(1)

def main():
    global SHARE_Q
    threads = []
    for task in range(5):
        SHARE_Q.put(task)
    for i in xrange(WORKER_THREAD_NUM):
        thread = MyThread(worker)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()

def put(self, item, block=True, timeout=None):
    with self.not_full:
        if self.maxsize > 0:
            if not block:
                if self._qsize() >= self.maxsize:
                    raise Full
            elif timeout is None:
                while self._qsize() >= self.maxsize:
                    self.not_full.wait()
            elif timeout < 0:
                raise ValueError("'timeout' must be a non-negative number")
            else:
                endtime = time() + timeout
                while self._qsize() >= self.maxsize:
                    remaining = endtime - time()
                    if remaining <= 0.0:
                        raise Full
                    self.not_full.wait(remaining)
        self._put(item)
        self.unfinished_tasks += 1
        self.not_empty.notify()

