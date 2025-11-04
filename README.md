# Projektna naloga - analiza slovenskih državnih tekmovanj v sestavljanju 3x3 rubikove kocke
*Avtor: David Šiška*

To je projektna naloga za predmet Uvod v programiranje.
V nalogi zberem približno 1000 podatkov o rezultatih na državnih tekmovanjih v hitrostnem sestavljanju rubikove kocke in jih interpretiram. Tu je nekaj osnovnih podatkov o tekmovanjih, ki bodo v pomoč pri razumevanju nekaterih uporabljenih terminov.

## Osnovni podatki 
Hitrostno sestavljanje rubikove kocke je hobi, ki je v zadnjih dvajsetih letih precej razcvetel v popularnosti. Zaradi velikega povpraševanja, so bila v začetku drugega tisočletja prvič organizirana tekmovanja v hitrostnem sestavljanju rubikove kocke, kmalu zatem, pa je bila ustanovljena mednarodna zveza za kockanje, znana tudi kot WCA (World Cube Association). Vse podatke v nalogi sem pridobil iz njihove uradne spletne strani (https://www.worldcubeassociation.org/). Tudi v Sloveniji skupina prostovoljcev od leta 2010 dalje organizira tekmovanja, ki jih odobri organizacija WCA. Ker je bilo do novembra 2025 organiziranih že kar 38 tekmovanj, sem se za analizo odločil osredotočiti le na največja in najpomembnejša - t.j. državna tekmovanja. Ta potekajo enkrat na leto od leta 2018 dalje in so veliko bolj prestižna. Na žalost podatki za leta 2018 in 2022 niso na voljo (problem s spletno stranjo, ne s programom), prav tako pa tekmovanja v letih 2020 in 2021 ni bilo zaradi karantene. Na državna tekmovanja lahko pridejo tudi tekmovalci iz tujine, vendar za zmagovalca tekmovanja velja najhitrejši Slovenec.

Za interpretacijo analize je potrebno osnovno znanje o potekanju tekmovanj. Na vsakem tekmovanju je več disciplin, t.j. tekmovalci se lahko primerjajo v sestavljanju več različnih tipov rubikovih kock (2x2x2, 3x3x3, 4x4x4 rubikova kocka, pyraminx, megaminx...). Najpopularnejša disciplina je klasična 3x3 rubikova kocka, zato se bom tudi nanjo osredotočal. Vsaka disciplina pa načeloma poteka v več krogih (rundah). V prvem krogu lahko sodelujejo vsi, v naslednje kroge pa pride le določen procent najhitrejših sestavljalcev. V zadnji krog (finali) pa navadno pride le najboljših 10-16 tekmovalcev. V vsakem krogu ima tekmovalec 5 poskusov. V vsakem poskusu dobi tekmovalec zmešano kocko, ki jo sestavi v prisotnosti sodnika, ki zagotovi, da se je čas pravlino meril. V vsakem krogu se poleg samih časov zabeleži posebej tudi najhitrejši poskus (t.i. "single") in povprečje (t.i. "average") vsakega tekmovalca, ki se izračuna tako da se znebimo najhitrejšega in najpočasnejšega časa, nato pa naredimo povprečje preostalih treh. Za uvrstitev na tekmovanju več šteje povprečje, saj je v najhitrejšem poskusu navadno prisotno tudi nekaj sreče. V podatkih bomo včasih zasledili tudi podatek o državnem rekordu (NR), celinskem rekordu (CR) ali svetovnem rekordu (CR). Te se zabeležijo bodisi k single ali average podatku, če je bil kateri od rekordov dosežen.

Cilj analize je spremljati razvoj državnih tekmovanj (število tekmovalcev, zastopanost držav...) in rezultate na tekmovanjih (spreminjanje časov na tekmovanjih, rekordi...), kjer se bom pogosto posebej osredotočil na Slovence.

## Navodila za uporabo
S pomočjo datoteke requirements.txt si lahko uporabnik naloži potrebne programe za zagon.
Poleg tega potrebuje naslednje knjižnice:
- selenium (razne knjižnice za pobiranje podatkov s spleta)
- time (upočasnitev programa, da nas spletna stran ne blokira)
- os (preverjanje poti datotek)
- re (uporaba regularnih izrazov)
- csv (ustvarjanje csv datotek)
- pandas (analiza podatkov v Jupyter notebooku)
- matplotlib.pyplot (risanje grafov)
- numpy (dodatne nastavitve za grafe)

## Zagon programa
Uporabnik najprej zažene datoteko zajem_podatkov.py, ki pobere podatke iz spletne strani in jih lokalno shrani kot html datoteke. Nato zažene shranjevanje podatkov.py, ki html datoteke predela in združi v csv datoteko s podatki. Nato zažene moja_analiza.ipynb, kjer lahko dostopa do analize podatkov in interpretacije.
