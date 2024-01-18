def tetel():
    n = int(input("N="))
    while n < 0:
        n = int(input("N="))
    ossz = 0
    for i in range(n+1):
        ossz += i
    print(f"Az első {n} db természetes szám összege: {ossz}")
