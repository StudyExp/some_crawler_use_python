# coding:utf-8

import urllib.request
import os
import re


def url_open(url):

    if not ('http' in url):
        url = 'http://'+url
    print('url is :' + url)
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0')
    response = urllib.request.urlopen(req)
    return response.read()


def get_page(url):
    html = url_open(url).decode('utf-8')
    pattern = r'<span class="current-comment-page">\[(\d{4})\]</span>'  #正则表达式寻找页面地址

    print(pattern)

    bbb = re.findall(pattern, html)

    print(bbb)
    # page = int(re.findall(pattern,html)[0])
    page = 150
    return page


def find_imgs(page_url):
    pattern = r'<img src="(.*?\.jpg)"'
    html = url_open(page_url).decode('utf-8')
    img_addrs = re.findall(pattern, html)
    return img_addrs


def save_imgs(img_addrs, page_num, folder):
    if not os.path.exists(str(page_num)):
        os.mkdir(str(page_num))
    os.chdir(str(page_num))
    for i in img_addrs:
        pattern = r'sinaimg.cn/mw600/(.*?).jpg'
        print('pattern is :' + pattern)
        filename = i.split('/')[-1]
        print('filename is :' + filename)
        print(i)

        url_str = i.split('//')[-1]
        url = 'http://'+url_str
        f = open(filename, 'wb')

        req = urllib.request.urlopen(url)
        buf = req.read()

        f.write(buf)
        f.close()

        # image = url_open(urlStr)
        # print(image)

        # with open(filename,'wb') as fnot:
        #     f.write(image)
        #     f.close()


def download_mm(folder='abc', pages=1):
    if not os.path.exists(folder):
        os.mkdir(folder)  # 新建文件夹
        print('成功创建文件夹', folder)

    os.chdir(folder)  #跳转到文件夹
    folder_top = os.getcwd()  #获取当前工作目录
    url = 'http://jandan.net/ooxx/'
    page_num = get_page(url)  #获取网页最新的地址
    print(page_num)
    for i in range(pages):
        page_num -= i  #递减下载几个网页
        page_url = url + 'page-' + str(page_num) + '#comments'  #组合网页地址
        img_addrs = find_imgs(page_url)  #获取图片地址

        print(img_addrs)
        print(folder)
        print(pages)
        save_imgs(img_addrs, page_num, folder)  #保存图片
        os.chdir(folder_top)


if __name__ == '__main__':
    folder = input("Please enter a folder(default is 'abc'): ")
    pages = input("How many pages do you wan to download(default is 10): ")

    # a = str(folder)
    # b = int(pages)
    #
    # print(a)
    # print(b)

    download_mm()