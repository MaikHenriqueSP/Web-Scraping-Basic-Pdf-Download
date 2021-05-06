from bs4 import BeautifulSoup
import requests
import pathlib
import re

BASE_URL = "http://www.ans.gov.br"
TISS_ENDPOINT_URL = "/prestadores/tiss-troca-de-informacao-de-saude-suplementar"
TARGET_TABLE_ROW_TITLE = "Componente Organizacional"

def get_request_content(request_url):
    response = requests.get(request_url)

    return response.content

def get_request_url(end_point_url):
    return f'''{BASE_URL}{end_point_url}'''

def get_anchor_by_header_title(header_title, content):
    soup = get_soup_instance(content)
    content_container = soup.find("div", class_= "item_page")
    header = soup.find("h2", string=re.compile(header_title))
    sibling_container = header.find_next_sibling("div", class_="alert alert-icolink")

    return sibling_container.a

def get_download_url(base_url = BASE_URL):    
    request_url = get_request_url(TISS_ENDPOINT_URL)
    content = get_request_content(request_url)
    anchor_tag = get_anchor_by_header_title("Padrão TISS – Versão", content)

    return anchor_tag["href"]

def get_soup_instance(content):
    soup = BeautifulSoup(content, "html.parser")
    return soup

def get_pdf_url(soup, target_title=TARGET_TABLE_ROW_TITLE ):
    table_container_div = soup.find("div", class_="table-responsive")
    table_body = table_container_div.table.tbody
    table_data = table_body.find("td", string=target_title)
    table_row = table_data.parent
    anchor_tag = table_row.find("a")

    return anchor_tag["href"]

def create_folder_if_not_exists(path):
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)

def save_pdf(pdf_content):
    folder_path = "./component_organizacional"
    file_name = "component_organizacional.pdf"
    file_path = f'''{folder_path}/{file_name}'''
   
    create_folder_if_not_exists(folder_path)
    with open(file_path, "wb") as f:
        print(file_path)
        f.write(pdf_content)


def download_pdf(download_enpoint):
    request_url = get_request_url(download_enpoint)
    content = get_request_content(request_url)
    soup = get_soup_instance(content)
    pdf_endpoint = get_pdf_url(soup)
    download_url = get_request_url(pdf_endpoint)
    pdf_content = get_request_content(download_url)
    save_pdf(pdf_content)


def main():
    download_endpoint_url = get_download_url()
    download_pdf(download_endpoint_url)
    

if __name__ == "__main__":
    main()