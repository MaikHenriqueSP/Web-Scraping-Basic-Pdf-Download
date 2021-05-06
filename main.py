from bs4 import BeautifulSoup
import requests
import pathlib

BASE_URL = "http://www.ans.gov.br"
TISS_ENDPOINT_URL = "/prestadores/tiss-troca-de-informacao-de-saude-suplementar"

def get_request_content(request_url):
    response = requests.get(request_url)
    return response.content

def get_request_url(end_point_url):
    return f'''{BASE_URL}{end_point_url}'''

def get_anchor_by_header_title(header_title, content):
    soup = BeautifulSoup(content, "html.parser")
    content_container = soup.find("div", class_= "item_page")
    header = soup.find("h2", string=re.compile(header_title))
    sibling_container = header.find_next_sibling("div", class_="alert alert-icolink")
    return sibling_container.a

def get_download_url(base_url = BASE_URL):    
    request_url = get_request_url(TISS_ENDPOINT_URL)
    content = get_request_content(request_url)

    get_anchor_by_header_title("Padrão TISS – Versão", content)

def main():
    get_download_url()
    

if __name__ == "__main__":
    main()