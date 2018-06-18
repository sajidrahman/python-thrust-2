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
    # insecure for Python versions prior to 2.7.9, no explicit hostname or certificate verification performed
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
        
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)    
    except Exception as e: #All other exceptions
        print(str(e))


if __name__=="__main__":
    main()