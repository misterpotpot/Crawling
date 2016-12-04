# -*- coding: utf8 -*-

import urllib2
import ssl


ssl._create_default_https_context = ssl._create_unverified_context

def check_charmap(chaine):
	result = chaine.replace("&#039;", "'")
	return result

def crawl(categorie, body, position):
	categories = []

	while 1:
		position_debut = body.find("""<a href="/wiki/Portail:""", position) + 23
		if position_debut == 22:
			break
		position_fin = body[position_debut:].find("\"") + position_debut
		c = str(check_charmap(body[position_debut:position_fin]))
		if c == categorie:
			break
		categories.append(c)
		position = position_fin

	return categories, position



url = "https://fr.wikipedia.org/wiki/Portail:Accueil"
req = urllib2.urlopen(url)
body = req.read()
position = 0

print "Categories pour Sciences \n"
categories, position = crawl("Technologies", body, position)
print categories

print "\n\nCategories pour Technologies \n"
categories, position = crawl("M%C3%A9decine", body, position)
print categories

print "\n\nCategories pour Medecine \n"
categories, position = crawl("Arts", body, position)
print categories

print "\n\nCategories pour Arts \n"
categories, position = crawl("Sport", body, position)
print categories

print "\n\nCategories pour Sport \n"
categories, position = crawl("Vie_quotidienne_et_loisirs", body, position)
print categories

print "\n\nCategories pour Loisirs \n"
categories, position = crawl("Soci%C3%A9t%C3%A9", body, position)
print categories

print "\n\nCategories pour Societe \n"
categories, position = crawl("Politique", body, position)
print categories

print "\n\nCategories pour Politique \n" 
categories, position = crawl("Religions_et_croyances", body, position) 
print categories

print "\n\nCategories pour Religions \n" 
categories, position = crawl("Histoire", body, position) 
print categories

print "\n\nCategories pour Histoire \n" 
categories, position = crawl("G%C3%A9ographie", body, position)
print categories

print "\n\nCategories pour Geographie \n"
categories, position = crawl("FIN!!!", body, position)
print categories