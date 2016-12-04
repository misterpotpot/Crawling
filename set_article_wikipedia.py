# -*- coding: utf8 -*-

import crawl_wikipedia




print "\nBot pour recuperer des articles wikipedia"

conn, liste_urls = crawl_wikipedia.initialiser("'../zapking.db'")
echecs = 0
i = 0
titre = ""

while 1:
	titre = raw_input("\n\nTitre de l'article ('Q' for exit)\n")
	if titre == "Q" or titre == "q":
		break
	url = "https://fr.wikipedia.org/wiki/" + str(titre)
	echecs = 0
	print "\nResultats du crawl ", i+1
	liste_urls, erreur = crawl_wikipedia.crawling(conn, liste_urls, url)
	echecs += erreur
	i += 1


crawl_wikipedia.finaliser(conn, echecs, i)