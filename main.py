from bs4 import BeautifulSoup
import requests
import pathlib

BASE_URL = "http://www.ans.gov.br"


def get_request_content(request_url):
    response = requests.get(request_url)
    return response.content

def get_download_url(base_url = BASE_URL):
    tiss_url = "/prestadores/tiss-troca-de-informacao-de-saude-suplementar"
    request_url = f'''{BASE_URL}{tiss_url}'''
    get_request_content(request_url)

def main():
    get_download_url()
    

if __name__ == "__main__":
    main()