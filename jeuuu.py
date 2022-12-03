import pyxel

# taille de la fenetre 128x128 pixels

pyxel.init(128, 128, title="Casse_Brique")

# position initiale du vaisseau et de la balle

vaisseau_x = 45
vaisseau_y = 110
balle_x = 63
balle_y = 106
vies = 3

def vaisseau_deplacement(x, y):
    """déplacement avec les touches de directions"""
    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 120) :
            x = x + 1
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 0) :
            x = x - 1

    
    
    return x, y

def balle_deplacement(x, y):
    if (x < 123):
        x = x + 1
        y = y - 1
    elif (x == 124):
        if (y > 5):
            x = x - 1
            y = y - 1
    elif (y == 5):
        return x,y
    return x, y 

# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y, balle_x, balle_y

    # mise à jour de la position du vaisseau
    vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)
    balle_deplacement_x, balle_deplacement_y = balle_deplacement(balle_x, balle_y)
    


# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)
    

    # vaisseau et balle
    pyxel.rect(vaisseau_x, vaisseau_y, 25, 8, 6)
    pyxel.tri(vaisseau_x +25, vaisseau_y, vaisseau_x +25, vaisseau_y + 7, vaisseau_x +25 + 7, vaisseau_y + 7,6)
    pyxel.tri(vaisseau_x , vaisseau_y, vaisseau_x , vaisseau_y + 7, vaisseau_x -7, vaisseau_y + 7,6)
    pyxel.circ(balle_x, balle_y, 3, 2)

pyxel.run(update, draw)

