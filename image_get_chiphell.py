import urllib2
import re
import os
import requests
from bs4 import BeautifulSoup


hdr = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'}


def get_sublinks(url):
    session = requests.session()
    source_content = session.get(url, headers=hdr)
    bs4Obj = BeautifulSoup(source_content.content, 'html.parser')
    image_links = bs4Obj.find_all("a", href=re.compile("^forum.*yes$"))
    # return image_links
    for link in image_links:
        page_url = "https://www.chiphell.com/" + link.attrs["href"]
        req2 = session.get(page_url, headers=hdr)
        html_content2 = urllib2.urlopen(req2)
        file_name = os.path.join(r"D:\download_image", link.attrs["src"].split("/")[-1])
        with open(file_name, "wb") as f:
            f.write(html_content2.read())
            html_content2.close()

def get_sublinks_2(url):
    session = requests.session()
    page_url = "https://www.chiphell.com/" + url
    source_content = session.get(page_url, headers=hdr)
    print source_content.text




def download_image(image_links):
    for link in image_links:
        req2 = urllib2.Request(link.attrs["href"], headers=hdr)
        html_content2 = urllib2.urlopen(req2)
        file_name = os.path.join(r"D:\download_image", link.attrs["src"].split("/")[-1])
        with open(file_name, "wb") as f:
            f.write(html_content2.read())
            html_content2.close()


get_sublinks_2("forum.php?mod=attachment&amp;aid=NjM2MDAxOXwwNjIzOGExNHwxNDcxOTQzODM2fDB8MTYzMDgwNg%3D%3D&amp;nothumb=yes")
# download_image(image_links)