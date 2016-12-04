# -*- coding: utf8 -*-

import crawl_wikipedia


def crawling(url, tour):
	conn, liste_urls = crawl_wikipedia.initialiser("'../zapking.db'")
	urls = crawl_wikipedia.def_urls(url)
	nb = len(urls)
	i = 0
	echecs = 0

	for x in urls:
		print "\n\nTour ", tour, "/14 - Resultats du crawl ", i+1 , " / ", nb ,"\n"
		liste_urls, erreur = crawl_wikipedia.crawling(conn, liste_urls, x)
		echecs += erreur
		i += 1

	crawl_wikipedia.finaliser(conn, echecs, nb)




print "\nBot pour crawler les articles bons wikipedia \n"

crawling("https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Bon_article", 1)
crawling("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Bon_article&pagefrom=Banque+populaire+%28IMOCA%29#mw-pages", 2)
crawling("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Bon_article&pagefrom=Cercle+athl%C3%A9tique+bastiais#mw-pages", 3)
crawling("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Bon_article&pagefrom=Crosby%2C+Sidney%0ASidney+Crosby#mw-pages", 4)
crawling("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Bon_article&pagefrom=EPTB+Seine+Grands+Lacs#mw-pages", 5)
crawling("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Bon_article&pagefrom=Gecko+l%C3%A9opard#mw-pages", 6)
crawling("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Bon_article&pagefrom=Holiday+%28chanson+de+Madonna%29#mw-pages", 7)
crawling("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Bon_article&pagefrom=Latium#mw-pages", 8)
crawling("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Bon_article&pagefrom=Michaux%2C+Paul%0APaul+Michaux#mw-pages", 9)
crawling("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Bon_article&pagefrom=Palais+de+Diocl%C3%A9tien#mw-pages", 10)
crawling("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Bon_article&pagefrom=Recuperation+informelle+des+dechets%0AR%C3%A9cup%C3%A9ration+informelle+des+d%C3%A9chets#mw-pages", 11)
crawling("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Bon_article&pagefrom=Scrabble#mw-pages", 12)
crawling("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Bon_article&pagefrom=Temple+de+l%27Amour#mw-pages", 13)
crawling("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Bon_article&pagefrom=Washington%2C+George%0AGeorge+Washington#mw-pages", 14)
