import requests
from bs4 import BeautifulSoup
from one_category_module import scrap_category

def scrap_book(book_url):
    """Extract book's data from url"""
    print("→ get book's data: ", book_url)
    
    response = requests.get(book_url)

    if response.ok:
        # Parser le code html
        soup = BeautifulSoup(response.text, "html.parser")

        # 1. product_page_url (URL du livre)
        # -> on a déjà l'URL du livre dans book_url

        # 2. universal_product_code (upc)

        product_information = soup.find("table",
                                        {"table table-striped", "tr", "td"})

        row = product_information.find_all("td")
        #print("--universal_product_code--")
        universal_product_code = row[0].text

        # 3. titre du livre
        title = soup.find("h1").text

        # 4. price_including_tax
        #print("--price_including_tax--")
        price_including_tax = row[2].text

        # 5. price_excluding_tax
        #print("--price_excluding_tax--")
        price_excluding_tax = row[3].text

        # 6. number_available
        number_available = row[5].text
        #print("--number_available--")

        # 7. product_description
        product_description = soup.select("article.product_page >p")
        if len(product_description)!=0:  
            product_description = soup.select("#product_description ~ p")[0].text 
        else:
            pass   
        # 8. category
        tag = soup.li.find_next_sibling().find_next_sibling()
        category = tag.text.lower().strip()

        # 9. review_rating
        #print("--review_rating--")
        review_rating = row[6].text

        # 10. image_url
        # on utilise soup.img et tag ['src'] pour trouver le lien
        # puis on reconstitue le lien avec:"http://books.toscrape.com/"+tag['src']
        tag = soup.img
        image_url = "http://books.toscrape.com/" + tag['src']

        return [
            book_url,
            universal_product_code,
            title,
            price_including_tax,
            price_excluding_tax,
            number_available,
            product_description,
            category,
            review_rating,
            image_url,
        ]
