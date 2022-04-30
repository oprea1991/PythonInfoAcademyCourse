"""
258 Tema 24
if, for, metode siruri de caractere, functii
PF - 09/06/2020 v4
"""  #
# pylint: disable=invalid-name

enunt = """
    Creati un program in care utilizatorul sa introduca un numar de telefon.
 	Acesta trebuie sa introduca un numar cu formatul de 10 cifre si sa inceapa cu 07.
  	Verificati daca utilizatorul 
  	- a introdus exclusiv cifre (isdigif)
  	- daca incepe cu 07 (cu ajutorul metodelor invatate si al unui if) 
  	- daca sirul contine 10 caractere (cu ajutorul len() ).
  	In caz contrar transmiteti  mesaje corespunzatoare de avertizare.
 	In cazul in care trece de aceste verificari atunci afisati mesajul <<Numar corect!>>
"""  #

sir = input(
    "Scrie un numar de telefon!\nCare sa contina 10 cifre si sa inceapa cu '07'\n"
)

if sir.isdigit():
    if sir.startswith("07"):

        if len(sir) == 10:
            print("Felicitari! Numarul e acceptat.")
        else:
            print("Numar de cifre invalid\n")
    else:
        print("Caracterele din sir nu sunt exclusiv numere sau nu incep 07")
else:
    print("Caracterele din sir nu sunt exclusiv numere sau nu incep 07")

# ---#--- sau ---#---#

nr_tel = input("Introduceti numarul de telefon(10 cifre, incepe cu 07): ")
if not nr_tel.isdigit():
    print("Numarul dv este gresit. Trebuie sa contina doar cifre")
else:
    if nr_tel.find("07") != 0:
        print("Numar invalid. Trebuie sa inceapa cu 07")
    else:
        if len(nr_tel) != 10:
            print("Numar invalid. Numarul cifrelor trebuie sa fie 10")
        else:
            print("Felicitari! Numar acceptat.")

input("\n\nApasa <enter> pt a iesi.")
