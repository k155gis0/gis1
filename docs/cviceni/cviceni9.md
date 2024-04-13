---
icon: material/numeric-9-box
title: Cvičení 9
---

# Volně dostupné GIS nástroje (QGIS)

## Cíl cvičení

Seznámit se s volně dostupnými (open source) GIS nástroji. V praktické
rovině je prezentován [QGIS](https://qgis.org).

## Základní pojmy

- [**open
  source**](https://cs.wikipedia.org/wiki/Otev%C5%99en%C3%BD_software) –
  počítačový software s otevřeným zdrojovým kódem
- [**svobodný
  software**](https://cs.wikipedia.org/wiki/Svobodn%C3%BD_software) –
  software, který uživatelé mohou používat k libovolnému účelu,
  kopírovat, distribuovat, studovat a měnit
- [**OSGeo**](https://www.osgeo.org/) – nevládní nezisková organizace, jejímž cílem je podporovat a prosazovat společný vývoj otevřených geoinformačních technologií a dat
- [**QGIS**](https://qgis.org) – svobodný a multiplatformní geografický informační systém (GIS)

## Použité datové podklady

Cílem je používat data přímo od jejich poskytovatelů. Pro případ technických problémů je ale připraven balíček již připravených dat. Aktualizovat balíček.

- [Data](https://geo.fsv.cvut.cz/vyuka/155gis1/geodata/gis1-cviceni10.zip)

Přehled dat, které budeme používat:

- balíček dat z RÚIAN pro jednu obec, budeme používat obec Zdiby. Pro kontrolu jednotlivých mezivýslednků doporučujeme použít totožnou obec.Stáhneme jako součást obsahu cvičení pomocí pluginu v QGIS.
- [číselník druhu pozemku](https://services.cuzk.cz/sestavy/cis/SC_D_POZEMKU.zip) – tabulka obsahující kódové hodnoty existujících druhů pozemku spolu s jejich textovým popisem a dalšími informacemi ve formátu CSV. Stáhnout jako běžný soubor.
- připravený styl pro *parcely* formou souboru ``parcely_styl.qmd``


## Náplň cvičení

Jako podpůrný materiál budeme používat školící materiály [QGIS pro
začátečníky](https://gismentors.github.io/qgis-zacatecnik) skupiny
[GISMentors](https://gismentors.cz).

### Načtení vstupních dat

Otevřeme QGIS a nainstalujeme plugin pro data z RÚIAN. Následně stáhneme data pro obec Zdiby a výstup uložíme do souboru ``zdiby_ruian.gpkg``. Po potvrzení nastavení v dialogovém okně se data stáhnou a náseldně se rovnou i  načtou do mapového okna.

Následně si stáhneme data číselníku druhu pozemku a načteme je do QGISu jako tabulková data bez geometrie.

Podklady:

- [přídání a export
  dat](https://gismentors.github.io/qgis-zacatecnik/vektorova_data/vektor_import.html#pridani-a-export-dat),
- [data s oddělenými
  hodnotami](https://gismentors.github.io/qgis-zacatecnik/vektorova_data/import_delim.html#import-dat)
  (pozor na datové typy - přetažení vs formulář)


### Připojení tabulkových dat

Připojíme tabulku s druhy pozemků k polygonové vrstvě *parcely*. Propojení je možné nastavit na zákaldě atributu s kódem druhu pozemku. Ten se jmenuje ``KOD`` a``DruhPozemkuKod``.

Podklady: [Postup
připojení dat](https://gismentors.github.io/qgis-zacatecnik/vektorova_data/join.html#postup-pripojeni)
 
### Nastavení stylu

Nastavíme symbologii pro *parcely* na základě druhu pozemku.
Styl je možné také sdílet s konkrétním nastavením. Vlastní vytvořený styl si uložíme do samostatného souboru.
Pro opačný postup použijeme již připravený styl pro vrstvu *parcely*, který lze načíst ze souboru ``parcely_styl.qmd``.

Q: Je spolehlivější sdílet styl založený na původním atributu, anebo na připojeném? 


Podklady:

- [Nastavení stylu](https://gismentors.github.io/qgis-zacatecnik/vektorova_data/vektor_data_prace.html#styl)
- [Ukládání stylování do souboru](https://gismentors.github.io/qgis-zacatecnik/vektorova_data/vektor_data_prace.html#ulozeni-a-nacteni-nastaveni-vrstvy-pomoci-souboru)

### Výpočet plochy a její použití

Dalším běžným úkolem je výpočet statistických údajů. Jedním z nejzákladnějších požadavků je práce s úrčováním plochy/výměry.
Zadáním je určit podíl jednotlivých druhů pozemků podle jejich výměry pro jednotlivá katastrální území.
Prvním krokem je spočítat plochu záznamům ve vrstvě *parcely* do atributu s názvem ``plocha_m `` pomocí *KALKULÁTORU POLÍ*.

Q: Jaký je rozdíl mezi výměrou v datech o parcelách a tou spočtenou přímo z geometrie?

Druhým krokem je sloučit parcely v jednotlivých katastrálních územích podle jejich druhu. Použijeme nástroj pro sloučení geometrii, kde je možné použít podmínku - *DISSOLVE*. Pole ``DruhPozemkuKod `` a ``KatastralniUzemiKod `` nastavíme jako parametry.
Pro aktualizaci plochy v atributu ``plocha_m `` použijeme nástroj aktualizce v atributové tabulce.
Výslední data popisují dobře hodnoty, ale jejich uspořádání není vhodné na jednoduché zpracování.

Podklady:

- [Kalkulátor polí](https://gismentors.github.io/qgis-zacatecnik/vektorova_data/editace.html#kalkulator-poli)
- [Prostorové analýzy](https://gismentors.github.io/qgis-zacatecnik/vektorova_data/prostorove_analyzy.html)
- [Dissolve](https://gismentors.github.io/qgis-zacatecnik/vektorova_data/prostorove_analyzy.html#rozpustit-dissolve)

### Alternativní postup

Druhý krok můžeme provést i za pomocí dotazu v *DB manageru*, kde si nejdříve musíme připojit ``zdiby_ruian.gpkg`` jako databázové připojení.

Pro rozložení do jednotlivých kroků může tato úloha vypadat následovně:

- SELECT DruhPozemkuKod, KatastralniUzemiKod, plocha_m FROM parcely
- SELECT DruhPozemkuKod, KatastralniUzemiKod, sum(plocha_m) FROM parcely group by DruhPozemkuKod, KatastralniUzemiKod
- SELECT DruhPozemkuKod, KatastralniUzemiKod, sum(CASE WHEN DruhPozemkuKod=2 THEN plocha_m END) DruhPozemkuKod_2 FROM parcely group by DruhPozemkuKod, KatastralniUzemiKod  + ostatní kategorie dle druhu pozemku

Výslednou vrstvu lze uložit jako samostatný výsledek a připojit k vrstvě *katastralniuzemi*. Pro tuto lze par vykreslit jednotlivé diagramy spočtených kategorií.

Podklady:

- [Kartodiagramy](https://gismentors.github.io/qgis-pokrocily/ruzne/grafy.html#zalozka-diagramdiagramy)

## Simulace výběru pozemků pro fotovoltaické elektrárny

Zjednodušeně si vyzkoušíme malou část takovéhoto postupu.
Jedna část definuje výběr podle druhu pozemku. Druhá pak odstraní části parcel, které jsou v příliš malé vzdálensoti od vybraných typů stavebních obejktů.

### Výběr parcel

Parcely lze vybrat na základě druhu pozemku a způsobu využití.
Nás zajímají parcely podle náseldující definice:

- DruhPozemkuKod může nabývat hodnoty 2,8,10,14
- ZpusobyVyuzitiPozemku může nabývat hodnoty  2,3,4,5,26. Pozor, tam kde je NULL hodnota, je pro nás také relevantní.

Vybrané parcely uložíme jako mezivýsledek do nové vrstvy.

Podklady:

- [Atributové dotazování](https://gismentors.github.io/qgis-zacatecnik/vektorova_data/dotazovani.html#atributove-dotazovani)


### Okolí budov

V odstupové vzdálenosti 500 m od určitých stavebních objektů nelze nic realizovat. 

Vybereme stavební objekty podle způsobu jejich využití, kterých se toto omezení týká -  ZpusobVyuzitiKod nabývá hodnoty 2,6,7,8.

Kolem vybraných budov pomocí funkce *BUFFER* obalovou zónu o velikosti 500 m. 

Následně potřebujeme ořezat vybrané parcely ořezat vytvořenou obalovou zónou budov. Pro tento krok použijeme funkci *DIFFERENCE*

Podklady:

- [Obalová zóna dle pevné vzdálenosti (buffer)](https://gismentors.github.io/qgis-zacatecnik/vektorova_data/prostorove_analyzy.html#obalova-zona-dle-pevne-vzdalenosti-buffer)
- [Rozdíl (difference)](https://gismentors.github.io/qgis-zacatecnik/vektorova_data/prostorove_analyzy.html#rozdil-difference)


<!---
### Vytvoření obalové zóny kolem dálnic

Přidáme vrstvu *silnice* a vybereme pomocí vzorce ``"typ" = 1``
dálnice.

Dále pomocí funkce **BUFFER** vytvoříme obalové zóny kolem dálnic s šířkou 10 km.

Podklady:

- [Atributové dotazování](https://gismentors.github.io/qgis-zacatecnik/vektorova_data/dotazovani.html#atributove-dotazovani)
- [Obalová zóna dle pevné vzdálenosti (buffer)](https://gismentors.github.io/qgis-zacatecnik/vektorova_data/prostorove_analyzy.html#obalova-zona-dle-pevne-vzdalenosti-buffer)

### Vyběr obcí

Vybereme obce, které alespoň částí svého území leží v 10km okolí dálnic.

Podklady: [Prostorové dotazování](https://gismentors.github.io/qgis-zacatecnik/vektorova_data/dotazovani.html#prostorove-dotazovani)

### Pokročilé dotazování

Pokročilé dotazování pomocí jazyka SQL umožňuje *Databázový manager*.
<!---

## Zadání domácího úkolu k semestrální práci

Zpracujte podklady i pro ostatní měsíce roku 2018.

Pomocí jazyka SQL zkuste vyřešit následující úlohy:

1. Zjistěte průměrnou nezaměstnanost v daném okrese
2. Proveďte agregace údajů na úrovni kraje
-->