import os, time, signal

def chldhandler(signum, stackframe):
    while 1:
        try:
            result = os.waitpid(-1, os.WNOHANG)
        except:
            break
        print("Reapend child process %d" % result[0])

signal.signal(signal.SIGCHLD, chldhandler)

print('Before the fork, my PID is', os.getpid())

pid = os.fork()

if pid:
    print("hello form PID %d" % pid)
    time.sleep(10)
    print('sleep done')
else:
    print('child sleeping 5')
    time.sleep(5)
