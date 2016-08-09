__author__ = 'kuni'

import re
import urllib2
from bs4 import BeautifulSoup

pages = set()


def get_web_links(pageUrl):
    # proxy_support = urllib2.ProxyHandler({"http": "http://10.144.1.10:8080"})
    # openr = urllib2.build_opener(proxy_support)
    # urllib2.install_opener(openr)

    global pages
    html_content = urllib2.urlopen("http://www.ivsky.com" + pageUrl)
    bsObj = BeautifulSoup(html_content, 'html.parser')
    for link in bsObj.find_all("a", {"href": re.compile("^(/tupian/)")}):
        if "href" in link.attrs:
            if link.attrs["href"] not in pages:
                new_page = link.attrs["href"]
                print new_page + " (" + link.get_text() + ")"
                pages.add(new_page)
                get_web_links(new_page)


get_web_links("")