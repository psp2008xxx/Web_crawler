import urllib2
import urllib
import re
import os
from bs4 import BeautifulSoup


def reporthook(block_read, block_size, total_size):
    if not block_read:
        print "Connection Open..."
        return
    if total_size < 0:
        print "Read %s blocks or (%s bytes)" % (block_read, block_read * block_size)
    else:
        ammount_read = block_read * block_size
        print "Read %s blocks or %d/%d" % (block_read, ammount_read, total_size)
    return


def jpg_download(url):
    hdr = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'}
    req = urllib2.Request(url, headers=hdr)

    try:
        html_content = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print e.fp.read()

    bs4Obj = BeautifulSoup(html_content, 'html.parser')
    image_locations = bs4Obj.find_all("input", src=re.compile("jpg$"))
    for link in image_locations:
        req2 = urllib2.Request(link.attrs["src"], headers=hdr)
        html_content2 = urllib2.urlopen(req2).read()
        file_name = os.path.join("D:\download_image",link.attrs["src"].split("/")[-1])
        open(file_name, "wb").write(html_content2)

        # urllib.urlretrieve(link.attrs["src"], os.path.join("D:\download_image",
        #                                                    link.attrs["src"].split("/")[-1]), reporthook=reporthook)


jpg_download("http://cl.mkfye.com/htm_data/16/1608/2013562.html")
