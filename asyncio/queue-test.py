import queue
import pdb

pdb.set_trace()
a = queue.Queue()
a.put("hello")
a.put("world")
print(a.get())
print(a.get())
a.task_done()
a.join()

