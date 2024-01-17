import sys
from io import BytesIO
import markdown
from fastapi import FastAPI
from fastapi.responses import HTMLResponse,StreamingResponse
import requests
import uvicorn
import urllib.parse
import pdfkit


#Windows geliştirme yaparken burası zorunludur.
conf = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")


app = FastAPI()

@app.get('/')
def index():
    return "FastApi Markdown Converter"

@app.post('/markdownurl')
def markdownurl(uri):
    url = urllib.parse.unquote_plus(uri).replace('%3A', ':')
    print(url)
    result = requests.get(url)
    if result.status_code != 200:
        return result

    result_content = result.text
    temp_html = markdown.markdown(result_content)

    return HTMLResponse(temp_html)


@app.post('/markdown/')
def markdown_post(content: str):
    temp_html = markdown.markdown(content)
    return HTMLResponse(temp_html)


@app.post('/pdf/')
def markdown_post(content: str):
    temp_html = markdown.markdown(content)

    pdf_file = pdfkit.from_string(temp_html,configuration=conf,options={
        'encoding': 'UTF-8'
    })

    return StreamingResponse(BytesIO(pdf_file),media_type='application/pdf')


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
