# Laeb API-st jooksva seisu ja kirjutab lokaalsesse PG baasi ühte tabelisse
# Parool ja muu baasi info on hetkel siia sisse kirjutatud
# Vaja oleks Dockeri peale viia

import os
import requests
import psycopg

def get_and_load_bikepoints():
    # 1. API Päring
    url = "https://api.tfl.gov.uk/BikePoint"
    try:
        response = requests.get(url)
        response.raise_for_status()
        bike_stations = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Viga API-st andmete pärimisel: {e}")
        return

    parsed_stations = []

    # Abifunktsioonid andmetüüpide turvaliseks teisendamiseks
    def to_bool(val):
        if val is None: return None
        return str(val).lower() in ['true', '1', 'yes']

    def to_int(val):
        try: return int(val)
        except (ValueError, TypeError): return None

    for station in bike_stations:
        # 2.1 Eraldame additionalProperties seest nii väärtused kui ka kõik muutmise ajad
        properties = {}
        modification_times = []
        
        for prop in station.get('additionalProperties', []):
            key_lower = prop.get('key', '').lower()
            properties[key_lower] = prop.get('value')
            
            # Korjame kokku selle omaduse muutmise aja, kui see on olemas
            if prop.get('modified'):
                modification_times.append(prop.get('modified'))
        
        # 2.2 Leiame kõige hilisema muutmise aja sellest massiivist
        # Kui aegu ei leitud, paneme väärtuseks None
        latest_modified = max(modification_times) if modification_times else None
            

        # Koostame ühe rea andmed, mis vastavad täpselt tabeli veergudele (va 'id', mis on IDENTITY)
        row = (
            station.get('id'),                                # bikepoint_id
            station.get('url'),                               # url
            station.get('commonName'),                        # commonname
            station.get('placeType'),                         # placetype
            properties.get('terminalname'),                   # terminalname
            to_bool(properties.get('installed')),             # is_installed
            to_bool(properties.get('locked')),                # is_locked
            to_int(properties.get('installdate')),            # installdate
            to_int(properties.get('removaldate')),            # removaldate
            to_bool(properties.get('temporary')),             # is_temporary
            to_int(properties.get('nbbikes')),                # nbbikes
            to_int(properties.get('nbemptydocks')),           # nbemptydocks
            to_int(properties.get('nbdocks')),                # nbdocks
            to_int(properties.get('nbstandardbikes')),        # nbstandardbikes
            to_int(properties.get('nbebikes')),               # nbebikes
            station.get('lat'),                               # lat
            station.get('lon'),                               # lon
            latest_modified                                   # modified timsestamp
        )
        parsed_stations.append(row)

    # 3. Andmebaasi ühendus ja laadimine
    # Muuda siin andmebaasi ühenduse andmed vastavalt enda omale
    db_config = "dbname=postgres user=postgres password=minusalaparool host=localhost port=5432"
    
    # SQL sammud: Loo tabel (kui pole) -> Tühjenda -> Sisesta uued andmed
    create_table_query = """
    CREATE TABLE IF NOT EXISTS bikepoint (
        id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        bikepoint_id VARCHAR(100) NOT NULL,
        url VARCHAR(100),
        commonname VARCHAR(1000),
        placetype VARCHAR(100),
        terminalname VARCHAR(100),
        is_installed BOOLEAN,
        is_locked BOOLEAN,
        installdate BIGINT,
        removaldate BIGINT,
        is_temporary BOOLEAN,
        nbbikes INTEGER,
        nbemptydocks INTEGER,
        nbdocks INTEGER,
        nbstandardbikes INTEGER,
        nbebikes INTEGER,
        lat NUMERIC(10,6),
        lon NUMERIC(10,6),
        modified TIMESTAMPTZ,
        loaded_at TIMESTAMP DEFAULT NOW()
    );
    """
    
    truncate_query = "TRUNCATE TABLE bikepoint;"
    
    insert_query = """
        INSERT INTO bikepoint (
            bikepoint_id, url, commonname, placetype, terminalname, 
            is_installed, is_locked, installdate, removaldate, is_temporary, 
            nbbikes, nbemptydocks, nbdocks, nbstandardbikes, nbebikes, lat, lon,
            modified
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        );
    """

    try:
        with psycopg.connect(db_config) as conn:
            with conn.cursor() as cur:
                # 3.1 Kontrollime/loome tabeli
                print("Kontrollin andmebaasi tabeli olemasolu...")
                cur.execute(create_table_query)
                
                # 3.2 Teeme tabeli tühjaks
                print("Tühjendan tabeli vanadest andmetest (TRUNCATE)...")
                cur.execute(truncate_query)
                
                # 3.3 Sisestame uued andmed
                print(f"Sisestan uued andmed... Kokku {len(parsed_stations)} jaama.")
                cur.executemany(insert_query, parsed_stations)
                
                # Kinnitame kõik tegevused ühe transaktsioonina
                conn.commit()
                print("Kogu protsess edukalt lõpetatud ja andmed uuendatud!")
                
    except Exception as e:
        print(f"Andmebaasi viga protsessi käigus: {e}")

# Käivitame koodi
if __name__ == "__main__":
    get_and_load_bikepoints()