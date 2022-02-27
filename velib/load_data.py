""" script that gets data using the DATA_API and """
import requests
from velib.models import Station


# thème: Mobilité et Espace Publique | Sujet: Vélib - Vélos et bornes

API_URL = 'https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&q=&rows=1439'


def parse_integer(s):
    """parse only digits in string and cast the number found to integer"""
    return int("".join([char for char in s if char.isdigit()]))


def activate_model(data):
    for record in data["records"]:
        # treat non-int values in id
        id = parse_integer(record["fields"]["stationcode"])
        # encountered no problem with the rest
        name = record["fields"]["name"]

        num_bikes = int(record["fields"]["ebike"]) + \
            int(record["fields"]["mechanical"])

        num_bikes_available = int(record["fields"]["numbikesavailable"])
        num_docks_available = int(record["fields"]["numdocksavailable"])
        capacity = int(record["fields"]["capacity"])
        is_renting = True if record["fields"]["is_renting"] == "OUI" else False
        is_installed = True if record["fields"]["is_installed"] == "OUI" else False
        is_returning = True if record["fields"]["is_returning"] == "Oui" else False
        commune = record["fields"]["nom_arrondissement_communes"]
        Station(id,
                name,
                num_bikes,
                num_bikes_available,
                num_docks_available,
                capacity,
                is_renting,
                is_installed,
                is_returning,
                commune
                ).save()


request = requests.get(API_URL)
data = request.json()
activate_model(data)
