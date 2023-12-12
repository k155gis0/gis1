# Semestrální práce - Analýza území

## Zadání
Nad zadaným územím proveďte následující analýzy s využitím GIS softwaru. Výsledky následně publikujte formou webové mapové aplikace na ArcGIS Online či pomocí open-source řešení (např. GISQuick). Tato aplikace může mít libovolnou formu – takovou, kterou uznáte za vhodnou či zajímavou (ArcGIS Instant Apps, Story Maps, Dashboards, Experience Builder,...). 

Svou aplikaci na konci semestru krátce odprezentujete před ostatními v 5 minutové prezentaci. Zároveň odevzdáte technickou zprávu s popisem postupu práce, vybranými vrstvami a důvodu výběru výsledného vizuálního stylu webové mapové aplikace.

Práce nad rámec základního zadání bude ohodnocena bonusovými body. Příklad: Místo klasické webové mapové aplikace vytvoříte interaktivní Story Maps s popisem dat a příslušnými obrázky.    

**Pro zadané území vypracujte následující úkoly:**

**1.** Z databáze RÚIAN vyberte zadanou obec a vyexportujte ji do samostatné vrstvy.

**2.** Zjistěte, zda se na území zadané lokality nachází chráněné území (zdroj: ZABAGED). Pokud ano, zobrazte jej v mapě jako samostatnou vrstvu.

**3.** Vytvořte samostatnou vrstvu, která bude obsahovat data způsobu využití půdy (zdroj: ZABAGED). Vrstvu vhodně symbolizujte na základě typů využití půdy.

**4.** Pro zadanou obec a obce s ní přímo sousedící stáhněte vámi zvolená data z Českého statistického úřadu (např. výsledky voleb či data cestovního ruchu). Tato data musejí mít dané údaje rozdělené dle obcí (ukazatel *OB*). Data propojte s atributovou tabulkou vybrané vrstvy obcí a jedoduše vizualizujte v samostatné vrstě.

**5.** Připojte WMS, WMTS či WFS službu dle vašeho výběru (např. historickou mapu, ortofoto či katastrální mapu). Lze připojit až v ArcGIS Online.

**6.** Georeferencujte rastry Státní mapy 1 : 5 000 – odvozené z 50. let 20. století. Najdete se na disku S. Georeferencujte pouze rastry, na kterých se vaše území nachází. Z georeferencovaných rastrů vytvořte mozaiku.

**7.** Na podkladu SMO5 vektorizujte území v okruku 500 metrů od definičního bodu obce. Ten vypočítejte jako těžiště polygonu obce. Tato data slučte na základě typů využití ploch (funkce Dissolve).

Rozlišujte následující typy využití ploch: 

- orná půda

- les

- trvalé travnaté porosty (louky, pastviny)

- budovy

- cestní síť (cesty, silnice)

- vodní plochy (řeky, potoky, rybníky), nevektorizujte malé vodní toky vyznačené pouze liniově

- ostatní plochy (nádvoří, lomy, neúrodná půda apod.)

**8.** Vektorizaci topologicky zkontrolujte dle pravidel *Must Not Have Gaps (Area)*, *Must Not Overlap With (Area-Area)* a *Must Not Overlap (Area)*.

**9.** Ve výsledné aplikaci porovnejte vývoj využití krajiny v 50. letech 20. století (vektorizace z SMO5) se současností (ZABAGED). Způsob porovnání zvolte dle vlastního uvážení (posuvník v aplikaci, nová vrstva s vypočtenými rozdíly apod.).

## Konkrétní zadání

## Termín odevzdání