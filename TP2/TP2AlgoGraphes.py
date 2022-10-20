"Indiquez ici vos nom et prénom :"



#%% Fonctions
def f(x): #La fontion f(x) calcule le cube de x
    return x*x*x
print("Le cube de 3 vaut", f(3))

def somme(n): #La fonction somme(n) donne 0 si n<=0 et la somme des n premiers entiers sinon
    s=0
    for i in range(n+1) : #Boucle faisant varier i de à à n+1 exclu
        s=s+i
    return  s

print("La somme des 5 premiers entiers est :",somme(5))
print("somme(-5) vaut :", somme(-5))

def euclide(a,b): #Une fonction récursive
    if b==0: #Condition d'arrêt
        return a
    else :
        return euclide(b,a%b) #Appel récursif
print("Le pgcd entre",3, "et",6,"vaut" ,euclide(6,9))

# Si la fonction f1 est définie dans un module (programme en Python) nommé prog.py, pour l'utiliser dans un autre module il faudra importer son contenu par # >>>from prog import f1

'''        print(G, N, CN)
        for i in range(len(G)):
            if G[i+1] == {} and i+1 not in CN:
                print("We're going to append this truc")
                N.append(i+1)
                del G[i+1]
            print(N)
        for i in range(len(N)):
            for j in range(len(G)):
                print("G equalds ", G)
                l = G[j+1]
                if N[i] in l:
                    CN.append(j+1)
                    if len(l) <= 1:
                        l = []
                        #print(j+1)
                    else:
                        l.remove(N[i])
                    #print(G)

                    G[j+1].remove(N[i])
                    if len(G[j+1]) == 0:
                        G[j+1] = {}
                    print(G, N[i])
        print("Noyau est égal à ", N, " et compémént à ", CN)
        for i in range(len(CN)):
            for j in range(len(G)):
                l = G[j+1]
                if CN[i] in l:
                    print(CN[i])
                    G[j+1].remove(CN[i])
                    if len(G[j+1]) == 0:
                        G[j+1] = {}
        print("End of cycle")


    m = 0
    #print(sommetNum)#'''

#%% Exercice 1 :

d = dict()
dico = dict()
dico[1] = { 2, 3, 4}
dico[2] = {4}
dico[3] = {4}
dico[4] = {5}
dico[5] = {}
#Graphe orienté sans circuits
#1. Chercher sans sommets sans suc
#Inserer das noyau

#graphe est repsrésenté par le dictionnaire
def Noyau(G):
    N = []

    CN = []
    i = 0
    for i in range(len(G)):
        if G[i+1] == {}:
            N.append(i+1)
    for i in range(len(N)):
        for j in range(len(G)):
            if N[i] in G[j+1]:
                CN.append(j+1)

    for k in list(G.keys()):
        if k in N:
            del G[k]
    print(N, "   ", CN)
    print(G)
    print()
    for i in range(len(CN)):
        for k in list(G.keys()):
            break
            print(CN[i] in G[k])
            if CN[i] in G[k]:
                G[k].remove(CN[i])
        for i in range(len(G)):
            print(CN[i] in G[k])
            if CN[i] in G[k]:
                G[k].remove(CN[i])
        #print(G)
    print(N, "   ", CN)
    #print(G)
    print()



Noyau(dico)





#%% Exercice 2 :

#%% Exercice 3 :

#%% Exercice 4 :

