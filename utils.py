import requests
from bs4 import BeautifulSoup


def get_soup_from_url(url):
    """
    Download l'information d'une page web et retourn une instance de
    BeautifulSoup avec cette information.
    """
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.content, "html.parser")
        return soup