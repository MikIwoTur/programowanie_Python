# zadanie 1
from random import randint
import requests

runda = 0

print("""Witaj nowy Uzytkoniku! Czy chcesz ze mna zagrac w gre???
      jezeli tak to... """)

while runda < 21:

    gracz = int(input("...wpisz tu liczbe od 0 do 20: "))
    maszyna = randint(0, 20)

    if gracz == maszyna:
        print("Brawo wygrales!")
        break
    else:
        print("jeszcze raz!")
        runda += 1

# zadanie 2


def struktura(accession):
    url = f"https://www.ebi.ac.uk/pdbe/graph-api/mappings/best_structures/{accession}"
    odpowiedz = requests.get(url)
    if odpowiedz.status_code == 200:
        return odpowiedz.json()
    return None


data = struktura("Q9NR28")


def najlepszePokrycie(data: dict) -> dict:

    slowniki = list(data.values())[0]
    slowniki = [s for s in slowniki if s["resolution"] != None]

    naj_pokrycie_slownik = max(slowniki, key=lambda i: i["coverage"])

    naj_pokrycie = [s for s in slowniki if s["coverage"]
                    == naj_pokrycie_slownik["coverage"]]

    naj_udost = min(naj_pokrycie, key=lambda i: i["resolution"])

    zmniejszony_slownik = {naj_udost["pdb_id"]:
                           {
        "chain_id": naj_udost["chain_id"],
        "unp_start": naj_udost["unp_start"],
        "unp_end": naj_udost["unp_end"]
    }
    }

    return zmniejszony_slownik


najWynik = najlepszePokrycie(data)
print(najWynik)

# zadanie 3


def dostep(pdb_id):
    url = f'https://www.ebi.ac.uk/pdbe/api/pdb/entry/molecules/{pdb_id}'
    odpowiedz = requests.get(url)
    if odpowiedz.status_code == 200:
        return odpowiedz.json()
    return None


infoMol = dostep(str(list(najWynik.keys())[0]))


def sekwencjeMolekularne(infoMol: dict, najWynik: dict) -> str:
    slowniki = list(infoMol.values())[0]
    klucz = str(list(najWynik.keys())[0])

    for slownik in slowniki:
        if slownik["molecule_type"] == "polypeptide(L)" and najWynik[klucz]["chain_id"] in slownik["in_chains"]:
            znaleziono = slownik

    sekwencje = znaleziono["sequence"]
    wynik = sekwencje[najWynik[klucz]
                      ["unp_start"] - 1: najWynik[klucz]["unp_end"]]
    return wynik


naszeSekwencje = sekwencjeMolekularne(infoMol, najWynik)
print(naszeSekwencje)
