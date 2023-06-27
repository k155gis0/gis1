<style>
  .md-typeset__table {width:100%;}
  tbody {width: 100%;display: table;}
  h2 {font-weight:700 !important;}
  /*h3 {text-transform:uppercase !important;}*/
  .md-button {line-height:1.2; text-align:center;padding-top:5px !important;transition: all .1s ease-in-out !important;}
  .md-button:hover {transform: scale(1.04)}
  .md-button:hover {background-color:#46817b !important; color:#eee !important;border-color:#46817b !important}
  .md-button:focus {background-color:#46817b !important; color:#eee !important;border-color:#46817b !important}
  .md-button-top-text {font-size:.7em;font-weight:300;}
  .md-button-top-text-icon {font-size:smaller;vertical-align: -0px;}
  /*.p-align-center{text-align:center;}*/
  figcaption {font-size:12px;margin-top:5px !important;text-align:center;line-height:1.2em;}
</style>

# Úvod do práce v prostředí ArcGIS, datové formáty, geodatabáze

---

## Cíl cvičení


---

## Základní pojmy


---

## Použité datové podklady


---

## Náplň cvičení
### Software
Během většiny výuky bude používán program **ArcGIS Pro** – pokročilý desktopový geografický informační systém (GIS) vyvinutý společností **Esri**. Umožňuje uživatelům **vytvářet**, **editovat**, **analyzovat** a **vizualizovat** prostorová data v různých vrstvách, včetně **rastrových** a **vektorových** map, **ortofotomap**, **digitálního výškového modelu** a dalších datasetů.  
Uživatelé mohou vytvářet a upravovat **atributy** a **geometrii** prvků, provádět pokročilé **analýzy**, vytvářet a **publikovat mapové vrstvy** a vytvářet **interaktivní mapové aplikace**. Program obsahuje také nástroje pro **vizualizaci** dat, tvorbu mapových prezentací a **sdílení výsledků** s ostatními uživateli.  

???+ note "&nbsp;<span style="color:#448aff">Pozn.</span>"
      Vzhledem k vysokým pořizovacím nákladům se systém ArcGIS využívá především ve velkých firmách a orgánech státní správy. V menších podnicích je rozšířenější jeho open source alternativa QGIS (tomu bude věnována pozornost v závěru kurzu).


### Spuštění a základní orientace v programu
Při spuštění probíhá ověření licence přes příslušnost k organizaci (ČVUT v Praze) – pomocí přihlášení k univerzitnímu účtu. Adresa (URL) pro ČVUT je *ctuprague.maps.arcgis.com* – poté proběhne automatické přesměrování na stránku s univerzitním přihlášením (ve formátu *username@cvut.cz* a heslo to KOSu).
<div style="text-align: center;">
<iframe width="560" height="315" src="https://www.youtube.com/embed/8nDVpVmxM-0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

---
<br>
![Albuquerque, New Mexico](../assets/cviceni1/img_01.png)

<table style="width: 100%;">
  <tbody>
    <tr>
      <td markdown><strong>RIBBON</strong></td>
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
  </tbody>
</table>

<figure markdown>
  ![](../assets/cviceni1/img_02.png){ style="height:150px;" align=left }&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  ![](../assets/cviceni1/img_03.png){ style="height:150px;" align=right }
  <figcaption>Všechny VIEWs a PANEs jsou dokovatelné – je možné je libovolně přemisťovat po obrazovce a přichytávat k ostatním prvkům</figcaption>
</figure>


[<span class="md-button-top-text"><span class="md-button-top-text-icon">:material-open-in-new:</span> pro.arcgis.com</span><br>Subscribe to our newsletter](#){ .md-button .md-button--primary .text-align-centera}
{: align=center }


[<span class="md-button-top-text"><span class="md-button-top-text-icon">:material-open-in-new:</span> pro.arcgis.com</span><br>Subscribe to our newsletter](#){ .md-button .md-button--primary .text-align-center}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[<span class="md-button-top-text"><span class="md-button-top-text-icon">:material-open-in-new:</span> pro.arcgis.com</span><br>Subscribe to our newsletter](#){ .md-button .md-button--primary .text-align-center}
{: align=center }

![](/assets/cviceni1/img_02.png){ style="height:150px;"}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![](/assets/cviceni1/img_03.png){ style="height:150px;"}
{: style="margin-bottom:0px;" align=center }
<figcaption>Všechny VIEWs a PANEs jsou dokovatelné – je možné je libovolně přemisťovat po obrazovce a přichytávat k ostatním prvkům</figcaption>


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
