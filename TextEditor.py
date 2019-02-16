from tkinter import *
from PieChart import Piechart

# Run this file. Type in the name of the file. Then type in the content you want in the file. Click draw pie chart button
#Press quit

def write_file():
    """Creates the text file and the content within it"""
    name = entry1.get()
    text = entry2.get()
    with open(name + ".txt", "w") as f:
        f.write(text)



def create_Pie():
    """Creates a pie chart object and draws the pie chart with its method"""
    test = Piechart(entry1.get())
    test.drawPie()


root = Tk()
Label(root, text="Name of file").grid(row=0)
Label(root, text="Text in file").grid(row=1)

entry1 = Entry(root)
entry2 = Entry(root)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

Button(root, text='Create File', command=write_file).grid(row=3, column=0, sticky=W, pady=4)
Button(root, text='Create Pie Chart', command=create_Pie).grid(row=3, column=1, sticky=W, pady=4)
Button(root, text='Quit', command=root.quit).grid(row=3, column=4, sticky=W, pady=4)

mainloop()
