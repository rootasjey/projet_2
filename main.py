from book_module import scrap_book
from one_category_module import scrap_category
from category_module import get_all_categories
from io_module import export_to_csv, create_dir, clean_files, save_image

# Importer un module depuis un subfolder
# → https://stackoverflow.com/questions/8953844/import-module-from-subfolder

def main():
    "Entry point"
    print("~~~~~~~~~~~~")
    print("~~~ main ~~~")
    print("~~~~~~~~~~~~")

    all_categories = get_all_categories()

    for category in all_categories:
        print(f"→ getting all books' urls from category: {category.name}")
        print("-----------------------------------------------")

        index = 0  # we track index to have a row number in csv
        books_data = []
        books_urls = scrap_category(category)

        dir_prefix = "data"
        cat_dir_path = dir_prefix + '/' + category.name.lower()

        create_dir(dir_prefix)
        create_dir(cat_dir_path)

        for book_url in books_urls:
            index += 1
            book_data = scrap_book(book_url)

            book_data.insert(0, index)
            books_data.append(book_data)


            last_arr_index = len(book_data) - 1
            image_url = book_data[last_arr_index]
            image_path_to_save = f"{cat_dir_path}/{(book_data[3]).replace('/','')}"

            save_image(image_url, image_path_to_save)

        export_to_csv(category, books_data, cat_dir_path)
        
        # limit the process to 1 category
        # remove the "return True" to process all categories
        

def dir_test():
  "Dir test"
  #create_dir("img_2")
  clean_files(".jpg")

main()