# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random
import leaderboard as lb
#-----game configuration----
turtleshape = "turtle"
turtlesize = 3
turtlecolor = "blue"

counter_interval = 1000   #1000 represents 1 second
timer_up = False
timer = 20
score = 0
#scoreboard varibles
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list =[]
player_name = input ("please enter your name")

#-----initialize turtle-----
bob = trtl.Turtle(shape=turtleshape)
bob.color(turtlecolor)
bob.shapesize(turtlesize)
bob.speed(50)

score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(-370,270)
score_writer.ht()

font_setup = ("Arial",30,"bold")
score_writer.write(score,font=font_setup)

counter =  trtl.Turtle()
counter.penup()
counter.ht()
counter.goto(300,275)

#-----game functions--------
def turtle_clicked(x,y):
    print ("bob got clicked")
    change_position()
    update_score()
def change_position():
  bob.penup()
  bob.ht()
  if not timer_up:
    bobx = random.randint(-400,400)
    boby = random.randint(-300,300)
    bob.goto(bobx,boby)
    bob.st()



def update_score():
    global score
    score += 1
    print(score)
    score_writer.clear()
    score_writer.write(score,font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score 
  global bob

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, bob, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, bob, score)





#-----events----------------



wn = trtl.Screen()
wn.bgcolor("red")
bob.onclick(turtle_clicked)

wn.ontimer(countdown, counter_interval)
wn.mainloop()