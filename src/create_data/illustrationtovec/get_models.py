import os
import wget
import gzip
import shutil

DIR = os.getcwd()

if not os.path.isfile("./tag_list.json.gz")
    url = 'https://github.com/rezoo/illustration2vec/releases/download/v2.0.0/tag_list.json.gz'
    tag_list = wget.download(url)
    with gzip.open(tag_list, 'rb') as f_in:
        with open('tag_list.json', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

if not os.path.isfile("./illust2vec_tag_ver200.caffemodel"):
    url = 'https://github.com/rezoo/illustration2vec/releases/download/v2.0.0/illust2vec_tag_ver200.caffemodel'
    wget.download(url)
