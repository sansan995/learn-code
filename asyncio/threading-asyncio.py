from threading import Thread

def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

def more_work(x):
    print(f'More world{x}')
    time.sleep(x)
    print(f'Finished more work{x}')

start = now()
new_loop = asyncio.new_event_loop()
t = Thread(target = start_loop, args = (new_loop,))
t.start()
print(f'TIME:{time.time()-start}')

new_loop.call_soon_threadsafe(more_work, 6)
new_loop.call_soon_threadsafe(more_work, 3)
