# Prostorové funkce (geoprocessing), spatial join

## Cíl cvičení

Seznámení se se základními geoprocessingovými nástroji v GISu v rámci řešení komplexní úlohy.

## Základní pojmy

- [**buffer**](https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/buffer.htm)
- [**clip**](https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/clip.htm)
- [**select**](https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/select.htm)
- [**intersect**](https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/intersect.htm)
- [**spatial join**](https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/spatial-join.htm)
- [**erase**](https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/erase.htm)
- [**union**](https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/union.htm)
- [**remove overlap**](https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/remove-overlap-multiple.htm)
- [**symmetrical difference**](https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/symmetrical-difference.htm)
- [**count overlapping features**](https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/count-overlapping-features.htm)

## Použité datové podklady

- Pobočky České pošty v Plzeňském kraji (bodová vrstva)
- Obce ČR (ArcČR 500, polygonová vrstva)

## Náplň cvičení

Představte si, že pracujete jako GIS analytik pro Českou poštu a vaším úkolem je z důvodu úspor navrhnout řešení snížení počtu poboček. Snahou tohoto kroku je však i minimalizace negativních dopadů na obyvatele, proto bylo rozhodnuto o následujících podmínkách, které musíte ve svém návrhu dodržet:

1. Rušení poboček nebude probíhat v obcích s méně než 2500 obyvateli.
2. V obcích nad 2500 obyvatel neklesne počet poboček pod 1.
3. Vzájemná vzdálenost poboček v jedné obci nebude nižší než 3 km vzdušnou čarou.

Jakou finanční úsporu jste schopni svým návrhem zajistit, pokud by provoz jedné pobočky vycházel ročně na 2,5 milionu CZK? Pro zjednodušení budete úlohu řešit pouze v rámci Plzeňského kraje a ke každé pobočce přistupovat rovnocenně.

## Pracovní postup

1. Výběr obcí nad 2500 obyvatel (atributový dotaz)
2. Výběr typu pobočky (DQ: ZKRNAZ_DRU = 'pošta')
2. Spatial join: výběr obcí + pobočky (přidat nové pole count(ID))
3. Výběr obcí nad 2500 obyvatel & více než 1 pobočkou
4. Výběr poboček, které se nachází v těchto obcích (prostorový dotaz)
5. Obalová zóna 3 km kolem výběru poboček ČP
6. Vizuální vytipování poboček ke zrušení
7. Ve vrstvě poboček tvorba pomocného atributu RUSENO (short), defaultní hodnota 0
8. Manuální výběr poboček ke zrušení, změna hodnoty atributu RUSENO na 1
9. Zobrazení rušených poboček, sumarizace (DQ: RUSENO = 1)

## Zadání domácího úkolu k semestrální práci
