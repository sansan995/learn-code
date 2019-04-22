#!/usr/bin/env python3

import asyncio

async def curl_down(url):
    print("Waiting:{}".format(url))
    cmd = "curl -i " + url

    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout = asyncio.subprocess.PIPE,
        stderr = asyncio.subprocess.PIPE
        )
    stdout, stderr = await proc.communicate()
    print("DOne Done DOne")
    print(stdout)
    return stdout

async def main():
    await asyncio.gather(
        curl_down("www.baidu.com"),
        curl_down("www.163.com"),
        curl_down("www.126.com"),
        )
    
asyncio.run(main())
    
