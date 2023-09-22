import cv2 as cv 
import numpy as np


#lire l'image
path='photos\\cartetest.png'
img = cv.imread(path)

#afficher l'image
cv.imshow('Carte',img)

# donne la version gris de l'image
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#detecte les lieux dans l'image là ou il y a une grande intensité ou couleur 
canny = cv.Canny(img,125,175)
cv.imshow('Canny Edges',canny)


#detecte les contours existant dans l'image 
contours, hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)

# Crée une image noire de la même taille que l'original
regions = np.zeros_like(gray)

# Dessine les contours sur l'image noire
cv.drawContours(regions, contours, -1, 255, thickness=cv.FILLED)

# Affiche les régions segmentées
cv.imshow('Regions', regions)

#donne le nombre de contours trouvé sur l'image
print(f'{len(contours)} contour(s)found !!')


#####################

# A terminer je n'ai pas toujours trouvé comment colorer la carte avec le theoreme de 4 couleurs 

######################

#pour que l'image ne disparait pas sur le champs
cv.waitKey(0)