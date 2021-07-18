import csv
import os
import requests

# Aide pour écrire dans un CSV
# → https://www.programiz.com/python-programming/writing-csv-files

def clean_files(ext):
  """Clean image files (delete them) of the specified extension [ext]"""
  files = os.listdir()

  print("Delete the following files:")
  for file in files:
    if file.endswith(ext):
      print(f"• {file}")
      os.remove(file)

def create_dir(path):
  """Create directory"""

  if not os.path.isdir(path):
      print(f'The directory {path} is not present. Creating a new one..')
      os.mkdir(path)
  else:
      print(f'The directory {path} is present.')


def export_to_csv(category, category_data, cat_dir_path):
    """Take a list and write data to a .csv"""
    print("----------")
    print(f"→ export {category.name} data to csv")
    print("----------\n")

    #file_name = cat_dir_path + "/" + category.name.lower() + '.csv'
    file_name = f"{cat_dir_path}/{category.name.lower()}.csv"
    #file_name = category[0].lower() + '.csv'

    with open(file_name, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter='|')
        csv_writer.writerow([
            "product_page_url", "universal_product_code (upc)", "title",
            "price_including_tax", "price_excluding_tax", "number_available",
            "product_description", "category", "review_rating", "image_url"
        ])

        csv_writer.writerows(category_data)

def save_image(url, path):
  """Save the image from the url specified to the path."""
  response = requests.get(url)
  index_ext = url.rfind(".")
  ext = url[index_ext:]

  print(f"💾 saving image {path}{ext}...")
  print("~~~")
  path_sanitazed = path.replace(":", "")
  path_sanitazed = path_sanitazed.replace(".", "")
  path_sanitazed = path_sanitazed.replace('"', "")
  path_sanitazed = path_sanitazed.replace('*', "")
  path_sanitazed = path_sanitazed.replace("'", "")
  path_sanitazed = path_sanitazed.replace("?", "")
  with open(f"{path_sanitazed}{ext}", "wb") as file_img:
      file_img.write(response.content)
  
