import string

#print(string.ascii_uppercase)


def szyfr(tekst, klucz):
    zaszyfrowany = " "
    for _ in tekst:
        print()
        numer = ord(x)
        litera = chr(numer + litera)
        zaszyfrowany = litera
    return zaszyfrowany
    
    #ord("A") == 43
    #chr("34") == "B"


szyfr()