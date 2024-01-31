import sys


def tetel():
    db = 0
    vege = 0
    legkis = sys.maxsize
    while (szam := int(input(">"))) != vege:
        if szam < legkis and szam != vege:
            legkis = szam
        db += 1
    return f"{db} számbol a legkisebb: {legkis}"