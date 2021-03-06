# -*- coding: utf8 -*-

import urllib2
import ssl
from datetime import datetime


ssl._create_default_https_context = ssl._create_unverified_context


def check_charmap(chaine):
	result = chaine.replace("&#039;", "'")
	return result


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


def check_url (url, liste):
	if url in liste:
		return True
	else:
		return False


def categorie_matching(input_cat, output_cat, match_cat):
	for x in input_cat:
		if x in output_cat:
			return match_cat
		else:
			return ""


def affecter_qs(date_creation, qualite, taille, contributeurs, redirections):
	date_crea = date_creation.split("-")
	duree = datetime.now() - datetime(int(date_crea[2]), int(date_crea[1]), int(date_crea[0]))
	facteur1 = 5 * (int(duree.days) ** (0.5))

	if qualite == "quali":
		facteur2 = 500
	elif qualite == "bon":
		facteur2 = 200
	else:
		facteur2 = 0

	facteur3 = 1 * (taille ** (0.5))
	facteur4 = 50 * (contributeurs ** (0.5))
	facteur5 = 75 * (redirections ** (0.5))

	score = int (facteur1 + facteur2 + facteur3 + facteur4 + facteur5)
	return score

	
def affecter_categories(input_categories):
	output_art = ['Arts', 'Histoire_de_l%27art', 'Baroque', 'Romantisme', 'Art_contemporain', 'Architecture_et_urbanisme', 'Architecture_chr%C3%A9tienne', 'Art_d%C3%A9co', 'Art_nouveau', 'Ch%C3%A2teaux', 'Ch%C3%A2teaux_de_France', 'Espaces_verts', 'Gratte-ciel', 'H%C3%B4tellerie', 'Arm%C3%A9nie/Monast%C3%A8res_arm%C3%A9niens', 'Monuments_historiques', 'Tour_Eiffel', 'Enluminure', 'Peinture', 'Sculpture', 'Animation', 'Animation_et_bande_dessin%C3%A9e_asiatiques', 'Disney', 'Disney/Pixar', 'Bande_dessin%C3%A9e', 'Bande_dessin%C3%A9e_francophone', 'Comics', 'DC_Comics', 'Marvel', 'Cin%C3%A9ma', 'Bollywood', 'Cin%C3%A9ma_belge', 'Cin%C3%A9ma_fran%C3%A7ais', 'Cin%C3%A9ma_qu%C3%A9b%C3%A9cois', 'Cin%C3%A9ma_italien', 'Cin%C3%A9ma_japonais', 'Cin%C3%A9ma_am%C3%A9ricain', 'Cin%C3%A9ma_britannique', 'R%C3%A9alisation_audiovisuelle', 'Time_Warner', 'H%C3%A9raldique', 'Jeu_vid%C3%A9o', 'Jeu_vid%C3%A9o_de_combat', 'Nintendo', 'Ubisoft', 'Photographie', 'T%C3%A9l%C3%A9vision', 'Eurovision', 'Jeux_t%C3%A9l%C3%A9vis%C3%A9s', 'S%C3%A9ries_t%C3%A9l%C3%A9vis%C3%A9es', 'S%C3%A9ries_t%C3%A9l%C3%A9vis%C3%A9es_am%C3%A9ricaines', 'T%C3%A9l%C3%A9vision_britannique', 'T%C3%A9l%C3%A9vision_fran%C3%A7aise', 'Arts_d%C3%A9coratifs', 'Ameublement', 'C%C3%A9ramique', 'Design', 'Arts_du_spectacle', 'Catch', 'Com%C3%A9dies_musicales', 'Danse', 'Marionnette', 'Op%C3%A9ra', 'Tauromachie', 'Th%C3%A9%C3%A2tre', 'Litt%C3%A9rature', 'Contes', 'Litt%C3%A9rature_am%C3%A9ricaine', 'Litt%C3%A9rature_britannique', 'Litt%C3%A9rature_d%27enfance_et_de_jeunesse', 'Litt%C3%A9rature_fran%C3%A7aise', 'Litt%C3%A9rature_italienne', 'Polar', 'Po%C3%A9sie', 'Musique', 'Musique/Chanson', 'Blues', 'Hip-hop', 'Jazz', 'Metal', 'Musique_bretonne', 'Musique_classique', 'Musique_country', 'Musiques_du_monde', 'Musique_%C3%A9lectronique', 'Gabber', 'Musique_impressionniste', 'Punk', 'Reggae', 'Rock', 'Rock_progressif', 'Salsa', 'Soul_et_funk', 'Y%C3%A9y%C3%A9', 'Clavecin', 'Guitare', 'Orgue', 'Percussions', 'ABBA', 'The_Beatles', 'Ludwig_van_Beethoven', 'Beyonc%C3%A9_Knowles', 'Bob_Dylan', 'Deep_Purple', 'Eminem', 'Lady_Gaga', 'Johnny_Hallyday', 'Michael_Jackson', 'Franz_Liszt', 'Madonna', 'Katy_Perry', 'Elvis_Presley', 'Rihanna', 'James_Bond', 'Ast%C3%A9rix', 'Tintin', 'Les_Simpson', 'South_Park', 'Fantasy_et_fantastique', 'Buffy_contre_les_vampires', 'Digimon', 'Doctor_Who', 'Donjons_et_Dragons', 'Pok%C3%A9mon', 'Royaumes_oubli%C3%A9s', 'Terre_du_Milieu', 'Harry_Potter', 'Pornographie', 'Science-fiction', 'Star_Wars', 'Star_Trek', 'Stargate', 'Warhammer_40,000', 'Western']
	output_geographie = ['G%C3%A9ographie', 'Arctique', 'Antarctique', 'Lacs_et_cours_d%27eau', 'Loire', 'Rh%C3%B4ne', 'Maritime', 'Abysses', 'Mer_M%C3%A9diterran%C3%A9e', 'Manche_(mer)', 'Mer_Adriatique', 'Mer_Baltique', 'Mer_du_Nord', 'Oc%C3%A9ans', 'Oc%C3%A9an_Atlantique', 'Oc%C3%A9an_Indien', 'Oc%C3%A9an_Pacifique', '%C3%8Eles', 'Montagne', 'Alpes', 'Carpates', 'Caucase', 'Massif_central', 'Massif_du_Jura', 'Morvan', 'Pyr%C3%A9n%C3%A9es', 'Bois_et_for%C3%AAt', 'Amazonie', 'Cartographie', 'Exploration', 'Information_g%C3%A9ographique', 'G%C3%A9od%C3%A9sie_et_g%C3%A9ophysique', 'M%C3%A9t%C3%A9orologie', 'Moyen-Orient', 'Afrique', 'Afrique_du_Sud', 'Le_Cap', 'Alg%C3%A9rie', 'Aur%C3%A8s', 'Kabylie', 'Angola', 'B%C3%A9nin', 'Botswana', 'Burkina_Faso', 'Burundi', 'Cameroun', 'Bamil%C3%A9k%C3%A9', 'Bassa', 'Plantes_du_Cameroun', '%C3%8Eles_Canaries', 'Cap-Vert', 'Comores', 'Ceuta,_Melilla_et_plazas_de_soberan%C3%ADa', 'C%C3%B4te_d%27Ivoire', 'Djibouti', '%C3%89gypte', 'Le_Caire', '%C3%89rythr%C3%A9e', '%C3%89thiopie', 'Gabon', 'Gambie', 'Ghana', 'Guin%C3%A9e', 'Guin%C3%A9e-Bissau', 'Guin%C3%A9e_%C3%A9quatoriale', 'Kenya', 'Lesotho', 'Liberia', 'Libye', 'Madagascar', 'Maghreb', 'Malawi', 'Mali', 'Maroc', 'Grand_Casablanca', 'Mekn%C3%A8s', 'Rabat-Sal%C3%A9', 'Mascareignes', 'Maurice', 'Mauritanie', 'Mayotte', 'Mozambique', 'Namibie', 'Niger', 'Nigeria', 'Ouganda', 'R%C3%A9publique_centrafricaine', 'R%C3%A9publique_du_Congo', 'R%C3%A9publique_d%C3%A9mocratique_du_Congo', 'La_R%C3%A9union', 'Saint-Denis_(La_R%C3%A9union)', 'Saint-Paul_(La_R%C3%A9union)', 'Saint-Pierre_(La_R%C3%A9union)', 'Rwanda', 'Sainte-H%C3%A9l%C3%A8ne,_Ascension_et_Tristan_da_Cunha', 'Sao_Tom%C3%A9-et-Principe', 'S%C3%A9n%C3%A9gal', 'Seychelles', 'Sierra_Leone', 'Somalie', 'Soudan', 'Soudan_du_Sud', 'Swaziland', 'Tanzanie', 'Tchad', 'Togo', 'Tunisie', 'Tunis', 'Zambie', 'Zimbabwe', 'Berb%C3%A8res', 'Monde_arabe', 'Am%C3%A9rique', 'Bermudes', 'Franco-Am%C3%A9ricains', 'Groenland', 'Micmacs', 'Nord-Am%C3%A9rindiens', 'Saint-Pierre-et-Miquelon', 'Canada', 'Alberta', 'Colombie-Britannique', '%C3%8Ele-du-Prince-%C3%89douard', 'Manitoba', 'Nouveau-Brunswick', 'Nouvelle-%C3%89cosse', 'Ontario', 'Qu%C3%A9bec', 'Saskatchewan', 'Terre-Neuve-et-Labrador', 'Nunavut', 'Territoires_du_Nord-Ouest', 'Yukon', 'Calgary', 'Edmonton', 'Laval_(Qu%C3%A9bec)', 'Montr%C3%A9al', 'Ottawa', 'Toronto', 'Ville_de_Qu%C3%A9bec', 'Vancouver', 'Winnipeg', 'Abitibi-T%C3%A9miscamingue', 'Bas-Saint-Laurent', 'Centre-du-Qu%C3%A9bec', 'Chaudi%C3%A8re-Appalaches', 'C%C3%B4te-Nord', 'Estrie', 'Gasp%C3%A9sie%E2%80%93%C3%8Eles-de-la-Madeleine', 'Lanaudi%C3%A8re', 'Laurentides', 'Mauricie', 'Mont%C3%A9r%C3%A9gie', 'Nord-du-Qu%C3%A9bec', 'Outaouais', 'Saguenay%E2%80%93Lac-Saint-Jean', 'Autochtones_du_Qu%C3%A9bec', 'Franco-Ontariens', 'Acadie', 'Cap-Breton', 'Nouvelle-France', '%C3%89tats-Unis', 'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'Californie', 'Caroline_du_Nord', 'Caroline_du_Sud', 'Colorado', 'Connecticut', 'Dakota_du_Nord', 'Dakota_du_Sud', 'Delaware', 'Floride', 'G%C3%A9orgie_(%C3%89tats-Unis)', 'Hawa%C3%AF', 'Idaho', 'Illinois', 'Iowa', 'Indiana', 'Kansas', 'Kentucky', 'Louisiane', 'Maine_(%C3%89tat)', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi_(%C3%89tat)', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New_Hampshire', 'New_Jersey', 'New_York_(%C3%89tat)', 'Nouveau-Mexique', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvanie', 'Rhode_Island', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginie', 'Virginie-Occidentale', 'Washington_(%C3%89tat)', 'Wisconsin', 'Wyoming', 'Guam', '%C3%8Eles_Mariannes_du_Nord', 'Porto_Rico', 'Atlanta', 'Baltimore', 'Boston', 'Chicago', 'Cincinnati', 'Cleveland', 'Dallas', 'Denver', 'D%C3%A9troit_(Michigan)', 'Houston', 'Indianapolis', 'Las_Vegas', 'Los_Angeles', 'Louisville', 'Miami', 'Minneapolis', 'New_York', 'La_Nouvelle-Orl%C3%A9ans', 'Orlando', 'Philadelphie', 'Phoenix', 'Pittsburgh', 'Saint-Louis_(Missouri)', 'Salt_Lake_City', 'San_Diego', 'San_Francisco', 'Seattle', 'Washington_(district_de_Columbia)', 'Mexique', 'Mexico', 'Belize', 'Costa_Rica', 'Guatemala', 'Honduras', 'Nicaragua', 'Panama', 'Salvador', 'Cara%C3%AFbe', 'Antigua-et-Barbuda', 'Bahamas', 'Barbade', 'Cuba', 'Dominique', 'Grenade', 'Guadeloupe', 'Ha%C3%AFti', '%C3%8Eles_Ca%C3%AFmans', '%C3%8Eles_Turques-et-Ca%C3%AFques', '%C3%8Eles_Vierges_am%C3%A9ricaines', '%C3%8Eles_Vierges_britanniques', 'Jama%C3%AFque', 'Martinique', 'Montserrat', 'R%C3%A9publique_dominicaine', 'Saint-Barth%C3%A9lemy_(Antilles_fran%C3%A7aises)', 'Saint-Christophe-et-Ni%C3%A9v%C3%A8s', 'Saint-Martin_(Antilles_fran%C3%A7aises)', 'Saint-Vincent-et-les-Grenadines', 'Sainte-Lucie', 'Trinit%C3%A9-et-Tobago', 'Argentine', 'Buenos_Aires', 'Bolivie', 'Br%C3%A9sil', 'Chili', 'Santiago', 'Colombie', 'Bogota', '%C3%89quateur', '%C3%8Eles_Gal%C3%A1pagos', 'G%C3%A9orgie_du_Sud-et-les_%C3%8Eles_Sandwich_du_Sud', 'Guyana', 'Guyane', '%C3%8Eles_Malouines', 'Paraguay', 'P%C3%A9rou', 'Lima', 'Suriname', 'Uruguay', 'Venezuela', 'Caracas', 'Br%C3%A9sil', 'Alagoas', 'Bahia', 'Cear%C3%A1', 'Mato_Grosso', 'Minas_Gerais', 'Par%C3%A1', 'Pernambouc', 'Rio_Grande_do_Norte', 'Rio_Grande_do_Sul', 'Florian%C3%B3polis', 'Rio_de_Janeiro', 'S%C3%A3o_Paulo', 'Asie', 'Abkhazie', 'Afghanistan', 'Arabie_saoudite', 'Bahre%C3%AFn', 'Bangladesh', 'Bhoutan', 'Birmanie', 'Brunei', 'Cambodge', 'R%C3%A9publique_populaire_de_Chine', 'Canton', 'Hong_Kong', 'P%C3%A9kin', 'Macao', 'Shanghai', 'Tibet', 'Cor%C3%A9e', 'Cor%C3%A9e_du_Sud', 'S%C3%A9oul', 'Cor%C3%A9e_du_Nord', '%C3%89mirats_arabes_unis', 'Inde', 'Bengale-Occidental', 'Bombay', 'Delhi', 'Indon%C3%A9sie', 'Irak', 'Iran', 'Isra%C3%ABl', 'J%C3%A9rusalem', 'Japon', 'Jordanie', 'Kazakhstan', 'Kirghizistan', 'Kowe%C3%AFt', 'Kurdistan', 'Liban', 'Laos', 'Malaisie', 'Kuala_Lumpur', 'Maldives', 'Mongolie', 'N%C3%A9pal', 'Oman', 'Oss%C3%A9tie_du_Sud', 'Ouzb%C3%A9kistan', 'Pakistan', 'Palestine', 'J%C3%A9rusalem', 'Philippines', 'Manille', 'Qatar', 'Doha', 'Russie', 'Sib%C3%A9rie', 'Singapour', 'Sri_Lanka', 'Syrie', 'Tadjikistan', 'Ta%C3%AFwan', 'Tha%C3%AFlande', 'Bangkok', 'Timor_oriental', 'Turkm%C3%A9nistan', 'Turquie', 'Vi%C3%AAt_Nam', 'H%C3%B4-Chi-Minh-Ville', 'Y%C3%A9men', 'Japon', 'Hokkaid%C5%8D', 'Pr%C3%A9fecture_d%27Aichi', 'Pr%C3%A9fecture_d%27Akita', 'Pr%C3%A9fecture_d%27Aomori', 'Pr%C3%A9fecture_de_Chiba', 'Pr%C3%A9fecture_de_Fukui', 'Pr%C3%A9fecture_de_Fukushima', 'Pr%C3%A9fecture_de_Gifu', 'Pr%C3%A9fecture_de_Gunma', 'Pr%C3%A9fecture_de_Hy%C5%8Dgo', 'Pr%C3%A9fecture_d%27Ibaraki', 'Pr%C3%A9fecture_d%27Ishikawa', 'Pr%C3%A9fecture_d%27Iwate', 'Pr%C3%A9fecture_de_Kanagawa', 'Pr%C3%A9fecture_de_Mie', 'Pr%C3%A9fecture_de_Miyagi', 'Pr%C3%A9fecture_de_Nagano', 'Pr%C3%A9fecture_de_Nara', 'Pr%C3%A9fecture_de_Niigata', 'Pr%C3%A9fecture_d%27Okayama', 'Pr%C3%A9fecture_de_Saitama', 'Pr%C3%A9fecture_de_Shiga', 'Pr%C3%A9fecture_de_Shimane', 'Pr%C3%A9fecture_de_Shizuoka', 'Pr%C3%A9fecture_de_Tochigi', 'Pr%C3%A9fecture_de_Tottori', 'Pr%C3%A9fecture_de_Toyama', 'Pr%C3%A9fecture_de_Wakayama', 'Pr%C3%A9fecture_de_Yamagata', 'Pr%C3%A9fecture_de_Yamanashi', 'Kyoto', 'Osaka', 'Tokyo', 'Monde_arabe', 'Monde_chinois', 'Monde_indien', 'Monde_malais', 'Europe', 'Union_europ%C3%A9enne', 'Allemagne', 'Autriche', 'Innsbruck', 'Vienne_(Autriche)', 'Belgique', 'Bulgarie', 'Chypre', 'Croatie', 'Danemark', 'Copenhague', '%C3%8Eles_F%C3%A9ro%C3%A9', 'Espagne', 'Finlande', '%C3%85land', 'Helsinki', 'Flandres', 'France', 'Gr%C3%A8ce', 'Ath%C3%A8nes', 'Cr%C3%A8te', 'Hongrie', 'Budapest', 'Irlande', 'Dublin', 'Italie', 'Luxembourg', 'Malte', 'Occitanie', 'Pays_basque', 'Pays-Bas', 'Amsterdam', 'Maastricht', 'Rotterdam', 'Pays_baltes', 'Estonie', 'Lettonie', 'Lituanie', 'Pays_catalans', 'Pologne', 'Cracovie', 'Varsovie', 'Portugal', 'A%C3%A7ores', 'Algarve', 'Lisbonne', 'Mad%C3%A8re', 'Roumanie', 'Bucarest', 'Royaume-Uni', 'Slovaquie', 'Bratislava', 'Ko%C5%A1ice', 'Slov%C3%A9nie', 'Su%C3%A8de', 'G%C3%B6teborg', 'Stockholm', 'R%C3%A9publique_tch%C3%A8que', 'Prague', 'Andorre', 'Albanie', 'Arm%C3%A9nie', 'Azerba%C3%AFdjan', 'Bi%C3%A9lorussie', 'Bosnie-Herz%C3%A9govine', 'G%C3%A9orgie_(pays)', 'Haut-Karabagh', 'Islande', 'Kosovo', 'Liechtenstein', 'Mac%C3%A9doine', 'Skopje', 'Moldavie', 'Transnistrie', 'Monaco', 'Mont%C3%A9n%C3%A9gro', 'Norv%C3%A8ge', 'Oslo', 'Russie', 'Moscou', 'Saint-P%C3%A9tersbourg', 'Sotchi', 'Saint-Marin', 'Serbie_et_peuple_serbe', 'Belgrade', 'Suisse', 'Turquie', 'Istanbul', 'Ukraine', 'Vatican', 'Allemagne', 'Bade-Wurtemberg', 'Basse-Saxe', 'Bavi%C3%A8re', 'Berlin', 'Brandebourg', 'Br%C3%AAme', 'Hambourg', 'Hesse', 'Mecklembourg-Pom%C3%A9ranie-Occidentale', 'Rh%C3%A9nanie-du-Nord-Westphalie', 'Rh%C3%A9nanie-Palatinat', 'Sarre', 'Saxe', 'Saxe-Anhalt', 'Schleswig-Holstein', 'Thuringe', 'Berlin', 'Br%C3%AAme', 'Cologne', 'Francfort-sur-le-Main', 'Hambourg', 'Mayence', 'Munich', 'Stuttgart', 'Belgique', 'Bruxelles', 'Flandre', 'Wallonie', 'Province_d%27Anvers', 'Brabant_flamand', 'Brabant_wallon', 'Flandre-Occidentale', 'Flandre-Orientale', 'Hainaut', 'Province_de_Li%C3%A8ge', 'Province_de_Luxembourg', 'Province_de_Namur', 'Li%C3%A8ge', 'Espagne', 'Andalousie', 'Aragon', 'Asturies', '%C3%8Eles_Bal%C3%A9ares', '%C3%8Eles_Canaries', 'Catalogne', 'Castille-et-Le%C3%B3n', 'Castille-La_Manche', 'Cantabrie', 'Communaut%C3%A9_autonome_du_Pays_basque', 'Estr%C3%A9madure', 'Galice', 'La_Rioja', 'Madrid', 'Navarre', 'R%C3%A9gion_de_Murcie', 'Pays_valencien', 'Barcelone', 'S%C3%A9ville', 'Valence_(Espagne)', 'France', 'France_d%27outre-mer', 'R%C3%A9gions_de_France', 'Auvergne-Rh%C3%B4ne-Alpes', 'Bretagne', 'Centre-Val_de_Loire', '%C3%8Ele-de-France', 'Normandie', 'Nouvelle-Aquitaine', 'Pays_de_la_Loire', 'Provence-Alpes-C%C3%B4te_d%27Azur', 'R%C3%A9gions_de_France', 'Anjou_et_Maine-et-Loire', 'Auvergne', 'Alsace', 'Bessin', 'Berry', 'Bourgogne', 'Bresse', 'Bugey', 'Charolais_Brionnais', 'C%C3%B4ti%C3%A8re', 'Champagne-Ardenne', 'Corse', 'Dauphin%C3%A9', 'Dombes', 'Franche-Comt%C3%A9', 'Languedoc-Roussillon', 'Limousin', 'Lorraine', 'Maine', 'Midi-Pyr%C3%A9n%C3%A9es', 'Nord-Pas-de-Calais', 'Picardie', 'Poitou-Charentes', 'Pays_de_Gex', 'Provence', 'Aveyron', 'Savoie', 'Ain', 'Aisne', 'Allier', 'Alpes-de-Haute-Provence', 'Hautes-Alpes', 'Alpes-Maritimes', 'Ard%C3%A8che', 'Ardennes', 'Ari%C3%A8ge', 'Aube', 'Aude', 'Aveyron', 'Bouches-du-Rh%C3%B4ne', 'Calvados', 'Cantal', 'Charente', 'Charente-Maritime', 'Corr%C3%A8ze', 'C%C3%B4te-d%27Or', 'C%C3%B4tes-d%27Armor', 'Creuse', 'Dordogne', 'Doubs', 'Dr%C3%B4me', 'Eure', 'Eure-et-Loir', 'Finist%C3%A8re', 'Gard', 'Haute-Garonne', 'Gers', 'Gironde', 'H%C3%A9rault', 'Ille-et-Vilaine', 'Indre', 'Indre-et-Loire', 'Is%C3%A8re', 'D%C3%A9partement_du_Jura', 'Landes', 'Loir-et-Cher', 'D%C3%A9partement_de_la_Loire', 'Haute-Loire', 'Loire-Atlantique', 'Loiret', 'Lot', 'Lot-et-Garonne', 'Loz%C3%A8re', 'Anjou_et_Maine-et-Loire', 'Manche', 'Marne', 'Haute-Marne', 'Mayenne', 'Meurthe-et-Moselle', 'Meuse', 'Morbihan', 'Moselle', 'Ni%C3%A8vre', 'Oise', 'Orne', 'Puy-de-D%C3%B4me', 'Pyr%C3%A9n%C3%A9es-Atlantiques', 'Hautes-Pyr%C3%A9n%C3%A9es', 'Pyr%C3%A9n%C3%A9es-Orientales', 'Bas-Rhin', 'Haut-Rhin', 'D%C3%A9partement_du_Rh%C3%B4ne', 'Haute-Sa%C3%B4ne', 'Sa%C3%B4ne-et-Loire', 'Sarthe', 'Savoie', 'Seine-Maritime', 'Seine-et-Marne', 'Yvelines', 'Deux-S%C3%A8vres', 'Somme', 'Tarn', 'Tarn-et-Garonne', 'Var', 'Vaucluse', 'Vend%C3%A9e', 'Vienne', 'Haute-Vienne', 'Vosges', 'Yonne', 'Territoire_de_Belfort', 'Essonne', 'Hauts-de-Seine', 'Seine-Saint-Denis', 'Val-de-Marne', 'Val-d%27Oise', 'Aix-en-Provence', 'Bordeaux', 'Grenoble_M%C3%A9tropole', 'Lille_M%C3%A9tropole', 'Grand_Lyon', 'Marseille', 'Montpellier', 'Nancy', 'Nantes', 'Nice', 'Paris', 'Rennes', 'Rouen', 'Strasbourg', 'Toulouse', 'Communes_de_France', 'Intercommunalit%C3%A9s_de_France', 'Abbeville', 'Amiens', 'Angers', 'Annecy', 'Arles', 'Arras', 'Avignon', 'Besan%C3%A7on', 'Boulogne-sur-Mer', 'Brest', 'Caen', 'Cambrai', 'Cannes', 'Pays_de_L%C3%A9rins', 'Cit%C3%A9s_en_Champagne', 'Chamb%C3%A9ry', 'Chamonix-Mont-Blanc', 'Charleville-M%C3%A9zi%C3%A8res', 'Cherbourg-en-Cotentin', 'Clermont-Ferrand', 'Colmar', 'Dijon', 'Dunkerque', 'Hy%C3%A8res', 'Laval_(Mayenne)', 'Le_Mans', 'Le_Touquet-Paris-Plage', 'Limoges', 'Lorient', 'Metz', 'Mulhouse', 'N%C3%AEmes', 'Orl%C3%A9ans', 'P%C3%A9rigueux', 'Perpignan', 'Quimper', 'Reims', 'Saint-Brieuc', 'Saint-%C3%89tienne', 'Saint-Malo', 'Saint-Nazaire', 'Toul', 'Toulon', 'Tours', 'Valence_(Dr%C3%B4me)', 'Vannes', 'Versailles', 'Vesoul', 'ViennAgglo', 'Camargue', 'C%C3%B4te_des_Isles', 'C%C3%B4te_d%27Opale', 'Pays_de_Bitche', 'Pays_de_Gu%C3%A9rande', 'Pays_de_Hanau', 'Vexin', 'Italie', 'Abruzzes', 'Basilicate', 'Calabre', 'Campanie', '%C3%89milie-Romagne', 'Frioul-V%C3%A9n%C3%A9tie_julienne', 'Latium', 'Ligurie', 'Lombardie', 'Marches', 'Molise', 'Ombrie', 'Pi%C3%A9mont', 'Pouilles', 'Sardaigne', 'Sicile', 'Toscane', 'Trentin-Haut-Adige', 'Vall%C3%A9e_d%27Aoste', 'V%C3%A9n%C3%A9tie', 'Bologne', 'Florence', 'G%C3%AAnes', 'Milan', 'Naples', 'Rome', 'Turin', 'Venise', 'Royaume-Uni', 'Angleterre', '%C3%89cosse', 'Irlande_du_Nord', 'Pays_de_Galles', 'Territoires_britanniques_d%27outre-mer', 'Gibraltar', '%C3%8Eles_Anglo-Normandes', '%C3%8Ele_de_Man', 'Nottinghamshire', 'Yorkshire', 'Birmingham', 'Glasgow', 'Liverpool', 'Londres', 'Manchester', 'Suisse', 'Espace_Mittelland', 'Fribourg', 'Gen%C3%A8ve', 'Grisons', 'Neuch%C3%A2tel', 'Suisse_centrale', 'Suisse_du_Nord-Ouest', 'Suisse_orientale', 'Tessin', 'Valais', 'Vaud', 'Zurich', 'Lausanne', 'Chemin_de_fer_en_Suisse', 'G%C3%A9ographie_de_la_Suisse', 'Politique_suisse', 'Culture_de_la_Suisse', 'Oc%C3%A9anie', '%C3%8Eles_Cook', '%C3%8Eles_Fidji', 'Guam', 'Kiribati', '%C3%8Eles_Marshall', '%C3%8Eles_Mariannes_du_Nord', 'Micron%C3%A9sie', 'Nauru', 'Niue', 'Nouvelle-Cal%C3%A9donie', 'Nouvelle-Z%C3%A9lande', 'Auckland', 'Palaos', 'Papouasie-Nouvelle-Guin%C3%A9e', '%C3%8Ele_de_P%C3%A2ques', 'Polyn%C3%A9sie_fran%C3%A7aise', 'Salomon', 'Samoa', 'Samoa_am%C3%A9ricaines', 'Tonga', 'Tuvalu', 'Vanuatu', 'Wallis-et-Futuna', 'Australie', 'Australie-M%C3%A9ridionale', 'Australie-Occidentale', 'Nouvelle-Galles_du_Sud', 'Tasmanie', 'Queensland', 'Victoria', 'Territoire_de_la_capitale_australienne', 'Territoire_du_Nord', 'Ad%C3%A9la%C3%AFde_(Australie)', 'Brisbane', 'Melbourne', 'Perth', 'Sydney', 'Sport', 'Cin%C3%A9ma', 'Entreprises/Articles_r%C3%A9cents_par_date']
	output_histoire = ['Histoire', 'Histoire_de_l%27art', 'Histoire_de_Bretagne', 'Histoire_du_Japon', 'Histoire_militaire', 'Histoire_militaire_de_la_Wallonie_et_des_Wallons', 'Histoire_des_sciences', 'Histoire_de_la_zoologie_et_de_la_botanique', 'Historiographie', 'Arch%C3%A9ologie', 'Biographie', 'G%C3%A9n%C3%A9alogie', 'Anthroponymie', 'H%C3%A9raldique', 'Pal%C3%A9ontologie', 'Vexillologie', 'Uniformologie_militaire', 'Pr%C3%A9histoire', 'C%C3%A9nozo%C3%AFque', 'M%C3%A9galithisme', 'Monde_antique', 'Am%C3%A9rique_pr%C3%A9colombienne', '%C3%89gypte_antique', '%C3%89trusques', 'Asie_antique', 'Gr%C3%A8ce_antique', 'M%C3%A9sopotamie', 'Monde_celtique', 'Peuple_juif_dans_l%27Antiquit%C3%A9', 'Ph%C3%A9niciens,_Carthage_et_monde_punique', 'Proche-Orient_ancien', 'Rome_antique', 'Hittites', 'Moyen_%C3%82ge', 'Anglo-Saxons', 'Bagratides', 'Monde_byzantin', 'Duch%C3%A9_de_Bretagne', 'Haut_Moyen_%C3%82ge', 'Moyen_%C3%82ge_central', 'Moyen_%C3%82ge_tardif', 'Monde_arabo-musulman', 'Al-Andalus', 'Croisades', 'Ordre_de_Saint-Jean_de_J%C3%A9rusalem', 'Ordre_du_Temple', 'Royaume_de_France', 'Saint-Empire_romain_germanique', 'Couronne_d%27Aragon', '%C3%89poque_moderne', 'Nouvelle-Espagne', 'Empire_colonial_portugais', 'Empire_ottoman', 'Renaissance', 'XVIIe_si%C3%A8cle', 'France_du_Grand_Si%C3%A8cle', 'Ch%C3%A2teau_de_Versailles', 'Nouvelle-France', 'Acadie', 'XVIIIe_si%C3%A8cle', 'Empire_britannique', 'Empire_russe', 'R%C3%A9volution_am%C3%A9ricaine', 'R%C3%A9volution_fran%C3%A7aise', 'Premier_Empire', '%C3%89poque_contemporaine', 'XIXe_si%C3%A8cle', 'Ann%C3%A9es_1800', 'Ann%C3%A9es_1810', 'Ann%C3%A9es_1820', 'Ann%C3%A9es_1830', 'Ann%C3%A9es_1840', 'Ann%C3%A9es_1850', 'Ann%C3%A9es_1860', 'Ann%C3%A9es_1870', 'Ann%C3%A9es_1880', 'Ann%C3%A9es_1890', 'XXe_si%C3%A8cle', 'Ann%C3%A9es_1900', 'Ann%C3%A9es_1910', 'Ann%C3%A9es_1940', 'Ann%C3%A9es_1950', 'Ann%C3%A9es_1960', 'Ann%C3%A9es_1970', 'Ann%C3%A9es_1980', 'Ann%C3%A9es_1990', 'XXIe_si%C3%A8cle', 'Ann%C3%A9es_2000', 'Ann%C3%A9es_2010', 'Allemagne_au_XIXe_si%C3%A8cle', 'France_au_XIXe_si%C3%A8cle', 'Empire_autrichien', 'Autriche-Hongrie', 'Guerre_de_S%C3%A9cession', 'Printemps_des_peuples', 'Risorgimento', 'Second_Empire', 'Empire_allemand', 'Empire_du_Japon', 'Titanic', 'Premi%C3%A8re_Guerre_mondiale', 'Entre-deux-guerres', 'Soci%C3%A9t%C3%A9_des_Nations', 'R%C3%A9publique_de_Weimar', 'Yougoslavie', 'Nazisme', 'Seconde_Guerre_mondiale', 'R%C3%A9sistance_fran%C3%A7aise', 'Conflit_isra%C3%A9lo-arabe', 'Guerre_froide', 'Cinqui%C3%A8me_R%C3%A9publique', 'URSS', 'RDA', 'Espace_post-sovi%C3%A9tique', 'Actualit%C3%A9s_et_%C3%A9v%C3%A9nements', 'Records']
	output_politique = ['Politique', 'Altermondialisme', 'Anarchisme', 'Capitalisme', 'Communisme', 'Conservatisme', 'Gaullisme', 'Lib%C3%A9ralisme', 'Marxisme', 'Monarchie', 'Nazisme', 'Paix', 'R%C3%A9publique', 'Fran%C3%A7ais', 'ONU', 'OTAN', 'Union_europ%C3%A9enne', 'Relations_internationales', 'Politique_belge', 'Politique_britannique', 'Politique_canadienne', 'Politique_qu%C3%A9b%C3%A9coise', 'Politique_aux_%C3%89tats-Unis', 'Politique_fran%C3%A7aise', 'Politique_suisse', 'Bio%C3%A9thique', 'Droit_fran%C3%A7ais', 'Droits_de_l%27homme', 'Environnement', 'Esclavage', 'Humanitaire_et_d%C3%A9veloppement', 'Monde_colonial', 'Syndicalisme', 'Politique_sociale']
	output_religion = ['Religions_et_croyances', 'Bouddhisme', 'Bouddhisme_zen', 'Christianisme', 'Bible', 'Catholicisme', 'Christianisme_%C3%A9vang%C3%A9lique', 'Chr%C3%A9tiens_d%27Orient', 'Compagnie_de_J%C3%A9sus', 'Mormonisme', 'Protestantisme', 'Vatican', 'Hindouisme', 'Islam', 'Ja%C3%AFnisme', 'Juda%C3%AFsme', 'Sikhisme', 'Mythologie', 'L%C3%A9gendaire', 'Cr%C3%A9atures_l%C3%A9gendaires', 'Vampires', 'L%C3%A9gende_arthurienne', 'Mythologie_%C3%A9gyptienne', 'Mythologie_grecque', 'Mythologie_nordique', 'Mythologie_romaine', 'Mythologies_pr%C3%A9colombiennes', 'Mythologie_azt%C3%A8que', 'Mythologie_maya', 'Mythologie_slave', 'Mythologie_basque', 'Paranormal', 'Vie_extraterrestre_et_ufologie', 'Ath%C3%A9isme', 'Franc-ma%C3%A7onnerie', 'Monachisme', 'Tao%C3%AFsme', 'Th%C3%A9ologie', 'Spiritualit%C3%A9']
	output_sciences = ['Sciences', 'Histoire_des_sciences', 'Histoire_de_la_zoologie_et_de_la_botanique', 'Biologie', 'Anatomie', 'Biochimie', 'Bio%C3%A9thique', 'Biologie_cellulaire_et_mol%C3%A9culaire', 'Biologie_marine', '%C3%89coatlas', '%C3%89cologie', 'Microbiologie', 'Neurosciences', 'Origine_et_%C3%A9volution_du_vivant', 'Parasitologie', 'Physiologie', 'Virologie', 'Botanique', 'Agriculture_et_agronomie', 'Jardinage_et_horticulture', 'Bois_et_for%C3%AAt', 'Mycologie', 'Permaculture', 'Phycologie', 'Zoologie', 'Animaux_de_compagnie', 'Arachnologie', 'Conservation_de_la_nature', 'Carcinologie', 'C%C3%A9tac%C3%A9s', 'Canid%C3%A9s', 'Dinosaures', '%C3%89chinodermes', '%C3%89levage', 'Entomologie', 'F%C3%A9lins', 'Herp%C3%A9tologie', 'Ichtyologie', 'Malacologie', 'Mammif%C3%A8res', 'Monde_%C3%A9questre', 'Ornithologie', 'P%C3%AAche', 'Primates', 'Math%C3%A9matiques', 'Alg%C3%A8bre_nouvelle_et_Fran%C3%A7ois_Vi%C3%A8te', 'Analyse', 'Arithm%C3%A9tique_et_th%C3%A9orie_des_nombres', 'Cryptologie', 'G%C3%A9om%C3%A9trie', 'Logique', 'Probabilit%C3%A9s_et_statistiques', 'Sciences_humaines_et_sociales', 'Anthropologie', 'D%C3%A9mographie', '%C3%89conomie', 'Linguistique', 'Philosophie', 'Psychologie', 'Sociologie', 'Chimie', 'Monde_quantique', 'Mat%C3%A9riaux', 'Physique', 'Couleurs', 'Optique', 'Sciences_de_la_Terre_et_de_l%27Univers', 'Astronomie', 'Cosmologie', 'Exoplan%C3%A8tes', 'Lune', 'Mars', 'Jupiter', 'Saturne', 'Plan%C3%A9to%C3%AFde', 'G%C3%A9od%C3%A9sie_et_g%C3%A9ophysique', 'G%C3%A9ographie', 'G%C3%A9ologie', 'Min%C3%A9raux_et_roches', 'Pal%C3%A9ontologie', 'Volcanisme', 'M%C3%A9t%C3%A9orologie', 'Sp%C3%A9l%C3%A9ologie', 'Temps', 'M%C3%A9decine', 'Autisme', 'Handicap', 'H%C3%A9matologie', 'Maladies_infectieuses', 'Mort', '%C5%92il_et_vue', 'Pharmacie', 'Premiers_secours_et_secourisme', 'Sexualit%C3%A9_et_sexologie', 'Soins_infirmiers_et_profession_infirmi%C3%A8re']
	output_societe = ['Soci%C3%A9t%C3%A9', 'Acad%C3%A9mie_fran%C3%A7aise', 'Associations', 'R%C3%A9compenses_et_distinctions', 'Alimentation_et_gastronomie', 'Bi%C3%A8re', 'Boisson', 'Caf%C3%A9', 'Chocolat', 'Cuisine_fran%C3%A7aise', 'Cuisine_italienne', 'Cuisine_japonaise', 'Dessert', 'Eau', 'Fromage', 'Pomme_de_terre', 'Th%C3%A9', 'V%C3%A9g%C3%A9tarisme', 'Vigne_et_vin', 'Whisky', 'Culture', 'Culture_de_la_Suisse', 'Culture_ivoirienne', 'Culture_russe', 'Culture_sourde', 'F%C3%AAtes_et_traditions', 'Humour', 'Mode', 'Lingerie', 'Mannequinat', 'Miss_France', 'Mus%C3%A9es', 'Mus%C3%A9e_d%27Orsay', 'Mus%C3%A9e_des_beaux-arts_de_Lyon', 'Mus%C3%A9e_du_Louvre', 'Mus%C3%A9e_du_Prado', 'Patrimoine_mondial', 'Patrimoine_culturel_immat%C3%A9riel', 'Protection_du_patrimoine', 'Lieux_patrimoniaux_du_Canada', 'Biens_d%27int%C3%A9r%C3%AAt_culturel_d%27Espagne', 'Monuments_historiques', 'Monuments_prot%C3%A9g%C3%A9s_du_Portugal', 'Odeurs,_senteurs_et_parfum', 'Publicit%C3%A9', 'Punk', '%C3%89conomie', 'Agriculture_et_agronomie', 'Protection_des_cultures', 'Capitalisme', 'Commerce', 'Entreprises', 'McDonald%27s', 'Sony', 'Coop%C3%A9ratives', 'Finance', 'Industrie', 'Management', 'Travail_et_m%C3%A9tiers', '%C3%89ducation', '%C3%89coles', '%C3%89criture', 'Grandes_%C3%A9coles', 'Arts_et_M%C3%A9tiers_ParisTech', 'Scoutisme', 'Universit%C3%A9', 'Universit%C3%A9s_am%C3%A9ricaines', 'Universit%C3%A9s_fran%C3%A7aises', '%C3%89ducation_au_Qu%C3%A9bec', 'Afro-Am%C3%A9ricains', 'Autisme', 'Femmes', 'Handicap', 'LGBT', 'Minorit%C3%A9s', 'S%C3%A9r%C3%A8res', 'Langues', 'Langue_arabe', 'Langues_cr%C3%A9oles_et_cr%C3%A9olophonie', 'Esp%C3%A9ranto', 'Fran%C3%A7ais', 'Langues_germaniques', 'Lusophonie', 'Sanskrit', 'Philosophie', 'Friedrich_Nietzsche', 'Lumi%C3%A8res', 'Martin_Heidegger', 'Philosophie_analytique', 'Philosophie_antique', 'Philosophie_indienne', 'Scepticisme', 'Thomas_d%27Aquin', 'Bio%C3%A9thique', 'Handicap', 'Psychotrope', 'Tabac', 'Arm%C3%A9e_fran%C3%A7aise', 'L%C3%A9gion_%C3%A9trang%C3%A8re', 'Forces_arm%C3%A9es_des_%C3%89tats-Unis', 'Forces_canadiennes', 'Royal_Navy', 'Arm%C3%A9e_italienne', 'Char_de_combat', 'Criminologie', 'Piraterie', 'Police', 'Prison', 'S%C3%A9curit%C3%A9_civile_et_sapeurs-pompiers', 'S%C3%A9curit%C3%A9_de_l%27information', 'S%C3%A9curit%C3%A9_informatique']
	output_sport = ['Sport', 'Arbitrage_sportif', 'Handisport', 'Jeux_olympiques', 'Patronages_sportifs_catholiques', 'Baseball', 'Basket-ball', 'Beach-volley', 'Cricket', 'Crosse', 'Curling', 'Football', 'Football_am%C3%A9ricain', 'Football_australien', 'Football_canadien', 'Handball', 'Hockey_sur_gazon', 'Hockey_sur_glace', 'Rink_hockey', 'Rugby_%C3%A0_XIII', 'Rugby_%C3%A0_XV', 'Sports_ga%C3%A9liques', 'Volley-ball', 'Sports_de_combat', 'Boxe_anglaise', 'Catch', 'Escrime', 'Judo', 'Karat%C3%A9', 'Taekwondo', 'Tir', 'Tir_%C3%A0_l%27arc', 'Sports_d%27hiver', 'Biathlon', 'Combin%C3%A9_nordique', 'Luge', 'Patinage_artistique', 'Saut_%C3%A0_ski', 'Ski', 'Ski_acrobatique', 'Ski_de_fond', 'Snowboard', 'Alpinisme_et_escalade', 'Athl%C3%A9tisme', 'Cyclisme', 'Tour_de_France', 'Golf', 'Gymnastique', 'Halt%C3%A9rophilie', 'Musculation', 'Parachutisme', 'Pentathlon_moderne', 'Snooker', 'Sp%C3%A9l%C3%A9ologie', 'Sports_de_raquette', 'Badminton', 'Tennis', 'Tennis_de_table', 'Triathlon', 'Sport_automobile', 'Formule_1', 'NASCAR', 'Rallye_automobile', 'Endurance_automobile', 'Sport_automobile_%C3%A0_%C3%A9nergies_alternatives', 'Sport_motocycliste', 'Sports_nautiques', 'Aviron', 'Cano%C3%AB-kayak', 'Natation', 'Natation_synchronis%C3%A9e', 'Plongeon', 'Surf', 'Voile', 'Water-polo', 'Vie_quotidienne_et_loisirs', 'Arts_martiaux_et_sports_de_combat', 'Mod%C3%A9lisme', 'A%C3%A9romod%C3%A9lisme', 'Parcs_de_loisirs', 'Plong%C3%A9e_sous-marine', 'Randonn%C3%A9e', 'Roller_et_skateboard', 'Sp%C3%A9l%C3%A9ologie', 'Tourisme', 'G%C3%A9n%C3%A9alogie', 'Collections', 'Aquariophilie', 'Numismatique', 'Philat%C3%A9lie', 'Jardinage_et_horticulture', 'Bonsa%C3%AF', 'Plantes_utiles', 'Jeux', 'Quiz', '%C3%89checs', 'Jeu_de_go', 'Lego', 'Poker', 'Transformers']
	output_technologie = ['Technologies', 'Industrie', 'Armes', 'Assainissement', 'Barrage', 'B%C3%A2timent_et_travaux_publics', '%C3%89lectricit%C3%A9_et_%C3%A9lectronique', '%C3%89nergie', '%C3%89nergie_fossile', '%C3%89nergie_renouvelable', 'Nucl%C3%A9aire', 'Froid_et_climatisation', 'G%C3%A9nie_m%C3%A9canique', 'Horlogerie', 'Mat%C3%A9riaux', 'Micro_et_nanotechnologie', 'Mine', 'Bassin_minier_du_Nord-Pas-de-Calais', 'Bassins_houillers_des_Vosges_et_du_Jura', 'Robotique', 'Textile', '%C3%89criture', '%C3%89dition', 'Information_g%C3%A9ographique', 'M%C3%A9dias', 'Journalisme', 'Presse_%C3%A9crite', 'Radio', 'T%C3%A9l%C3%A9vision', 'Renseignement', 'Sciences_de_l%27information_et_des_biblioth%C3%A8ques', 'S%C3%A9curit%C3%A9_de_l%27information', 'Technologies_de_l%27information_et_de_la_communication_pour_l%27enseignement', 'T%C3%A9l%C3%A9communications', 'Informatique', 'Apple', 'Bases_de_donn%C3%A9es', 'Donn%C3%A9es', 'GNU/Linux', 'Google', 'Imagerie_num%C3%A9rique', 'Informatique_th%C3%A9orique', 'Internet', 'Logiciel', 'Logiciels_libres', 'Microsoft', 'Programmation_informatique', 'R%C3%A9seaux_informatiques', 'S%C3%A9curit%C3%A9_informatique', 'Web_s%C3%A9mantique', 'Transports', 'A%C3%A9ronautique', 'H%C3%A9licopt%C3%A8res', 'Astronautique', 'Autobus', 'Automobile', 'Bicyclette', 'Camion', 'Chemin_de_fer', 'Grande_vitesse_ferroviaire', 'Chemin_de_fer_en_Am%C3%A9rique_du_Nord', 'Chemin_de_fer_en_Suisse', 'Maritime', 'Titanic', 'Paquebots', 'Phares', 'Ports', 'Voile', 'Sous-marins', 'Motocyclette', 'Ponts', 'Route', 'Tunnels', 'Transports_en_commun', 'Transports_en_%C3%8Ele-de-France', 'Transports_%C3%A0_Los_Angeles']

	x = input_categories.split(";")
	output = ""
	output = output + categorie_matching(x, output_art, "art;")
	output = output + categorie_matching(x, output_geographie, "geographie;")
	output = output + categorie_matching(x, output_histoire, "histoire;")
	output = output + categorie_matching(x, output_politique, "politique;")
	output = output + categorie_matching(x, output_religion, "religion;")
	output = output + categorie_matching(x, output_sciences, "sciences;")
	output = output + categorie_matching(x, output_societe, "societe;")
	output = output + categorie_matching(x, output_sport, "sport;")
	output = output + categorie_matching(x, output_technologie, "technologie;")

	return output


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


def crawling_special_wiki(url, tour, total_tour):
	from classCrawler import *
	urls = def_urls(url)
	nb = len(urls)
	wikipedia = Wikipedia(n=nb)
	i = 0

	for x in urls:
		print "\n\nTour ", tour, "/", total_tour, " - Resultats du crawl ", i+1 , " / ", nb ,"\n"
		succes_crawl = wikipedia.crawling(x)
		i += 1
	del(wikipedia)


def crawling_categories_wiki(categorie, body, position):
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


def get_categories_wikipedia():
	url = "https://fr.wikipedia.org/wiki/Portail:Accueil"
	req = urllib2.urlopen(url)
	body = req.read()
	position = 0

	print "Categories pour Sciences \n"
	categories, position = crawling_categories_wiki("Technologies", body, position)
	print categories

	print "\n\nCategories pour Technologies \n"
	categories, position = crawling_categories_wiki("M%C3%A9decine", body, position)
	print categories

	print "\n\nCategories pour Medecine \n"
	categories, position = crawling_categories_wiki("Arts", body, position)
	print categories

	print "\n\nCategories pour Arts \n"
	categories, position = crawling_categories_wiki("Sport", body, position)
	print categories

	print "\n\nCategories pour Sport \n"
	categories, position = crawling_categories_wiki("Vie_quotidienne_et_loisirs", body, position)
	print categories

	print "\n\nCategories pour Loisirs \n"
	categories, position = crawling_categories_wiki("Soci%C3%A9t%C3%A9", body, position)
	print categories

	print "\n\nCategories pour Societe \n"
	categories, position = crawling_categories_wiki("Politique", body, position)
	print categories

	print "\n\nCategories pour Politique \n" 
	categories, position = crawling_categories_wiki("Religions_et_croyances", body, position) 
	print categories

	print "\n\nCategories pour Religions \n" 
	categories, position = crawling_categories_wiki("Histoire", body, position) 
	print categories

	print "\n\nCategories pour Histoire \n" 
	categories, position = crawling_categories_wiki("G%C3%A9ographie", body, position)
	print categories

	print "\n\nCategories pour Geographie \n"
	categories, position = crawling_categories_wiki("FIN!!!", body, position)
	print categories