# -*- coding: utf8 -*-

import crawl_wikipedia




print "\nBot pour crawler wikipedia \n"
nb = int(input("Nombre de crawl : "))

conn, liste_urls = crawl_wikipedia.initialiser("'../zapking.db'")
i = 0
echecs = 0

while (i < nb):
	print "\n\nResultats du crawl ", i+1 , " / ", nb ,"\n"
	liste_urls, erreur = crawl_wikipedia.crawling(conn, liste_urls, "https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard")
	echecs += erreur
	i += 1

crawl_wikipedia.finaliser(conn, echecs, nb)