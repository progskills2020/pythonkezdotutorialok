
"""
szam1 = int(input("adja meg a szamot:"))
szam2 = int(input("adja meg a szamot:"))

if szam1 == szam2:
    print("egyenlok")
elif szam1 < szam2:
    print("az első szám kisebb")
else:
    print("második szám kisebb")
"""

"""
ferfi_e = True

kerdes = input("kerem adja meg a nemét(ferfi,no)")

if kerdes == "ferfi":
    ferfi_e = True
elif kerdes == "no":
    ferfi_e = False
else:
    print("rossz erteket adott meg")

if ferfi_e:
    print("a ferfi mozsdo jobbra van")
else:
    print("a noi mozsdo balra van")
"""

nev1 = input("Kérem adja meg a nevét:")
kor1 = int(input("Kérem adja meg a korát:"))

if kor1 <= 25:
    print("Szia %s, te %d éves vagy." % (nev1, kor1))
elif kor1>25 and kor1 <= 65:
    print("Jó napot kivánok %s, ön %d éves." % (nev1, kor1))
else:
    print("Tiszteltetem %s, ön %d éves." % (nev1, kor1))



 
