# Module de fonctions qui calculent une surface
from math import *      

def surface_disque(rayon):
    # cette fonction calcule et renvoie la surface d'un disque
    # paramètre à fournir : le rayon du disque
    return(pi*rayon**2)
    
def surface_carre(arete):
    # cette fonction calcule et renvoie la surface d'un carré
    # paramètre à fournir : l'arête du carré
    return(arete*arete)
    
def surface_rectangle(longueur, largeur):
    # cette fonction calcule et renvoie la surface d'un rectangle
    # paramètres à fournir : la longueur et la largeur du rectangle
    return(longueur*largeur)
    
def surface_triangle(base, hauteur):
    # cette fonction calcule et renvoie la surface d'un triangle
    # paramètres à fournir : la base et la hauteur du triangle
    return(base*hauteur/2)