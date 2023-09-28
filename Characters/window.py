import turtle

class Window:

    def createWindow(title, color, width, height, tracer):
        wn = turtle.Screen() #crea una pantalla
        wn.title("Jueguito de Pong") # titulo
        wn.bgcolor("black") # fondo de la pantalla
        wn.setup(width=800, height=600) #tamanio de la pantalla
        wn.tracer(0) #hace que la pantalla no se actualice

        return wn