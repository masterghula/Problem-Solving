import turtle as t

# this code generates a pre-fractal Koch curve with initiator length Size
# to level k

#set size and level of prefractal

k=4
size =300


# set position and speed of turtle and penwidth

t.hideturtle()
t.penup()
t.goto(-300,-50)
t.pendown()
t.pensize(1)
t.speed(0)

def koch(prefractal, size):

    if prefractal == 0:
        t.forward(size)
    else:

        for angle in [60, -120, 60, 0]:
           koch(prefractal-1, size/3)
           t.left(angle)

for i in range (3):
    koch(k,size)
    t.left(-120)