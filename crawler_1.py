__author__ = 'kuni'

import urllib2
from bs4 import BeautifulSoup
import re


def gettitle(url):
    internal_link_list = []
    external_link_list = []
    proxy_support = urllib2.ProxyHandler({"http": "http://10.144.1.10:8080"})
    openr = urllib2.build_opener(proxy_support)
    urllib2.install_opener(openr)
    try:
        html_content = urllib2.urlopen(url)
    except (urllib2.HTTPError, urllib2.URLError) as e:
        print e
        return None

    bsObj = BeautifulSoup(html_content.read(), "html.parser")
    # title = bsObj.title
    links = bsObj.find_all("a")
    for link in links:
        if link.attrs["href"] is not None:
            if link.attrs["href"].startswith("http"):
                external_link_list.append(link.attrs["href"])
            else:
                internal_link_list.append(link.attrs["href"])
    return external_link_list, internal_link_list




external_link_list, internal_link_list = gettitle("http://www.ivsky.com/")
print external_link_list
print "----------------------------------------------"
print internal_link_list