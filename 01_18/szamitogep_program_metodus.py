from Szamitogep import Szamitogep

def listaba(list: Szamitogep):
    szamitogepek = []
    f = open("szamitogepek.txt", "r", encoding="utf8")
    f.readline()
    sorok = f.readlines()
    f.close()
    for i in range(len(sorok)):
        darab = Szamitogep(sorok[i])
        szamitogepek.append(darab)

    return szamitogepek
def kiiras(szamitogepek):
    for i in range(len(szamitogepek)):
        op_r = szamitogepek[i].op_r
        ram = szamitogepek[i].ram
        print(f"{op_r} ({ram})")

def atlag(szamitogepek):
    print("Átlag: ", end="")
    ossz = 0
    for i in range(len(szamitogepek)):
        ossz += szamitogepek[i].ram
    print(round(ossz / len(szamitogepek), 3))

def legtobb(szamitogepek):
    print("Legtöbb ram-ot tartalmazó oprendszer: ", end="")
    max = 0
    for i in range(len(szamitogepek)):
        if szamitogepek[max].ram < szamitogepek[i].ram:
            max = i
    print(szamitogepek[max].op_r)

def w_szamol(szamitogepek):
    w_g = 0
    print(f"Hány Windows-os gépünk van? ", end="")
    for i in range(len(szamitogepek)):
        if szamitogepek[i].op_r == "Win":
            w_g += 1
    print(f"Válasz: {w_g}")

def van_e(szamitogepek):
    vizsgalt_ram = 22
    print(f"Van-e {vizsgalt_ram} GB-nál nagyobb windows: ", end="")
    i = 0
    seged = False
    while i <= len(szamitogepek) - 1 and seged == False:
        if szamitogepek[i].ram > vizsgalt_ram and szamitogepek[i].op_r == "Win":
            seged = True
        else:
            i += 1

    if seged == True:
        print("Van")
    else:
        print("Nincs")

