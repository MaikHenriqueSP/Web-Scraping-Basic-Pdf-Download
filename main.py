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

def get_download_url(base_url = BASE_URL):    
    request_url = get_request_url(TISS_ENDPOINT_URL)
    content = get_request_content(request_url)

def main():
    get_download_url()
    

if __name__ == "__main__":
    main()