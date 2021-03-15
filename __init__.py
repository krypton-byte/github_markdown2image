import imgkit
import requests
from bs4 import BeautifulSoup
from io import BytesIO
import os
import apt
class README_NOTFOUND(Exception):
    pass
if os.name == "posix":
    requirements=["wkhtmltopdf", "xvfb"]
    Cache=apt.Cache()
    for package in requirements:
        if Cache[package]:
            if Cache[package].is_installed:
                pass
            else:
                print(f"{package} REQUIRED")
        else:
            print(f"{package} REQUIRED")
def readme(url, out=False):
    path="/".join(__file__.split("/")[:-1])
    for i_ in list({"gt.css", "gt1.css", "gt2.css"} - set(os.listdir(path))):
        open(path+f"/{i_}", "wb").write(requests.get(f"https://github.com/krypton-byte/Github_Markdown_render/raw/master/{i_}").content)
    assert type(out) in [bool, str] and not out==True
    source=requests.get(url)
    parser=BeautifulSoup(source.text, "html.parser")
    if parser.find_all(class_='markdown-body entry-content container-lg'):
        scraper=parser.find_all(class_='markdown-body entry-content container-lg')[0].__str__()
        res=imgkit.from_string(scraper, out, css=[path+"/gt.css", path+"/gt1.css", path+"/gt2.css"], options={"enable-local-file-access":None})
        if not out:
            return BytesIO(res)
    else:
        raise README_NOTFOUND()

        
