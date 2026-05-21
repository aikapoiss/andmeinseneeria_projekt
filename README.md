# Londoni jalgrattarendi koormuse dünaamika

## Projekti kirjeldus

See projekt analüüsib Londoni jalgrattarendi süsteemi (TfL BikePoint) andmeid, et:
1. Tuvastada, millistes piirkondades tekib tipptundidel suurim rataste defitsiit
2. Analüüsida ratta asukohtade (dokkide) tühjenemise kiirust
3. Leida mustrid ja seosed piirkonna tunnetuste ning rataste kättesaadavuse vahel

## Andmeallikad

- **API**: [Transport for London BikePoint API](https://api.tfl.gov.uk/BikePoint)
- **Uuenemise sagedus**: ~1 kord minutis (kuid mitte kõikide asukohtade info ei uuene sünkroonselt)
- **Andmete tüüp**: Real-time hetkeseisud, aegridade ehitamine

## Projekti struktuuri selgitus

```
andmeinseneeria_projekt/
├── data/                      # Andmete kataloog
│   ├── raw/                   # Töötlemata JSON/CSV andmefailid
│   ├── processed/             # Töödelud ja koondatud andmed
│   └── metadata.json          # Dokkide info (koordinaadid, nimetused)
│
├── src/                       # Põhikood
│   ├── collectors/            # Andmete kogumine
│   │   └── bike_api.py       # TfL API päringud
│   ├── processors/            # Andmete töötlemine
│   │   ├── aggregators.py    # Andmete koondamine (aja alusel)
│   │   ├── time_series.py    # Aegridade konstrueerimine
│   │   └── spatial.py        # Geograafiline analüüs (piirkonnad)
│   ├── analyzers/             # Andmete analüüs
│   │   ├── deficits.py       # Rataste defitsiidi analüüs
│   │   ├── patterns.py       # Mustrite tuvastamine
│   │   └── dynamics.py       # Dünaamika uurimine
│   └── utils/                 # Abifunktsioonid
│       ├── config.py         # Konfiguratsioon
│       ├── geo.py            # Geograafilised funktsioonid
│       └── time.py           # Aja töötlemise funktsioonid
│
├── notebooks/                 # Jupyter notebookid
│   ├── 01_eda.ipynb          # Exploratory data analysis
│   ├── 02_deficits.ipynb     # Defitsiidi analüüs
│   └── 03_dynamics.ipynb     # Dünaamika visualiseerimise
│
├── tests/                     # Automaattestid
│   ├── test_collectors.py
│   ├── test_processors.py
│   └── test_analyzers.py
│
├── config/
│   └── settings.yaml          # Projekti seaded
│
├── scripts/
│   ├── collect_data.py        # Käivitamisskript andmete kogumiseks
│   ├── process_data.py        # Andmete töötlemise skript
│   └── schedule_collector.py  # Korraldatud andmete kogumine (cron/scheduler)
│
├── docs/
│   ├── api_structure.md       # TfL API dokumentatsioon
│   ├── data_schema.md         # Andmete skeemid
│   └── analysis_questions.md  # Analüüsimisküsimused
│
├── requirements.txt
├── .gitignore
└── LICENSE
```

## Installatsioon

```bash
git clone https://github.com/aikapoiss/andmeinseneeria_projekt.git
cd andmeinseneeria_projekt
pip install -r requirements.txt
```

## Kasutamine

### 1. Andmete kogumine
```bash
python scripts/collect_data.py
```

### 2. Andmete töötlemine
```bash
python scripts/process_data.py
```

### 3. Analüüsimisnotebookide käivitamine
```bash
jupyter notebook notebooks/
```

## Peamised analüüsimisküsimused

1. **Piirkondlik defitsiit**: Millistes piirkondades (borough/district) on tipptundidel kõige suurem rataste puudus?
2. **Tühjenemise kiirus**: Kui kiiresti erinevad dokid tühjenevad ja millised on võimalikud põhjused?
3. **Ajakava mustrid**: Kas defitsiidil on ennustatavad mustrid nädalapäevade/tunnide kaupa?
4. **Geograafilised mustrid**: Kas defitsiit on korreleeritud transpordivõrgu või näiteks avalike kohtadega?

## Aegridade ehitamine

Andmete korduva kogumise (minutilise) alusel ehitame:
- **Aegrittead**: igas dokis vabade rataste arv ajas
- **Agregeeritud aegrittead**: piirkondade kaupa aggregeeritud andmed
- **Tuletatud tunnused**: rataste puuduse määr, tühjenemise kiirus (deriivaat) jne

## Litsents

See projekt on avalik ja kasutab TfL avatud andmeid.

## Kontakt

Projekti autor: [aikapoiss](https://github.com/aikapoiss)
