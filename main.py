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

@app.post('/htmlfromurl')
def htmlfromurl(uri):
    url = urllib.parse.unquote_plus(uri).replace('%3A', ':')

    result = requests.get(url)
    if result.status_code != 200:
        return result

    result_content = result.text
    temp_html = markdown.markdown(result_content)

    return HTMLResponse(temp_html)


@app.post('/htmlfromcontent/')
def htmlfromcontent(content: str):
    temp_html = markdown.markdown(content)
    return HTMLResponse(temp_html)


@app.post('/pdffromcontent/')
def pdffromcontent(content: str):
    temp_html = markdown.markdown(content)

    pdf_file = pdfkit.from_string(temp_html,configuration=conf,options={
        'encoding': 'UTF-8'
    })

    return StreamingResponse(BytesIO(pdf_file),media_type='application/pdf')


@app.post('/pdffromurl/')
def pdffromurl(uri: str):

    url = urllib.parse.unquote_plus(uri).replace('%3A', ':')

    result = requests.get(url)
    if result.status_code != 200:
        return result

    result_content = result.text
    temp_html = markdown.markdown(result_content)

    pdf_file = pdfkit.from_string(temp_html,configuration=conf,options={
        'encoding': 'UTF-8'
    })

    return StreamingResponse(BytesIO(pdf_file),media_type='application/pdf')


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
