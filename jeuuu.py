import pyxel


pyxel.init(128, 128, title="Nuit du c0de")


vaisseau_x = 45
vaisseau_y = 100
balle_x = 60
balle_y = 80


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
     
    

def update():
    
    global vaisseau_x, vaisseau_y, balle_x, balle_y

    # mise à jour de la position du vaisseau
    vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)
    balle_x, balle_y = balle_deplacement(balle_x, balle_y)
    
  

def draw():
    
  
    pyxel.cls(0)

        pyxel.rect(vaisseau_x, vaisseau_y, 35, 5, 5)
        pyxel.circ(balle_x, balle_y, 2, 3)

pyxel.run(update, draw)


