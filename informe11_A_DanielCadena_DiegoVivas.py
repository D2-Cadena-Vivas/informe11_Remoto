#parteA
#a

import numpy as np

def generador(valor_minimo,valor_maximo):
    a = np.random.randint(valor_minimo,valor_maximo, size=48).reshape(4,12)
    return a

#b

ingresos= generador(100,180)

egresos= generador(60,130)

#c

def imprimir(i):
    print("dimensiones: ", np.ndim(i),"\n")
    print("Bucaramanga  ", i[0])
    print("Floridablanca", i[1])
    print("Giron        ", i[2])
    print("Piedecuesta  ", i[3])
#d

imprimir(ingresos)
print()
imprimir(egresos)

#e

def calculador(A,B) :
    R= A-B
    return R

#f

ganancias=calculador(ingresos,egresos)

print()

#g

def mejor_ciudad(g) :
    suma=0
    cont=-1
    i=-100
    for nivel in g:
        for dato in nivel: 
            suma=suma+dato
            suma1=suma
        if suma != 0 :
            suma=0
            cont=cont+1
        if suma1> i:
            i=suma1
            level=cont
    if level == 0:
        print('Bucaramanga es la mejor ciudad con',i,'millones de ganancia')
    elif level == 1:
        print('Floridablanca es la mejor ciudad con',i,'millones de ganancia')
    elif level == 2:
        print('Giron es la mejor ciudad con',i,'millones de ganancia')
    elif level == 3:
        print('Piedecuesta es la mejor ciudad con',i,'millones de ganancia')


mejor_ciudad(ganancias)

print()

#h

def peor_ciudad(g):
    suma=0
    cont=-1
    i=1000
    for nivel in g:
        for dato in nivel: 
            suma=suma+dato
            suma1=suma
        if suma != 0 :
            suma=0
            cont=cont+1
        if suma1 < i:
            i=suma1
            level=cont
    if level == 0:
        print('Bucaramanga es la peor ciudad con',i,'millones de ganancia')
    elif level == 1:
        print('Floridablanca es la peor ciudad con',i,'millones de ganancia')
    elif level == 2:
        print('Giron es la peor ciudad con',i,'millones de ganancia')
    elif level == 3:
        print('Piedecuesta es la peor ciudad con',i,'millones de ganancia')

peor_ciudad(ganancias)

print()

#i

def mejor_mes(g):
    cont=-1
    for nivel in g:
        cont=cont+1
        if cont == 0:
            mes=0
            cont2=0
            i=-100
            for dato in nivel:
                cont2=cont2+1
                if dato>i :
                    mes=cont2
                    i=dato
            print('el mes ',mes,'de Bucaramanga fue el mejor con',i,'millones de ganancia')
        elif cont== 1:
            mes=0
            i=-100
            cont2=0
            for dato in nivel:
                cont2=cont2+1
                if dato>i :
                    mes=cont2
                    i=dato
            print('el mes ',mes,'de Floridablanca fue el mejor con',i,'millones de ganancia')
        elif cont== 2:
            mes=0
            i=-100
            cont2=0
            for dato in nivel:
                cont2=cont2+1
                if dato>i :
                    mes=cont2
                    i=dato
            print('el mes ',mes,'de Giron fue el mejor con',i,'millones de ganancia')
        elif cont== 3:
            mes=0
            i=-100
            cont2=0
            for dato in nivel:
                cont2=cont2+1
                if dato>i :
                    mes=cont2
                    i=dato
            print('el mes ',mes,'de Piedecuesta fue el mejor con',i,'millones de ganancia')


mejor_mes(ganancias)
