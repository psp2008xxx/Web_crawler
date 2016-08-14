#!/usr/bin/python
#coding=utf-8


import pymysql
import urllib2
import re
from bs4 import BeautifulSoup



base_url = "http://www.netbian.com"
conn = pymysql.connect(host="127.0.0.1", user="root", passwd="password", db="scraping")
cur = conn.cursor()
cur.execute("USE scraping")
cur.execute('SET NAMES utf8;')
cur.execute('SET CHARACTER SET utf8;')
cur.execute('SET character_set_connection=utf8;')


def store_data(title, content):
    cur.execute("INSERT TABLE pages(title, content) VALUES(\"%s\", \"%s\")", (title, content))
    cur.connection.commit()

def get_links(url):
    sub_link_contents = {}
    html_content = urllib2.urlopen(url)
    bs4Obj = BeautifulSoup(html_content, "html.parser")
    sub_urls = bs4Obj.findAll("a",{"href":re.compile(".*"), "title":re.compile(".*")})

    for sub_url in sub_urls:
        sub_link_contents[sub_url.attrs["title"]] = base_url + sub_url.attrs["href"]
    return sub_link_contents

link_contents = get_links(base_url)
for title,link_content in link_contents.items():
    print title, link_content
    store_data(title, link_content)

