from turtle import Turtle
from GetFileInfo import getFrequencies
import random


class Piechart:
    """Pie chart object. This object is initialized with the name of the file it is going to read"""
    file_name = ""

    def __init__(self, file_name):
        """Initialized pie chart object with the name of the text file its going to draw"""
        self.file_name = file_name

    def drawPie(self):
        """Used getFrequencies from GetFileInfo.py to obtain the information it needs.
        This function draws the pie chart which shows the probability of each character showing up in a text file."""

        letter_frequencies = getFrequencies(self.file_name)

        COLORS = ['mediumpurple', 'aquamarine1', 'red', 'cyan', 'white', 'blue', 'yellow', 'orange',\
                    'purple', 'pink', 'black', 'violet', 'indigo', 'aliceblue', 'antiquewhite', \
                    'ivory1', 'antiquewhite4', 'aqua', 'green', 'aquamarine2', 'aquamarine4'\
                    , 'brown', 'brown4', 'burlywood','gold1', 'gold2', 'gold3', 'gold4', 'gray' \
                    , 'ivory2', 'ivory3', 'ivory4']

        Circle_Radius = 250
        label_length = Circle_Radius * 1.2
        font_size = 12
        text_font = ("Times", font_size, "bold")

        pie_chart = Turtle()
        pie_chart.penup()
        pie_chart.sety(-Circle_Radius)
        pie_chart.pendown()

        picked_Colors = []
        """Draws the pie chart and colors it"""
        for _, frequencies in letter_frequencies:
            color = random.choice(COLORS)
            while color in picked_Colors:
                color = random.choice(COLORS)
            pie_chart.fillcolor(color)
            picked_Colors.append(color)

            pie_chart.begin_fill()
            pie_chart.circle(Circle_Radius, frequencies * 360)
            position = pie_chart.position()
            pie_chart.goto(0, 0)
            pie_chart.end_fill()
            pie_chart.setposition(position)

        pie_chart.penup()
        pie_chart.sety(-label_length)
        # Show all colors are different
        print(picked_Colors)

        """Labeled each color slice"""
        for label, frequencies in letter_frequencies:
            pie_chart.circle(label_length, frequencies * 360 / 2)
            pie_chart.write(label, align="center", font=text_font)
            pie_chart.circle(label_length, frequencies * 360 / 2)

        pie_chart.hideturtle()





