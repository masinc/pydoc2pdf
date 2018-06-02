# pydoc2pdf

## これはなに？

pythonの日本語ドキュメントをpdfに変換する。

英語版ではpythonのPDFやオフライン版が提供されているが日本語版にはないので作った

## 使い方

### 必要なもの

- python 3.x
- [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html) Google製の HTMLをPDFに変換するアプリケーション
- pythonライブラリ

```cmd
pip install beautifulsoup4
pip install pdfkit
pip install requests
```

or

```cmd
conda install beautifulsoup4
conda install requests
pip install pdfkit
```

### 実行方法

main.pyのvesion変数とcategory変数を適切な値にして実行する。

- version pythonのバージョン (3.6 , 3.5など)
- category main.py参照 (libraryなど)