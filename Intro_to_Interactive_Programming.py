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






