import asyncio
import base64
import os
import re

import execjs
from aiohttp_requests import requests
from lxml import etree

HOST = "http://shaoq.com:7777/"
MAIN_PAGE_URL = f"{HOST}exam"

async def req():
    resp  = await requests.get(MAIN_PAGE_URL)
    resp_text = await resp.text()
    print(resp_text)
    image_urls = [f"{HOST}{image.get('src')}" for image in etree.HTML(resp_text).xpath('//img')]
    await asyncio.gather(*[requests.get(image_url) for image_url in image_urls])
    
    resp1 = await requests.get(MAIN_PAGE_URL)
    resp1_text = await resp1.text()
    print('###############################')
    print(resp1_text)
    doc = etree.HTML(resp1_text)

    js = execjs.compile(open(f"{os.path.dirname(__file__)}/js/exam1.js", encoding="utf-8").read())
    css = base64.b64decode(js.call('get_css',resp1_text)).decode()
    print('###############################')
    print(css)

    css_dict = css2dict(css)
    spans = doc.xpath('//span')
    for span in spans:
        span.text = css_dict.get(span.get("class"))

    for bad in doc.xpath("//body/p|//body/script"):
        bad.getparent().remove(bad)

    exam_text = "".join([text.strip() for text in doc.xpath('//body//text()')])
    print('###############################')
    print(exam_text)

def css2dict(css: str) -> dict:
    return dict(re.findall(r'\.(.+)::before {content: "(.+)";}', css))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(req())
