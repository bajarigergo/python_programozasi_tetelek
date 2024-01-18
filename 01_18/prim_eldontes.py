def tetel():
    n = int(input("szám:\n"))
    prim = False
    if n < 2:
        prim = False
    else:
        i = 2
        while (i <= n**0.5) and n % i != 0:
            i += 1
        prim = i > n**0.5
    print(f"Prím" if prim else f"Nem prím")


