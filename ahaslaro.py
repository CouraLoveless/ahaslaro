import turtle

wn = turtle.Screen()
wn.title("Ahas Laro")
wn.bgcolor("white")
wn.setup(width=800, height=800)
wn.tracer(0)

#snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"

#main
while True:
    wn.update()

wn.mainloop()

