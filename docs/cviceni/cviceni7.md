---
icon: material/numeric-7-box
title: Cvičení 7
---

# ArcGIS Online, webové služby, připojení do ArcGIS Pro

## Cíl cvičení

Náplní cvičení je seznámení s prostředním ArcGIS Online. V rámci cvičení si vyzkoušíte publikaci dat z ArcGIS Pro do ArcGIS Online a jejich využití v opačném směru. Ukážeme si také publikaci standardizovaných mapových služeb pomocí ArcGIS Serveru a to, jak je také lze v prostředí ArcGIS Online využít.

## Základní pojmy

- [**ArcGIS Online**](https://doc.arcgis.com/en/arcgis-online/get-started/get-started.htm) – cloudové prostředí pro ukládání, vizualizaci, tvorbu, správu a vytěžování geografických dat

- **webová služba** – rozhraní, skrze které spolu komunikují servery anebo server & klient; speciálně [webová mapová služba](https://mediaspace.esri.com/media/t/1_05edhhbq) je standard pro komunikaci s tzv. *webovým mapovým serverem* poskytujícím geoprostorová data (mapy, vektorová data, dlaždice, nástroje apod.) prostřednictvím internetu

- **publikace dat** – odeslání lokálně uložené mapové kompozice na server (cloud) a vytvoření datové vrstvy přístupné skrze internet

- [**ArcGIS Server**](https://www.esri.com/en-us/arcgis/products/arcgis-enterprise/overview) – součást řešení ArcGIS Enterprise – vlastní mapový server umožňující publikaci webových mapových služeb

- [**Feature Layer**](https://mediaspace.esri.com/media/t/1_ids5c2qs) – typ dat publikovaných do ArcGIS Online – vektorová vrstva nebo skupina vrstev

- [**Tile Layer**](https://www.esri.com/arcgis-blog/products/sharing-collaboration/sharing-collaboration/best-practices-for-using-tile-layers/) – typ dat publikovaných do ArcGIS Online – rastrová vrstva nebo skupina vrstev využívající dlaždicovou cache pro rychlejší načítání obsahu

- [**kredity**](https://www.esri.com/en-us/arcgis/products/credits/overview) – platební jednotka, pomocí které se uskutečňuje úhrada nákladů za vybrané služby ArcGIS Online (úložiště, geoprocessing, data enrichment, využívání cloudových nástrojů jako je on-line geokódování apod.). Každý student má na začátku alokováno 100 kreditů, aby si mohl vyzkoušet používání služeb, které kredity spotřebovávají

## Použité datové podklady

- [Císařské otisky stabilního katastru](../../data/#cisarske-otisky-stabilniho-katastru)
- [Státní mapa 1 : 5 000 – odvozená](../../data/#statni-mapa-1-:-5-500-0-–-odvozena)
- klad SMO5

## Náplň cvičení

### **Vlastní obsah na ArcGIS Online a jeho zveřejnění**

### Vytvořte mapu obcí s rozšířenou působností jednoho z krajů ČR


### Vytvořte webovou mapu v cloudu ArcGIS Online, obsahující silnice, železnice a správní členění vašeho kraje na ORP

### Vyzkoušejte si vytvořit mapovou kompozici kraje s využitím dat z různého umístění



## Úlohy k procvičení

!!! task-fg-color "Úlohy"

    K řešení následujích úloh použijte datovou sadu [ArcČR
    500](../../data/#arccr-500) verzi 3.3 dostupnou na disku *S* ve složče
    ``K155\Public\data\GIS\ArcCR500 3.3``. Zde také najdete souboru s
    popisem dat ve formátu PDF. 
    
    1. Vytvořte mapu obcí s rozšířenou působností jednoho z krajů ČR.

        Použijte data ORP z datové sady ArcČR
        (ObceSRozsirenouPusobnosti_Polygony), vyexportujte do nové třídy prvků
        pouze zvolený kraj. Mapu doplňte zastavěnými oblastmi obcí nad 5 tisíc
        obyvatel.

        Vyexportujte mapu (Share As ► Service ► My hosted content) a umístěte
        na ArcGIS Online do svého umístění. Jako typ zvolte Feature Service,
        nikoli Tile Layer. Můžete nasdílet se skupinou CTU Prague.

        Jednotlivé plochy ORP popište. Barevnost zvolte tak, aby z mapy byla
        zároveň poznat i příslušnost ORP k okresům (ORP jsou do okresů
        skladebné).


    2. Vytvořte mapovou službu WMS (OGC standard) nebo Mapping Service
       (Esri nativní) silnic a železnic ve vašem kraji.

        Použijte příslušné vrstvy z ArcČR, ořízněte na velikost kraje.

        Vyexportujte mapu (Share As ► Service ► ArcGIS Server) a umístěte na
        server *gis.fsv.cvut.cz* do složky GIS1_2018. Jako typ zvolte mimo
        Mapping také standard *WMS*, případně jiné.

        Připravte si ještě vrstvu vodních ploch (VodniPlochy_Polygony),
        ořízněte ji na plochu kraje a uložte do své složky jako shapefile,
        poslouží později.


    3. Vyzkoušejte si vytvořit mapovou kompozici kraje s využitím dat z různého umístění.

        V mapové kompozici můžete využívat data umístěná v různých formátech:

        - data z ArcGIS Online nebo z vlastního Portal for ArcGIS,
        - data z WMS, WMTS služeb,
        - data ze služeb ArcGIS Serveru,
        - data z WFS služeb,
        - souborová data uložená jako SHP, CSV, GPX aj.,
        - dynamické vrstvy *Živého atlasu Esri*
