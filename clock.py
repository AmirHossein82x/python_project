from tkinter import *
from time import *

def update():
    time_string = strftime('%I:%M:%S %p')  # return urrent time
    time_label.config(text=time_string)

    day_string = strftime('%A')  
    day_label.config(text=day_string)

    date_string = strftime('%B %d, %Y')  
    date_label.config(text=date_string)

    #time_label.after(1000, update) # after 1000 mili second , updte function will perform again
    window.after(1000, update)

window = Tk()

time_label = Label(window, font=('Arial', 50), fg='#00FF00', bg='black')
time_label.pack()

day_label = Label(window, font=('Ink Free', 50))
day_label.pack()

date_label = Label(window, font=('Ink Free', 30))
date_label.pack()

update()

window.mainloop()