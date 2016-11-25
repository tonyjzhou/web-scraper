from urllib.request import urlopen

from bs4 import BeautifulSoup

html = urlopen("http://wired.com")
print(BeautifulSoup(html.read(), "html.parser"))
