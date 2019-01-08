from __future__ import division
from math import log

def choix_base(e,base1):
    ok,supp=0,"de départd'arrivée" 
    while not ok:
        base=input("Entrer la base "+supp[e:e+9]+" (entre 2 et 36) : ")
        try:
            base_n=int(base)
            if base_n<2 or base_n>36:
                print ("Désolé, valeur hors limite. Veuillez recommencer S.V.P.\n")
            else:
                if e==9 and base_n==base1:
                   print ("Désolé, Les bases sont les mêmes. Veuillez recommencer S.V.P.\n")
                else:
                    ok=1           
        except ValueError:
            print("Désolé, ceci n'est pas un nombre. Veuillez recommencer S.V.P.\n")
    return base_n
                     
def choix_du_nombre(a):
    ok=0
    while not ok:
        nombre=input("Entrer le nombre à convertir : ").upper()
        chiffre='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:a]
        for car in nombre:
            if car not in chiffre:
                print('Désolé, '+car+' n\'existe pas en base '+str(a)+'. Veuillez recommencer, S.V.P\n')
                break
            else:
                ok=1
    return nombre

def vers_dix(s,a):
    l,nombre,s=len(s),0,s[::-1]
    chiffre='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(l):       
        nombre+=chiffre.find(s[i])*a**i
    return nombre

def vers_base(nombre_cr,a):
    nombre,nombre_div='',int(log(nombre_cr)//log(a))+1
    chiffre='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(nombre_div):
        nombre_cr,r=nombre_cr//a,nombre_cr%a
        nombre=chiffre[r]+nombre
    return nombre           

base_départ=choix_base(0,0)
nombre=choix_du_nombre(base_départ)
base_arrivée=choix_base(9,base_départ)

if base_départ!=10:
    nombre_cr=vers_dix(nombre,base_départ)
else:
    nombre_cr=int(nombre)
if base_arrivée !=10:
    rep=vers_base(nombre_cr,base_arrivée)
else:
    rep=str(nombre_cr)  

print("   ")
print("le nombre",nombre,"écrit en base",base_départ,"s'écrit",rep,"en base",base_arrivée)