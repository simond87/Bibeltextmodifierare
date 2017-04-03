import random
import zlib
import gzip
import shutil

"""kommando för att justera fil i ubuntu-skalet: grep -v '^#' ursprungligfil.txt | cut -f 2 > nyfil.txt"""

y = open("hau.txt" , 'r')

z = y.read()
y.close()

x = z[:]

print (x)

def ta_bort_tecknen(texten):
    rensad = "".join(c for c in texten
                     if c == ' ' or c == '\n' or random.random() < 0.9)
    return rensad

def ta_bort_ord(texten):
    rensad = " ".join(w for w in texten.split()
                     if w == '.' or w == ',' or w == ';' or random.random() < 0.9)
    return rensad

print("Vänligen vänta...\n")

teckenkapad_text = ta_bort_tecknen(x)

print("Teckenkapad text:\n")

print (teckenkapad_text)

ordkapad_text = ta_bort_ord(x)

print("\n\nOrdkapad text:\n")

print (ordkapad_text)

#ursprunglig_fil = open("corpus/myv.txt" , 'r+')
"""with open ('corpus/myv.txt', 'rb') as f_in, gzip.open('komprimerad.txt.gz', 'wb') as f_out:
    shutil.copyfileobj(f_in, f_out)"""

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

#ursprunglig_fil.close()
