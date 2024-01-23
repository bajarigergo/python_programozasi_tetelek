from Szamitogep import Szamitogep

peldany1 = Szamitogep("Win", 32)
peldany2 = Szamitogep("Mac", 16)
peldany3 = Szamitogep("Win", 16)

szamitogepek = []

szamitogepek.append(peldany1)
szamitogepek.append(peldany2)
szamitogepek.append(peldany3)
for i in range(len(szamitogepek)):
    op_r = szamitogepek[i].op_r
    ram = szamitogepek[i].ram
    print(f"{op_r} ({ram})")

print("Átlag: ", end="")
ossz = 0
for i in range(len(szamitogepek)):
    ossz += szamitogepek[i].ram
print(round(ossz / len(szamitogepek), 3))


print("Legtöbb ram-ot tartalmazó oprendszer: ", end="")
max = 0
for i in range(len(szamitogepek)):
    if szamitogepek[max].ram < szamitogepek[i].ram:
        max = i
print(szamitogepek[max].op_r)

w_g = 0
print(f"Hány Windows-os gépünk van? ", end="")
for i in range(len(szamitogepek)):
    if szamitogepek[i].op_r == "Win":
        w_g += 1
print(f"Válasz: {w_g}")




# eldontes tétele:



# van = False
# for i in range(len(szamitogepek)):
#     if szamitogepek[i].ram > vizsgalt_ram and szamitogepek[i].op_r == "Win":
#         van = True
#         i = len(szamitogepek)-1
#
# if van == True:
#     print("Van")
# else:
#     print("Nincs")
#


vizsgalt_ram = 22
print(f"Van-e {vizsgalt_ram} GB-nál nagyobb windows: ", end="")
i = 0
seged = False
while i <= len(szamitogepek)-1 and seged == False:
    if szamitogepek[i].ram > vizsgalt_ram and szamitogepek[i].op_r == "Win":
        seged = True
    else:
        i += 1

if seged == True:
    print("Van")
else:
    print("Nincs")
