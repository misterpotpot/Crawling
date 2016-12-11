# -*- coding: utf8 -*-

import urllib2
import ssl
import sqlite3
from fonctionsCrawler import *


ssl._create_default_https_context = ssl._create_unverified_context


class Log():
	"""Classe définissant le log à la bdd. C'est la classe parent de crawler. Elle contient
	- table
	- conn """


	def __init__(self, table, db="../zapking.db"): 
		self.table = table
		self.conn = sqlite3.connect(db)
		self.conn.text_factory = str


	def __del__(self):
		self.conn.close()


	def statut(self):
		cursor = self.conn.cursor()
		querry = str("SELECT href FROM " + self.table + " WHERE push = 0")
		cursor.execute(querry)
		i = 0
		for x in cursor.fetchall():
			i += 1
		print i, " articles de '", self.table, "' n'ont pas encore ete push dans 'urls'"
		cursor.close()


	def push(self):
		cursor = self.conn.cursor()
		cursor.execute("""SELECT * FROM urls_wikipedia WHERE push = 0""")
		nb = 0

		for x in cursor.fetchall():
			qs = affecter_qs(x[3], x[4], x[5], x[6], x[7])
			categories = affecter_categories(x[2])
			if len(str(datetime.today().day)) == 1:
				jour = "0" + str(datetime.today().day)
			else:
				jour = str(datetime.today().day)
			if len(str(datetime.today().month)) == 1:
				mois = "0" + str(datetime.today().month)
			else:
				mois = str(datetime.today().month)
			date_push = jour + "-" + mois + "-" + str(datetime.today().year)
			cursor.execute("""UPDATE urls_wikipedia SET qs = ?, push = 1 WHERE id = ?""", (qs, x[0]))
			cursor.execute("""INSERT INTO urls (href, categories, qs, qs_0, site, lang, date_push) 
				VALUES (?, ?, ?, ?, ?, ?, ?)""", (x[1], categories, qs, qs, "wikipedia", "FR", date_push))
			self.conn.commit()
			nb += 1
			print "\nImport ", nb, " termine"
			print "Categories : ", categories
			print "Quality score : ", qs

		cursor.close()
		print "\n\n", nb, " articles ont ete push dans la bdd principale"








class Crawler(Log): 
	"""Classe définissant le crawler. C'est la classe fille de Log et classe parent de Wikipedia. Elle contient
	- table
	- conn
	- liste_urls 
	- nb_crawl
	- echecs """


	def __init__(self, table, db="../zapking.db", nb_crawl=100): 
		self.table = table
		self.conn = sqlite3.connect(db)
		self.conn.text_factory = str
		self.nb_crawl = nb_crawl
		self.echecs = 0
		cursor = self.conn.cursor()
		querry = str("SELECT href FROM " + self.table)
		cursor.execute(querry)
		self.liste_urls = []
		for x in cursor.fetchall():
			self.liste_urls.append(x[0])
		cursor.close()


	def __del__(self):
		self.conn.close()
		taux_import = round(100 - ((100 * self.echecs) / self.nb_crawl), 2)
		print "\n\nCrawling termine !\nTaux d'import = ", taux_import, " %"


	def set_url(self):
		url = ""
		while 1:
			url = raw_input("\n\nEntrez l'url ('Q' for exit)\n")
			if url == "Q" or url == "q":
				break
			print "\nResultats du crawl ", i+1
			succes_crawl = self.crawling(url)
			i += 1







class Wikipedia(Crawler):
	"""Classe défininssant le crawling des Urls de wikipedia. Classe fille de Crawler. Elle contient
	- table
	- conn
	- liste_urls
	- nb_crawl
	- echecs """


	def __init__(self, t="urls_wikipedia", d="../zapking.db", n=100):
		Crawler.__init__(self, table=t, db=d, nb_crawl=n)


	def set_url(self):
		titre = ""
		while 1:
			titre = raw_input("\n\nTitre de l'article ('Q' for exit)\n")
			if titre == "Q" or titre == "q":
				break
			self.nb_crawl += 1
			print "\nResultats du crawl ", self.nb_crawl
			url = "https://fr.wikipedia.org/wiki/" + str(titre)
			succes_crawl = self.crawling(url)

	
	def crawling(self, url):
		try:
			req = urllib2.urlopen(url)
		except:
			print url
			print "Echec de l'import : cet article n'existe pas sur wikipedia"
			self.echecs += 1
			return 0
		href = check_charmap(req.geturl())
		body = req.read()
		position = 0

		if check_url(href, self.liste_urls):
			print href
			print "Echec de l'import : cette url est deja en base"
			self.echecs += 1
			return 0
		elif body.find("""<div class="center"><b>Wikipédia ne possède pas d'article avec ce nom.</b></div>""", position) > 0:
			print href
			print "Echec de l'import : cet article n'existe pas sur wikipedia"
			self.echecs += 1
			return 0
		else:
			self.liste_urls.append(href)
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
			try:
				req2 = urllib2.urlopen(url2)
			except:
				print href
				print "Echec de l'import : wikipedia ne donne pas la page info"
				self.echecs += 1
				return 0

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

			cursor = self.conn.cursor()
			cursor.execute("""INSERT INTO urls_wikipedia (href, categories, date_creation, qualite, taille, contributeurs, redirections, qs, lang, push) 
				VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (href, categories, date_creation, qualite, taille, contributeurs, redirections, 0, "FR", 0))
			self.conn.commit()
			cursor.close()

			print href
			print "Categories : ", categories
			print "Date de creation : ", date_creation
			print "Qualite : ", qualite
			print "Taille : ", taille
			print "Contributeurs : ", contributeurs
			print "Redirections : ",redirections


	def crawl_random(self):
		for i in range(self.nb_crawl):
			print "\n\nResultats du crawl ", i+1 , " / ", self.nb_crawl ,"\n"
			succes_crawl = self.crawling("https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard")