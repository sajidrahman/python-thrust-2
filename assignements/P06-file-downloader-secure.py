'''
Created on Jun 10, 2018

@author: sajid
'''
from pip._vendor.distlib.compat import raw_input

from urllib.parse import urlparse
from urllib.parse import urlsplit
import urllib.request, urllib.parse, urllib.error
import sys
import ssl

def main():
    input = raw_input(">Enter url - ")
    url = urlparse(input)
    if not url.scheme == 'https':
        sys.exit("Only HTTPS links are allowed for file download operation.")
    download_file(input)

def download_file(url):
    blocksize = 1000000
    ctx = ssl.create_default_context()
    ctx.check_hostname = True
    ctx.verify_mode = ssl.CERT_REQUIRED
    
    try:
        temp_downloaded_file = urllib.request.urlopen(url, context = ctx)
        downloaded_filename = url.rsplit('/', 1)[-1]
        filehandler = open(downloaded_filename, 'wb')
        size = 0
        
        while True:
            chunks = temp_downloaded_file.read(blocksize)
            if len(chunks) < 1:
                break
            size+= len(chunks)
            filehandler.write(chunks)
        
        print(size, 'characters downloaded')
        filehandler.close()
        
    except Exception as e:
        print(str(e))


if __name__=="__main__":
    main()