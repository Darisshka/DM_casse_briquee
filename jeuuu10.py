import pyxel
import random
# taille de la fenetre 128x128 pixels

pyxel.init(128, 128, title="Casse_Brique")

# settings vaisseau 

vaisseau_x = 50
vaisseau_y = 110

#settings balle
balle_x = 63
balle_y = 106
deplacement_vertical = 1
deplacement_horizontal = random.randint(-1,1)
balle_velocity_x = 1
balle_velocity_y = -1


#briques


#vies et score
score = 0
vies = 3
win = True

def vaisseau_deplacement(x, y):
    """déplacement avec les touches de directions"""
    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 92) :
            x = x + 6
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 10) :
            x = x - 6

 
    
    return x, y

def balle_deplacement(x, y):
    if (x < 128):
        x = x + 1
        y = y - 1
    elif (x == 128):
        if (y > 5):
            x = x - 1
            y = y - 1
    elif (y == 5):
        return x,y
    return x,y
    

# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y, balle_x, balle_y, deplacement_vertical, deplacement_horizontal

    # mise à jour de la position du vaisseau
    vaisseau_x, vaisseau_y, = vaisseau_deplacement(vaisseau_x, vaisseau_y)
    balle_deplacement_x, balle_deplacement_y = balle_deplacement(balle_x, balle_y)
    
    balle_y = balle_y + deplacement_vertical
    balle_x = balle_x + deplacement_horizontal
    
   
    
    if (balle_x >= 5 | balle_x <= 125) & (balle_y >= 40 | balle_y <= 44):
        deplacement_vertical = -deplacement_vertical
    if (balle_x >= 5  |  balle_x <= 125) & (balle_y >= 30 | balle_y <= 34):
        deplacement_vertical = -deplacement_vertical
    if (balle_x >= 5  |  balle_x <= 125) & (balle_y >= 20 | balle_y <= 24):
        deplacement_vertical = -deplacement_vertical
    
        
    
    
    
    if balle_x == 128 : 
        deplacement_horizontal = -1
        
    elif balle_x == 0 : 
        deplacement_horizontal = 1
    
    if balle_y + 5 == 128 :
        vies = vies - 1
        balle_y = 64
        balle_x = 64
        deplacement_vertical = 1

        deplacement_horizontal = random.randint(-1,1)

        
    if balle_y == 0 :
        deplacement_vertical = 1
        
    if balle_y == vaisseau_y and vaisseau_x <= balle_x <=vaisseau_x + 32 :
        deplacement_vertical = -1
        
    if vaisseau_y <= balle_y <= vaisseau_y + 16  and vaisseau_x + 32 <= balle_x <=vaisseau_x + 32 + 16 :
        deplacement_vertical = -1
        deplacement_horizontal = random.randint(-1,1)
        
    if vaisseau_y <= balle_y <= vaisseau_y + 16 and vaisseau_x - 14 <= balle_x <= vaisseau_x :
        deplacement_vertical = -1
        deplacement_horizontal = random.randint(-1,1)
        

# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""
    global vaisseau_x, vaisseau_y, balle_x, balle_y,deplacement_vertical,deplacement_horizontal, vies
    if vies > 0:
    # vide la fenetre
       pyxel.cls(0)
    

    # vaisseau et balle
    pyxel.rect(vaisseau_x, vaisseau_y, 25, 8, 6)
    pyxel.tri(vaisseau_x +25, vaisseau_y, vaisseau_x +25, vaisseau_y + 7, vaisseau_x +25 + 7, vaisseau_y + 7,6)
    pyxel.tri(vaisseau_x , vaisseau_y, vaisseau_x , vaisseau_y + 7, vaisseau_x -7, vaisseau_y + 7,6)
    
    pyxel.circ(balle_x, balle_y, 3, 2)
    
    #briques 1
    pyxel.rect(5, 20, 20, 4, 2) 
    pyxel.rect(30, 20, 20, 4, 2)   
    pyxel.rect(55, 20, 20, 4, 2)  
    pyxel.rect(80, 20, 20, 4, 2)
    pyxel.rect(105, 20, 20, 4, 2)
    #briques 2
    pyxel.rect(5, 30, 20, 4, 7) 
    pyxel.rect(30, 30, 20, 4, 7)   
    pyxel.rect(55, 30, 20, 4, 7) 
    pyxel.rect(80, 30, 20, 4, 7) 
    pyxel.rect(105, 30, 20, 4, 7)
    #briques2
    pyxel.rect(5, 40, 20, 4, 10) 
    pyxel.rect(30, 40, 20, 4, 10)   
    pyxel.rect(55, 40, 20, 4, 10) 
    pyxel.rect(80, 40, 20, 4, 10) 
    pyxel.rect(105, 40, 20, 4, 10)
    

if vies == 0:
        pyxel.cls(0)
        pyxel.text(55, 64, "Game Over", 7)
    

       
      
      

pyxel.run(update, draw)
