---
icon: material/numeric-1-box
title: Cvičení 1
---

# Úvod do práce v prostředí ArcGIS, prostorová data, datové zdroje

## Cíl cvičení

Seznámení s programem ArcGIS Pro, základní orientace v prostředí programu, přidávání dat do mapy a ovládání mapy

<hr class="level-1">

## Základní pojmy

### Software pro výuku
Během většiny výuky bude používán program **ArcGIS Pro** – pokročilý desktopový geografický informační systém (GIS) vyvinutý společností **Esri**. Umožňuje uživatelům **vytvářet**, **editovat**, **analyzovat** a **vizualizovat** prostorová data v různých vrstvách, včetně **rastrových** a **vektorových** map, **ortofotomap**, **digitálního výškového modelu** a dalších datasetů.  
Uživatelé mohou vytvářet a upravovat **atributy** a **geometrii** prvků, provádět pokročilé **analýzy**, vytvářet a **publikovat mapové vrstvy** a vytvářet **interaktivní mapové aplikace**. Program obsahuje také nástroje pro **vizualizaci** dat, tvorbu mapových prezentací a **sdílení výsledků** s ostatními uživateli.  

![](../assets/cviceni1/agp_logo.png#only-light){ .no-filter .off-glb width=200px}
![](../assets/cviceni1/agp_logo2.png#only-dark){ .no-filter .off-glb width=200px}
{: align=center}

!!! note-grey "Pozn."

    Vzhledem k vysokým pořizovacím nákladům se systém ArcGIS využívá především ve velkých firmách a orgánech státní správy. V menších podnicích je rozšířenější jeho open source alternativa [QGIS](https://www.qgis.org/){: target="_blank"} (tomu bude věnována pozornost v [závěru kurzu](/cviceni/cviceni9/)).

### Prostorová (GIS) data <span style="font-size:60%;font-style:italic;vertical-align:10%;margin-left:15px;">(vektorová)</span>
Geografický informační systém (GIS) využívá obecně jakákoliv data obsahující __prostorovou (polohovou) informaci__. Poloha může být reprezentována nejen kombinací souřadnic (_X + Y_, _šířka + délka_ aj.), ale také např. adresou (o libovolné podrobnosti). Doplňkem k polohové informaci obvykle bývá připojena jakákoliv další informace formou atributů v __atributové tabulce__.

<div class="centered_tab_labels" markdown>
=== "CELÁ MAPA"

    ![](https://geo.fsv.cvut.cz/data/cehak/MkDocs/gis-1/cviceni1/tab-01.png){.no-filter width="500"}
    {align=center}

    <figcaption>Schematická ukázka prostorových dat a k nim přiřazených atributových tabulek</figcaption>

=== "Body"
    
    ![](https://geo.fsv.cvut.cz/data/cehak/MkDocs/gis-1/cviceni1/tab-02.png){.no-filter width="500"}
    {align=center}

    <figcaption>Schematická ukázka prostorových dat a k nim přiřazených atributových tabulek</figcaption>

=== "Linie"

    ![](https://geo.fsv.cvut.cz/data/cehak/MkDocs/gis-1/cviceni1/tab-03.png){.no-filter width="500"}
    {align=center}

    <figcaption>Schematická ukázka prostorových dat a k nim přiřazených atributových tabulek</figcaption>

=== "Polygony"

    ![](https://geo.fsv.cvut.cz/data/cehak/MkDocs/gis-1/cviceni1/tab-04.png){.no-filter width="500"}
    {align=center}

    <figcaption>Schematická ukázka prostorových dat a k nim přiřazených atributových tabulek</figcaption>

</div>


__Ukládání prostorových dat__: Data lze ukládat mnoha různými způsoby. Datových formátů existuje mnoho, pro začátek uvedeme některé základní.

- __Shapefile__: formát od spol. _Esri_ s převážně otevřenou specifikací, obsahuje geometrii a vlastnosti (atributy) prostorových prvků, v současnosti asi nejpoužívanější, přestože má mnoho nevýhod a z dnešního pohledu je poněkud zastaralý, jedna z charakteristik formátu je povinné rozdělení do více souborů (`.shp`, `.shx` a `.dbf`, příp. další nepovinné), což přináší obtíže při přesouvání, kopírování apod.
- __Geodatabáze (GDB)__: nativní datová struktura systému _ArcGIS_ – primární datový formát pro správu a editaci dat, obsahuje kolekci datasetů různých typů (vektor, rastr i jiné), zároveň dokáže uchovávat údaje o datové integritě (domény, subtypy apod.) nebo topologii
- __GeoJSON__: otevřený standard reprezentující vektorová data a přiřazené atributy, založen na formátu `JSON` a je tedy uživatelsky čitelný a velmi rozšířený
- __GML / KML__: podobně jako GeoJSON – otevřený standard reprezentující vektorová data a přiřazené atributy, založen na formátu `XML`, tedy opět uživatelsky čitelný
- __GeoPackage (GPKG)__: relativně nový formát _standardu OGC_, podporuje vektorová i rastrová data, překonává mnoho limitů formátu `Shapefile` (např. se jedná o pouze 1 soubor), výchozí formát systému _QGIS_
- __CSV__: sice není formátem přímo určeným pro prostorová data, nicméně často se jako výměnný formát používá, soubor obsahuje pouze atributy, z nichž některé mohou reprezentovat prostorovou složku (souřadnice či adresu) – tu pak GIS software rozpozná a polohově vizualizuje

<!-- Ve výčtu chybí některé __rastrové formáty__, těm se bude výuka věnovat v průběhu pozdějších cvičení. -->

<hr class="level-1">

## Náplň cvičení

### Spuštění a základní orientace v programu

Při spuštění probíhá ověření licence přes příslušnost k organizaci (ČVUT v Praze) – pomocí přihlášení k univerzitnímu účtu. Adresa (URL) pro ČVUT je *ctuprague.maps.arcgis.com* – poté proběhne automatické přesměrování na stránku s univerzitním přihlášením (ve formátu *username@cvut.cz* a heslo to KOSu).

<div class="process_container">
  <iframe class="video" src="https://www.youtube.com/embed/8nDVpVmxM-0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  <img src="../../assets/cviceni1/img_01.png">
</div> <!-- kvuli tomu iframe to nejde bez html (nenasel jsem zpusob) -->

Uživatelské protředí programu se skládá ze tří základních prvků:

<div class="table_headerless table_small_padding table_centered" markdown>
|   |   |
| - | - |
| __RIBBON__ | nabídka funkcí programu (prvek shodný s jinými programy, např. Microsoft Word), nabídka se kontextově mění podle akcí uživatele       |
| __PANE__   | panely a vlastnosti funkcí, mnoho funkcí spouští svůj Pane, přes který se daná funkce ovládá, např. Obsah mapy (Contents), Symbologie |
| __VIEW__   | okno s mapou (2D) nebo scénou (3D)                                                                                                    |
</div>  <!-- prazdne radky nelze smazat, Markdown nebere tabulky bez zahlavi, musel jsem vyresit pres css -->

![](../assets/cviceni1/img_02.png)
![](../assets/cviceni1/img_03.png)
{: .process_container}

<figcaption>Všechny VIEWs a PANEs jsou dokovatelné – je možné je libovolně přemisťovat po obrazovce a přichytávat k ostatním prvkům</figcaption>

[Working with Panes in ArcGIS Pro](https://www.youtube.com/watch?v=qNDwVJV_kFk){ .md-button .md-button--primary .button_smaller .external_link_icon target="_blank"}
{: .button_array}

---

__Další zdroje:__
{: align=center }

[<span>pro.arcgis.com</span><br>Introduction to ArcGIS Pro](https://pro.arcgis.com/en/pro-app/latest/get-started/get-started.htm){ .md-button .md-button--primary .server_name .external_link_icon_small target="_blank"}
[<span>pro.arcgis.com</span><br>Introducing ArcGIS Pro](https://pro.arcgis.com/en/pro-app/latest/get-started/introducing-arcgis-pro.htm){ .md-button .md-button--primary .server_name .external_link_icon_small target="_blank"}
{: .button_array}

<hr class="level-1">

### Přidání dat do mapy

__Vytvoření mapy:__ _:material-tab: Insert_{: .outlined} :octicons-arrow-right-24: _:material-button-cursor: New Map_{: .outlined}

![](../assets/cviceni1/img_09.png)
{: .process_container}

[Create a map or scene](https://pro.arcgis.com/en/pro-app/latest/help/projects/add-maps-to-a-project.htm#GUID-660CA711-919A-44B0-952A-F2054937077B){ .md-button .md-button--primary .button_smaller .external_link_icon target="_blank"}
{: .button_array}

---

__Přidání dat do mapy__ (lokálně uložených): _:material-tab: Map_{: .outlined} → _:material-button-cursor: Add Data_{: .outlined} → _:material-button-cursor: Data_{: .outlined} → vybrat soubor...

![](../assets/cviceni1/img_10.png)
![](../assets/cviceni1/arrow.svg){: .off-glb .process_icon}
![](../assets/cviceni1/img_11.png)
![](../assets/cviceni1/arrow.svg){: .off-glb .process_icon}
![](../assets/cviceni1/img_12.png)
{: .process_container}

<figcaption>Pokud se soubor ve struktuře neobjevuje, lze dialog obnovit klávesou F5</figcaption>

[Add data from the Add Data dialog box](https://pro.arcgis.com/en/pro-app/latest/help/mapping/layer-properties/add-layers-to-a-map.htm#ESRI_SECTION2_1C48753A1FD546F385580EF9197DBB8C){ .md-button .md-button--primary .button_smaller .external_link_icon target="_blank"}
[:octicons-video-16: Video](https://geo.fsv.cvut.cz/data/cehak/MkDocs/gis-1/cviceni1/01-pridani_dat.mp4){ .md-button .md-button--primary .button_smaller target="_blank"}
{: .button_array}

---

Aby pro procházení dat nebylo nutné pokaždé procházet adresářovou strukturu, hodí se adresáře s daty _připojit do projektu_.

__Připojení adresáře do projektu__: V _Catalog Pane_ ( _:material-tab: View_{: .outlined} → _:material-button-cursor: Catalog Pane_{: .outlined} ) přes pravé tl. myši na "_Folders_" vybrat _:material-form-dropdown: Add Folder Connection_{: .outlined} → vložit nebo zvolit cestu... → data ve složce přetáhnout (Drag&Drop) do prostoru mapy

![](../assets/cviceni1/img_05.png)
![](../assets/cviceni1/arrow.svg){: .off-glb .process_icon}
![](../assets/cviceni1/img_04.png)
![](../assets/cviceni1/arrow.svg){: .off-glb .process_icon}
![](../assets/cviceni1/img_06.png)
![](../assets/cviceni1/arrow.svg){: .off-glb .process_icon}
![](../assets/cviceni1/img_23.png)
{: .process_container}

<figcaption>Cesta ke zvolenému adresáři zůstane v nabídce mezi položkami "Folders". Adresář nemusí být lokální, lze takto připojit i např. fakultní disk H:\.</figcaption>

[Connect to a folder](https://pro.arcgis.com/en/pro-app/latest/help/projects/connect-to-a-folder.htm){ .md-button .md-button--primary .button_smaller .external_link_icon target="_blank"}
[The Project Pane](https://pro.arcgis.com/en/pro-app/latest/help/projects/the-project-pane.htm){ .md-button .md-button--primary .button_smaller .external_link_icon target="_blank"}
[:octicons-video-16: Video](https://geo.fsv.cvut.cz/data/cehak/MkDocs/gis-1/cviceni1/02-pripojeni_adresare.mp4){ .md-button .md-button--primary .button_smaller target="_blank"}
{: .button_array}

---

...totéž lze udělat s geodatabází. V geodatabázi jsou data uložena efektivněji, nelze do ní však vložit cokoli.

__Připojení geodatabáze do projektu__: V _Catalog Pane_ ( _:material-tab: View_{: .outlined} → _:material-button-cursor: Catalog Pane_{: .outlined} ) přes pravé tl. myši na "_Databases_" vybrat _:material-form-dropdown: Add Database_{: .outlined} → vložit nebo zvolit cestu ke geodatabázi... → data ve složce přetáhnout (Drag&Drop) do prostoru mapy

![](../assets/cviceni1/img_05.png)
![](../assets/cviceni1/arrow.svg){: .off-glb .process_icon}
![](../assets/cviceni1/img_07.png)
![](../assets/cviceni1/arrow.svg){: .off-glb .process_icon}
![](../assets/cviceni1/img_08.png)
![](../assets/cviceni1/arrow.svg){: .off-glb .process_icon}
![](../assets/cviceni1/img_24.png)
{: .process_container}

<figcaption>Cesta ke zvolené geodatabázi zůstane v nabídce mezi položkami "Databases". Cesta opět nemusí být pouze lokální.</figcaption>

[:material-open-in-new: Connect to a database](https://pro.arcgis.com/en/pro-app/latest/help/projects/connect-to-a-database.htm){ .md-button .md-button--primary .button_smaller target="_blank"}
[:octicons-video-16: Video](https://geo.fsv.cvut.cz/data/cehak/MkDocs/gis-1/cviceni1/03-pripojeni_databaze.mp4){ .md-button .md-button--primary .button_smaller target="_blank"}
{: .button_array}

---

__Pořadí vrstev__: V obsahu mapy (_Contents Pane_) se zobrazují všechny vrstvy obsažené v mapě. Zaškrtávacím políčkem vlevo lze jednotlivým vrstvám přepínat viditelnost. Výměnou pořadí vrstev v obsahu se změní jejich pořadí vykreslování v mapě.

![](../assets/cviceni1/img_29.png)
![](../assets/cviceni1/arrow.svg){: .off-glb .process_icon}
![](../assets/cviceni1/img_30.png)
![](../assets/cviceni1/arrow.svg){: .off-glb .process_icon}
![](../assets/cviceni1/img_31.png)
{: .process_container}

<figcaption>Contents Pane a změna pořadí a přepínání viditelnosti vrstev</figcaption>

[:octicons-video-16: Video](https://geo.fsv.cvut.cz/data/cehak/MkDocs/gis-1/cviceni1/04-poradi_vrstev.mp4){ .md-button .md-button--primary .button_smaller target="_blank"}
{: .button_array}

---

__Nastavení (vlastnosti) mapy__: V _Contents Pane_ (Obsah) přes pravé tl. myši na název mapy vybrat _:material-form-dropdown: Properties_{: .outlined}

![](../assets/cviceni1/img_21.png)
![](../assets/cviceni1/arrow.svg){: .off-glb .process_icon}
![](../assets/cviceni1/img_22.png)
![](../assets/cviceni1/arrow.svg){: .off-glb .process_icon}
![](../assets/cviceni1/img_25.png)
{: .process_container}

Pro začátek jsou zajímavé tyto položky:

- Záložka _:material-label-outline: General_{: .outlined}

    - __Name__ (Název mapy)
    - __Reference scale__ (Referenční měřítko): Zafixuje velikost mapové symbologie pro zadané měřítko. 
    [:material-open-in-new: Map reference scales](https://pro.arcgis.com/en/pro-app/latest/help/mapping/properties/map-reference-scales.htm){ .md-button .md-button--primary .button_smaller target="_blank" align=right}
    - __Rotation__: Úhel natočení mapy

- Záložka _:material-label-outline: Coordinate systems_{: .outlined}

    - Informace o souřadnicovém systému zobrazení mapy (zvlášť pro polohu a pro výšku).
    - __POZOR__, pokud se souř. systém __vložených dat__ liší od systému __mapy__, jsou data __dočasně__ převedena do souř. systému __mapy__. Jedná se však o tzv. __On-the-fly__ transformaci, která je pro kombinaci některých souř. systémů __zjednodušená__ a data na sebe nemusí správně navazovat. Tato situace se __nedoporučuje__, neboť může přinést __nepřesné výsledky__ mapové vizualizace i datových analýz. [__Podrobnější informace__](https://www.esri.com/arcgis-blog/products/arcgis-pro/mapping/projection-on-the-fly-and-geographic-transformations)
    {: style="color:#888;font-size:smaller; line-height:1.1;"}

[:octicons-video-16: Video](https://geo.fsv.cvut.cz/data/cehak/MkDocs/gis-1/cviceni1/05-vlastnosti_mapy.mp4){ .md-button .md-button--primary .button_smaller target="_blank"}
{: .button_array}

<hr class="level-1">

### Kde získat data

__Lokálně uložené soubory__:  přístup přes systémovou cestu, např.:

`C:\Users\Student1\Documents\Geodatabase.gdb\Layer1`
`\\\\data.fsv.cvut.cz\Shares\K155\Public\data\PragueRoads.gdb`
{: align="center" style="font-size:smaller;line-height:1.1; column-gap:50px;" .button_array}

__Data online ke stažení__: stažení z libovolného zdroje na lokální disk ve formě souborů, dále shodný přístup jako s lokálně uloženými soubory (viz výše)
{: id="data_online" }

[ArcČR](https://www.arcgis.com/home/item.html?id=16fd9804dac04020938452a77c1ed350){ .md-button .md-button--primary .button_smaller .external_link_icon target="_blank"}
[Geoportal Praha](https://www.geoportalpraha.cz/cs/data/otevrena-data/seznam){ .md-button .md-button--primary .button_smaller .external_link_icon target="_blank"}
[Geoportal data.Brno](https://data.brno.cz/explore){ .md-button .md-button--primary .button_smaller .external_link_icon target="_blank"}
[otevřená data AOPK](https://gis-aopkcr.opendata.arcgis.com/){ .md-button .md-button--primary .button_smaller .external_link_icon target="_blank"}
[geoportál ČSÚ](https://geodata.statistika.cz){ .md-button .md-button--primary .button_smaller .external_link_icon target="_blank"}
{: .button_array}

__Připojení streamovaných dat__: _bude součástí budoucích cvičení_
{: style="color:#888"}

- připojení datových služeb přes URL adresu, nevyžaduje ruční lokální ukládání, existuje více standardů pro poskytování těchto služeb
{: style="color:#888;font-size:smaller; line-height:1.1;"}

[:octicons-video-16: Video](https://geo.fsv.cvut.cz/data/cehak/MkDocs/gis-1/cviceni1/06-stazeni_dat.mp4){ .md-button .md-button--primary .button_smaller target="_blank"}
{: .button_array}

<hr class="level-1">

### Ovládání mapy

__Explore Tool__: Pohyb v mapě a vyvolávání pop-upů (vyskakovacích oken), funkce tlačítek myši viz obr.

- __Pop-up__ (Vyskakovací okno): Je jedním ze základních prvků grafického prostředí GIS aplikací. Jeho (nejčastějším) účelem je poskytnout rychlý náhled informací o daném prvku po kliknutí na jeho geometrii. Podoba okna je ale konfigurovatelná a nástroje pro úpravu velice variabilní. Ve výchozím stavu pop-up zobrazuje výpis atributů ve formě tabulky (obr.).
[Pop-ups](https://pro.arcgis.com/en/pro-app/latest/help/mapping/navigation/pop-ups.htm){ .md-button .md-button--primary .button_smaller .external_link_icon target="_blank"}
- __Měřítko mapy__: Udává poměr zmenšení mapy vzhledem ke skutečnosti. V rohu mapového okna (obr.) lze vybrat z nabízených měřítek nebo i nastavit libovolnou vlastní hodnotu.
[Map scales and scale properties](https://pro.arcgis.com/en/pro-app/latest/help/mapping/navigation/map-scales-and-scale-properties.htm){ .md-button .md-button--primary .button_smaller .external_link_icon target="_blank"}

![](../assets/cviceni1/img_13.png)
![](../assets/cviceni1/arrow.svg){: .off-glb .process_icon}
![](../assets/cviceni1/img_16.png)
![](../assets/cviceni1/arrow.svg){: .off-glb .process_icon}
![](../assets/cviceni1/img_26.png)
![](../assets/cviceni1/arrow.svg){: .off-glb .process_icon}
![](../assets/cviceni1/img_27.png)
{: .process_container}

[Navigation](https://pro.arcgis.com/en/pro-app/latest/help/mapping/navigation/navigation-in-arcgis-pro.htm){ .md-button .md-button--primary .button_smaller .external_link_icon target="_blank"}
[Navigate maps and scenes](https://pro.arcgis.com/en/pro-app/latest/get-started/navigate-your-data.htm){ .md-button .md-button--primary .button_smaller .external_link_icon target="_blank"}
[:octicons-video-16: Video](https://geo.fsv.cvut.cz/data/cehak/MkDocs/gis-1/cviceni1/07-ovladani_mapy.mp4){ .md-button .md-button--primary .button_smaller target="_blank"}
{: .button_array}

---

<!--               ↓↓↓ odkazuje na to link ze cviceni 2! -->
__Select Tool__{: #select-tool}: Pohyb v mapě a interaktivní vybírání prvků kurzorem. Zrušení výběru viz obr.

- __Přidání prvků do výběru__: `Shift + klik`
- __Odebrání prvků z výběru__: `Ctrl + klik`

![](../assets/cviceni1/img_14.png)
![](../assets/cviceni1/arrow.svg){: .off-glb .process_icon}
![](../assets/cviceni1/img_17.png)
![](../assets/cviceni1/arrow.svg){: .off-glb .process_icon}
![](../assets/cviceni1/img_18.png)
![](../assets/cviceni1/arrow.svg){: .off-glb .process_icon}
![](../assets/cviceni1/img_32.png){ data-title="Zrušení výběru" data-description="" }
{: .process_container}

[Select features interactively](https://pro.arcgis.com/en/pro-app/latest/help/mapping/navigation/select-features-interactively.htm){ .md-button .md-button--primary .button_smaller .external_link_icon target="_blank"}
[Select features for editing](https://pro.arcgis.com/en/pro-app/latest/help/editing/select-features-for-editing.htm){ .md-button .md-button--primary .button_smaller .external_link_icon target="_blank"}
[:octicons-video-16: Video](https://geo.fsv.cvut.cz/data/cehak/MkDocs/gis-1/cviceni1/08-vybery.mp4){ .md-button .md-button--primary .button_smaller target="_blank"}
{: .button_array}

---

__Measure Tool__: Interaktivní měření vzdáleností, úhlů apod.

![](../assets/cviceni1/img_15.png)
![](../assets/cviceni1/arrow.svg){: .off-glb .process_icon}
![](../assets/cviceni1/img_19.png)
![](../assets/cviceni1/arrow.svg){: .off-glb .process_icon}
![](../assets/cviceni1/img_20.png)
{: .process_container}

[Measure](https://pro.arcgis.com/en/pro-app/latest/help/mapping/navigation/measure.htm){ .md-button .md-button--primary .button_smaller .external_link_icon target="_blank"}
[:octicons-video-16: Video](https://geo.fsv.cvut.cz/data/cehak/MkDocs/gis-1/cviceni1/09-mereni.mp4){ .md-button .md-button--primary .button_smaller target="_blank"}
{: .button_array}

<hr class="level-1">

__Doplňkové zdroje:__
{: align=center}

[<span>pro.arcgis.com</span><br>ArcGIS Pro keyboard shortcuts](https://pro.arcgis.com/en/pro-app/latest/get-started/arcgis-pro-keyboard-shortcuts.htm){ .md-button .md-button--primary .server_name .external_link_icon_small target="_blank"}
[<span>:octicons-file-16: PDF</span><br>ArcGIS Pro shortcuts](https://www.esri.com/content/dam/esrisites/en-us/media/pdf/g526942-arcgis-pro-kybrd-shrtct-FINAL.pdf){ .md-button .md-button--primary .server_name target="_blank"}
{: .button_array}

<hr class="level-1">

### Atributová tabulka

Atributová tabulka je __doplňkem k prostorovým datům__ – obohacuje každý prvek (geometrii) o __další informace__ (tzv. atributy). Tyto informace jsou pro práci v GIS klíčové, protože geometrie sama o sobě (bez atributů) nám mnoho informací nepřinese. Atributová tabulka je proto součástí každé (vektorové) vrstvy.

Tabulka obsahuje sloupce – tzv. __atributy__ (fields), a řádky – tzv. __záznamy__ (records). Každý prvek tak obsahuje hodnoty všech atributů – příklad viz obr. níže.

![](../assets/cviceni1/img_37.png)
{: .process_container}

<figcaption>Atributová tabulka</figcaption>

Otevřít atributovou tabulku

Vybrat záznamy

Zjistit počet prvků / počet vybraných prvků

Přidat pole / editovat pole

[Tables](https://pro.arcgis.com/en/pro-app/latest/help/data/tables/tables-in-arcgis-pro.htm){ .md-button .md-button--primary .button_smaller .external_link_icon target="_blank"}
[Open tabular data](https://pro.arcgis.com/en/pro-app/latest/help/data/tables/open-tabular-data.htm){ .md-button .md-button--primary .button_smaller .external_link_icon target="_blank"}
[Interact with a table](https://pro.arcgis.com/en/pro-app/latest/help/data/tables/interact-with-a-table.htm){ .md-button .md-button--primary .button_smaller .external_link_icon target="_blank"}
[Select records in a table interactively](https://pro.arcgis.com/en/pro-app/latest/help/data/tables/select-records-in-a-table-interactively.htm){ .md-button .md-button--primary .button_smaller .external_link_icon target="_blank"}
[Edit an active table](https://pro.arcgis.com/en/pro-app/latest/help/data/tables/edit-an-active-table.htm){ .md-button .md-button--primary .button_smaller .external_link_icon target="_blank"}
{: .button_array}

<!-- 
<hr class="level-1">

## Úlohy k procvičení

!!! task-fg-color "Úloha"

    - Zadání
        - Zobrazte v mapovém okně zadané vrstvy z geoportálu, mapa musí mít __zadané měřítko__, __natočení__ a __projekci__ (souř. systém), vrstvy musí mít __správné pořadí__ a __výběrem označené zadané prvky__. Dále nad mapou zobrazte __vyskakovací okno__ (pop-up) zadaného prvku a správně určete __vzdálenost mezi zadanými prvky__.
        - Použijte data z geoportálu &nbsp;[:material-open-in-new: Geoportal data.Brno](https://data.brno.cz/explore){ .md-button .md-button--primary .button_smaller target="_blank"}&nbsp; – konkrétně datovou vrstvu obsahující __`zastávky MHD`__ a __`trasy linek MHD`__, výstupní formát libovolný (doporučujeme __`Shapefile`__ nebo __`Souborová geodatabáze`__)

    - Výstupy
        - Screenshot mapy splňující všechny výše popsané vlastnosti
        - Screenshot pop-upu nad zadaným prvkem
        - Napsat vzdálenost mezi konkrétními dvěma prvky

    - Individuální zadání
        - DODĚLAT

 -->
<br><br><br><br><br>
