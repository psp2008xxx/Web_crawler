import urllib2
import re
import os
import requests
from bs4 import BeautifulSoup
import shutil
import time


hdr = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'}


def download_image(url):
    session = requests.session()
    source_content = session.get(url, headers=hdr)
    bs4Obj = BeautifulSoup(source_content.content, 'html.parser')
    image_links = bs4Obj.find_all("a", {"href":re.compile("^forum.*nothumb=yes$"), "class":"xw1"})
    for link in image_links:
        time.sleep(2)
        page_url = "https://www.chiphell.com/" + link.attrs["href"].replace('&amp;','&')
        page_content = session.get(page_url, headers=hdr, stream=True)
        file_name = os.path.join(r"D:\download_image", link.get_text())
        with open(file_name, "wb") as f:
            page_content.raw.decode_content = True
            shutil.copyfileobj(page_content.raw, f)




download_image("https://www.chiphell.com/thread-1630806-1-1.html")
