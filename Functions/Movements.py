'''Clase que define los movimientos del jugador'''


class Movement:

    # Funcion que define el movimiento player1
    def movement_up(player):
        y = player.ycor() 
        y += 20 #anade 20 pixels a la coordenada Y
        player.sety(y)

    def movement_down(player):
        y = player.ycor() 
        y -= 20 #anade 20 pixels a la coordenada Y
        player.sety(y)



    # Funcion que define el movimiento player1
    def player_1_up(player_1):
        y = player_1.ycor() 
        y += 20 #anade 20 pixels a la coordenada Y
        player_1.sety(y)

    def player_1_down(player_1):
        y = player_1.ycor() 
        y -= 20 #anade 20 pixels a la coordenada Y
        player_1.sety(y)


    # Funcion que define el movimiento arriba del player2
    def player_2_up(player_2):
        y = player_2.ycor() 
        y += 20 #anade 20 pixels a la coordenada Y
        player_2.sety(y)

    def player_2_down(player_2):
        y = player_2.ycor() 
        y -= 20 #anade 20 pixels a la coordenada Y
        player_2.sety(y)         

        
