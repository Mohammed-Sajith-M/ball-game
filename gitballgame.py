import turtle

a=0
b=0

win=turtle.Screen()

win.setup(800,600)
win.bgcolor("red")
win.title("game")
win.tracer(0)

#left

left=turtle.Turtle()
left.shape("square")
left.color("white")
left.shapesize(stretch_wid=5,stretch_len=1)
left.penup()
left.speed()
left.goto(-380,0)

#right

right=turtle.Turtle()
right.shape("square")
right.color("white")
right.shapesize(stretch_wid=5,stretch_len=1)
right.penup()
right.speed()
right.goto(380,0)

#ball

ball=turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.speed(2)
ball.dx = 0.5
ball.dy = 0.5

#score display

score = turtle.Turtle()
score.penup()
score.goto(0,260)
score.write("player A : 0 player B : 0",font=("Arial",26),align="center")
score.hideturtle()

#moving

def left_up():

    left.sety(left.ycor() + 20)

def left_down():

    left.sety(left.ycor() - 20)

def right_up():

    right.sety(right.ycor() + 20)

def right_down():

    right.sety(right.ycor() - 20)

win.listen()

win.onkeypress(left_up,'w')
win.onkeypress(left_down,'s')
win.onkeypress(right_up,'Up')
win.onkeypress(right_down,'Down')

while(True):

    win.update()

    #ball moving

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    
    #ball top

    if(ball.ycor() > 290):
        
        ball.dy = -0.5

    #ball bottom

    if(ball.ycor() < -290):
        
        ball.dy = 0.5

    #ball right

    if(ball.xcor() > 390):

        ball.dx = -0.5

        a = a + 1


        score.clear()
         
        score.write("player A : {} player B : {}".format(a,b),font=("Arial"),align="center")        

    #ball left

    if( ball.xcor() < -390):
        
         ball.dx = 0.5

         b = b+1

         score.clear()
         
         score.write("player A : {} player B : {}".format(a,b),font=("Arail"),align="center")

    #collision right

    if(ball.xcor()>360 and ball.ycor() < (right.ycor()+50) and ball.ycor()>(right.ycor()-50)):
        
        ball.dx = -0.5

    #collision left
        
    if(ball.xcor()<-360 and ball.ycor() < (left.ycor()+50) and ball.ycor()>(left.ycor()-50)):
        
        ball.dx = 0.5

    if(a==10 or b==10):

        win.bgcolor("blue")

        end = turtle.Turtle()

        if(a==10):

            end.color("yellow")
            end.write("player A is win",align = "center",font=("Arial",26))
            break

        else:

            end.color("yellow")
            end.write("player B is win",align = "center",font=("Arial",26))
            break