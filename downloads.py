#Download images using file containing image URLs
import urllib
import csv


f = open('imgs.txt','w')
input_file = open('imgurls.txt','r')
for line in input_file:
    line = line.replace('\n', '')
    URL= line
    IMAGE = URL.rsplit('/',1)[1]
    urllib.urlretrieve(URL, IMAGE)
    f.write(URL + '\n')

f.close() # you can omit in most cases as the destructor will call if
