
import random
import zlib
from scipy import stats as st

"""kommando för att justera fil i ubuntu-skalet: grep -v '^#' ursprungligfil.txt | cut -f 2 > nyfil.txt

y = open("agd.txt" , 'r', encoding="utf8")

z = y.read()
y.close()

x = z[:]"""

#print (x)

def beraekna():
    filer = ["agd.txt", "bgr.txt", "bmb.txt", "cym.txt", "deu.txt", "dug.txt", "eus.txt", "hau.txt", "hlt.txt",
             "hun.txt", "inb.txt", "ind.txt", "jav.txt", "kmh.txt", "leu.txt", "lip.txt", "mal.txt", "mhx.txt",
             "myv.txt"]
    morfar = []
    syntar = []

    for fil in filer:
        y = open(fil, 'r', encoding="utf8")

        z = y.read()
        y.close()
        x = z[:]

        print("\n\nVänligen vänta...\n")

        teckenkapad_text = ta_bort_tecknen(x)

        ordkapad_text = ta_bort_ord(x)

        storlek_kompr_urspr = len(zlib.compress(x.encode()))

        storlek_kompr_teckenkapad_text = len(zlib.compress(teckenkapad_text.encode()))

        storlek_kompr_ordkapad_text = len(zlib.compress(ordkapad_text.encode()))

        storlek_ej_kompr_ursprunglig_text = len(x.encode())

        storlek_ej_kompr_teckenkapad_text = len(teckenkapad_text.encode())

        print("   **********   " + fil[:3].upper() + "   **********   ")
        print("\nStorlek ursprunglig text: " + str(storlek_ej_kompr_ursprunglig_text))

        print("\nStorlek teckenkapad text: " + str(storlek_ej_kompr_teckenkapad_text))

        print("\nStorlek ordkapad text: " + str(len(ordkapad_text.encode())))

        print("\nStorlek komprimerad ursprunglig text: " + str(storlek_kompr_urspr))

        print("\nStorlek komprimerad teckenkapad text: " + str(storlek_kompr_teckenkapad_text))

        print("\nStorlek komprimerad ordkapad text: " + str(storlek_kompr_ordkapad_text))

        morf = storlek_kompr_teckenkapad_text / storlek_kompr_urspr
        morfar.append(morf)

        synt = storlek_kompr_ordkapad_text / storlek_kompr_urspr
        syntar.append(synt)

        print("Komplexitetsvärden:")
        print("\nmorf: " + str(morf))
        print("\nsynt: " + str(synt))

    koef_och_pvaerde = st.pearsonr(morfar,syntar)

    print ("\nKorrelationskoeffiecient: " + str(koef_och_pvaerde[0]))
    print("\nP-värde: " + str(koef_och_pvaerde[1]))

def ta_bort_tecknen(texten):
    rensad = "".join(c for c in texten
                     if c == ' ' or c == '\n' or random.random() < 0.9)
    return rensad

def ta_bort_ord(texten):
    rensad = " ".join(w for w in texten.split()
                     if w == '.' or w == ',' or w == ';' or random.random() < 0.9)
    return rensad

beraekna()



"""
print("Vänligen vänta...\n")

teckenkapad_text = ta_bort_tecknen(x)

print("Teckenkapad text:\n")

print (teckenkapad_text)

ordkapad_text = ta_bort_ord(x)

print("\n\nOrdkapad text:\n")

print (ordkapad_text)

#ursprunglig_fil = open("corpus/myv.txt" , 'r+')


storlek_kompr_urspr = len(zlib.compress(x.encode()))

storlek_kompr_teckenkapad_text = len(zlib.compress(teckenkapad_text.encode()))

storlek_kompr_ordkapad_text = len(zlib.compress(ordkapad_text.encode()))


storlek_ej_kompr_ursprunglig_text = len(x.encode())

storlek_ej_kompr_teckenkapad_text = len(teckenkapad_text.encode())


print("\nStorlek ursprunglig text: " + str(len(x.encode())))

print("\nStorlek teckenkapad text: " + str(len(teckenkapad_text.encode())))

print("\nStorlek ordkapad text: " + str(len(ordkapad_text.encode())))


print("\nStorlek komprimerad ursprunglig text: " + str(storlek_kompr_urspr))

print("\nStorlek komprimerad teckenkapad text: " + str(storlek_kompr_teckenkapad_text))

print("\nStorlek komprimerad ordkapad text: " + str(storlek_kompr_ordkapad_text))

morf = storlek_kompr_teckenkapad_text / storlek_kompr_urspr

synt = storlek_kompr_ordkapad_text / storlek_kompr_urspr

print ("Komplexitetsvärden:")
print("\nmorf: " + str(morf))
print ("\nsynt: " + str(synt))"""


#ursprunglig_fil.close()