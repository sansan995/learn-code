#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio

async def curl_down(url):
    print('Waiting:', url)
    cmd = "curl -i " + url

    proc = await asyncio.create_subprocess_shell(
            cmd,
            stdout = asyncio.subprocess.PIPE,
            stderr = asyncio.subprocess.PIPE
            )
    stdout, stderr= await proc.communicate()
    print("Done Done Done ")
    return stdout

coroutine1 = curl_down("www.baidu.com")
coroutine2 = curl_down("www.163.com")
coroutine3 = curl_down("www.bilibili.com")

tasks = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3)
]
#asyncio.run(asyncio.wait(tasks))
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print('Task ret: ', task.result())


