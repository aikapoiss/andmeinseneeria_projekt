# Andmete skeemid

## 1. Töötlemata andmed (Raw)

### `raw/bikepoint_snapshot_{timestamp}.json`

Kas ajahetkel tehtud API vastus (täies ulatuses).

```json
[
  {
    "id": "BikePoints_1",
    "commonName": "River Street , Clerkenwell",
    "lat": 51.5309905,
    "lon": -0.10122347,
    "additionalProperties": [...]
  },
  ...
]
```

## 2. Metaandmed (jaama omadused)

### `data/metadata.json`

Jaamade staatiline teave (asukohad, nimetused).

```json
{
  "BikePoints_1": {
    "id": "BikePoints_1",
    "name": "River Street , Clerkenwell",
    "lat": 51.5309905,
    "lon": -0.10122347,
    "borough": "Islington",
    "terminal_name": "001023",
    "installation_date": "2009-04-25"
  },
  ...
}
```

## 3. Töödelud andmed (Processed)

### `processed/time_series.csv` või `processed/time_series.parquet`

Aegrittead igas jaamas.

| timestamp | station_id | station_name | lat | lon | nb_bikes | nb_empty_docks | nb_docks | occupancy_rate | is_installed | is_locked |
|-----------|-----------|--------------|-----|-----|----------|-------|----------|-------|-----|---|
| 2025-05-21 08:00:00 | BikePoints_1 | River Street , Clerkenwell | 51.53 | -0.10 | 20 | 5 | 25 | 0.80 | true | false |
| 2025-05-21 08:01:00 | BikePoints_1 | River Street , Clerkenwell | 51.53 | -0.10 | 19 | 6 | 25 | 0.76 | true | false |

### `processed/deficit_analysis.csv`

Defitsiidi analüüsi tulemused.

| hour | day_of_week | station_id | station_name | borough | avg_nb_bikes | min_nb_bikes | deficit_score | shortage_frequency |
|------|-----------|---------|--------|-----|-----|-----|----|
| 8 | Monday | BikePoints_1 | River Street | Islington | 8.5 | 1 | 0.78 | 0.35 |

### `processed/dynamics.csv`

Dünaamika analüüs (tühjenemise kiirus).

| station_id | station_name | borough | hour | avg_bike_loss_per_minute | avg_emptying_time_minutes | volatility |
|-----------|---------|-----|-----|-------|-------|----|
| BikePoints_1 | River Street | Islington | 8 | 0.45 | ~10 | 0.23 |

## 4. Tuletatud tunnused

- **Occupancy Rate**: `nb_bikes / nb_docks`
- **Empty Dock Rate**: `nb_empty_docks / nb_docks`
- **Deficit Score**: Kuidas ratas on saadaval (0-1, kus 0 = puudus)
- **Emptying Time**: Aeg, mis kulub dokil täiest tühjenemiseks
- **Bike Loss Rate**: Rataste kaotuse kiirus ajaühiku kohta (derivaadid)

## 5. Piirkondade määratlemine

Londoni administratiivsed ringkonnad (boroughs), kuhu jaaamad klassifitseeritakse geograafiliste koordinaatide alusel.

**32 Londoni ringkonda**:
- City of London
- Barking and Dagenham
- Barnet
- Bexley
- Brent
- Bromley
- Camden
- Croydon
- Ealing
- Enfield
- Greenwich
- Hackney
- Hammersmith and Fulham
- Haringey
- Harrow
- Havering
- Hillingdon
- Hounslow
- Islington
- Kensington and Chelsea
- Kingston upon Thames
- Lambeth
- Lewisham
- Merton
- Newham
- Redbridge
- Richmond upon Thames
- Southwark
- Sutton
- Tower Hamlets
- Waltham Forest
- Wandsworth

## Aegridade konstrueerimise strateegia

1. **Hetkeseisud** (Raw): Korduval API päringul kogutud andmed
2. **Tiidetud aegrittead**: Puuduvate ajahetkede interpoleerimine
3. **Agregeerimised**: Tunnilt tunnile, päevalt päevale aegrittead
4. **Tuletused**: Kiirused, muutused, muud matemaatilised operatsioonid
