
#c'est la fonction principale du programme qui va colorer le graphe
#elle prend en parametre un graphe 
def colorer_graphe(graphe):
    
    #################PHASE INITIALISATION ###################
    # Dictionnaire pour stocker la couleur attribuée à chaque sommet
    couleurs = {} 
    # Dictionnaire pour suivre les couleurs restantes disponibles pour chacun des sommet
    disponibles = {}  
    
   ####################PHASE ITERATION ################
    for sommet in graphe:
        #Initialiser toutes les couleurs à None puisque le graphe n'est pas encore colorié
        couleurs[sommet] = None
        #Initialiser nos 4 couleurs possibles
        disponibles[sommet] = {1, 2, 3, 4}

    # Parcourir tous les sommets
    for sommet in graphe:
        #Stocker les voisins de chaque sommet 
        voisins = graphe[sommet]

        # Parcourir les voisins du sommet
        for voisin in voisins:
            #si le voisin a dejà une couleur 
            if couleurs[voisin] is not None:
                #on supprime cette couleur des couleurs disponibles 
                disponibles[sommet].discard(couleurs[voisin])

        # Attribuer la première couleur disponible au sommet
        couleurs[sommet] = next(iter(disponibles[sommet]))
        
    #apres parcours du graphe chaque sommet à une couleur attribué 
    ##################PHASE RETOUR DE SOLUTION##################
    return couleurs


#EXEMPLE DE TEST DU PROGRAMME : 
graphe = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['A', 'B', 'C']
}

resultat = colorer_graphe(graphe)

for sommet, couleur in resultat.items():
    print(f"Sommet {sommet} est coloré avec la couleur {couleur}")