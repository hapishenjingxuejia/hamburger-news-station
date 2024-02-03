import time
import easygui  
  
def convert_seconds(seconds):  
    minutes = seconds // 60  
    remaining_seconds = seconds % 60  
    return f"{minutes}分钟{remaining_seconds}秒"  
  
def countdown_timer(seconds):  
    while seconds > 0:  
        print(convert_seconds(seconds), end="\r")  
        time.sleep(1)  
        seconds -= 1  
    easygui.msgbox("计时结束！","timer.proedition",'ok')
  
# 设置一个5分钟（300秒）的倒计时计时器  
timer_seconds = 5 * 60  
countdown_timer(timer_seconds)