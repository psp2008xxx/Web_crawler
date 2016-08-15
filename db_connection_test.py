#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymysql
import urllib2
import re
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')


base_url = "http://www.netbian.com"
conn = pymysql.connect(host="127.0.0.1", user="root", passwd="password", db="scraping", charset='utf8')
cur = conn.cursor()
cur.execute("USE scraping")


def store_data(title, content):
    sql_command = "INSERT INTO pages (title, content) VALUES(\"%s\", \"%s\")" % (title.encode("utf-8"), content)
    cur.execute(sql_command)
    cur.connection.commit()


def get_links(url):
    sub_link_contents = {}
    html_content = urllib2.urlopen(url)
    bs4Obj = BeautifulSoup(html_content, "html.parser")
    sub_urls = bs4Obj.findAll("a", {"href": re.compile(".*"), "title": re.compile(".*")})

    for sub_url in sub_urls:
        # sub_url.attrs["title"] = sub_url.attrs["title"].encode('utf-8')
        # print sub_url.attrs["title"].__class__
        sub_link_contents[sub_url.attrs["title"]] = base_url + sub_url.attrs["href"]
    return sub_link_contents


link_contents = get_links(base_url)
for title, link_content in link_contents.items():
    store_data(title, link_content)
cur.close()
conn.close()

