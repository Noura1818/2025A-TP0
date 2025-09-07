import math as m

# transformation du input en int (entier)
r = int(input('Entrer le rayon (en mm):'))
#formule de l'aire d'un cercle (importer math en m pour mettre la valeur pi)
Aire = (m.pi)*(r**2)
#print l'air dun cercle en transformant la formule Aire en string(str) pour le rendre compatible avec le string (texte)
print('Laire du cercle est (en mm2) : ' + str(Aire))
