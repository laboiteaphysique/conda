import math      

def surface_disque(rayon):
    """
    fonction qui calcule et renvoie la surface du disque
    :param rayon: le rayon du disque
    :type rayon: int ou float
    :return: la surface du disque (unité (au carré) de celle du rayon)
    :rtype: float
    """
    return math.pi*rayon**2
    
def surface_carre(arete):
    """
    fonction qui calcule et renvoie la surface d'un carré
    :param arête: la longueur d'un des côtés du carré
    :type arete: int ou float
    :return: la surface du carré dans l'unité (au carré) de celle d'arete
    :rtype: int ou float
    """
    return arete*arete
    
def surface_rectangle(longueur, largeur):
    """
    fonction qui calcule et renvoie la surface d'un carré
    :param longueur: la longueur du rectangle
    :type longueur: int ou float
    :param largeur: la largeur du rectangle
    :type largeur: int ou float
    :return: la surface du rectangle 
    :rtype: int ou float
    
    :CU: la longueur et la largeur doivent être dans la même unité
    """
    return longueur*largeur
    
def surface_triangle(base, hauteur):
    """
    fonction qui calcule et renvoie la surface d'un triangle
    :param base: la base du triangle
    :type base: int ou float
    :param hauteur: la hauteur du triangle
    :type hauteur: int ou float
    :return: la surface du triangle 
    :rtype: int ou float
    
    :CU: la base et la hauteur doivent être dans la même unité
    """
    return base*hauteur/2