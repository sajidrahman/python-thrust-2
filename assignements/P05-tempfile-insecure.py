'''
Created on Jun 18, 2018

@author: sajid
'''

import tempfile

tempfile.tempdir = '/Users/sajid/Desktop'

print('gettempdir():', tempfile.gettempdir())

def main():
    text_content = 'Lorem ipsum dolor sit amet, te stet diceret impedit cum. Ea est noster option, ut mei elitr suscipit, sed ne docendi urbanitas. Eum persecuti persequeris mediocritatem ne, ferri aperiam accommodare sea ad, usu id sumo justo maiestatis. Mel eu populo sensibus consectetuer, qui ei noluisse indoctum, labore numquam id mei. Altera quaerendum interpretaris cu eam, ius cu dicat fierent convenire, ex dolorum inciderint has.'
    create_temp_file('_suffix','prefix_', text_content)

def create_temp_file(_suffix, prefix_, content):
    tempfilename = tempfile.mktemp(suffix=_suffix, prefix=prefix_, dir=None)
    with open(tempfilename, "w") as temp:
        temp.write(content)

        print(temp.name)
        return temp.name

if __name__=="__main__":
    main()