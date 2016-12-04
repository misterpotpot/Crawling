# -*- coding: utf8 -*-

import crawl_wikipedia


def crawling(url, tour):
	conn, liste_urls = crawl_wikipedia.initialiser("'../zapking.db'")
	urls = crawl_wikipedia.def_urls(url)
	nb = len(urls)
	i = 0
	echecs = 0

	for x in urls:
		print "\n\nTour ", tour, "/8 - Resultats du crawl ", i+1 , " / ", nb ,"\n"
		liste_urls, erreur = crawl_wikipedia.crawling(conn, liste_urls, x)
		echecs += erreur
		i += 1

	crawl_wikipedia.finaliser(conn, echecs, nb)




print "\nBot pour crawler les articles quali wikipedia \n"

crawling("https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Article_de_qualit%C3%A9", 1)
crawling("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Article_de_qualit%C3%A9&pagefrom=Boston#mw-pages", 2)
crawling("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Article_de_qualit%C3%A9&pagefrom=Dingo+%28Disney%29#mw-pages", 3)
crawling("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Article_de_qualit%C3%A9&pagefrom=G%C3%A9ographie+de+la+Suisse#mw-pages", 4)
crawling("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Article_de_qualit%C3%A9&pagefrom=Kerouac%2C+Jack%0AJack+Kerouac#mw-pages", 5)
crawling("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Article_de_qualit%C3%A9&pagefrom=Mouvement+pour+les+droits+des+personnes+autistes#mw-pages", 6)
crawling("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Article_de_qualit%C3%A9&pagefrom=Queen#mw-pages", 7)
crawling("https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Article_de_qualit%C3%A9&pagefrom=Super+Aguri+Formula+1+Team#mw-pages", 8)
