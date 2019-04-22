import thread
from time import sleep, ctime

def loop0():
    print("start loop 0 at:", ctime())
    sleep(4)
    print('loop 0 done at:', ctime())

def loop1():
    print("start loop 1 at:", ctime())
    sleep(4)
    print('loop 1 done at:', ctime())

def mian():
    print('starting at', ctime())
    thread.start_new_thread(loop0, ())
    thread.start_new_thread(loop1, ())
    sleep(5)
    print("all Done")

mian()

