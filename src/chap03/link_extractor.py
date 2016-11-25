from urllib.request import urlopen

from bs4 import BeautifulSoup

html = urlopen("http://www.wsj.com")
bs_object = BeautifulSoup(html, "html.parser")
url_attr = 'href'
for link in bs_object.findAll("a"):
    if url_attr in link.attrs:
        print(link.attrs[url_attr])
