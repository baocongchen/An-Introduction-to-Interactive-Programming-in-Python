__author__ = 'Tran'
import random
def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    future = present_value *(1+rate_per_period)**periods
    assert isinstance(future, object)
    return future
print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)

#Project
def name_to_number(name):
    names = ["rock", "Spock", "paper", "lizard", "scissors"]
    if name in names:
        if name == names[0]:
            return 0
        elif name == names[1]:
            return 1
        elif name == names[2]:
            return 2
        elif name == names[3]:
            return 3
        elif name == names[4]:
            return 4
    return 'Out of conversion range'

def number_to_name(number):
    names = ['rock','Spock','paper','lizard','scissors']
    if number == 0:
        return names[0]
    elif number == 1:
        return names[1]
    elif number == 2:
        return names[2]
    elif number == 3:
        return names[3]
    elif number == 4:
        return names[4]
    else:
        return 'Out of conversion range'

def rpsls(player_choice):
    print
    print "Player chooses " + player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses " + comp_choice
    result = comp_number - player_number
    if result == 1 or result == 2:
        return "Computer wins!"
    elif result == 0:
        return "Player and computer tie!"
    else:
        return "Player wins!"

#Project
import simplegui
# define global variables
count = 0
interval = 100
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    if t == 0:
        return "0:00.0"
    elif t > 0 and t < 10:
        return "0:00" + '.' + str(t)[-1]
    elif t > 0 and t < 99:
        return "0:0" + str(t)[:-1] + '.' + str(t)[-1]
    elif t >= 99 and t < 600:
        return "0:" + str(t)[:-1] + '.' + str(t)[-1]
    else:
        minute = (t/10/60)
        if (t/10-minute*60) > 9:
            return str(minute) + ':' + str(t/10-minute*60) + '.' + str(t)[-1]
        else:
            return str(minute) + ':0' + str(t/10-minute*60) + '.' + str(t)[-1]

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global count
    count = count + 1
    timer.start()

def stop():
    timer.stop()

def reset():
    global count
    count = 0

# define event handler for timer with 0.1 sec interval
def event_handler():
    pass
# define draw handler
def draw(canvas):
    canvas.draw_text(str(format(count)), [200, 200], 40, "White")

# create frame
frame = simplegui.create_frame("Stop Watch", 400, 400)

# register event handlers
timer = simplegui.create_timer(interval, start)
frame.add_button('Start', start,50)
frame.add_button('Stop', stop,50)
frame.add_button('Reset', reset,50)
frame.set_draw_handler(draw)
# start frame
frame.start()


#Quiz
def findlast(size):
    listofnumber = [0,1]
    for i in range(size):
        listofnumber.append(listofnumber[-1]+listofnumber[-2]) 
    return listofnumber[-1]

#Quiz
import simplegui

source_center = (220, 100)
source_size = (100, 100)
frame_size = [200, 200]
image_size = [1521, 1818]

def draw(canvas):
    canvas.draw_image(image, source_center,
                      source_size,
                      (frame_size[0] / 2, frame_size[1] / 2),
                      tuple(frame_size))

frame = simplegui.create_frame("test", frame_size[0], frame_size[1])
frame.set_draw_handler(draw)
image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/alphatest.png")

frame.start()


#Project
#Make "Pong" game

# Implementation of classic arcade game Pong
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2];  
    ball_vel = [random.randrange(120, 240), random.randrange(60, 180)]
    if direction == RIGHT:
        ball_vel[1] = -ball_vel[1]
    if direction == LEFT:
        ball_vel[0] = -ball_vel[0]
        ball_vel[1] = -ball_vel[1]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    if score1 >= score2:
        spawn_ball(LEFT)
    else:
        spawn_ball(RIGHT)


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
   
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT-BALL_RADIUS:  
        ball_vel[1] = -ball_vel[1]
   
    if ball_pos[0] <= BALL_RADIUS:  
        if paddle1_pos - HALF_PAD_HEIGHT <= ball_pos[1] and  ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT:  
            ball_vel[0] = -ball_vel[0]  
            ball_vel[0] += ball_vel[0]*0.1  
            ball_vel[1] += ball_vel[1]*0.1  
        else:  
            spawn_ball(RIGHT)  
            score2 += 1  
    elif ball_pos[0] >= WIDTH-BALL_RADIUS:  
        if paddle2_pos - HALF_PAD_HEIGHT <= ball_pos[1] and ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT:  
            ball_vel[0] = -ball_vel[0]  
            ball_vel[0] = ball_vel[0]*1.1  
            ball_vel[1] = ball_vel[1]*1.1  
        else:  
            spawn_ball(LEFT)  
            score1 += 1
        
    ball_pos[0]+=ball_vel[0]/60  
    ball_pos[1]+=ball_vel[1]/60
            
    # draw ball
    canvas.draw_circle(ball_pos, 20, 1, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    if HALF_PAD_HEIGHT <= paddle1_pos + paddle1_vel and paddle1_pos + paddle1_vel <= HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos += paddle1_vel  
    if HALF_PAD_HEIGHT <= paddle2_pos + paddle2_vel and paddle2_pos + paddle2_vel <= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], 
                [HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], 
                PAD_WIDTH, "White")   
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], 
                [WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], 
                PAD_WIDTH, "White")
    
    # draw scores
    canvas.draw_text(str(score1)+"  :  "+str(score2), 
                (WIDTH / 2 - 36, 40), 36, "Blue")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    vel = 5
    if key == simplegui.KEY_MAP['s']:  
        paddle1_vel = vel  
    elif key == simplegui.KEY_MAP['w']:  
        paddle1_vel = -vel  
    elif key == simplegui.KEY_MAP['up']:  
        paddle2_vel = -vel  
    elif key == simplegui.KEY_MAP['down']:  
        paddle2_vel = vel 
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['s']:  
        paddle1_vel = 0  
    elif key == simplegui.KEY_MAP['w']:  
        paddle1_vel = 0  
    elif key == simplegui.KEY_MAP['up']:  
        paddle2_vel = 0  
    elif key == simplegui.KEY_MAP['down']:  
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset", new_game)

# start frame
new_game()
frame.start()



