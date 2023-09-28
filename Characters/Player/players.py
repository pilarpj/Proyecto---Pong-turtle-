import turtle


class Player:

    def __init__(self):
        self.turtle = t = turtle.Turtle()
        t.penup()
        t.color("red")

    def createPlayer(speed, shape, color, cords, shapesize):
        # PLayer 1
        player = turtle.Turtle()
        player.speed(speed) #velocidad de la animacion
        player.shape(shape) #forma
        player.color(color) #color del elemento
        player.penup()
        player.goto(cords[0], cords[1]) #donde empieza en coordenadas
        player.shapesize(stretch_wid=shapesize[0], stretch_len = shapesize[1]) # 5 veces mas alto, 1 de ancho (20x20 pixels por defecto)

        return player
    

    def move_up(self):
        y = self.turtle.ycor() 
        y += 20 #anade 20 pixels a la coordenada Y
        self.turtle.sety(y)
        print('entra')
 



