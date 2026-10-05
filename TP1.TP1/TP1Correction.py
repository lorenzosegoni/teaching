### Exercice 1 

## Question 1

def foncDeux(x) :
    if (0 <= x <= 1) or (2 <= x < 5) :
        return 0
    elif 1 < x < 2 :
        return 1
    else :
        return 2

## Question 2-a

# Renvoie True si n est pair et False sinon.

## Question 2-b

print( mafonc(3) )
#False
print( mafonc(2) )
#True
print( type(mafonc(3)) )
#class 'bool

## Question 3

def fonc_Trois(x) :
    if (0 <= x <= 1) or (2 <= x < 5) :
        return True
    else :
        return False

# Variante Rapide

def fonc_Trois(x) :
    return (0 <= x <= 1) or (2 <= x < 5)

## Question 4
print( True + True + False +True )
# 3

print( True * True * False * True )
# 0

# Explication : True = 1 et False = 0


### Exercice 2

## Question 4

def frequence (machaine, carac) :
    nb_occurrences = 0
    for caractere in machaine :
        if caractere == carac :
            nb_occurrences += 1
    return nb_occurrences / len (machaine) #Frequence!

# Variante avec ce que on a vu avant

def frequence (machaine, carac) :
    nb_occurrences = 0
    for caractere in machaine :
        nb_occurrences += (caractere == carac) #True = 1
    return nb_occurrences / len (machaine)

## Question 5

def remplace_TOUS_car(chaine, carac, remplacant) :
    reponse = ''
    for caractere in chaine :
        if caractere == carac :
            reponse += remplacant #Attention au += avec une str
        else :
            reponse += caractere
    return reponse

## Question 6

def remplace_UN_car(chaine, carac, remplacant) :
    reponse = '' #initialisation
    jaipasfini = True #Pour etre sur de modifier que 1
    for caractere in chaine :
        if (caractere == carac) and jaipasfini == True:
            reponse += remplacant
            jaipasfini = False # 1 fois seulment
        else :
            reponse += caractere
    return reponse

#Autre version

def remplace_UN_car(chaine, carac, remplacant) :
    reponse = ''
    for k in range(len(chaine)) :
        if chaine[k] == carac  :
            reponse += remplacant
            reponse += chaine [k+1 :] # Suite de la chaine
            return reponse 
        else :
            reponse += caractere
    return reponse #Important pour donner le résultat final

## Question 7

# On utilise bien le slicing

def es_tu_la(chaine, mot) :
    if mot == '' :
        return True # Cas trivial
    for i in range (0, len(chaine) - len (mot) + 1) : #Attention Range pour eviter erreur
        if chaine[ i : i + len(mot) ] == mot : #Attention bien la longuer!
            return True
    return False

## Question 8

# Version 1 : On utilise le mécanisme d'indexation à l'envers :

def estunpalindrome(machaine) :
    n = len (machaine)
    for i in range(n) :
        if machaine[i] != machaine[-i -1] :
            return False

    return True

# Version 2 : Version 1 mais optimisé

def estunpalindrome(machaine) :
    n = len (machaine)
    for i in range(n // 2) :
        if machaine[i] != machaine[-i -1] :
            return False

    return True

# Version 3 : avec le slicing

# Exemple :
'''
>>> c = "abc"

>>> c[ : : -1]
'cba'
'''

def estunpalindrome(machaine) :
    return machaine == machaine [ : : -1]

## Question 9

# Ici on utilise la fonction .upper()

# Exemple :
'''
>>> "BlaBlA".upper()
'BLABLA'
'''

def estunpalindrome_sans_maj(machaine) :
    return estunpalindrome(machaine.upper())

### Exercice 3 

## Question 3 a

def unTerme(n) :
    u = 2
    for l in range (n) :
        u = (1 + u**2)**(0.5)
    return u
    
#Version Récursive

def unTerme_R(n) :
    if n==0 :
        return 2
    else :
        return (1 + unTerme_R(n-1)**2)**(0.5)

## Question 3 

def listeDeTermes(n) :
    reponse =[]
    for k in range (n+1) :
        reponse.append(unTerme(k))
    return reponse

def listeDeTermes_Version_2(n) :
    reponse =[2]
    for l in range (n) :
        reponse.append( (1 + reponse[-1]**2)**(1/2) ) #On utilise le dernier térme
    return reponse

# Version 2 trés meilleur car éviter de relancer toujours la boucle

## Question 4

def maximum(maliste) :
    reponse = maliste[0]
    for element in maliste [1:] : # pas la peine de reprendre l'élément d'indice 0
        if element > reponse : #comparaison du maximum
            reponse = element
    return reponse

## Question 5

def estendouble(maliste, objet) :
    compteur = 0 # Compteur
    for element in maliste
        if element == objet : 
            compteur += 1
            if compteur == 2 : 
                return True  # dès qu'on atteint 2, on peut quitter la fonction 
    return False

## Question 6

## Version avec le mot clé in

def yadesdoubles_in(maliste) :
    deja_vus  = []
    for element in maliste :
        if element in deja_vus :
            return True
        else :
            deja_vus.append(element)
    return False


 ##autre idée

#sans le mot-clé in

def yadesdoubles(maliste) :
    for i in range (len(maliste)) : #On fixe un élément
        for j in range (i+1, len(maliste)) :  #et on le compare avec les succéssif
            if maliste[j] == maliste [i] :
                return True
    return False
