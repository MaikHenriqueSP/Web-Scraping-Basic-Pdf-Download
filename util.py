from bs4 import BeautifulSoup
import requests
import pathlib

def get_request_content(request_url):
    response = requests.get(request_url)

    return response.content

def get_request_url(base_url, end_point_url):
    return f'''{base_url}{end_point_url}'''

def get_soup_instance(content):
    soup = BeautifulSoup(content, "html.parser")
    return soup

def create_folder_if_not_exists(path):
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)