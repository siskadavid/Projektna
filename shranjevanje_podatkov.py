import os
import re
import csv

# Precompiled regex izrazi
competition_data_re = r"<div class=\"results-data\">.*<\/table><\/div>"
competition_data_re_compiled = re.compile(competition_data_re, re.DOTALL)
rounds_data_re = r"<h2>(?P<round_title>.*?)</h2>.*?<tbody class=\"\">(?P<round_data>.*?)</tbody></table>"
rounds_data_re_compiled = re.compile(rounds_data_re, re.DOTALL)
rows_data_re = r"<tr class=\"\">(?P<row>.*?)</tr>"
rows_data_re_compiled = re.compile(rows_data_re, re.DOTALL)
fields_data_re = r"<td.*?>(?P<field>.*?)</td>"
fields_data_re_compiled = re.compile(fields_data_re, re.DOTALL)
name_data_re = r"<a.*?>(?P<name>.*?)</a>"
name_data_re_compiled = re.compile(name_data_re, re.DOTALL)
flag_data_re = r"<span><span class=\"fi fi-(?P<flag>\w+)\"></span></span>"
flag_data_re_compiled = re.compile(flag_data_re)

# Naložimo html datoteke s podatki tekmovanj in jih predelamo v csv format
parsed_data = [["Mesto", "Ime", "Single", "SingleRekord", "Average", "AverageRekord", "Drzava", "Poskusi", "ImeRunde", "Leto"]] # Seznam s podatki iz vseh tekmovanj
for leto in range(2019, 2026):
	results_file_url = f"datoteke/html/SlovenianNationals{leto}.html"
	if os.path.exists(results_file_url): # Preverimo če ta datoteka sploh obstaja
		with open(results_file_url, "r", encoding="utf-8") as file:
			competition_page = file.read()
			competition_data = competition_data_re_compiled.search(competition_page).string # Izoliramo le del HTMLja, ki vsebuje tabelo z rezultati
			rounds_data = rounds_data_re_compiled.finditer(competition_data) # Izoliramo vsako tabelo (rundo) s funkcijo finditer da lahko po njih iteriramo
			for round in rounds_data:
				round_title = round.group("round_title") # Ime runde (npr. 3x3x3 Cube Final)
				round_data = round.group("round_data") # Preostanek podatkov runde (tabela brez glave)
				rows_data = rows_data_re_compiled.finditer(round_data) # Izoliramo in iteriramo po vsaki vrstici v tabeli
				for row in rows_data:
					row_data = row.group("row") # Izoliramo samo del vrstice s podatki, ki nas zanimajo
					fields_data = fields_data_re_compiled.findall(row_data) # Shranimo vsako celico v vrstici kot element seznama
					fields_data[1] = name_data_re_compiled.search(fields_data[1]).group("name") # Prilagodimo prvi element, da ostane le ime brez linka na WCA id
					fields_data[6] = flag_data_re_compiled.search(fields_data[6]).group("flag") # Prilagodimo šesti element, da ostane le kratica zastave
					parsed_data.append(fields_data) # V seznam dodamo ostale podatke
					fields_data.append(round_title) # V seznam dodamo ime runde
					fields_data.append(leto) # V seznam dodamo leto tekmovanja

# Shranimo seznam vseh podatkov v csv datoteko
all_file_url = f"datoteke/csv/SlovenianNationals.csv"
with open(all_file_url, "w", newline = "", encoding = "utf-8") as data_file:
	writer = csv.writer(data_file)
	writer.writerows(parsed_data)
	print(f"Podatki shranjeni za Slovenian Nationals.")