import turtle

class Ball:

    def createBall(speed, shape, color, coords, dx, dy):
        ball = turtle.Turtle()
        ball.speed(speed)
        ball.shape(shape)
        ball.color(color)
        ball.penup()
        ball.goto(coords[0], coords[1])
        ball.dx = dx #movimiento X
        ball.dy = dy #movimiento Y

        return ball
