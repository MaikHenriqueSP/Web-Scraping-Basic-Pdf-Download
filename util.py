from bs4 import BeautifulSoup
import requests
import pathlib

'''
    Utilities file which holds the commonly used functions used throughout the application
'''


'''
    Args:
        request_url (string): Target url in which the request will be done
    Returns:
        The content payload in bytes
'''
def get_request_content(request_url):
    response = requests.get(request_url)

    return response.content

'''
    Args:
        base_url (string): The url which is the first part of the concatenated url
        end_point_url (string): Last part of the url 
    Returns
        A concatenated string of the url
'''
def get_request_url(base_url, end_point_url):
    return f'''{base_url}{end_point_url}'''


'''
    Args:
        content (bytes): Content payload
    Returns:
        BeautifulSoup instance parsed with html.parser
'''
def get_soup_instance(content):
    soup = BeautifulSoup(content, "html.parser")
    return soup


'''
    Args:
        path (string): The path where the folder should be created
'''
def create_folder_if_not_exists(path):
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)