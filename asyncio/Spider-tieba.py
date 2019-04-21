import urllib.request

def loadPage(url, filename):
    print("download " + filename)
    headers = {'User-Agent':'Mozilla/5.0'}
    request = urllib.request.Request(url, headers = headers)
    content = urllib.request.urlopen(request).read()
    return content

def writePage(html, filename):
    print('saveing ' + filename)
    with open(unicode(filename, 'utf-8'), 'w') as f:
        f.write(heml)
    print('_' * 30)

def tiebaSpider(url, beginPage, endPage):
    for page in range(beginPage, endPage + 1):
        pn = (page - 1) * 50
        filename = 'now' + str(page) + '.html'
        fullurl = url + '&pn' + str(pn)
        html = loadPage(fullurl, filename)
        writePage(html, filename)

if __name__ == '__main__':
    kw = raw_input('now- tieba name:')
    beginPage = int(raw_input('start:'))
    endPage = int(raw_input('end:'))

    url = 'https://teba.baidu.com/f?'
    key = urllib.parse.urlencode({'kw':kw})
    fullurl = url + key
    tiebaSpider(fullurl, beginPage, endPage)

