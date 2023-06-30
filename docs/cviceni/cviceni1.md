<style>
  .md-typeset__table {width:100%;}
  tbody {width: 100%;display: table;}
  h2 {font-weight:700 !important;}
  /*h3 {text-transform:uppercase !important;}*/
  .md-button {text-align:center;transition: all .1s ease-in-out !important;}
  .md-button:hover {transform: scale(1.04);opacity:.8;background-color:var(--md-primary-fg-color) !important;border-color:var(--md-primary-fg-color) !important;color:var(--md-primary-bg-color) !important;/*filter: brightness(80%);*/}
  .md-button:focus {opacity:.8;background-color:var(--md-primary-fg-color) !important;border-color:var(--md-primary-fg-color) !important;color:var(--md-primary-bg-color) !important;}
  .url-name {line-height:1.2;padding-top:5px !important;}
  .url-name span:first-child {font-size:.7em; font-weight:300;}
  .url-name span.twemoji {vertical-align:-0px;}
  figcaption {font-size:12px;margin-top:5px !important;text-align:center;line-height:1.2em;}
  hr {background-color:var(--md-primary-fg-color);height:2px;margin-bottom:3em !important;}
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
### Software pro výuku
Během většiny výuky bude používán program **ArcGIS Pro** – pokročilý desktopový geografický informační systém (GIS) vyvinutý společností **Esri**. Umožňuje uživatelům **vytvářet**, **editovat**, **analyzovat** a **vizualizovat** prostorová data v různých vrstvách, včetně **rastrových** a **vektorových** map, **ortofotomap**, **digitálního výškového modelu** a dalších datasetů.  
Uživatelé mohou vytvářet a upravovat **atributy** a **geometrii** prvků, provádět pokročilé **analýzy**, vytvářet a **publikovat mapové vrstvy** a vytvářet **interaktivní mapové aplikace**. Program obsahuje také nástroje pro **vizualizaci** dat, tvorbu mapových prezentací a **sdílení výsledků** s ostatními uživateli.  

???+ note "&nbsp;<span style="color:#448aff">Pozn.</span>"
      Vzhledem k vysokým pořizovacím nákladům se systém ArcGIS využívá především ve velkých firmách a orgánech státní správy. V menších podnicích je rozšířenější jeho open source alternativa QGIS (tomu bude věnována pozornost v závěru kurzu).

---

### Spuštění a základní orientace v programu
Při spuštění probíhá ověření licence přes příslušnost k organizaci (ČVUT v Praze) – pomocí přihlášení k univerzitnímu účtu. Adresa (URL) pro ČVUT je *ctuprague.maps.arcgis.com* – poté proběhne automatické přesměrování na stránku s univerzitním přihlášením (ve formátu *username@cvut.cz* a heslo to KOSu).
<div style="text-align: center;">
<iframe width="560" height="315" src="https://www.youtube.com/embed/8nDVpVmxM-0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

<br>
![](../assets/cviceni1/img_01.png)
{:align=center}

<table style="width: 100%;">
  <tbody>
    <tr>
      <td markdown><strong>RIBBON</strong></td>
      <td>nabídka funkcí programu (prvek shodný s jinými programy, např. Microsoft Word), nabídka se kontextově mění podle akcí uživatele</td>
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

![](../assets/cviceni1/img_02.png){ style="height:150px;"}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![](../assets/cviceni1/img_03.png){ style="height:150px;"}
{: style="margin-bottom:0px;" align=center }
<figcaption>Všechny VIEWs a PANEs jsou dokovatelné – je možné je libovolně přemisťovat po obrazovce a přichytávat k ostatním prvkům</figcaption>

Všechny zmíněné prvky grafického prostředí lze přenastavit. Přidávat/přemisťovat/mazat karty, ikony nástrojů nebo měnit umístění _Views_ a _Panes_.

<br>
<div style="text-align:center;font-weight:bold;text-decoration:underline">Další zdroje:</div>

[<span>:material-open-in-new: pro.arcgis.com</span><br>Introduction to ArcGIS Pro](https://pro.arcgis.com/en/pro-app/latest/get-started/get-started.htm){ .md-button .md-button--primary .url-name target="_blank"}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[<span>:material-open-in-new: pro.arcgis.com</span><br>Introducing ArcGIS Pro](https://pro.arcgis.com/en/pro-app/latest/get-started/introducing-arcgis-pro.htm){ .md-button .md-button--primary .url-name target="_blank"}
{: align=center }

---

### Přidání dat do mapy (Catalog Pane)

<table style="border: 0px">
  <tr>
    <td><img src="/assets/cviceni1/img_09.png"></td>
    <td><img src="/assets/cviceni1/img_10.png"></td>
    <td><img src="/assets/cviceni1/img_10.png"></td>
    <td><img src="/assets/cviceni1/img_10.png"></td>
  </tr>
  <tr>
    <td>Vytvoření prázdné mapy (_Insert → New Map_)</td>
    <td>Přidání dat do mapy (_Map → Add Data_)</td>
    <td>Přidání dat do mapy (_Map → Add Data_)</td>
    <td>Přidání dat do mapy (_Map → Add Data_)</td>
  </tr>
</table>


![](../assets/cviceni1/img_09.png){align=left}
Vytvoření prázdné mapy (_Insert → New Map_)
<br><br><br><br>

&nbsp;&nbsp;&nbsp;:fontawesome-solid-down-long:

![](../assets/cviceni1/img_10.png){align=left}
Přidání dat do mapy (_Map → Add Data_)

<br><br><br><br>

![](../assets/cviceni1/img_05.png){align=left}
Zobrazení datového katalogu (_View_ → _Catalog Pane_) při prvním spuštění by měl být ukotven na pravé straně obrazovky
<br><br><br><br>

__Připojení složky__: V Catalog Pane přes pravé tl. myši na "_Folders_" vybrat "_Add Folder Connection_" → a najít cestu ke složce

<div style="display:table; margin:auto">
  <span style="display: table-cell;vertical-align: middle;"><img src="/assets/cviceni1/img_04.png"></span>
  <span style="display: table-cell;vertical-align: middle;width:100px;padding:30px"><svg height="100%" viewBox="0 0 512 512"><path d="M334.5 414c8.8 3.8 19 2 26-4.6l144-136c4.8-4.5 7.5-10.8 7.5-17.4s-2.7-12.9-7.5-17.4l-144-136c-7-6.6-17.2-8.4-26-4.6s-14.5 12.5-14.5 22l0 72L32 192c-17.7 0-32 14.3-32 32l0 64c0 17.7 14.3 32 32 32l288 0 0 72c0 9.6 5.7 18.2 14.5 22z" style="fill:#007ac2"/></svg></span>
  <span style="display: table-cell;vertical-align: middle;"><img src="/assets/cviceni1/img_06.png"></span>
</div>

__Připojení databáze__: V Catalog Pane přes pravé tl. myši na "_Databases_" vybrat "_Add Database_" → a najít cestu ke složce
<div style="display:table; margin:auto">
  <span style="display: table-cell;vertical-align: middle;"><img src="/assets/cviceni1/img_07.png"></span>
  <span style="display: table-cell;vertical-align: middle;width:100px;padding:30px"><svg height="100%" viewBox="0 0 512 512"><path d="M334.5 414c8.8 3.8 19 2 26-4.6l144-136c4.8-4.5 7.5-10.8 7.5-17.4s-2.7-12.9-7.5-17.4l-144-136c-7-6.6-17.2-8.4-26-4.6s-14.5 12.5-14.5 22l0 72L32 192c-17.7 0-32 14.3-32 32l0 64c0 17.7 14.3 32 32 32l288 0 0 72c0 9.6 5.7 18.2 14.5 22z" style="fill:#007ac2"/></svg></span>
  <span style="display: table-cell;vertical-align: middle;"><img src="/assets/cviceni1/img_08.png"></span>
</div>

<br>
<div style="text-align:center;font-weight:bold;text-decoration:underline">Další zdroje:</div>

[<span>:material-open-in-new: pro.arcgis.com</span><br>The Project Pane](https://pro.arcgis.com/en/pro-app/latest/help/projects/the-project-pane.htm){ .md-button .md-button--primary .url-name target="_blank"}
{: align=center }

---



<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
## Zadání domácího úkolu k semestrální práci

---

<span style="font-size:50px;text-transform:uppercase;font-weight:800;">Test nadpisů:</span>

# Nadpis 1

## Nadpis 2

### Nadpis 3

#### Nadpis 4

##### Nadpis 5

###### Nadpis 6

...další text...




<style>
@import "compass/css3";

.tabs {
  margin: 20px;
  padding: 0;
	list-style: none;
	position: relative;
	border-bottom: 1px solid red;
  
	.active-tab {
		border: 1px solid #ccc;
		border-bottom: none;
		position: relative;
		color: blue;
    
		&:after {
			width: 100%;
			height: 2px;
			position: absolute;
			content: "";
			bottom: -0.1em;
			left: 0;
			background: white;
		}
	}
  
	li {
		display: inline-block;
		cursor: pointer;
		color: #3a5ea7;
		padding: 5px 10px;
    
		&:first-child {
			margin-left: 10px;
		}
	}
}

.tabs-content {
	margin: 20px;
	padding: 0;
	list-style: none;
  
	li {
		display: none;
	}
}
</style>

<script>
$(function () {

  var activeIndex = $('.active-tab').index(),
      $contentlis = $('.tabs-content li'),
      $tabslis = $('.tabs li');
  
  // Show content of active tab on loads
  $contentlis.eq(activeIndex).show();

  $('.tabs').on('click', 'li', function (e) {
    var $current = $(e.currentTarget),
        index = $current.index();
    
    $tabslis.removeClass('active-tab');
    $current.addClass('active-tab');
    $contentlis.hide().eq(index).show();
	 });
});
</script>



<ul class="tabs">
  <li class="active-tab">First tab</li>
	<li>Second tab</li>
	<li>Third tab</li>
</ul>

<ul class="tabs-content">
	<li>Content of first tab</li>
  <li>Content of second tab</li>
  <li>Content of third tab</li>
</ul>