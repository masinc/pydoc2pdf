#coding: utf-8

from bs4 import BeautifulSoup
import requests
import pdfkit
import os, shutil, re

# 3.5 や 3.6など
version = '3.6'

#カテゴリを以下から指定する
# whatsnew What's New in Python
# tutorial  チュートリアル
# library   ライブラリリファレンス
# reference 言語リファレンス
# setup     Pythonのセットアップと利用
# installing    Pythonモジュールのインストール
# distributing Pythonモジュールの配布
# c-api     Python/C API
# howto     Python HOWTO
# faq       Python FAQ
category = 'library'



URL_BASE = f"https://docs.python.jp/{version}/{category}/"
DIR_BASE = os.path.dirname(os.path.abspath(__file__))

#HTMLを書き込む
def write_html(filename, text):
    with open(filename , "w", encoding='utf-8') as f:
        f.write(text)

#urlからパースしてコンテンツを読み込む
def get_html_contents(file):
    r = requests.get(URL_BASE + file)
    r.encoding = 'utf-8'
    return BeautifulSoup(r.text.encode(), "html.parser").select_one('.body > .section')

def mkdirs(str):
    try:
        os.makedirs(str)
    except:
        pass


def main():
    HTML_INDEX = 'index.html'
    DIR_TMP = os.path.join(DIR_BASE, 'tmp', version, category) 
    print(DIR_TMP)
    DIR_OUT = os.path.join(DIR_BASE, 'out', version) 
    print(DIR_OUT)

    mkdirs(DIR_TMP)
    mkdirs(DIR_OUT)

    #まずindex.htmlを取得する
    index_html = get_html_contents(HTML_INDEX)
    write_html(os.path.join(DIR_TMP,HTML_INDEX), index_html.prettify())

    #index.htmlから同階層のURL一覧を取得する
    files = [file for file in 
                [a.get('href') for a in index_html.find_all('a') ] #<a href="">を抽出
                if not('#' in file) and not(':' in file) # #や:の含まない相対URLのみを抽出
    ]


    for file in files:
        html =  get_html_contents(file)    
        write_html(os.path.join(DIR_TMP, file),  html.prettify())        
        print(f"write: {file}")

    paths = [ os.path.join(DIR_TMP, path) for path in [HTML_INDEX] + files]

    options = {
        'margin-top': '0.1in',
        'margin-right': '0.1in',
        'margin-bottom': '0.1in',
        'margin-left': '0.1in',
        'encoding' : 'UTF-8',
        # 'no-outline' : None
    }
    pdfkit.from_file( paths, os.path.join(DIR_OUT, f"{category}.pdf") , options=options)
    shutil.rmtree(os.path.join(DIR_TMP))

main()