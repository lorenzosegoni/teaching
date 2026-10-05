### Exercice 1

## Question 1a

'''
#La fonction mystere(parametre) calcule et renvoie la valeur minimale présente dans la LISTE parametre.
'''

## Question &b

def indice_minimum(maliste):
    ind_min = 0
    for i in range(1, len(maliste)):
        if maliste[i] < maliste[ind_min]: 
            ind_min = i
    return ind_min

## Question 2a

def est_triangulaire(n):
    k = 1  # Entier courant que l'on additionne
    S = 1  # Somme cumulée 1 + ... + k
    while S < n:
        k += 1
        S += k
    return S == n

## Question 2b

def est_palindrome(n):
    s = str(n)
    for i in range(len(s) // 2): # Attention // 2
        if s[i] != s[len(s) - 1 - i]: # Ici c'est mieux de reflechir avec les differences !
            return False
    return True
  
## Question 2c

# On fait un hybride entre les deux fonction d'avant

def dix_premiers_triangulaires_palindromes():
    resultats = []
    k = 1
    S = 1
    while len(resultats) < 10:
        if est_palindrome(S):
            resultats.append(S)
        k += 1
        S += k
    return resultats


## Question 3a

def liste_des_mots(maphrase) :
  reponse = []
  mot_suivant = ""
  
  for char in maphrase :
    if char != " " :
      mot_suivant += char
    else :
      if mot_suivant != "" :
        reponse.append(mot_suivant)
        mot_suivant = ""
  if mot_suivant != "" :
    reponse.append(mot_suivant)
  return reponse


def liste_des_mots_2(maphrase) :
  reponse = []
  k = 0 # Cette variable va explorer les indices des caractères de maphrase
  indice_debut_mot = 0 # Cette variable contiendra l’indice du début de mot
  while k < len(maphrase) :
    while (k < len(maphrase) ) and (maphrase[k] != " ") :
      k += 1
    
    nouveau_mot = maphrase[indice_debut_mot:k]
    
    if nouveau_mot != ’’ :
      reponse.append(nouveau_mot)
    
    indice_debut_mot = k+1
    k += 1
  return reponse

## Question 3b

def mot_y_es_tu(maphrase, monmot):
    mots = liste_des_mots(maphrase)
    for m in mots:
        if m == monmot:
            return True
    return False

## Question 3c

def mot_y_es_tu_II(maphrase,monmot) :
  reponse = []
  la_liste_des_mots = liste_des_mots(maphrase)

  for indice_mot in range(len(la_liste_des_mots)) :
    if la_liste_des_mots [indice_mot] == monmot :
      reponse.append(indice_mot)
  return reponse

# Question 4 : Résolution par dichotomie

# Ici je simplifie la fonciton avec des min et des max

def dichotomie(f, a, b, epsilon):

    gauche = min(a, b)
    droite = max(a, b)
    
    while (droite - gauche) > epsilon:
        milieu = (gauche + droite) / 2.0
        if f(gauche) * f(milieu) <= 0:
            droite = milieu
        else:
            gauche = milieu
    return (gauche + droite) / 2.0

# Question 5a

def diviseurs_propres_for(n):
    divs = []
    for k in range(1, n): # On prend pas 0 pour eviter problemes
        if n % k == 0:
            divs.append(k)
    return divs

def diviseurs_propres_while(n):
    divs = []
    k = 1
    while k < n:
        if n % k == 0:
            divs.append(k)
        k += 1
    return divs

# La version avec boucle for est généralement préférable ici car le nombre d'itérations est fini et connu à l'avance.

# Question 5b

parfaits = []
candidat = 2
while len(parfaits) < 4:
  somme_divs = sum(diviseurs_propres_for(candidat))
  if somme_divs == candidat:
    parfaits.append(candidat)
  candidat += 1
  
print(parfaits)
