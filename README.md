# Markdown Oluşturucusu

Merhaba Twitter'da gördüğüm [MarkDown PDF Oluşturma](https://x.com/0xfsk/status/1747579061185007803?s=20) postuna istinaden daha önce milyarkez yaptığım PDF oluştma işini markdown ile nasıl kullanırım diye biraz düşündükten sonra değişik iş alanlarında kullanılabilir (faturalar, sözleşme olutşurma v.s) şeklinde düşünerek hazır python paketleri ile yapmak için şöyle kısa bir api geliştirdim.


# Bağımlılıklar

WkHtmltoPdf Converter
Bu uygulama free geliştirilen bir html'den pdf oluşturucu. Windows ve Linux ortamlar için ayrı ayrı yüklemesinin yapılması gerekiyor. 

Debian/Ubuntu için;

    sudo apt-get install xvfb
    sudo apt-get install xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic
    sudo apt-get install wkhtmltopdf

MacOs için;

    brew install homebrew/cask/wkhtmltopdf

Windows için;
[WKHtmlToPdf Download](https://objects.githubusercontent.com/github-production-release-asset-2e65be/271714/70314134-52da-11e7-81d9-a3f151bef518?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA/20240117/us-east-1/s3/aws4_request&X-Amz-Date=20240117T123837Z&X-Amz-Expires=300&X-Amz-Signature=7e78a2f0e4bfe4a2b85961939cd4a360b6491c8e26c0d62ea2006061dce87475&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=271714&response-content-disposition=attachment;%20filename=wkhtmltox-0.12.4_msvc2015-win64.exe&response-content-type=application/octet-stream)



## Kütüphaneler

    pip install requests
    pip install FastApi
    pip install uvicorn["standard"]
    pip install pdfkit

## Uygulamanın Çalıştırılması

    python main.py

[Bu ekran](http://localhost:8000/docs) üzerinden swagger dokümantasyonuna erişebilirsiniz.


## Örnek İstekler

URL'den Html Üretmek için;
 

    curl -X 'POST'  \
      'http://localhost:8000/markdownurl?uri=https%3A%2F%2Fgithub.com%2FErtugrulKra%2FtestREADME.md' \ 
        -H 'accept: application/json' \
        -d ''

String Content ile Üretmek için;

    curl -X 'POST' \  'http://localhost:8000/markdown/?content=MARKDOWNCONTENT' \ 
     -H 'accept: application/json' \ 
     -d ''


PDF üretmek için 

    curl -X 'POST' \
      'http://localhost:8000/pdf/?content=MARKDOWNCONTENT
      -H 'accept: application/json' \
      -d ''
