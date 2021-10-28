# ------------- Introduction -------------

# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2020C
# Assignment: 1
# Author: Nguyen Anh Duy (s3878141)
# Created date: 09/12/2020
# Last modified date: 13/12/2020

# ------------- Setup -------------

# import modules
import turtle  # to draw the clock
import time    # to draw the time, write the time string and create a delay for drawing the clock
from datetime import datetime  # to get the current date and current time

# initialise the screen
window = turtle.Screen()
window.setup(1100, 800)
window.tracer(0)  # use to delete any animation that the turtle creates below

# initialise the turtle for drawing the clock
clock_pen = turtle.Turtle()
clock_pen.hideturtle()

# ------------- Functions -------------


def move_turtle_pos(turtle_name, x_pos, y_pos):
    """
    move the turtle to a new position
    """
    turtle_name.penup()
    turtle_name.setpos(x_pos, y_pos)
    turtle_name.pendown()


def move_turtle(turtle_name, length):
    """
    move the turtle towards a specific length
    """
    turtle_name.penup()
    turtle_name.fd(length)
    turtle_name.pendown()


def write_number(turtle_name, data):
    """
    font formats for writing the clock numbers
    """
    turtle_name.write(data, move=False, align="center", font=("Arial", 30, "bold"))


def write_string(turtle_name, data):
    """
    font formats for writing the clock string
    """
    turtle_name.write(data, move=False, align="center", font=("Arial", 20, "bold"))


def draw_clock(hour: int, minute: int, second: int):
    """
    The function will draw the clock with the given time
    """
    # initialise the drawing position, radius of the clock and the drawing pen
    start_x_pos = 0
    start_y_pos = 300
    pen_width = 30
    radius = 300

    # draw the clock shape
    color_list = ["#3D3D3D", "#616161", "#C1C1C1"]  # from left to right: grey color from dark to light depth
    for i in range(3):  # 3 colors in the list will be used to decorate the clock
        clock_pen.seth(180)
        clock_pen.pencolor(color_list[i])
        move_turtle_pos(clock_pen, start_x_pos, start_y_pos)
        clock_pen.pensize(pen_width)
        clock_pen.circle(radius)  # draw a circle for the clock shape
        # line 79 to 81: draw another circle with a different color inside the previous circle (decorating only)
        start_y_pos -= 5
        pen_width = pen_width // 2
        radius -= 5

    # draw the 'hour' clock hand
    clock_pen.pensize(7)
    clock_pen.pencolor("black")
    move_turtle_pos(clock_pen, 0, 0)  # move the turtle to the center
    if hour > 12:  # hour is in 24-hour format so the 'if' statement is needed to calculate the right angle
        hour_angle = ((hour - 12) / 12) * 360
    else:
        hour_angle = (hour / 12) * 360  # there are 12 hours so divided by 12, multiplied by 360 to get the angle
    clock_pen.seth(90)
    clock_pen.rt(hour_angle)
    clock_pen.fd(140)  # the 'hour' clock hand's length

    # draw the 'minute' clock hand
    clock_pen.pensize(5)
    clock_pen.pencolor("#777777")
    move_turtle_pos(clock_pen, 0, 0)  # move the turtle to the center
    minute_angle = (minute / 60) * 360  # there are 60 minutes so divided by 60, multiplied by 360 to get the angle
    clock_pen.seth(90)
    clock_pen.rt(minute_angle)
    clock_pen.fd(220)  # the 'minute' clock hand's length

    # draw the 'second' clock hand
    clock_pen.pensize(3)
    clock_pen.pencolor("red")
    move_turtle_pos(clock_pen, 0, 0)  # move the turtle to the center
    second_angle = (second / 60) * 360  # there are 60 seconds so divided by 60, multiplied by 360 to get the angle
    clock_pen.seth(90)
    clock_pen.rt(second_angle)
    clock_pen.fd(250)  # the 'second' clock hand's length

    # draw the clock slash
    move_turtle_pos(clock_pen, 0, 0)  # move the turtle to the center
    clock_pen.seth(270)
    clock_pen.pencolor("black")
    for i in range(60):
        if i % 5 == 0:
            clock_pen.pensize(5)  # there are 12 hours so the slashes for 'hour' will be darker
        else:
            clock_pen.pensize(1)  # the slashes for 'second' will be lighter
        move_turtle(clock_pen, 270)
        clock_pen.fd(15)
        move_turtle_pos(clock_pen, 0, 0)
        clock_pen.rt(6)

    # draw the clock number
    clock_pen.pencolor("black")
    move_turtle_pos(clock_pen, 0, 0)
    clock_pen.seth(60)  # the turtle will write number 1 first
    clock_pen.pensize(2)
    for i in range(12):
        # line 134 - 143: align the numbers on the clock
        if 0 < i < 9:
            if 2 < i < 8:
                if i in [4, 5, 6]:
                    move_turtle(clock_pen, 260)
                else:
                    move_turtle(clock_pen, 255)
            else:
                move_turtle(clock_pen, 245)
        else:
            move_turtle(clock_pen, 230)
        write_number(clock_pen, str(i + 1))  # write the numbers from 1 to 12 on the clock
        move_turtle_pos(clock_pen, 0, 0)  # move the turtle to the center
        clock_pen.rt(30)  # there are 12 hours, 360 / 12 = 30 so the angle here is 30 degrees


def get_countdown_time(first_date: datetime, last_date: datetime):
    """
    :assumption: first_date will be the current date, last_date will be the 'New Year' date
    :return: the countdown time until New Year or the celebration string when it has reached/passed New Year.
    """
    if last_date <= first_date:  # if today is 'New Year' day or that day has passed --> output a celebration string
        output_string = "There are 0 day, 0 hour, 0 minute, 0 second left. Happy New Year!"
    else:  # if it is not New Year yet --> output countdown time
        time_remaining = last_date - first_date
        day_left = time_remaining.days
        hour = datetime.now().hour  # get the current hour in 24-hour format
        minute = datetime.now().minute  # get the current minute
        second = datetime.now().second  # get the current second
        hour_left = 23 - hour
        min_left = 59 - minute
        sec_left = 60 - second
        output_string = "There are {} day, {} hour, {} minute, {} second left to New Year".format(
            day_left, hour_left, min_left, sec_left)  # produce a countdown string
    return output_string


# ------------- Main program -------------

# update the clock and the countdown for every second
while True:
    curr_hour = datetime.now().hour  # get the current hour in 24-hour format
    curr_min = datetime.now().minute  # get the current minute
    curr_sec = datetime.now().second  # get the current second
    draw_clock(curr_hour, curr_min, curr_sec)  # drawing the clock

    # write the current time and the countdown under the clock
    clock_pen.pencolor("green")
    new_year = datetime(2021, 1, 1, 0, 0, 0)
    curr_date = datetime.now()
    curr_time_string = "Current time is {}. ".format(time.strftime("%Y-%m-%d %T"))
    countdown_string = get_countdown_time(curr_date, new_year)
    move_turtle_pos(clock_pen, 0, -370)  # move turtle to the position for writing the time
    write_string(clock_pen, curr_time_string + countdown_string)
    window.update()  # finish clearing the animation above
    time.sleep(0.77)  # delay for drawing the clock (the 'second' clock hand) at the best accuracy as possible
    clock_pen.clear()  # clear the previous clock to draw another clock after updating the time
