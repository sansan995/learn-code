#!/usr/bin/env python3

# countdown.py
# 用户自定义类可以通过提供__getstate__() 和 __setstate__()
# pickle.dump() 就会调用_getstate__()获取序列化的对象
# pickle.loads() 就会调用__setstate__()反序列化调用
import time
import threading

class Countdown:
    def __init__(self, n):
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.daemon = True
        self.thr.start()

    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)

    def __getstate__(self):
        return self.n

    def __serstate__(self, n):
        self.__init__(n)

