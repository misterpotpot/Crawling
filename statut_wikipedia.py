# -*- coding: utf8 -*-

import sqlite3



conn = sqlite3.connect('../zapking.db')
cursor = conn.cursor()
cursor.execute("""SELECT href FROM urls_wikipedia WHERE push = 0""")
i = 0
for x in cursor.fetchall():
	i += 1
print i, " articles de 'urls_wikipedia' n'ont pas encore ete push dans 'urls'"
cursor.close()
conn.close()