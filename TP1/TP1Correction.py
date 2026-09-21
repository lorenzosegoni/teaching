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


### Exercice 3

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

'''
Principe :
On strocke le nombre de lettre du mot recherché puis, à l'aide du slicing, on fait glisser une fenêtre de cette taille sur la (grande) chaîne. Si à un moment cette fenêtre

Notons qu'on a donc besoin de boucler sur les indices des caractères de la chaîne, et non sur leurs valeurs.
'''

def es_tu_la(chaine, mot) :

    # On commence par traiter le cas trivial :
    if mot == '' :
        return True

    # En effet, si le mot à chercher est vide, la fonction devrait toujours renvoyer True. Même si la chaie est vide ! Or ce qui suit renverrait False avec uen chaîen vide... Autant commencer par traiter le cas trivial à part !

    # Sinon, on applique l'idée :

    longueur_mot = len(mot)



    # on va faire boucler i de 0 jusqu'à len(chaine) - len(mot)
    # Ca ne sert à rien de regarder les tous derniers caractères
    # formant une chaine trop petite pour être égale à 'mot'

    # Attention, ne pas oublier le "+ 1" dans le range

    for i in range (0, len(chaine) - len (mot) + 1) :
        if chaine[ i : i + len(mot) ] == mot :
            return True
            # Si on trouve une occurrence du mot, on peut (et doit)  renvoyer True. Ce return est donc dans la boucle.

    return False

    # Il faut avoir éclusé toutes les possibilités (sans trouver le mot) pour renvoyer ce False : ce return est donc APRES la boucle

    # Il faut bien comprendre cette dissymétrie entre les return

## Question 8

# Version 1 : On utilise le mécanisme d'indexation à l'envers des caractères d'une chaîne :

'''
machaine[-1] est le dernier caractère, machaine[-2] l'avant-dernier, etc.
Aisni, pour i>= 0, machaine [i] est le i+1 ° caractère en partant de la gauche
et machaine [-i-1] est le i+1 ° caractère en partant de la droite (le symétrique du précédent donc)

On doit donc vérifier si pour tout i dans [0, len(machaine) -1 ], on a machaine [i] = machaine [-i-1]
Dès que c'est faux, on peut s'arrêter et renvoyer False
Si ce n'est jamais faux , c'est que 'machaine' est un palaindrome, et on peut renvoyer True

Comprenez-vous bien pourquoi le 'return False' est DANS la boucle alors que le 'return True' est APRES la boucle ?
'''

def estunpalindrome(machaine) :
    n = len (machaine)
    for i in range(n) :
        if machaine[i] != machaine[-i -1] :
            return False

    return True

# Version 2 : Pareil, mais en faisant une boucle deux fois plus petite : il suffit de regarder les indices jusqu'à n // 2 (les vérifications suivantes sont redondantes)

# Notez bien l'usage de '//' et non de '/'. Clair ?

def estunpalindrome(machaine) :
    n = len (machaine)
    for i in range(n // 2) :
        if machaine[i] != machaine[-i -1] :
            return False

    return True

# Version 3 : EN utilisant le slicing de manière subtile, grâce au fait qu'on peut spécifier un pas lorsqu'on "slice" (voir le poly) et ce pas peut être négatif, entraînant la lecture de la chaîen à rebours.

# En particulier, la syntaxe machaine [ : : -1] renvoie une copie de ma_chaine à l'envers !

# Exemple :
'''
>>> c = "abc"

>>> c[ : : -1]
'cba'
'''

def estunpalindrome(machaine) :
    return machaine == machaine [ : : -1]


## Question 9

# C'est l'occasion d'utiliser la 'méthode' .upper() des chaînes de caractères qui transforme une chaîen en la même, mais avec toutes lettres en majuscules

# Voir le paragraphe 4.4.4 du cours

# Exemple :
'''
>>> "BlaBlA".upper()
'BLABLA'
'''

# On va donc appliquer la fonction de la question précédente, mais en commençant par mettre toutes les lettres en majuscules :

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