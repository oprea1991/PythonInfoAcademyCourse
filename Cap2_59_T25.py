"""
259 Tema 25
exercitiu - cauta numarul
PF - 15/06/2020 v4
"""  #

# pylint: disable=invalid-name
# pylint: disable=pointless-string-statement
# pylint: disable=trailing-whitespace
# pylint: disable=no-else-break

from random import randint

"""
1. Din modulul random importam functia randint ();
2. Cream o variabila care contine un numar aleator cu functia randint Ex: randint(0, 100)
   va genera numere aleatoare intregi intre 0 si 100;
3. Cream o variabila care sa stocheze numarul de incercari, initial zero;
4. Creati o bucla, care sa va permita sa alegeti un numar:
    4.1. Incrementati numarul de incercari cu unu;
    4.2. Testati daca este numarul corect, caz in care afisati un mesaj 
    de felicitare si iesiti cu break;
    4.3. Daca nu este corect testati daca numarul ales este mai mare decat numarul corect,
    afisati un mesaj care sugereaza ca numarul e prea mare si continuati bucla(continue);
    4.4. Daca nu este corect testati daca numarul ales este mai mic decat numarul corect,
    afisati un mesaj care sugereaza ca numarrul e prea mic si continuati bucla(continue  
"""  #
from random import randint