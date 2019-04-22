from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print('error urlopen():'+ e)

    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError as e:
        print("error read:" + e)
    return title 
title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print('Title could not be fould')
else:
    print(title)

