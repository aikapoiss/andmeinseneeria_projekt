# Analüüsimisküsimused ja uurimistöö

## Peamised uurimisküsimused

### 1. Rataste defitsiidi piirkondlik levik

**Küsimus**: Millistes Londoni piirkondades (boroughs) tekib tipptundidel suurim rataste defitsiit?

**Analüüs**:
- Defitsiidi määra määramine tunniti ja piirkondade kaupa
- Tipptunnide tuvastamine (millal on defitsiit suurim?)
- Piirkondade järjestamine defitsiidi raskuse järgi
- Ruumilise visualiseerimise (kaardid) tegemine

**Väljund**:
- Piirkondade defitsiidi pingerida
- Kaardid tipptundide defitsiidist
- Ajalised mustrihised

### 2. Dokkide tühjenemise kiirus

**Küsimus**: Milline on ratta asukohtade (dokkide) tühjenemise kiirus ja kas see varieerub piirkondade/jaaamade lõikes?

**Analüüs**:
- Iga jaamatesisese rataste arvu muutuste arvutamine (derivaadid)
- Tühjenemise kiiruse (rataste kaotamine/minutis) modelleerimine
- Jaaamade klassifitseerimine kiiruse järgi
- Ajaliste mustrite tuvastamine

**Väljund**:
- Tühjenemise kiiruse jaotuskaardid
- Top N kiireimalt tühjenevate jaamade nimed
- Ennustavad mudelid (millal jaam tühjub?)

### 3. Ajakavalised mustrid

**Küsimus**: Kas defitsiidil ja tühjenemise kiirusel on ennustatavad mustrid nädalapäevade, tunnitega?

**Analüüs**:
- Tunnipõhine analüüs (heatmapid)
- Nädalapõhine analüüs (esmaspäev vs pühapäev)
- Hooajalisus (suve vs talv?)
- Ajaridade dekompositsioon (trend + seasonaalus + jääk)

**Väljund**:
- Heatmapid (tund × piirkond × defitsiit)
- Seasonaalsetele mustritele sobivad mudelid
- Ennustused tulevase defitsiidi kohta

### 4. Ruumiline korrelatsioon

**Küsimus**: Kas defitsiit on korreleeritud naaberjaamadega? Kas esinevad kobar-mustrid (clustering)?

**Analüüs**:
- Geograafilise läheduse ja defitsiidi korrelatsioon
- Klasteranalüüs (K-means, DBSCAN)
- Ruumiline autokorrelatsioon (Moran's I)

**Väljund**:
- Ruumilised klastrid ("kuumad alad")
- Korrelatsioonmaatriksid

## Sekundaarsed analüüsid

### 5. Rataste hajutamise strateegia

**Küsimus**: Kus peaks olema "repareerija" jaaamad (kus ratast rohkem liigub)?

**Analüüs**:
- Jaamade klassifitseerimine: allikad (source) vs neeldujad (sink)
- Rataste liikumismustrite ennustamine

### 6. Infrastruktuuri taseme mõju

**Küsimus**: Kas jaamade suurus (doki arv) mõjutab defitsiidi ja tühjenemise kiirust?

**Analüüs**:
- Korrelatsioon jaamatesuususe ja defitsiidi vahel
- Optimaalse jaamatesuuse uurimine

### 7. Infratranspordi seosed

**Küsimus**: Kas defitsiit on kõrge lähedal peamiste transpordisõlmedele (metro jaamad, bussipeatsused)?

**Analüüs**:
- Kauguse arvutamine lähimate metrojaamade jne kaugusele
- Ruumiline analüüs

## Uurimistöö metoodoloogia

### Enne analüüsi
1. Andmete kogumise automatiseerimine
2. Andmekvaliteedi kontroll (puuduvad väärtused, outliiers)
3. Metaandmete (piirkonnakuuluvus) täitmine

### Ajal
1. Kirjeldav statistika
2. Visualiseerimised (erinevad graafikud)
3. Statistiline testimine (hüpoteeside kontrollimine)
4. Prediktiivsed mudelid

### Väljund
1. Jupyter notebookid analüüside jaoks
2. CSV/Parquet andmefailid resultaatidega
3. Visualiseerimised (PNG/HTML)
4. Lõpparuanne (markdown)
