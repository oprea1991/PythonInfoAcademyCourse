"""
251 Boolean
Boolean
PF - 08/05/2020 v4
"""  #

# pylint: disable=invalid-name
# pylint: disable=pointless-string-statement

"""Boolean Operators
-------------------------------------
True    and     True    este      True
True    and     False   este      False
False   and     True    este      False
False   and     False   este      False
-------------------------------------
True    or      True    este      True
True    or      False   este      True
False   or      True    este      True
False   or      False   este      False
-------------------------------------
Not     True    este      False
Not     False   este      True
---------------------------------

-----------PRECEDENTA------------
not     este evaluat primul;

and     este evaluat dupa not;

or      este evaluat ultimul.
"""  #

# dati exemple proprii pentru fiecare situatie din cele de mai sus
print((5 + 3) >= 8 and 7 < 10)

# dati 7 exemple utilizand operatori not, and si or combinati,
# Ex: not (10 ** 2) > 101 and (10 >5 or 100 < 0) este True


input("Apasa <enter> pt a iesi.")
