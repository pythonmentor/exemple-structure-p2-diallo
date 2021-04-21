"""
1. télécharger une page (de livre) -> E extract
2. extraire l'information continue dans un page de livre -> T transform
3. enregistrer l'information d'un livre dans un fichier csv -> L load
"""

from utils import get_soup_from_url


def extract_book_info(soup):
    pass


def save_book_info(csvfile, book_info):
    pass


def main():
    """
    Fonction de lancement principale du script.
    """
    soup = get_soup_from_url(
        "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    )
    book_info = extract_book_info(soup)
    with open('une-categorie.csv', 'w', encoding='utf-8-sig') as csvfile:
        save_book_info(csvfile, book_info)


if __name__ == "__main__":
    main()