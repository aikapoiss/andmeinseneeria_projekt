# TfL BikePoint API Struktuuri dokumentatsioon

## API Ülevaade

**BaseURL**: `https://api.tfl.gov.uk`

**Dokumentatsioon**: https://api.tfl.gov.uk/swagger/ui/index.html?url=/swagger/docs/v1

## Peamised endpointid

### 1. Kõikide BikePoint jaama info
```
GET /BikePoint
```

**Vastus**: JSON massiiv kõikidest jaamadest

**Näide vastusestruktuurist**:
```json
{
  "$type": "TfL.Api.Presentation.Entities.BikePoint, TfL.Api.Presentation.Entities",
  "id": "BikePoints_1",
  "url": "/BikePoint/1",
  "commonName": "River Street , Clerkenwell",
  "placeType": "BikePoint",
  "additionalProperties": [
    {
      "$type": "TfL.Api.Presentation.Entities.AdditionalProperties, TfL.Api.Presentation.Entities",
      "key": "NbBikes",
      "value": "20"
    },
    {
      "key": "NbEmptyDocks",
      "value": "5"
    },
    {
      "key": "NbDocks",
      "value": "25"
    },
    {
      "key": "IsInstalled",
      "value": "true"
    },
    {
      "key": "IsLocked",
      "value": "false"
    },
    {
      "key": "InstallationDate",
      "value": "/Date(1209081600000)/"
    },
    {
      "key": "RemovalDate",
      "value": ""
    },
    {
      "key": "Temporary",
      "value": "false"
    },
    {
      "key": "TerminalName",
      "value": "001023"
    }
  ],
  "lat": 51.5309905,
  "lon": -0.10122347
}
```

### 2. Ühe BikePoint jaama info
```
GET /BikePoint/{id}
```

**Parametrid**:
- `id`: BikePoint ID (nt "BikePoints_1")

## Andmete väljad

| Väli | Selgitus |
|------|----------|
| `id` | Unikaalne jaamateidentifikaator |
| `commonName` | Jaamatenimi (aadress) |
| `lat`, `lon` | Geograafilised koordinaadid |
| `NbBikes` | Saadaolevate rataste arv |
| `NbEmptyDocks` | Tühjad dokid (saadaolevad parkimiskohad) |
| `NbDocks` | Kokku dokkide (parkimiskohtade) arv |
| `IsInstalled` | Kas jaam on paigaldatud |
| `IsLocked` | Kas jaam on lukustatud |
| `InstallationDate` | Paigaldamiskuupäev |
| `TerminalName` | Terminali number |
| `Temporary` | Kas jaam on ajutine |

## Tähtis info

1. **Andmete uuenemise sagedus**: Ligikaudu 1 kord minutis, kuid mitte kõik jaamad ei uuene sünkroonselt
2. **API piirangud**: Otsese hinnatasu ei ole, kuid on rate limiting
3. **Ajalooandmed**: API pakub ainult hetkeseisu, mitte ajalooandmeid
4. **Timestamp**: Andmete hetke aega ei tagastata otse, tuleb ise salvestada

## Näide API päringust (Python)

```python
import requests

base_url = "https://api.tfl.gov.uk"

# Kõik BikePointid
response = requests.get(f"{base_url}/BikePoint")
data = response.json()

for station in data:
    station_id = station['id']
    name = station['commonName']
    lat = station['lat']
    lon = station['lon']
    
    # Leia "NbBikes" väärtus
    props = {prop['key']: prop['value'] for prop in station['additionalProperties']}
    nb_bikes = props.get('NbBikes')
    nb_empty_docks = props.get('NbEmptyDocks')
    nb_docks = props.get('NbDocks')
    
    print(f"{name}: {nb_bikes} ratast, {nb_empty_docks} tühja dokki")
```
