import turtle

t = turtle.Turtle()
t.speed(5)

# วงกลมที่ 1
t.circle(50)

# วงกลมที่ 2
t.penup()
t.goto(60, 0)
t.pendown()
t.circle(50)

# วงกลมที่ 3
t.penup()
t.goto(30, 52)
t.pendown()
t.circle(50)

turtle.done()