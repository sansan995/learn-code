import threading
import requests
import os

def main():
    crete_die('pic')
    queue = [ i for i in range(1, 72) ]
    threads = []
    while len(queue) > 0:
        for thread in threads:
            if not thread.is_alive():
                threads.remove(thread)

        while len(threads) < 5 and len(queue) > 0:
            cur_page = queue.pop(0)
            url = 'https://meizitu.com/a/more_{}.html'.format(cur__page)
            thread = therading.Thread(target=execute, args=(url,))
            thread.setDaemon(True)
            thread.start()
            print('{}download this page number')
            therads.append(thread)
