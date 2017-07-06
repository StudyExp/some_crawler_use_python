#!/usr/bin/python
#-*- coding: utf-8 -*-
#encoding=utf-8

import urllib2
import urllib
import os
from bs4 import BeautifulSoup
def getAllImageLink(index):

    str = 'http://www.dbmeinv.com/?pager_offset=%s' % index

    html = urllib2.urlopen(str).read()

    # html = urllib2.urlopen('http://www.ivsky.com/tupian/mujinhua_v37031/').read()

    soup = BeautifulSoup(html, "lxml")

    liResult = soup.findAll('li', attrs={"class": "span3"})

    # liResult1 = soup.findAll('div', attrs={"class": "il_img"})

    print liResult

    i=0

    for li in liResult:
        i = i+1
        imageEntityArray = li.findAll('img')
        for image in imageEntityArray:
            link = image.get('src')
            imageName = image.get('title')
            # filesavepath = '/Users/cyrill/Desktop/DBMeiNv/%s.jpg' % imageName
            filesavepath = '/Users/cyrill/Desktop/DBMeiNv/%s-%s.jpg' %(index, i)
            urllib.urlretrieve(link, filesavepath)
            print filesavepath

if __name__ == '__main__':
    for index in range(1, 10, 1):
        getAllImageLink(index)



