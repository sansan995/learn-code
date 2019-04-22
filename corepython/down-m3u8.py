import aiohttp
import asyncio
import re

def merge_file(path):
    os.chdir(path)
    cmd = "copy /b * new.tmp"
    cmd_del = "del /Q"
    os.system(cmd)
    os.system(cmd_del + '*.ts')
    os.system(cmd_del + '*.mp4')
    os.rename("new.tmp", "new.mp4")

async def download(url):
    download_path = os.getcwd() + "\downts"
    if not os.path.exists(download_path):
        os.mkdir(download_path)

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    url = 'https://135zyv6.xw0371.com/2019/03/15/YvMKCpwDW6HZ8lUk/playlist.m3u8'
    downpath = []
    async with aiohttp.ClientSession() as session:
        m3u8 = await fetch(session, url)
        if "EXTM3U" not in m3u8:
            raise BaseException('file is not m3u8')
        
        file_line = m3u8.split("\n")
        #print(file_line)
        for i in file_line:
            if re.match(r'[^#]', i):
        #        print(i)
                downpath.append(i)
            
loop = asyncio.get_event_loop()
loop.run_until_complete(main())



