# -*- coding: utf8 -*-

from classCrawler import *
from time import sleep
from fonctionsCrawler import *



Condition = True
while Condition == True:
	print "\n\n************************"
	print "* Crawling - Wikipedia *"
	print "************************"
	print "\nChoisissez un mode :\n'random'     => Crawl des articles au hasard de Wikipedia\n'statut'     => Indique combien d'articles n'ont pas ete push dans la bdd principale\n'push'       => Push les articles dans la bdd princiaple et leur affecte QS et categories\n'article'    => Permet de rentrer à la main un article de Wikipedia en indiquant son titre\n'bon'        => Recupere tous les articles etiquetes bon par Wikipedia \n'qualite'    => Recupere tous les articles etiquetes de qualite par Wikipedia \n'categories' => Recupere toutes les categories de Wikipedia et fait le categorie matching avec nos categories internes\n'quit'       => Quitter le programme"
	mode = raw_input()
	if mode == "random":
		print "\n\nBot pour crawler wikipedia \n"
		nb_crawl = int(input("Nombre de crawl : "))
		wikipedia = Wikipedia(n=nb_crawl)
		wikipedia.crawl_random()
		del(wikipedia)
	elif mode == "statut":
		print "\n\nStatuts de Wikipedia\n"
		log = Log(table = "urls_wikipedia")
		log.statut()
		del(log)
	elif mode == "push":
		print "Push wikipedia \n"
		log = Log(table = "urls_wikipedia")
		log.statut()
		sleep(1)
		log.push()
		del(log)
	elif mode == "article":
		print "\n\nBot pour recuperer des articles wikipedia \n"
		wikipedia = Wikipedia(n=0)
		wikipedia.set_url()
		del(wikipedia)
	elif mode == "bon":
		print "\n\nBot pour crawler les articles bons wikipedia \n"
		crawling_special_wiki("https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Bon_article", 1, 14)
		crawling_special_wiki("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Bon_article&pagefrom=Banque+populaire+%28IMOCA%29#mw-pages", 2, 14)
		crawling_special_wiki("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Bon_article&pagefrom=Cercle+athl%C3%A9tique+bastiais#mw-pages", 3, 14)
		crawling_special_wiki("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Bon_article&pagefrom=Crosby%2C+Sidney%0ASidney+Crosby#mw-pages", 4, 14)
		crawling_special_wiki("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Bon_article&pagefrom=EPTB+Seine+Grands+Lacs#mw-pages", 5, 14)
		crawling_special_wiki("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Bon_article&pagefrom=Gecko+l%C3%A9opard#mw-pages", 6, 14)
		crawling_special_wiki("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Bon_article&pagefrom=Holiday+%28chanson+de+Madonna%29#mw-pages", 7, 14)
		crawling_special_wiki("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Bon_article&pagefrom=Latium#mw-pages", 8, 14)
		crawling_special_wiki("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Bon_article&pagefrom=Michaux%2C+Paul%0APaul+Michaux#mw-pages", 9, 14)
		crawling_special_wiki("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Bon_article&pagefrom=Palais+de+Diocl%C3%A9tien#mw-pages", 10, 14)
		crawling_special_wiki("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Bon_article&pagefrom=Recuperation+informelle+des+dechets%0AR%C3%A9cup%C3%A9ration+informelle+des+d%C3%A9chets#mw-pages", 11, 14)
		crawling_special_wiki("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Bon_article&pagefrom=Scrabble#mw-pages", 12, 14)
		crawling_special_wiki("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Bon_article&pagefrom=Temple+de+l%27Amour#mw-pages", 13, 14)
		crawling_special_wiki("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Bon_article&pagefrom=Washington%2C+George%0AGeorge+Washington#mw-pages", 14, 14)
	elif mode == "qualite":
		print "\n\nBot pour crawler les articles quali wikipedia \n"
		crawling_special_wiki("https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Article_de_qualit%C3%A9", 1, 8)
		crawling_special_wiki("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Article_de_qualit%C3%A9&pagefrom=Boston#mw-pages", 2, 8)
		crawling_special_wiki("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Article_de_qualit%C3%A9&pagefrom=Dingo+%28Disney%29#mw-pages", 3, 8)
		crawling_special_wiki("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Article_de_qualit%C3%A9&pagefrom=G%C3%A9ographie+de+la+Suisse#mw-pages", 4, 8)
		crawling_special_wiki("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Article_de_qualit%C3%A9&pagefrom=Kerouac%2C+Jack%0AJack+Kerouac#mw-pages", 5, 8)
		crawling_special_wiki("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Article_de_qualit%C3%A9&pagefrom=Mouvement+pour+les+droits+des+personnes+autistes#mw-pages", 6, 8)
		crawling_special_wiki("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Article_de_qualit%C3%A9&pagefrom=Queen#mw-pages", 7, 8)
		crawling_special_wiki("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Article_de_qualit%C3%A9&pagefrom=Super+Aguri+Formula+1+Team#mw-pages", 8, 8)
	elif mode == "categories":
		print "\n\nBot pour recuperer et matcher les categories de wikipedia \n"
		get_categories_wikipedia()
	elif mode == "quit":
		Condition = False
	else:
		print "\n\nErreur, ce mode n'est pas reconnu. Reessayez !"