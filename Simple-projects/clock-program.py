# CLOCK PROGRAM IN PYTHON USING TKINTER

from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000,update)


window = Tk()

window.title('Simple Clock App')

time_label = Label(window,font=("Arial",50),fg="#00FF00",bg="black")
time_label.pack()

day_label = Label(window,font=("Arial",25,"bold"))
day_label.pack()

date_label = Label(window,font=("Arial",30))
date_label.pack()

update()

window.mainloop()


'''

strftime - String Format Time 

Code    Meaning	Example
-----------------------------------------------------------
%Y	    Full year	2026
%y	    Last two digits of year	26
%m	    Month (01–12)	07
%B	    Full month name	July
%b	    Short month name	Jul
%d	    Day of month	19
%A	    Full weekday	Sunday
%a	    Short weekday	Sun
%H	    Hour (24-hour)	16
%I	    Hour (12-hour)	04
%M	    Minutes	45
%S	    Seconds	30
%p	    AM/PM	PM
%f	    Microseconds	123456
%j	    Day of year	200
%U	    Week number (Sunday first)	29
%W	    Week number (Monday first)	28
%w	    Weekday number (Sunday=0)	0
%c	    Complete date and time	Sun Jul 19 16:45:30 2026
%x	    Date representation	07/19/26
%X	    Time representation	16:45:30
%%	    Prints a % sign	%

'''