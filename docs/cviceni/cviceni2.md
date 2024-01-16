---
icon: material/numeric-2-box
title: Cvičení 2
---

# Vektorová data, atributové dotazy, prostorové dotazy

<!-- ## Cíl cvičení -->

## Základní pojmy

### Vektorová a rastrová prostorová data

<div class="grid_container">
  <div class="grid_item" style="flex:1 1 300px;">
    <span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M2 3v6h2.95l2 6H6v6h6v-4.59L17.41 11H22V5h-6v4.57L10.59 15H9.06l-2-6H8V3M4 5h2v2H4m14 0h2v2h-2M8 17h2v2H8Z"></path></svg></span>&nbsp;
    <strong>Vektorová data</strong>
    <hr style="margin:10px 0 !important;">
    <p>Tvořena <strong>vrcholy</strong> (Vertices) a <strong>cestami</strong> (Paths) – ty jsou určeny skutečnými souřadnicemi</p>
    <p>Podrobnost je určena <strong>podrobností souřadnic vrcholů</strong></p>
    <p>Vhodné pro <strong>diskrétně rozložená data</strong> (např. poloha bodů, kategorie pokrytí půdy)</p>
    <p>Možné problémy s <strong>topologií</strong> (mezery a překryvy)</p>
  </div>
  <div class="grid_item" style="flex:1 1 300px;">
    <span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M10 4v4h4V4h-4m6 0v4h4V4h-4m0 6v4h4v-4h-4m0 6v4h4v-4h-4m-2 4v-4h-4v4h4m-6 0v-4H4v4h4m0-6v-4H4v4h4m0-6V4H4v4h4m2 6h4v-4h-4v4M4 2h16a2 2 0 0 1 2 2v16a2 2 0 0 1-2 2H4c-1.08 0-2-.9-2-2V4a2 2 0 0 1 2-2Z"></path></svg></span>&nbsp;
    <strong>Rastrová data</strong>
    <span style="font-size:60%;font-style:italic;vertical-align:10%;margin-left:15px;color:#888">součástí budoucích cvičení</span>
    <hr style="margin:10px 0 !important;">
    <p>Tvořena pravidelnou mřížkou <strong>pixelů</strong> – ty jsou určeny pixelovými souřadnicemi (pořadí řádku/sloupce)</p>
    <p>Podrobnost je určena <strong>velikostí pixelu</strong> (v metrech)</p>
    <p>Vhodné pro jevy měnící se <strong>spojitě</strong> (např. model terénu, znečištění ovzduší) i <strong>diskrétně</strong>, dále pak <strong>obrazová data</strong> (např. satelitní)</p>
  </div>
</div>

<!-- ## Použité datové podklady -->

## Náplň cvičení

### Atributové dotazy

Atributový dotaz (Attribute Query) je metoda výběru/filtrace prvků na základě **hodnot jejich atributů**. Doplňuje tak metodu [interaktivního výběru prvků](/cviceni/cviceni1/#select-tool) z 1. cvičení. Základem je pravidlo pro výběr – tzv. **výraz** (Expression). ArcGIS Pro umožňuje sestavovat výrazy interaktivně pomocí dialogu, nicméně pro využití plného potenciálu výrazů je vhodné využít kód v jazyce _SQL_.
<br><br>

**Atributový dotaz** (nad daty v mapě): _:material-tab: Map_{: .outlined} → _:material-button-cursor: Select By Attributes_{: .outlined} → vyplnit údaje do dialogu nástroje...
[Select features using attributes](https://pro.arcgis.com/en/pro-app/latest/help/mapping/navigation/select-features-using-attributes.htm){ .md-button .md-button--primary .button_smaller .external_link_icon target="_blank"}

![](../assets/cviceni1/img_33.png)
![](../assets/cviceni1/arrow.svg){: .off-glb .process_icon}
![](../assets/cviceni1/img_34.png)
![](../assets/cviceni1/arrow.svg){: .off-glb .process_icon}
![](../assets/cviceni1/img_35.png)
{: .process_container}

<figcaption markdown>Do pole `Input Rows` je automaticky předvyplněna vrstva vybraná v obsahu mapy </figcaption>

Pomocí přepínátka ![](../assets/cviceni1/img_36.png){: .off-glb style="vertical-align: -20%;margin:0px 5px;"} lze měnit zápis mezi interaktivním dialogovým zadáním a výrazem v jazyce SQL.

[Introduction to query expressions](https://pro.arcgis.com/en/pro-app/latest/help/mapping/navigation/write-a-query-in-the-query-builder.htm){ .md-button .md-button--primary .button_smaller .external_link_icon target="\_blank"}
[Construct and modify queries](https://pro.arcgis.com/en/pro-app/latest/help/mapping/navigation/construct-and-modify-queries.htm){ .md-button .md-button--primary .button_smaller .external_link_icon target="\_blank"}
{: .button_array}

<style>
  details.page_color_admonition summary:first-child::before {background-color:var(--md-primary-fg-color) !important;}
  /* details.page_color_admonition summary:first-child         {color:#009485 !important;} */
  details.page_color_admonition summary:first-child::after  {color:var(--md-primary-fg-color) !important;}
  details.page_color_admonition {border-color: var(--md-primary-fg-color) !important;margin:50px 0px;}
  details.page_color_admonition summary {background-color: #0094851a !important;}
</style>
<details class="task-fg-color page_color_admonition" open="">
  <summary>Příklad k vyzkoušení<div style="display:inline-block; border-left: 1px solid var(--md-admonition-fg-color); height:.9rem;vertical-align:-20%;margin:0px 20px"></div><span style="font-weight:normal;">testování atributových dotazů na skutečných datech</span></summary>
  <iframe style="filter:none !important;margin-top:.6rem;" width="100%" height="500" frameborder="0" allowfullscreen src="https://geo.fsv.cvut.cz/data/hoffmann/appquery/"></iframe>
  <hr class="level-1" style="margin-top:5px !important; margin-bottom:0px !important;">
  <div style="margin-top:10px;margin-left:10px;font-weight:bold;font-size:larger;">Schéma atributů vrstvy:</div>
  
  <div class="table_small_padding">
    <table>
        <tr>
        <th>atribut</th>
        <th>datový typ</th>
        <th>popis</th>
        </tr>
        <tr>
        <td>stop_name</td>
        <td><code>string</code></td>
        <td>Název zastávky</td>
        </tr>
        <tr>
        <td>routes_nam</td>
        <td><code>string</code></td>
        <td>Označení linek, které obsluhují zastávku, ve formátu <code>-cislolinky-,-cislolinky-</code> řazeno vzestupně</td>
        </tr>
        <tr>
        <td>route_type</td>
        <td><code>integer</code></td>
        <td>ID druhu dopravy, které obsluhují zastávku, <br><code>0=tramvaj</code>, <code>1=metro</code>, <code>2=vlak</code>, <code>3=autobus</code>, <code>4=přívoz</code>, <code>7=lanovka</code>, <code>8=tramvaj i autobus</code></td>
        </tr>
        <tr>
        <td>on_request</td>
        <td><code>integer</code></td>
        <td>Zastávka na znamení <code>0=není na znamení</code>, <code>1=je na znamení</code></td>
        </tr>
        <tr>
        <td>platf_len</td>
        <td><code>float</code></td>
        <td>Délka nástupiště (metry)</td>
        </tr>
    </table>
  </div>
</details>

<hr class="level-1">

### Prostorové dotazy

Prostorový dotaz (Spatial Query) je metoda výběru/filtrace prvků jedné vrstvy na základě vzájemné polohy s prvky druhé vrstvy. Funkce využívá jako vstup <code>__vrstvu vybíraných prvků__</code>, <code>__vrstvu pro překryvnou analýzu__</code> a <code>__vztah pro překryvnou analýzu__</code>.

<!-- ![](https://geo.fsv.cvut.cz/data/cehak/155SGEA/img_01.svg){ .off-glb .no-filter }
![](https://geo.fsv.cvut.cz/data/cehak/155SGEA/img_02.svg){ .off-glb .no-filter }
{: .process_container style="flex-wrap:wrap; row-gap: 10px;"} -->

![](https://geo.fsv.cvut.cz/data/cehak/155SGEA/img_01.svg){ .no-filter }
![](https://geo.fsv.cvut.cz/data/cehak/155SGEA/img_02.svg){ .no-filter }
{: .process_container}

<div class="table_headerless table_small_padding table_centered centered_tab_labels" markdown> <!-- trik: vlastnosti tabulky pro vsechny podrizene -->

=== "Výběr BODŮ..."

    === "...v překrytu s BODY"

        ![](https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/GUID-1ECFFABC-3608-4BB4-86A8-FD6FA0F16C13-web.gif){ style="filter:none !important;" }
        {: align=center}

        <table style="width:unset;">
            <tr><td>Intersect</td><td>A</td></tr>
            <tr><td>Intersect (DBMS)</td><td>A</td></tr>
            <tr><td>Contains</td><td>A</td></tr>
            <tr><td>Contains Clementini</td><td>A</td></tr>
            <tr><td>Within</td><td>A</td></tr>
            <tr><td>Within Clementini</td><td>A</td></tr>
            <tr><td>Are identical to</td><td>A</td></tr>
            <tr><td>Have their center in</td><td>A</td></tr>
        </table>

    === "...v překrytu s LINIEMI"

        ![](https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/GUID-171AD80E-550B-4017-AEB7-1A681D722F60-web.gif){ style="filter:none !important;" }
        {: align=center}

        <table id="small_table_padding" style="width:unset;">
            <tr><td>Intersect</td><td>A, C</td></tr>
            <tr><td>Intersect (DBMS)</td><td>A, C</td></tr>
            <tr><td>Within</td><td>A, C</td></tr>
            <tr><td>Completely within</td><td>A</td></tr>
            <tr><td>Within Clementini</td><td>A</td></tr>
            <tr><td>Have their center in</td><td>A, C</td></tr>
            <tr><td>Boundary touches</td><td>C</td></tr>
        </table>

    === "...v překrytu s POLYGONY"

        ![](https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/GUID-12153063-E9B3-42E5-A786-E3FAF6BB004E-web.gif){ style="filter:none !important;" }
        {: align=center}

        <table id="small_table_padding" style="width:unset;">
          <tr><td>Intersect</td><td>A, C</td></tr>
          <tr><td>Intersect (DBMS)</td><td>A, C</td></tr>
          <tr><td>Within</td><td>A, C</td></tr>
          <tr><td>Completely within</td><td>A</td></tr>
          <tr><td>Within Clementini</td><td>A</td></tr>
          <tr><td>Have their center in</td><td>A, C</td></tr>
          <tr><td>Boundary touches</td><td>C</td></tr>
        </table>

=== "Výběr LINIÍ..."


    === "...v překrytu s BODY"

        ![](https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/GUID-FD60FA73-31CD-4BD7-B03C-06806851BC9E-web.gif){ style="filter:none !important;" }
        {: align=center}

        <table id="small_table_padding" style="width:unset;">
          <tr><td>Intersect</td><td>A, C, D</td></tr>
          <tr><td>Intersect (DBMS)</td><td>A, C, D</td></tr>
          <tr><td>Contains</td><td>A, C, D</td></tr>
          <tr><td>Completely contains</td><td>A, D</td></tr>
          <tr><td>Contains Clementini</td><td>A, D</td></tr>
          <tr><td>Have their center in</td><td>D</td></tr>
          <tr><td>Boundary touches</td><td>C</td></tr>
        </table>

    === "...v překrytu s LINIEMI"

        ![](https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/GUID-09D6FB47-31A3-47C3-A8B8-19BB659EBA8A-web.gif){ style="filter:none !important;" }
        {: align=center}

        <table id="small_table_padding" style="width:unset;">
          <tr><td>Intersect</td><td>A, C, D, E, F, G, H, I, J</td></tr>
          <tr><td>Intersect (DBMS)</td><td>A, C, D, E, F, G, H, I, J</td></tr>
          <tr><td>Contains</td><td>G, H</td></tr>
          <tr><td>Completely contains</td><td>G</td></tr>
          <tr><td>Contains Clementini</td><td>G, H</td></tr>
          <tr><td>Within</td><td>F, H</td></tr>
          <tr><td>Completely within</td><td>F</td></tr>
          <tr><td>Within Clementini</td><td>F, H</td></tr>
          <tr><td>Are identical to</td><td>H</td></tr>
          <tr><td>Boundary touches</td><td>C, E</td></tr>
          <tr><td>Share a line segment with</td><td>F, G, H, I, J</td></tr>
        </table>

    === "...v překrytu s POLYGONY"

        ![](https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/GUID-54663F11-5B47-46A5-82C1-37FD1FDDC835-web.gif){ style="filter:none !important;" }
        {: align=center}

        <table id="small_table_padding" style="width:unset;">
          <tr><td>Intersect</td><td>A, C, D, E, F, G, H, I, J, K, L, M, N, O</td></tr>
          <tr><td>Intersect (DBMS)</td><td>A, C, D, E, F, G, H, I, J, K, L, M, N, O</td></tr>
          <tr><td>Within</td><td>A, D, G, H, I, O</td></tr>
          <tr><td>Completely within</td><td>A</td></tr>
          <tr><td>Within Clementini</td><td>A, D, G, H, I</td></tr>
          <tr><td>Boundary touches</td><td>F, G, H, I, K, L, M, N, O</td></tr>
          <tr><td>Share a line segment with</td><td>G, I, J, K, M, O</td></tr>
          <tr><td>Crossed by the outline of</td><td>C, E, H, L, N</td></tr>
          <tr><td>Have their center in</td><td>A, C, D, E, G, H, I, J, O</td></tr>
        </table>

=== "Výběr POLYGONŮ..."


    === "...v překrytu s BODY"

        ![](https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/GUID-0973BB65-5DAE-461A-8B84-E58332CDA443-web.gif){ style="filter:none !important;" }
        {: align=center}

        <table id="small_table_padding" style="width:unset;">
          <tr><td>Intersect</td><td>A, B</td></tr>
          <tr><td>Intersect (DBMS)</td><td>A, B</td></tr>
          <tr><td>Contains</td><td>A, B</td></tr>
          <tr><td>Completely contains</td><td>A</td></tr>
          <tr><td>Contains Clementini</td><td>A</td></tr>
          <tr><td>Have their center in</td><td>A, D</td></tr>
          <tr><td>Boundary touches</td><td>B</td></tr>
        </table>

    === "...v překrytu s LINIEMI"

        ![](https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/GUID-EFDE4E93-532E-4D6E-BB29-9BBFC783CEC7-web.gif){ style="filter:none !important;" }
        {: align=center}

        <table id="small_table_padding" style="width:unset;">
          <tr><td>Intersect</td><td>A, C, D, E, F, G, H, I, J, K, L, M, N, O</td></tr>
          <tr><td>Intersect (DBMS)</td><td>A, C, D, E, F, G, H, I, J, K, L, M, N, O</td></tr>
          <tr><td>Contains</td><td>A, D, G, H, I, O</td></tr>
          <tr><td>Completely contains</td><td>A</td></tr>
          <tr><td>Contains Clementini</td><td>A, D, G, H, I</td></tr>
          <tr><td>Boundary touches</td><td>F, G, H, I, K, L, M, N, O</td></tr>
          <tr><td>Share a line segment with</td><td>G, I, J, K, M, O</td></tr>
          <tr><td>Crossed by the outline of</td><td>C, E, H, L, N</td></tr>
          <tr><td>Have their center in</td><td>E, I, L</td></tr>
        </table>

    === "...v překrytu s POLYGONY"

        ![](https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/GUID-7802EBC1-8E73-4071-AE12-4445AB1C24B5-web.gif){ style="filter:none !important;" }
        {: align=center}

        <table id="small_table_padding" style="width:unset;">
          <tr><td>Intersect</td><td>A, C, D, E, F, G, H, I, J, K, M</td></tr>
          <tr><td>Intersect (DBMS)</td><td>A, C, D, E, F, G, H, I, J, K, M</td></tr>
          <tr><td>Contains</td><td>C, E, H, M</td></tr>
          <tr><td>Completely contains</td><td>C</td></tr>
          <tr><td>Contains Clementini</td><td>C, E, H, M</td></tr>
          <tr><td>Within</td><td>F, G, H, M</td></tr>
          <tr><td>Completely within</td><td>F</td></tr>
          <tr><td>Within Clementini</td><td>F, G, H, M</td></tr>
          <tr><td>Are identical to</td><td>H, M</td></tr>
          <tr><td>Boundary touches</td><td>D, E, G, H, I, J, M</td></tr>
          <tr><td>Share a line segment with</td><td>D, H, I, M</td></tr>
          <tr><td>Crossed by the outline of</td><td>A, E, G, J, K</td></tr>
          <tr><td>Have their center in</td><td>C, E, F, G, H, K, L</td></tr>
        </table>
        
</div>

<!-- <figcaption markdown>zdroj: [Select By Location graphic examples](https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/select-by-location-graphical-examples.htm)</figcaption> -->


[:material-open-in-new: Select features by location](https://pro.arcgis.com/en/pro-app/latest/help/mapping/navigation/select-features-by-location.htm){ .md-button .md-button--primary .button_smaller target="\_blank"}
[:material-open-in-new: Select Layer By Location (Data Management)](https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/select-layer-by-location.htm){ .md-button .md-button--primary .button_smaller target="\_blank"}
[:material-open-in-new: Select By Location graphic examples](https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/select-by-location-graphical-examples.htm){ .md-button .md-button--primary .button_smaller target="\_blank"}
{: align=center style="display:flex; justify-content:center; align-items:center; column-gap:20px; row-gap:10px; flex-wrap:wrap;"}

<br><br><br><br><br><br>

<!-- ## Zadání domácího úkolu k semestrální práci -->


asdfasdf


