# projet_2
P2_scraping
Déscription du projet:
le projet consiste à développer une version bêta d’un système pour suivre les prix des livres 
chez Books to Scrape, un revendeur de livres en ligne. En pratique, dans cette version bêta
le programme n'effectuera pas une véritable surveillance en temps réel des prix sur la durée.
Il s'agira simplement d'une application exécutable à la demande visant à récupérer les prix au moment de son exécution. 


1-Creation et activation de l'environnement virtuel:
  -lancer le terminal(ex:PowerShell)
  -avec la commande pwd trouver l'endroit ou on se situe sur le pc.
  -avec la commande cd se déplacer jusqu'au répertoire qui abrite le projet.
  -exécuter la commande virtualenv nom(venv,ou autre nom qu'on choisit )
  -avec la commande env/Scripts/activate.ps1 on active l'environnement virtuelle.
  -on installe les paquets python nécéssaire a l'éxécution du programme (fourni dans le fichier requirements.txt)dans notre cas:
     beautifulsoup4==4.9.3
     bs4==0.0.1
     certifi==2021.5.30
     charset-normalizer==2.0.3
     idna==3.2
     requests==2.26.0
     soupsieve==2.2.1
     urllib3==1.26.6
     
2-les étapes de l'exécution du programme:
Le systeme de décompose en quatre module python :
main.py
book_module.py
one_category_module.py
category_module.py
module_class.py
le programme s’exucute dans le module main.py selon l’ordre suivant :
données d’entré : https://book.toscrape.com/
a partir de se site internet,le module catégory.py s’exécute et extrait touts les urls de chaque catégorie qui sont stocker dans une liste.
A partir de la liste des urls le module le module one_category.py ouvre chaque url de chaque catégorie pour exécuter le module book_module.py 
qui se charge d’extraire les informations de chaque livre selon la demande ;
titre,
description du livre
,prix hors taxe,
prix avec taxe,
nombre de vu ainsi 
l’url de l’image 
ses données seront stocker dans un fichier csv
en suite le système télécharge chaque image de chaque livre est l’enregistre dans un dossier qui porte le nom de la catégorie.
