import time
from progress.bar import Bar,ChargingBar,FillingCirclesBar,FillingSquaresBar
import easygui
import random

usd = 10

def security():
    global usd
    passw = 20240130
    controllpassw = 19911225
    inp = int(easygui.passwordbox("enter password","security",))
    if inp != 00000000:
        if inp == passw or inp == controllpassw:
            if inp == controllpassw:
                if easygui.buttonbox("choose.","sys",choices = ["reset time","exit"]) == "reset time":
                    usd = int(easygui.enterbox("enter times(file system)"))
                else:
                    usd = 10
                    pass
            else:
                pass
        else:
            easygui.msgbox("fuck you , bitch!")
    else:
        easygui.msgbox("please RESTART.  00203900000xx00000")

security()


full_bar = usd

#define bars
easygui.msgbox("Processing, loading files.......","filesys","load more files now")
bar = Bar('Processing:  ', max= full_bar)
bar2 = ChargingBar('Searching files exsistance:  ', max= full_bar) 
bar3 = FillingSquaresBar("Loading files......" , max = full_bar)
bar4 = FillingCirclesBar("GPU accelerating......", max = full_bar)

#show bars
for i in range(full_bar):
   # 执行一些任务
    time.sleep(random.randint(0,1))
    bar2.next()
print(".")
for i in range(full_bar):
    time.sleep(random.randint(0,1))
    bar.next()
print(".")
for i in range(full_bar):
    time.sleep(random.randint(0,1))
    bar4.next()
print(".")
for i in range(full_bar):
    time.sleep(random.randint(0,1))
    bar3.next()

#finishes
bar.finish()
bar2.finish()
bar3.finish()
print("done.")



