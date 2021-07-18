import requests
from bs4 import BeautifulSoup
from category_class import Category

url = "https://books.toscrape.com/index.html"


def get_all_categories():
    """Retrieve all categories from home page"""

    all_categories = []
    response = requests.get(url)

    if response.ok:
        # Parser le code html
        soup = BeautifulSoup(response.text, "html.parser")
        #aList = soup.find_all('a', 'nav nav-list' == True)[3:53]
        aList = soup.select("ul.nav-list ul li")

        if (aList == None):
          return all_categories

        for aElement in aList:
          cat_url = "https://books.toscrape.com/" + aElement.a.get('href')
          cat_name = aElement.a.text.strip()

          category = Category(cat_name, cat_url)
          all_categories.append(category)

    print(f"→ Retrieved {len(all_categories)} categories from home page\n")
    return all_categories





