## Exercice 1
# Question 1
# Question 2a
# Question 2b
# Question 3
# Question 4

## Exercice 2
# Question 3
# Question 4
# Question 5
# Question 6
# Question 7
# Question 8
# Question 9

## Exercice 3

from math import sqrt 

# Question 3a

def unTerme(n) :
    u = 2
    for i in range(n) :
        u = sqrt(1 + u**2)
    return u

def unTermeBis(n) :
    if n == 0 :
        return 2
    else :
        return sqrt(1 + unTermeBis(n-1)**2)
      
# Question 3b

def listeDeTermes(n) :
    u = 2
    liste = [u]
    for i in range(n) :
        u = sqrt(1 + u**2)
        liste.append(u)
    return liste
  
# Question 4

def maximum(maliste):
    max=maliste[0]
    for k in range(len(maliste)):
        if max<maliste[k]:
            max=maliste[k]
    return max
  
# Question 5

def estendouble(maliste,objet):
    a=0
    for i in maliste:
        if i == objet:
            a+=1
    if a>=2:
        return True
    return False
  
# Question 6

def yadesdoubles(liste):
    for k in liste:
        if estendouble(liste,k):
            return True
    return False

## Bonus

# Question 1

def pi(n):
    u=1
    v=2
    for i in range(n-1):
         u=(u+v)/2
         v=sqrt(u*v)   
    return sqrt(27)/v

# Question 2



