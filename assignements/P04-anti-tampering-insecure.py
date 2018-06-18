'''
Created on Jun 7, 2018

@author: sajid
'''

import hashlib
import hmac
import time


SECRET_KEY = b'super_secret_key^($0'

    
def main():
    file1 = "new_master.txt"
    hash1 = create_digest(file)
#     print("Going to sleep...")
#     time.sleep(5)
    verify_digest(hash1, file1)
    
    
def create_digest(file):
    signed_digest_maker = hmac.new(SECRET_KEY, b'')
    with open(file, 'rb') as f:
        while True:
            block = f.read(1024)
            if not block:
                break
            signed_digest_maker.update(block)
    f.close()
    digest = signed_digest_maker.hexdigest()
    print(digest)
    return digest
    
def verify_digest(actual_digest, file):
    incoming_digest = create_digest(file)
#   comparing hash values as string is vulnerable to timing attack  
    if str(actual_digest) == str(incoming_digest):
        print("OK: digest matches")
    else:
        print("WARNING: Data corruption")
    
    

if __name__=="__main__":
    main()