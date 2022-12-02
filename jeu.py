import pyxel


pyxel.init(128, 128, title="Nuit du c0de")


vaisseau_x = 45
vaisseau_y = 100

def vaisseau_deplacement(x, y):
    """déplacement avec les touches de directions"""

    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 120) :
            x = x + 1
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 0) :
            x = x - 1
   
    return x, y




    global vaisseau_x, vaisseau_y

    # mise à jour de la position du vaisseau
    vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)
    
    platform_x = 180
platform_y = 260
platform_velocity = 10
platform_color = 5
platform_sideWidth = 30
platform_width = 50
platform_height = 15

# variables linked to the ball 
ball_x = screen_width / 2
ball_y = screen_height / 2
ball_totalVelocity = 5
ball_velocity_x = (- ball_totalVelocity)
ball_velocity_y = (- ball_totalVelocity)
ball_radius = 4
ball_color = 5
ball_run = False



def draw():
    

   
    pyxel.cls(0)

    
    pyxel.rect(vaisseau_x, vaisseau_y, 35, 5, 5)

pyxel.run(update, draw)
