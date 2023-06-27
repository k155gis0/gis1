<style>
  .md-button--primary:hover {background-color:#46817b !important; color:#eee !important;border-color:#46817b !important}
  .md-typeset__table {width:100%;}
  tbody {width: 100%;display: table;}
</style>

# Úvod do práce v prostředí ArcGIS, datové formáty, geodatabáze

---

## Cíl cvičení
xxyy

---

## Základní pojmy


---

## Použité datové podklady


---

## Náplň cvičení
### Software
Během většiny výuky bude používán program **ArcGIS Pro** – pokročilý desktopový geografický informační systém (GIS) vyvinutý společností **Esri**. Umožňuje uživatelům **vytvářet**, **editovat**, **analyzovat** a **vizualizovat** prostorová data v různých vrstvách, včetně **rastrových** a **vektorových** map, **ortofotomap**, **digitálního výškového modelu** a dalších datasetů.  
Uživatelé mohou vytvářet a upravovat **atributy** a **geometrii** prvků, provádět pokročilé **analýzy**, vytvářet a **publikovat mapové vrstvy** a vytvářet **interaktivní mapové aplikace**. Program obsahuje také nástroje pro **vizualizaci** dat, tvorbu mapových prezentací a **sdílení výsledků** s ostatními uživateli.  
<span style="font-size: 12px;">*Vzhledem k vysokým pořizovacím nákladům se systém ArcGIS využívá především ve velkých firmách a orgánech státní správy. V menších podnicích je rozšířenější jeho open source alternativa QGIS (tomu bude věnována pozornost v závěru kurzu).*</span>

### Spuštění a základní orientace v programu
Při spuštění probíhá ověření licence přes příslušnost k organizaci (ČVUT v Praze) – pomocí přihlášení k univerzitnímu účtu. Adresa (URL) pro ČVUT je *ctuprague.maps.arcgis.com* – poté proběhne automatické přesměrování na stránku s univerzitním přihlášením (ve formátu *username@cvut.cz* a heslo to KOSu).
<div style="text-align: center;">
<iframe width="560" height="315" src="https://www.youtube.com/embed/8nDVpVmxM-0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

---
<br>
![Albuquerque, New Mexico](/assets/cviceni1/img_01.png)

<table style="width: 100%;">
  <tbody>
    <tr>
      <td markdown><strong>RIBBON(1){ .annotate }</strong> <br>(Pás karet)</td>
      <td>nabídka funkcí programu (prvek shodný s jinými programy, např. Microsoft Word), nabídka se kontextově mění podle činnosti uživatele</td>
    </tr>
    <tr>
      <td><strong>VIEW</strong></td>
      <td>okno s mapou (2D) nebo scénou (3D)</td>
    </tr>
    <tr>
      <td><strong>PANE</strong></td>
      <td>panely a vlastnosti funkcí, mnoho funkcí spouští svůj Pane, přes který se daná funkce ovládá, např. Obsah mapy (Contents), Symbologie</td>
    </tr>
  </tbody style="width:100%">
</table>

1.  :man_raising_hand: I'm an annotation! I can contain `code`, __formatted
    text__, images, ... basically anything that can be expressed in Markdown.

![Image title](https://dummyimage.com/600x400/eee/aaa){ width="300" }
![Image title](https://dummyimage.com/600x400/eee/aaa){ width="300" }

<figure markdown>
  ![Image title](https://dummyimage.com/600x400/eee/aaa){ width="300" align=left }
  ![Image title](https://dummyimage.com/600x400/eee/aaa){ width="300" align=right }
</figure>


[Subscribe to our newsletter](#){ .md-button .md-button--primary }



Grafické prostředí je rozděleno na několik základních částí:
RIBBON (Pás karet)	– nabídka funkcí programu (prvek shodný s jinými programy, např. Microsoft Word), nabídka se kontextově mění podle činnosti uživatele
VIEW	– okno s mapou (2D) nebo scénou (3D)
PANE	– panely a vlastnosti funkcí, mnoho funkcí spouští svůj Pane, přes který se daná funkce ovládá, např. Obsah mapy (Contents), Symbologie
Pane: dokovatelné okno


## Zadání domácího úkolu k semestrální práci



# Test nadpisů

## Nadpis 2

### Nadpis 3

#### Nadpis 4

##### Nadpis 5

###### Nadpis 6

####### Nadpis 7

...další text...
