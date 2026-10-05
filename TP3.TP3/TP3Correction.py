import random as rd

### Exercice 1

## Question 1

def moyenne(liste):
    somme = 0
    for element in liste:
        somme += element
    return somme / len(liste)

## Question 2
    
def frequence(liste, objet):
    freq=0
    for element in liste:
        if element == objet:
            freq +=1
    return freq / len(liste)

def frenquence_2(liste,objet):
    return liste.count(objet) /len(liste)

### Exercice 2


## Question 1

# On verifie que la moyennemon_randint(1,6) empirique est similaire à la moyenne simulé
# Et on vérifie que tous les éléménet sont entre l'intervalle 0 et 1

L = []

for i in range(1000):
    L.append(rd.random())

print( moyenne(L) )

L_count = []

for element in L:
    if 0<element<1 :
        L_count.append(True)
    else:
        L_count.append(False)

print( False in L_count )

## Question 2

#Pareil avec un interval discret [[a,b]]
a=2
b=6

L = []

for i in range(1000):
    L.append(rd.randint(a,b))

print( moyenne(L) )

L_count = []

for element in L:
    if a<=element<=b :
        L_count.append(True)
    else:
        L_count.append(False)

print( False in L_count )

### Exercice 3

## Question 1

def mon_randint(a,b):
    l=[k for k in range(a,b+1)]
    return l[int(rd.random()*len(l))]

## Question 2

def mon_choice(maliste):
    return maliste[rd.randint(0,len(maliste)-1)]

## Question 3

# Simulation de 1 dé

print(mon_randint(1,6))

print(mon_choice([1,2,3,4,5,6]))

## Question 4

L = [ ]

for i in range(1000):
    L.append(mon_randint(1,6) + mon_randint(1,6))

L_f = []

for i in range(1,13):
    L_f.append( frequence(L,i) )

print(L_f)

### Exercice 4

def selection_point():
    x=rd.random()
    y=rd.random()
    return [x,y]

def pi_montecarlo(N):
    L = []
    for i in range(N):
        l = selection_point()
        if (l[0]**2 + l[1]**2)**0.5 < 1:
            L.append(1)
        else :
            L.append(0)
    return 4 * sum(L) / len(L)
    
print( pi_montecarlo(10000) )

### Exercice 5

## Question 1

def P_ou_F(p):
    x = rd.random()
    if x < p:
        return 1 #Pile
    else: 
        return 0 #Face

def lancers(n,p):
    L =[]
    for i in range(n):
        L.append( P_ou_F(p) )
    return L

## Question 2 

def nb_piles(n,p):
    L = lancers(n,p)
    return sum(L)
    
## Question 3a

def estime_au_moins_un_pile(n,p,nb_essais=10000):
    nb_s = 0
    for i in range(nb_essaie):
        if 1 in lancers(n,p):
            nb_s +=1
    return nb_s / nb_essais
    
## Question 3b






















