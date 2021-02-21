import imgkit
import requests
from bs4 import BeautifulSoup
from io import BytesIO
class README_NOTFOUND(Exception):
    pass
def readme(url, out=False):
    assert type(out) in [bool, str] and not out==True
    source=requests.get(url)
    parser=BeautifulSoup(source.text, "html.parser")
    if parser.find_all(class_='markdown-body entry-content container-lg'):
        scraper=parser.find_all(class_='markdown-body entry-content container-lg')[0].__str__()
        res=imgkit.from_string(scraper, out, css=["Github_Markdown_render/gt.css", "Github_Markdown_render/gt1.css", "Github_Markdown_render/gt2.css"])
        if not out:
            return BytesIO(res)
    else:
        raise README_NOTFOUND()

        
