import turtle
import time
import random
import os
import sys

if os.path.exists("highscore.txt"):
   print("Fail exists")
else:
   f = open("highscore.txt", "w")
   f.write("0")
   time.sleep(1)
   

def end():
  if turtle.textinput("Question", "If you want to end type: end") ==  "end":
      sys.exit()
  else:
    turtle.clearscreen()
    main()

def main():
  
  def up():
      if snake.heading() != 270:
          snake.setheading(90)
  def down():
      if snake.heading() != 90:
          snake.setheading(270)
  def left():
      if snake.heading() != 0:
          snake.setheading(180)
  def right():
      if snake.heading() != 180:
          snake.setheading(0)

  def move():
      if snake.heading() == 90:
          y = snake.ycor()
          snake.sety(y+20)
      if snake.heading() == 270:
          y = snake.ycor()
          snake.sety(y-20)
      if snake.heading() == 180:
          x = snake.xcor()
          snake.setx(x-20)
      if snake.heading() == 0:
          x = snake.xcor()
          snake.setx(x+20)

  cscore = 0
  delay = 0.1

  f = open("highscore.txt", "r")
  high_score = int(f.read())

  g = high_score

  screen = turtle.Screen()
  screen.setup(width=600, height=600)
  screen.tracer(0)

  snake = turtle.Turtle()
  snake.speed(0)
  snake.shape('square')
  snake.color("black")
  snake.penup()
  snake.goto(0, 0)
  snake.direction = 'stop'

  food = turtle.Turtle()
  food.speed(0)
  food.shape('square')
  food.color("red")
  food.penup()
  food.goto(0, 100)

  score = turtle.Turtle()
  score.speed(0)
  score.shape('square')
  score.color("black")
  score.penup()
  score.hideturtle()
  score.goto(0, 260)
  score.write("Score: 0 High score: {}".format(high_score), align = 'center', font=("family", 24, "normal"))

  bodies = []

  screen.listen()

  screen.onkeypress(up, "Up")
  screen.onkeypress(down, "Down")
  screen.onkeypress(left, "Left")
  screen.onkeypress(right, "Right")

  while True:
    screen.update()

    if snake.xcor() > 290 or snake.ycor() > 290 or snake.xcor() < -290 or snake.ycor() < -290:

      for body in bodies:
        body.goto(400, 400)
      bodies.clear()
      if g < cscore:
          f = open("highscore.txt", "w")
          f.write(str(cscore))
          f.close()
      cscore = 0
      delay = 0.1

      # score.clear
      # score.write("Score: {} High score: {}".format(cscore, high_score), align="center", font=("ds_digital", 24, "normal"))
      
      end()

    if snake.distance(food) <= 20:
      x = random.randint(-290, 290)
      y = random.randint(-290, 290)
      food.goto(x, y)

      new_body = turtle.Turtle()
      new_body.speed(0)
      new_body.shape("square")
      new_body.color("black")
      new_body.penup()
      bodies.append(new_body)

      delay = delay - 0.002
      cscore += 1

      if cscore >= high_score:
        high_score = cscore
      score.clear()
      score.write("Score: {} High score: {}".format(cscore, high_score), align = 'center', font=("ds_digital", 24, "normal"))

    for i in range(len(bodies)-1,0,-1):
      x = bodies[i-1].xcor()
      y = bodies[i-1].ycor()
      bodies[i].goto(x,y)

    if len(bodies) > 0:
      x = snake.xcor()
      y = snake.ycor()
      bodies[0].goto(x, y)
    move()

    for body in bodies:
      if body.distance(snake) < 20:
        time.sleep(1)
        snake.goto(0, 0)
        snake.heading()

        for body in bodies:
          body.goto(400,400)
        bodies.clear()
        if g < cscore:
          f = open("highscore.txt", "w")
          f.write(str(cscore))
          f.close()
        cscore = 0
        delay  = 0.1
        score.clear()
        score.write("Score: {} High score: {}".format(cscore, high_score), align = 'center', font=("ds_digital", 24, "normal"))
        
        end()
    time.sleep(delay)
  screen.mainloop()
main()