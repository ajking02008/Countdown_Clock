# ------------- Introduction -------------

# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2020C
# Assignment: 1
# Author: Nguyen Anh Duy (s3878141)
# Created date: 08/12/2020
# Last modified date: 12/12/2020

# ------------- Setup -------------

# import modules
import random  # to create random numbers for a list
import turtle  # to draw a histogram

# initialise the turtle and the screen
window = turtle.Screen()
window.setup(700, 800)
logo = turtle.Turtle()
logo.pensize(3)
logo.hideturtle()

# ------------- Functions -------------


def init_random_list(amount, min_num, max_num):
    """
    return a list of random numbers based on the amount and the given range
    """
    num_list = []
    for i in range(amount):
        mark = random.randint(min_num, max_num)
        num_list.append(mark)
    print(num_list)
    return num_list


def move_turtle_pos(turtle_name, x_pos, y_pos):
    """
    move the turtle to a new position
    """
    turtle_name.penup()
    turtle_name.setpos(x_pos, y_pos)
    turtle_name.pendown()


def write_line(turtle_name, data):
    """
    font formats for writing words and numbers
     """
    turtle_name.write(data, False, "center", ('Arial', 22, ""))


def draw_bar(turtle_name, height):
    """
    draw the bar chart with the given height
    """
    turtle_name.seth(90)
    turtle_name.fillcolor("#2a9df4")
    turtle_name.begin_fill()
    for i in range(2):  # a loop to draw a rectangle (the bar chart)
        turtle_name.fd(height)
        turtle_name.rt(90)
        turtle_name.fd(50)
        turtle_name.rt(90)
    turtle_name.end_fill()


def draw_mark_histogram(grade_list: list):
    """
    :param grade_list: user will input a list of 100 numbers (between 0 and 100)
    :return: a histogram that displays the frequencies of each grade given above
    """

    # create a dictionary to count the quantity for each grade
    result_list = {
        "NN": 0,
        "PA": 0,
        "CR": 0,
        "DI": 0,
        "HD": 0
    }

    # sort out the grade based on the given condition
    for i in range(len(grade_list)):
        mark = grade_list[i]  # create a variable to store the number in that position
        if mark >= 80:
            result_list["HD"] += 1  # increase the count for "HD" by 1
        elif 70 <= mark < 80:
            result_list["DI"] += 1  # increase the count for "DI" by 1
        elif 60 <= mark < 70:
            result_list["CR"] += 1  # increase the count for "CR" by 1
        elif 50 <= mark < 60:
            result_list["PA"] += 1  # increase the count for "PA" by 1
        else:
            result_list["NN"] += 1  # increase the count for "NN" by 1

    # initialise the drawing positions (to use it later for drawing the chart)
    start_x_pos = -200
    start_y_pos = -200

    # draw y-axis (Frequencies)
    logo.seth(90)
    move_turtle_pos(logo, start_x_pos, start_y_pos)  # move the turtle to the first drawing position
    logo.fd(550)  # y-axis length
    move_turtle_pos(logo, -270, 325)  # move turtle to the position for writing the word "Frequencies"
    write_line(logo, "Frequencies")
    # line 109- 110: adjust the positions to write the numbers on the y-axis
    logo.seth(0)
    draw_x_pos = start_x_pos - 30
    draw_y_pos = start_y_pos + 50  # the positions to write the first number: 10
    for i in range(10):
        move_turtle_pos(logo, draw_x_pos, draw_y_pos - 15)  # draw_y_pos - 15 is just to align the numbers on the axis
        write_line(logo, (i+1)*10)  # write the numbers from 10 to 100
        move_turtle_pos(logo, draw_x_pos + 20, draw_y_pos)  # draw the slash on the y-axis
        logo.fd(15)
        draw_y_pos += 50  # move the turtle up to write the next number

    # draw x-axis (Final Grade)
    move_turtle_pos(logo, start_x_pos, start_y_pos)  # move the turtle to the first drawing position
    logo.seth(0)
    logo.fd(400)  # x-axis length
    move_turtle_pos(logo, 0, -270)  # move turtle to the position for writing the word "Final Grade"
    write_line(logo, "Final Grade")
    draw_x_pos = start_x_pos + 75
    draw_y_pos = start_y_pos  # the positions to draw the first grade's bar chart: NN
    for key in result_list.keys():  # return the grade inside the result_list
        move_turtle_pos(logo, draw_x_pos + 25, draw_y_pos - 30)  # alignment for writing the grades on the x-axis
        write_line(logo, key)  # write the grade
        move_turtle_pos(logo, draw_x_pos, draw_y_pos)
        # the height of the bar chart is scaled up 5 times
        draw_bar(logo, result_list[key]*5)
        draw_x_pos += 50  # move the turtle to draw the next bar chart


# ------------- Main program -------------

# create a list of random numbers
draw_list = init_random_list(100, 0, 100)

# draw the histogram based on the list
draw_mark_histogram(draw_list)
window.exitonclick()
