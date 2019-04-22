#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://www.baidu.com")
bsObj = BeautifulSoup(html)
for link in bsObj.findAll("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])

