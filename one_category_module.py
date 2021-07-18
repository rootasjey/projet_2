from bs4 import BeautifulSoup
import requests
import re

def scrap_category(category):
    links = []
    total_pages_int = 1

    base_response = requests.get(category.url)
    base_soup = BeautifulSoup(base_response.text, "html.parser")
    li_total_pages_array = base_soup.select("li.current")

    if len(li_total_pages_array) > 0:
        li_total_pages = (li_total_pages_array)[0].text
        array_string = li_total_pages.split()
        
        #print(array_string)
        total_pages_str = array_string[len(array_string) - 1]
        total_pages_int = int(total_pages_str)

    min_page = 1
    max_page = (total_pages_int + 1)

    # max_page est exclusif
    for i in range(min_page, max_page):
        # modifier l'url suivante pour s'adapter au paramètre
        #url = f"https://books.toscrape.com/catalogue/category/books/mystery_3/page-{str(i)}.html"
        url = category.url

        # checker le nom des fonctions
        if int(max_page) == 2:
            url=category.url
        else:
            url = url.replace(url,category.url[0:int(len(category.url)-10)])
            url += f"page-{str(i)}.html"
            
        
        print(url)

        # print(url)
        response = requests.get(url)

        if response.ok:
            soup = BeautifulSoup(response.text, "html.parser")
            #links = [] # liens de chaque bouquin
            h3 = soup.find_all('h3')

            for h in h3:
                partial_link = h.find('a').get("href")[9:]

                complete_link = 'https://books.toscrape.com/catalogue/' + partial_link

                #print(complete_link)
                links.append(complete_link)
    return links
