# -*- coding: utf8 -*-

import urllib2
import ssl
import sqlite3


ssl._create_default_https_context = ssl._create_unverified_context


def check_charmap(chaine):
	result = chaine.replace("&#039;", "'")
	return result


def check_url (url, liste):
	if url in liste:
		return True
	else:
		return False


def format_date (d):
	d = d.replace(">1 ", ">01 ")
	d = d.replace(">2 ", ">02 ")
	d = d.replace(">3 ", ">03 ")
	d = d.replace(">4 ", ">04 ")
	d = d.replace(">5 ", ">05 ")
	d = d.replace(">6 ", ">06 ")
	d = d.replace(">7 ", ">07 ")
	d = d.replace(">8 ", ">08 ")
	d = d.replace(">9 ", ">09 ")
	d = d.replace("janvier", "01")
	d = d.replace("février", "02")
	d = d.replace("mars", "03")
	d = d.replace("avril", "04")
	d = d.replace("mai", "05")
	d = d.replace("juin", "06")
	d = d.replace("juillet", "07")
	d = d.replace("août", "08")
	d = d.replace("septembre", "09")
	d = d.replace("octobre", "10")
	d = d.replace("novembre", "11")
	d = d.replace("décembre", "12")
	d = d.replace(">", "")
	d = d.replace(" ", "-")

	return d


def initialiser (database_name):
	conn = sqlite3.connect('../zapking.db')
	conn.text_factory = str
	cursor = conn.cursor()
	cursor.execute("""SELECT href FROM urls_wikipedia""")
	liste_urls = []
	for x in cursor.fetchall():
		liste_urls.append(x[0])
	cursor.close()

	return conn, liste_urls


def finaliser (conn, echecs, nb):
	conn.close()

	taux_import = round((100 - (100 * echecs / nb)), 2)
	print "\n\nCrawling termine !\nTaux d'import = ", taux_import, " %"


def crawling(conn, liste_urls, url):
	try:
		req = urllib2.urlopen(url)
	except:
		print url
		print "Echec de l'import : cet article n'existe pas sur wikipedia"
		return liste_urls, 1
	href = check_charmap(req.geturl())
	body = req.read()
	position = 0

	if check_url(href, liste_urls):
		print href
		print "Echec de l'import : cette url est deja en base"
		return liste_urls, 1
	elif body.find("""<div class="center"><b>Wikipédia ne possède pas d'article avec ce nom.</b></div>""", position) > 0:
		print href
		print "Echec de l'import : cet article n'existe pas sur wikipedia"
		return liste_urls, 1
	else:
		liste_urls.append(href)
		categories = ""

		while 1:
			position_debut = body.find("""<li><span class="bandeau-portail-element"><span class="bandeau-portail-icone"><a href="/wiki/Portail:""", position) + 101
			if position_debut == 100:
				break
			position_fin = body[position_debut:].find("\"") + position_debut
			categories += body[position_debut:position_fin] + ";"
			position = position_fin

		title = href[30:]
		url2 = "https://fr.wikipedia.org/w/index.php?title=" + title + "&action=info"
		req2 = urllib2.urlopen(url2)
		body2 = req2.read()

		p1 = body2.find("""Taille de la page (en octets)</td><td>""") + 38
		p2 = body2[p1:].find("<") + p1
		taille = body2[p1:p2]
		taille = int(taille.replace("\xc2\xa0", ""))

		p1 = body2.find("""Nombre de contributeurs ayant la page dans leur liste de suivi</td><td>""") + 71
		p2 = body2[p1:].find("<") + p1
		contributeurs = body2[p1:p2]
		if contributeurs == "Moins de 30 observateurs":
			contributeurs = 0
		else:
			contributeurs = int(contributeurs)


		p1 = body2.find("""Nombre de redirections vers cette page</a></td><td>""") + 51
		p2 = body2[p1:].find("<") + p1
		redirections = int(body2[p1:p2])

		p1 = body2.find("""Date de création de la page</td><td>""") + 37
		p1 = body2[p1:].find(">") + p1
		p2 = body2[p1:].find(" à") + p1
		date_creation = body2[p1:p2]
		date_creation = format_date(date_creation)

		if body.find("""<i>Vous lisez un «&#160;<a href="/wiki/Wikip%C3%A9dia:Articles_de_qualit%C3%A9" title="Wikipédia:Articles de qualité">article de qualité</a>&#160;».</i>""") > 0:
			qualite = "quali"
		elif body.find("""<i>Vous lisez un «&#160;<a href="/wiki/Wikip%C3%A9dia:Bons_articles" title="Wikipédia:Bons articles">bon article</a>&#160;».</i>""") > 0:
			qualite = "bon"
		else:
			qualite = "standard"

		cursor = conn.cursor()
		cursor.execute("""INSERT INTO urls_wikipedia (href, categories, date_creation, qualite, taille, contributeurs, redirections, qs, lang, push) 
			VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (href, categories, date_creation, qualite, taille, contributeurs, redirections, 0, "FR", 0))
		conn.commit()
		cursor.close()

		print href
		print "Categories : ", categories
		print "Date de creation : ", date_creation
		print "Qualite : ", qualite
		print "Taille : ", taille
		print "Contributeurs : ", contributeurs
		print "Redirections : ",redirections

		return liste_urls, 0
	

def def_urls(url):
	req = urllib2.urlopen(url)
	body = req.read()
	main = "https://fr.wikipedia.org/wiki/"
	urls = []
	position = 0
	while 1:
		position_debut = body.find("""<li><a href="/wiki/""", position) + 19
		if position_debut < 30:
			break
		position_fin = body[position_debut:].find("\"") + position_debut
		new_url = main + body[position_debut:position_fin]
		urls.append(new_url)
		position = position_fin

	del urls[-2:]
	print "Urls chargees"
	return urls



