# Vektorizace, tvorba geodatabáze, kontrola topologie

## Cíl cvičení

Navázání na minulé cvičení. Ukázka automatického ořezu footprintu. Tvorba vlastní geodatabáze, vektorizace a práce s atributy. Ukázka kontroly topologie vektorových dat.

## Základní pojmy

- [**geodatabáze**](https://pro.arcgis.com/en/pro-app/3.0/help/data/geodatabases/overview/what-is-a-geodatabase-.htm) – prostředí pro správu bází geografických dat

- [**dataset**](https://pro.arcgis.com/en/pro-app/latest/help/data/feature-datasets/feature-datasets-in-arcgis-pro.htm) – soubor shrnující pod sebe vybrané třídy prvků se stejným souřadnicovým systémem

- **vektorizace** – přepracování mapy v analogové formě, popř. digitální mapy v rastrové formě do vektorové formy

- [**třída prvků**](https://pro.arcgis.com/en/pro-app/3.0/help/data/geodatabases/overview/feature-class-basics.htm) – homogenní kolekce společných prvků, z nichž má každý stejnou prostorovou reprezentaci (např. body, linie nebo polygony) a společnou sadu sloupců atributů

- [**subtyp**](https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/overview/an-overview-of-subtypes.htm) – množina prvků v tabulce, které mají stejné atributy; používají se pro kategorizaci dat

- [**topologie**](https://pro.arcgis.com/en/pro-app/latest/help/data/topologies/topology-in-arcgis.htm) – definování struktury prvků geosystému na základě jejich vztahů konektivity (vzájemného spojení) a kontinuity (vzájemné polohy)

## Použité datové podklady

- [Císařské otisky stabilního katastru](../../data/#cisarske-otisky-stabilniho-katastru)
- [Státní mapa 1 : 5 000 – odvozená](../../data/#statni-mapa-1-:-5-500-0-–-odvozena)
- klad SMO5

## Pozn

- nahrát data smo5 rastry + smo5 klad

## Náplň cvičení

### Založení nové geodatabáze

**1.** Geodatabázi vytvoříme kliknutím pravým tlačítkem myši na složku našeho projektu v záložce *Catalog* -> *New* -> *File Geodatabase*.

???+ note "&nbsp;<span style="color:#448aff">Poznámka ke geodatabázi:</span>"
      Takto vytvořenou geodatabázi můžeme otevřít v jakémkoliv jiném ArcGIS Pro Projektu. Geodatabáze je vhodná pro sdílení GIS dat – lze jí otevřít také v jiných GIS softwarech (např. QGIS)

<figure markdown>
![new_gdb](../assets/cviceni6/new_gdb.png "Tvorba nové geodatabáze")
    <figcaption>Tvorba nové geodatabáze</figcaption>
</figure>

### Importu předem georeferencovaného rastru

**1.** Do mapy si načteme částečně georeferencované listy Státní mapy 1 : 5 000 – odvozené (SMO5). Bude nutné negeoreferencované listy souřadnicově umístit.

**2.** Oproti císařským otiskům stabilního katastru, které se georeferencují na identické body v mapě, lze SMO5 georeferencovat na rohové body mapových listů, které mají dané souřadnice v sysému S–JTSK (EPSG:5514). Pro georeferencování použijeme síť kladu mapových listů SMO5 (síť o rozměrech 2,5x2 km).

**3.** Dle postupu z minulého cvičení si georeferencujeme zbývající souřadnicově nepřipojené mapové listy. Následně vytvoříme v nové geodatabázi mozaiku, do které georeferencované rastry importujeme.

### Automatický ořez footprintu

Ve stavu, kdy máme přidané georeferencované rastry do mozaiky, je potřeba oříznout jejich footprint tak, aby se vytvořila bezešvá mapová vrstva. Footprint lze upravit ručně (viz minulé cvičení) nebo automaticky načtením kladu mapových listů.

**1.** V mapovém okně otevřeme mozaiku a klad mapových listů. Kladu mapových listů změníme symbologii tak, abychom viděli pouze hrany listů. 

<figure markdown>
![klad](../assets/cviceni6/klad.png "Mozaika a klad mapových listů v mapovém okně")
    <figcaption>Mozaika a klad mapových listů v mapovém okně</figcaption>
</figure>

**2.** Před automatickým ořezem footprintů je nutné zkontrolovat pojmenování listů, které musí být jak v mozaice, tak v kladu listů stejné. Případně je potřebný jiný jednoznačný atribut, na základě kterého se obě vrstvy propojí.

<figure markdown>
![klad_tabulka](../assets/cviceni6/klad_tabulka.png "Ukázka atributových tabulek předpřipravených vrstev"){ width="800" }
    <figcaption>Ukázka atributových tabulek předpřipravených vrstev</figcaption>
</figure>

**3.** Automatický ožez footprintu probíhá následovně: pravým kliknutím myši na danou mozaiku -> *Modify* -> *Import Footprints or Boundary*. 

**4.** Ve funkci *Import Mosaic Dataset Geometry* nastavíme parametry dle obrázku níže.

- *Target Feature Class* – vrstva, jejíž geometrii chceme upravit. 

- *Target Join Field* – sloupec s jednoznačným indetifikátorem výstupní vrstvy.

- *Input Feature Class* – ořezová vrstva.

- *Input Join Field* – sloupec s jednoznačným indetifikátorem ořezové vrstvy.

<figure markdown>
![import_footprint](../assets/cviceni6/import_footprint.png "Nastavení funkce Import Mosaic Dataset Geometry")
    <figcaption>Nastavení funkce Import Mosaic Dataset Geometry</figcaption>
</figure>

**5.** Výsledek funkce *Import Mosaic Dataset Geometry* je vidět níže.

<figure markdown>
![aut_orez](../assets/cviceni6/aut_orez.png "Výsledek automatického ořezu footprintu")
    <figcaption>Výsledek automatického ořezu footprintu</figcaption>
</figure>

### Vytvoření nového datasetu v geodatabázi

**1.** Pro vytvoření souhrného datasetu, ve kterém budeme následně uchovávat některé datové vrstvy, je nutné kliknout pravým tlačítkem na cílovou geodatabázi -> *New* -> *Feature Dataset*.

**2.** Otevře se funkce *Create Feature Dataset*, ve které určíme mimo cílové geodatabáze také název a souřadnicový systém datasetu.

<figure markdown>
![dataset](../assets/cviceni6/dataset.png "Vytvoření datasetu")
    <figcaption>Vytvoření datasetu</figcaption>
</figure>

### Vektorizace

Pro analýzu rastrových map, je téměř vždy nutná jejich vektorizace, tedy převedení mapy do vektorové podoby. Existují různé možnosti automatizace tohoto procesu, ale my si ukážeme nejjednodušší metodu, kterou je manuální vektorizace.

#### Založení třídy prvků

**1.** Nejprve je nutné vytvořit si třídy, do kterých budeme vektorizaci zakreslovat. Tento krok se samozřejmě liší dle specifik dané práce, ale pro naši ukázku to znamená, že musíme vytvořit třídy pro typy využití pozemků SMO5, kterou budeme vektorizovat:

- plochy – les, louka, pastvina, orná půda, nádvoří, zahrada, hřbitov apod.
- domy – kostel, domy bez značení
- vodstvo – vodní toky, vodní plochy
- cestní síť

???+ note "&nbsp;<span style="color:#448aff">Tip před tvorbou třídy prvků:</span>"
      Před tvorbou tříd prvků pro vektorizaci rastrové mapy je vhodné nahlédnout do legendy, abychom měli představu o mapovém obsahu.

<figure markdown>
![SMO5_legenda](../assets/cviceni6/SMO5_legenda.png "Legenda SMO5"){ width="600" }
    <figcaption>Legenda SMO5</figcaption>
</figure>

**2.** Pro vytvoření třídy prvků musíme kliknout pravým tlačítkem na příslušný *Feature Dataset* v *Catalogu* -> *New* -> *Feature Class*.

**3.** V této ukázce vytvoříme 4 třídy prvků (plochy, domy, vodstvo a cesty). Ve funkci *Create Feature Class* zvolíme jméno třídy a její typ (pro nás *Polygon*). Následně klineme na *Next*.

**4.** Na druhé stránce funkce *Create Feature Class* nastavujeme atributová pole třídy. Zde vytvoříme nové pole s názvem *druh_pozemku* po kliknutí na tlačítko *Click here to add a new field*. Datový typ přiřadíme číselný, například *Long Integer*. Tato čísla budou reprezentovat kódy různých druhů pozemku v mapě. Pokračujeme tlačítkem *Next*.

**5.** Na třetí stránce zkontrolujeme souřadnicový systém třídy prvků. Nastavení na dalších stránkách můžeme pomechat ve výchozím stavu.

<figure markdown>
![trida_prvku](../assets/cviceni6/trida_prvku.png "Založení třídy prvků"){ width="800" }
    <figcaption>Založení třídy prvků</figcaption>
</figure>

#### Práce se subtypy

Pro kategorizaci dat v atributové tabulce je vhodné používat subtypy. V jednoduchosti se jedná o kódy jednotlivých typů atributů v tabulce, kterám je přiřazen popis pro přehlednější práci. V této ukázce vytvoříme subtypy pro třídu prvků *Plochy*, který nám bude určovat druh využití pozemku.

**1.** Zobrazíme si atributovou tabulku vrstvy *Plochy*. 

**2.** V horní části programu si rozklikneme záložku *Table*

<figure markdown>
![table](../assets/cviceni6/table.png "Zobrazení polí atributové tabulky"){ width="800" }
    <figcaption>Zobrazení polí atributové tabulky</figcaption>
</figure>

**3.** Otevře se nám nová nabídka, ve které zvolíme tlačítko *Subtypes* a následně *Create/Manage*.

<figure markdown>
![subtypes1](../assets/cviceni6/subtypes1.png "Zapnutí editace subtypů"){ width="800" }
    <figcaption>Zapnutí editace subtypů</figcaption>
</figure>

**4.** V okně *Manage Subtypes* vybereme pole (*Subtype Field*), které chceme editovat a přiřadíme kódy dle druhů využití pozemků, které budeme na zájmovém území vektorizovat. Není problém se kdykoliv do této nabídky vrátit v průběhu práce a případně nový subtyp přidat či smazat.

**5.** Editaci potvrdíme tlačítkem *OK* a následně ji uložíme ikonou *Save* v horní části obrazovky.

<figure markdown>
![subtypes2](../assets/cviceni6/subtypes2.png "Přiřazení kódu subtypům")
    <figcaption>Přiřazení kódu subtypům</figcaption>
</figure>

???+ note "&nbsp;<span style="color:#448aff">Rozlišení subtypů v symbologii:</span>"
      Pro přehlednější práci s daty, je vhodné rozlišit typy ploch barevně. To lze provést přes kliknutí pravým tlačítkem na vrstvu v *Contents* -> *Symbology* -> změnit *Single Symbol* na *Unique Values* -> změnit atribut v nabídce *Field 1* na požadovaný (např. *druh_pozemku*).

#### Kresba

Následuje samotný proces vektorizace, tedy "obkeslení" rastrových dat a vytvoření nových dat ve vektorové formě.

**1.** Nástroje editace vektorových dat se nacházejí v záložce *Edit* v horní části programu. 

**2.** Nové prvky vytvoříme tlačítkem *Create* -> zvolení kresby daného subtypu v okně *Create Features*.

**3.** Vektorizované body přidáváme levým tlačítkem myši. Pro dokončení vektorizace určitého prvku buď dvakrát klikneme levým tlačítkem myši nebo zvolíme ikonu *Finish* v nástrojích v dolní části obrazovky. Při vektorizaci je potřeba myslet na nastavení přichycování bodů ([Snapping](https://pro.arcgis.com/en/pro-app/latest/help/editing/enable-snapping.htm)).

<figure markdown>
![vekt](../assets/cviceni6/vekt.png "Vektorizace rastrové mapy")
    <figcaption>Vektorizace rastrové mapy</figcaption>
</figure>

**Popis nejčastěji používaných funkcí a klávesových zkratek pro vektorizaci dat:**

- *Right Angle Line* – pravoúhlá linie
- *Direction Direction* – průsečík dvou linií
- *Arc Segment* – oblouk
- *Trace* - přichycení na jiný vektorový prvek v mapě
- stisknutí D – určení délky linie
- stisknutí A – určení úhlu linie
- stisknutí P – rovnoběžná kresba s linií určenou kurzorem myši
- držení T – zobrazení lomových bodů v okolí kurzoru
- stisknutí F2 – dokončení kresby
- stisknutí F3 – dokončení kresby v pravém úhlu
- stisknutí pravého tlačítka myši – zobrazení dalších možností kresby

???+ note "&nbsp;<span style="color:#448aff">Uložení editace:</span>"
      Po provedení změn v editaci vektorových dat, je nutné stiknout tlačítko *Save* v záložce *Edit*.


### Kontrola topologie vektorových dat






## Zadání domácího úkolu k semestrální práci

1. Dle postupu ze cvičení vektorizujte plochy SMO5 na zadaném katastrálním území. Při vektorizaci rozlišujte typy využití ploch stejně jako na cvičení. 

2. Proveďte kontrolu topologie a veškerá data mějte přehledně uložená v geodatabázi.
