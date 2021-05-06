# -*- coding: utf-8 -*-
from util import *
import re

'''
@author: Maik Henrique
This mini-project aims to demonstrate the basics of web-scrapping, it simply works by getting into the target page
and then looking for the most recent version page of the pdf we aim to download, it then go to the download page and
download it to a local folder.
'''

'''
Attributes:
    BASE_URL: Defines the base target url, whiche is then combined with different endpoints as the execution progress
    TISS_ENDPOINT_URL: Defines the initial endpoint which will be scrapped in order to extract the download page endpoint
    TARGET_TABLE_ROW_TITLE: Defines the target row table title which we aim to extract the content
'''
BASE_URL = "http://www.ans.gov.br"
TISS_ENDPOINT_URL = "/prestadores/tiss-troca-de-informacao-de-saude-suplementar"
TARGET_TABLE_ROW_TITLE = "Componente Organizacional"
TARGET_SECTION_TITLE = "Padrão TISS – Versão"

'''
    Args:
        header_title (string): A string which must be the target title of the container
        content (bytes): A payload in bytes representing the response from the request
    Returns: 
        The anchor tag that is related to the header_title

'''
def get_anchor_by_header_title(header_title, content):
    soup = get_soup_instance(content)
    content_container = soup.find("div", class_= "item_page")
    header = soup.find("h2", string=re.compile(header_title))
    sibling_container = header.find_next_sibling("div", class_="alert alert-icolink")

    return sibling_container.a

'''
    Args:
        base_url (string): Url the will be requests withing the target endpoint
    Returns:
        download_url (string): The endpoint of the download page

'''
def get_download_url(base_url = BASE_URL):    
    request_url = get_request_url(BASE_URL, TISS_ENDPOINT_URL)
    content = get_request_content(request_url)
    anchor_tag = get_anchor_by_header_title(TARGET_SECTION_TITLE, content)

    return anchor_tag["href"]

'''
    Args:
        soup: BeautifulSoup instance entangled with the related content
        target_title (string):  The title which will be checked against the row title
    Returns:
        pdf_url (string): The endpoint where the pdf can be downloaded
'''
def get_pdf_url(soup, target_title=TARGET_TABLE_ROW_TITLE ):
    table_container_div = soup.find("div", class_="table-responsive")
    table_body = table_container_div.table.tbody
    table_data = table_body.find("td", string=target_title)
    table_row = table_data.parent
    anchor_tag = table_row.find("a")

    return anchor_tag["href"]

'''
    Write the pdf_content into a pdf file at the specified path 

    Args:
        pdf_content (bytes): A raw of bytes that are a response from the pdf request
'''

def save_pdf(pdf_content):
    folder_path = "./component_organizacional"
    file_name = "component_organizacional.pdf"
    file_path = f'''{folder_path}/{file_name}'''
   
    create_folder_if_not_exists(folder_path)
    with open(file_path, "wb") as f:        
        f.write(pdf_content)

'''
    Args:
        download_endpoint(string): The endpoint where the pdf file is stored
'''
def download_pdf(download_enpoint):
    request_url = get_request_url(BASE_URL, download_enpoint)
    content = get_request_content(request_url)
    soup = get_soup_instance(content)
    pdf_endpoint = get_pdf_url(soup)
    download_url = get_request_url(BASE_URL, pdf_endpoint)
    pdf_content = get_request_content(download_url)
    save_pdf(pdf_content)


def main():
    download_endpoint_url = get_download_url()
    download_pdf(download_endpoint_url)
    

if __name__ == "__main__":
    main()