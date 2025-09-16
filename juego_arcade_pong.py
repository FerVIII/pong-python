"""2. Juego de Arcade Pong 
Reproduce el clásico juego de arcade Pong. Para ello puedes usar el módulo "turtle" para 
crear los componentes del juego y detectar las colisiones de la pelota con las paletas de los 
jugadores. También puedes definir una serie de asignaciones de teclas para establecer los 
controles del usuario para las paletas de los jugadores izquierda y derecha."""

import turtle

# Configuración de la ventana del juego
wn = turtle.Screen()
wn.title("Pong - Juego Arcade Clásico")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paleta izquierda (clásica)
paleta_izq = turtle.Turtle()
paleta_izq.speed(0)
paleta_izq.shape("square")
paleta_izq.color("green")
paleta_izq.shapesize(stretch_wid=6, stretch_len=1)
paleta_izq.penup()
paleta_izq.goto(-350, 0)

# Paleta derecha (clásica)
paleta_der = turtle.Turtle()
paleta_der.speed(0)
paleta_der.shape("square")
paleta_der.color("blue")
paleta_der.shapesize(stretch_wid=6, stretch_len=1)
paleta_der.penup()
paleta_der.goto(350, 0)

# Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.color("orange")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 0.2
pelota.dy = 0.2

# Marcador
score_izq = 0
score_der = 0

marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("yellow")
marcador.penup()
marcador.hideturtle()
marcador.goto(0, 260)
marcador.write("Jugador Izq: 0  Jugador Der: 0", align="center", font=("Courier", 24, "normal"))

# Dibuja la línea central (red)
red = turtle.Turtle()
red.color("white")
red.hideturtle()
red.penup()
red.goto(0, 300)
red.setheading(-90)
red.pensize(3)
for _ in range(25):
    red.pendown()
    red.forward(12)
    red.penup()
    red.forward(12)

# Funciones para mover las paletas
def paleta_izq_arriba():
    y = paleta_izq.ycor()
    if y < 250:
        paleta_izq.sety(y + 30)

def paleta_izq_abajo():
    y = paleta_izq.ycor()
    if y > -250:
        paleta_izq.sety(y - 30)

def paleta_der_arriba():
    y = paleta_der.ycor()
    if y < 250:
        paleta_der.sety(y + 30)

def paleta_der_abajo():
    y = paleta_der.ycor()
    if y > -250:
        paleta_der.sety(y - 30)

# Asignación de teclas
wn.listen()
wn.onkeypress(paleta_izq_arriba, "w")
wn.onkeypress(paleta_izq_abajo, "s")
wn.onkeypress(paleta_der_arriba, "Up")
wn.onkeypress(paleta_der_abajo, "Down")

# Bucle principal del juego
while True:
    wn.update()

    # Movimiento de la pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    # Colisión con los bordes superior e inferior
    if pelota.ycor() > 290:
        pelota.sety(290)
        pelota.dy *= -1

    if pelota.ycor() < -290:
        pelota.sety(-290)
        pelota.dy *= -1

    # Colisión con el borde derecho (punto para izquierda)
    if pelota.xcor() > 390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        score_izq += 1
        marcador.clear()
        marcador.write(f"Jugador Izq: {score_izq}  Jugador Der: {score_der}", align="center", font=("Courier", 24, "normal"))

    # Colisión con el borde izquierdo (punto para derecha)
    if pelota.xcor() < -390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        score_der += 1
        marcador.clear()
        marcador.write(f"Jugador Izq: {score_izq}  Jugador Der: {score_der}", align="center", font=("Courier", 24, "normal"))

    # Colisión con las paletas
    if (340 < pelota.xcor() < 350) and (paleta_der.ycor() - 60 < pelota.ycor() < paleta_der.ycor() + 60):
        pelota.setx(340)
        pelota.dx *= -1

    if (-350 < pelota.xcor() < -340) and (paleta_izq.ycor() - 60 < pelota.ycor() < paleta_izq.ycor() + 60):
        pelota.setx(-340)
        pelota.dx *= -1

    # Control de velocidad de la pelota
    if score_izq % 5 == 0 and score_izq > 0:
        pelota.dx *= 1.1
        pelota.dy *= 1.1
    if score_der % 5 == 0 and score_der > 0:
        pelota.dx *= 1.1
        pelota.dy *= 1.1
    # Control de la velocidad de actualización de la ventana
    wn.update()

