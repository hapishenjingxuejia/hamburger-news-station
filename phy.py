import easygui #for guis
import time #for time factoring
import random #get random numbers
#importings

#hello
easygui.msgbox("helo from the ISW!")

#variable
in_a = 0
in_b = 0

#define function
def ms():
    global in_a,in_b
    in_a = easygui.enterbox("enter number")
    in_ai = float(in_a)
    in_b = in_ai * 3.6
    easygui.msgbox("the answer is " + str(in_b) + " km/h","sys")

def kmh():
    global in_a,in_b
    in_a = easygui.enterbox("enter number")
    in_ai = float(in_a)
    if in_ai != 0:
        in_b = in_ai / 3.6
        easygui.msgbox("the answer is " + str(in_b) + " m/s","sys")

    elif in_ai == 0:
        easygui.msgbox("the number is invaliad")
    else:
        easygui.msgbox("the thing you have put in here is not reconizeable. PLEASE RESTART.")
    pass


#choice helper
inputn = easygui.buttonbox("enter what you want","sys",choices = ["m/s -> km/h","km/h -> m/s"])
if inputn == "m/s -> km/h":
    ms()
if inputn == "km/h -> m/s":
    kmh()
