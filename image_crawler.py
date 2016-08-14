import urllib2
import urllib
import re
import os
import time
from bs4 import BeautifulSoup


hdr = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    # 'Connection': 'keep-alive'}
}


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


def get_sublinks(url):
    req = urllib2.Request(url, headers=hdr)

    try:
        html_content = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print e.fp.read()

    bs4Obj = BeautifulSoup(html_content, 'html.parser')
    html_content.close()
    image_links = bs4Obj.find_all("h3")
    sub_links_dict = {}
    for link in image_links:
        if link.find("a", href=re.compile("^htm_data")) and link.get_text().endswith("P]"):
            sub_links_dict[link.a.attrs["href"].split("/")[-1].replace(".html", "")] = "http://cl.mkfye.com/" + \
                                                                                       link.a.attrs["href"]

    print sub_links_dict
    return sub_links_dict


def download_image(url_dict):
    for link_key, values in url_dict.items():
        req = urllib2.Request(values, headers=hdr)
        sub_directory = "D:\download_image" + os.sep + link_key
        os.mkdir(sub_directory)
        image_locations = ""
        try:
            html_content = urllib2.urlopen(req)
            bs4Obj = BeautifulSoup(html_content, 'html.parser')
            html_content.close()
            image_locations = bs4Obj.find_all("input", src=re.compile("(jpg|jpeg)$"))
        except:
            print "You Got error 1 here"

        for link in image_locations:
            print link.attrs["src"]
            try:
                req2 = urllib2.Request(link.attrs["src"], headers=hdr)
                html_content2 = urllib2.urlopen(req2)
                file_name = os.path.join(sub_directory, link.attrs["src"].split("/")[-1])
                with open(file_name, "wb") as f:
                    f.write(html_content2.read())
                html_content2.close()
            except:
                print "You got Error 2 here"
                time.sleep(5)


            # urllib.urlretrieve(link.attrs["src"], os.path.join("D:\download_image",
            # link.attrs["src"].split("/")[-1]), reporthook=reporthook)


sub_links_dict = get_sublinks("http://cl.mkfye.com/thread0806.php?fid=16")
download_image(sub_links_dict)