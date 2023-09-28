import turtle
import time
import winsound

from Characters.Player import players
from Characters.Ball import ball
from Characters import window

#Score
score_1 = 0
score_2 = 0

#Crea la pantalla
wn = window.Window.createWindow("Pong by @Boyitopocalipsis", "black", 800, 600, 0)

# Crea los players
player_1 = players.Player.createPlayer(0, "square", "white", [-350,0], [5,1])
player_2 = players.Player.createPlayer(0, "square", "white", [350,0], [5,1])

# Crea la pelota
ball = ball.Ball.createBall(0, 'circle', 'green', [0,0], 2, 2)



# Pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup() #para no hacer una linea cuando se mueva
pen.hideturtle() #ocultarlo
pen.goto(0,260)
pen.write('Jugador1: 0 Jugador2: 0', align='center', font=('Courier',24, 'normal'))



#############
# FUNCIONES #
#############

# Funcion que define el movimiento player1
def player_1_up():
    y = player_1.ycor() 
    y += 20 #anade 20 pixels a la coordenada Y
    player_1.sety(y)

def player_1_down():
    y = player_1.ycor() 
    y -= 20 #anade 20 pixels a la coordenada Y
    player_1.sety(y)


# Funcion que define el movimiento arriba del player2
def player_2_up():
    y = player_2.ycor() 
    y += 20 #anade 20 pixels a la coordenada Y
    player_2.sety(y)

def player_2_down():
    y = player_2.ycor() 
    y -= 20 #anade 20 pixels a la coordenada Y
    player_2.sety(y)         


##########################
# DETECTOR DE MOVIMIENTO #
##########################

# Tecla W llama a la fnc player_1_up al pulsar W
wn.listen()
wn.onkeypress(player_1_up, "w")
wn.onkeypress(player_1_down, "s")

wn.listen()
wn.onkeypress(player_2_up, "Up")
wn.onkeypress(player_2_down, "Down")


################## 
# Main game loop #
##################
while True:
    wn.update()

    # Reduce el tiempo del bucle para que la bola vaya a mayor o menor velocidad
    time.sleep(1/90)
    
    #Movimiento de la pelota
    ball.setx(ball.xcor() + ball.dx) #ball.xcor() devuelve la coordenada X, ball.dx() le sumamos 2 pixels
    ball.sety(ball.ycor() + ball.dy) #ball.ycor() devuelve la coordenada Y, ball.dy() le sumamos 2 pixels

    #Border para que no se salga
    # Coordenada Y arriba, si choca vuelve y suena
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound(r'bounce.wav', winsound.SND_ASYNC)

    # Coordenada Y abajo, si choca vuelve y suena
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound(r'bounce.wav', winsound.SND_ASYNC)
  
    # Coordenada X derecha, debe reiniciarse porque es gol
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1    
        score_1 += 1
        pen.clear()
        pen.write('Jugador1: {} Jugador2: {}'.format(score_1, score_2), align='center', font=('Courier',24, 'normal'))
        

    # Coordenada X izquierda, debe reiniciarse porque es gol
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1  
        score_2 += 1 
        pen.clear()
        pen.write('Jugador1: {} Jugador2: {}'.format(score_1, score_2), align='center', font=('Courier',24, 'normal'))
       

    # Colision de la bola con los players
    # Colision con player 2
    # Si la coordenada X de la pelota (ball.xcor()) es mayor del punto izquierdo del player 2  ( > 330 ) y menor que el punto derecho ( < 340 ) y
    # Si la coordenada Y de la pelota esta entre el lado superior y el lado inferior
    if (ball.xcor() > 330 and ball.xcor() < 350) and (player_2.ycor() + 60 > ball.ycor() > player_2.ycor() - 60):
        ball.dx *= -1
        winsound.PlaySound(r'bounce.wav', winsound.SND_ASYNC)
       

    # Colision con player 1
    if (ball.xcor() < -330  and ball.xcor() > -350) and (player_1.ycor() + 60 > ball.ycor() > player_1.ycor() - 60):
        ball.dx *= -1  
        winsound.PlaySound(r'bounce.wav', winsound.SND_ASYNC)
       
