import requests
import json
from bs4 import BeautifulSoup
import re
url = 'https://www.ahu.cc/index.php?s=vod-play-id-47755-sid-3-pid-8.html'
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0'}
list = []

def get_page(url):
    try:
        response = requests.get(url, headers=headers, timeout = 10)
        if response.status_code == 200:
            return response.text
        return None
    except(RequestException):
        return None

def parse_page(html):
    doc = BeautifulSoup(html, 'lxml')
    item = doc.find_all(attrs={"class":'left'})
    items = str(item).split(',')
    
    for i in items:
        if re.search('https', i):
            i = re.sub('\\\/','/',i)
            list.append(i)

def get_m3u8_url(url):
    try:
        content = requests.get(url, headers = headers).text
        data = json.loads(content)
        

html = get_page(url)
parse_page(html)
print(list)
