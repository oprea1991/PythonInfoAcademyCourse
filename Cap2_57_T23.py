"""
257 Tema 23
if, for
PF - 08/05/2020 v4
"""  #

# pylint: disable=invalid-name
# pylint: disable=pointless-string-statement

enunt = """
Creati un program in care utilizatorul sa introduca un numar de telefon.
    Acesta trebuie sa introduca un numar cu formatul de 10 cifre si sa inceapa cu 07
Realizati acest program cu ajutorul unui if in if astfel :
    Nu aveti voie sa folositi and sau or in if. 
Verificati daca utilizatorul a introdus exclusiv cifre (isdigit).
    In caz contrar avertizati utilizatorul de greseala si iesiti din program
Daca sirul de caractere este format din cifre, 
    numarati caracterele sirului cu ajutorul unui for. Daca numarul de caractere difera informati utilizatorul.
Daca numarul de caractere al sirului este 10 verificati daca primele doua caractere
    sunt 0 si 7 cu ajutorul unui for. Daca primele doua caractere difera informati utilizatorul.
In cazul in care trece de toate aceste verificari atunci afisati mesajul <<Felicitari!>>
"""  #

print('Introduceti numarul de telefon: ')
print('Numarul trebuie sa contina 10 cifre')
print('Numarul trebuie sa inceapa cu 07')
print('Felicitari!')
print('Numarul trebuie sa contina doar cifre')
