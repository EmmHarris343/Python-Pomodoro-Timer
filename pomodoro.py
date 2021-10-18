# This is a Pomodoro timer, 
#!/usr/bin/python3

import time
#import datetime
from datetime import datetime, date, time, timedelta
from tkinter.font import BOLD
from PIL import Image, ImageTk
import PIL.Image

#import Tkinter
import tkinter as tk
from tkinter import *
top = tk.Tk()

counter = 0
active_counter = False
breakTime = False
breakLongTime = False
timeoutTime = False
sessionCounter = 0

global timerSleep



#bgColor = "#F0F0F0" # White
bgColor = "#FCF8DE"
grnButton = "#A6EF4D"
grnButtonH = "#C0f382"
redButton = "#E2574C"
redButtonH = "#E4675d"
orgButton = "#e07719"
orgButtonH = "#ecad75"
gryButton = "#939393"
gryButtonH = "#d3d3d3"

darkGreyColor = "#23272B"





# LAYOUT, COLOURS, BUTTONS, FONTS, DECLARES:
def main():
    global l
    global l_time
    global l_TmtSM1, l_TmtSM2, l_TmtSM3, l_TmtSM4, imgSM, imgSMgry
    global startButton, stopButton
    # Define/ Configure Buttons, Images, Lables etc
    top.title('Pomodoro Timer')
    l = Label(top, text = "Lets Focus Today", width=26, font=('Purisa',18, BOLD), background=bgColor)
    l_time = Label(top, text = "No Timer", width=20, font=('Purisa',17, BOLD), background=bgColor)
    l_rWords = Label(top, text = "Repeat 4 Times\n To get a 25 Min break", width=20, font=('Purisa', 16, BOLD), background=bgColor)
    startButton = Button(top, height=2, width=12, text ="Start Session", command = startBtn, bd=0, padx=0, pady=0, background=grnButton, font=('Times',18), activebackground=grnButtonH)
    rstButton = Button(top, height=2, width=12, text ="Reset Session", command = rstBtn, bd=0, padx=0, pady=0,background=gryButton, font=('Times',18), activebackground=gryButtonH)
    # Image Declare:
    # Curly Bracket:
    imgCurlyI = PhotoImage(file = r"Images/curlybracket.png")
    imgCurly = imgCurlyI.subsample(10, 10)
    l_Curly = Label(top, image = imgCurly, bg=bgColor)

    # Tomatos:
    imgTomato = PhotoImage(file = r"Images/tomatoSM.png")
    imgTomatoGry = PhotoImage(file = r"Images/tomatoSMgry.png")
    imgSMgry = imgTomatoGry.subsample(14, 14)
    imgLG = imgTomato.subsample(8, 8)
    imgSM = imgTomato.subsample(14, 14)
    top.config(background=bgColor)
    l_TmtLG = Label(top, image = imgLG, bg=bgColor)

    # Things
    fRepeat = tk.Frame(top)

    l_TmtSM1 = Label(fRepeat, image=imgSM, bg=bgColor, width=40)
    l_TmtSM2 = Label(fRepeat, image=imgSM, bg=bgColor, width=40)
    l_TmtSM3 = Label(fRepeat, image=imgSM, bg=bgColor, width=40)
    l_TmtSM4 = Label(fRepeat, image=imgSM, bg=bgColor, width=40)

    l_TmtSM1.config(image=imgSMgry)
    l_TmtSM2.config(image=imgSMgry)
    l_TmtSM3.config(image=imgSMgry)
    l_TmtSM4.config(image=imgSMgry)
    # Columns ----> (X)
    # Rows: |
    #       |
    #       |
    #       V (Y)


    #Aligning Through Grid:

    # Lable Status
    l.grid(column=1, row=0, sticky=tk.N, ipadx=25, pady=30, columnspan=2)
    # Lable Time
    l_time.grid(column=1, row=1, sticky=tk.N, ipadx=100, ipady=5, columnspan=2)

    # Button
    startButton.grid(column=1, row=2, sticky=tk.N, ipadx=25, pady=1, columnspan=2)
    rstButton.grid(column=1, row=3, sticky=tk.N, ipadx=25, pady=1, columnspan=2)

    # Images (Tomato)
    # Corner Tomato
    l_TmtLG.grid(column=0, row=0, sticky=tk.NW, padx=1, pady=5)
    
    # Row of Tomatos (The frame of all tomatos)
    fRepeat.grid(column=1, row=4, sticky=tk.N, padx=150, pady=5)
    # Curly Bracket Under Tomatos
    l_Curly.grid(column=1, row=5, sticky=tk.N, ipadx=25, ipady=1, columnspan=2)
    # Text Below Curly Bracket
    l_rWords.grid(column=1, row=6, sticky=tk.N, ipadx=25, pady=0, columnspan=2)

    l_TmtSM1.pack(side="left")
    l_TmtSM2.pack(side="left")
    l_TmtSM3.pack(side="left")
    l_TmtSM4.pack(side="left")

    top.geometry("600x480")
    top.mainloop()
    print("Finished Program Goodbye :3")
    



# Timers:
def focusTimer():
    print("[NOTICE] Focus Timer (Returning Time Remaining) -- CALLED")
    l.config(text = "Started Focus Session")
    global focusSet, focusTime, breakSet, breakTime, breakLongTime, timeoutTime
    focusTime = True
    focusSet = (datetime.now() + timedelta(seconds=20)) 
    # Stop Other Timers:
    breakTime = False
    breakLongTime = False
    timeoutTime = False
# 
def breakTimer():
    print("[NOTICE] BreakTimer (Returning Time Remaining) -- CALLED")
    global breakSet, breakTime, breakLongTime, focusTime, timeoutTime
    # ENABLE  TIMER:
    breakTime = True
    # Set The Timer:
    breakSet = (datetime.now() + timedelta(seconds=5))
    # Stop Other Timers:
    breakLongTime = False
    focusTime = False

# 
def breakTimerLong():
    print("[NOTICE] BreakTimer (Returning Time Remaining) -- CALLED")
    global breakLongSet, breakLongTime, breakTime, focusTime, timeoutTime
    # ENABLE  TIMER:
    breakLongTime = True
    # Set The Timer:
    breakLongSet = (datetime.now() + timedelta(seconds=20))
    # Stop Other Timers:
    focusTime = False
    breakTime = False
# 
def timeoutTimer():
    print("[NOTICE] timeoutTimer (Returning Time Remaining) -- CALLED")
    global timeoutSet, timeoutTime, breakTime, breakLongTime, focusTime
    # ENABLE  TIMER:
    timeoutTime = True
    # Set The Timer:
    timeoutSet = (datetime.now() + timedelta(seconds=10))
    # Stop Other Timers:
    focusTime = False
    startButton.config(text ="Next Session", command = startNxtBtn, bd=0, padx=0, pady=0, background=orgButton, font=('Times',18), activebackground=orgButtonH)

def addTomato():
    if sessionCounter >= 1:
        l_TmtSM1.config(image=imgSM)
    if sessionCounter >= 2:
        l_TmtSM2.config(image=imgSM)
    if sessionCounter >= 3:
        l_TmtSM3.config(image=imgSM)
    if sessionCounter >= 4:
        l_TmtSM4.config(image=imgSM)

# RESET EVERYTHING
def resetTimers():
    print("[NOTICE] Reset Timers - CALLED")
    top.title("Pomodoro Timer - Stopped 0:0")
    l.config(text="Reset, Start New Session")
    l_time.config(text="0:00")
    global active_counter, focusTime, breakTime, breakLongTime, timeoutTime, timerSleep
    l_TmtSM1.config(image=imgSMgry)
    l_TmtSM2.config(image=imgSMgry)
    l_TmtSM3.config(image=imgSMgry)
    l_TmtSM4.config(image=imgSMgry)
    active_counter = False
    focusTime = False
    breakTime = False
    breakLongTime = False
    timeoutTime = False
    l_time.after_cancel(timerSleep)
    startButton.config(text ="Start New Session", command = startBtn, bd=0, padx=0, pady=0, background=grnButton, font=('Times',18), activebackground=grnButtonH)


# Session Has Timed out:
def sessionTimeout():
    print("[NOTICE] Session Timeout - CALLED")
    top.title("Pomodoro Timer - Reset")
    l.config(text="Timeout Reached, All Reset")
    l_time.config(text="0:00")
    global active_counter, focusTime, breakTime, timeoutTime, timerSleep
    l_TmtSM1.config(image=imgSMgry)
    l_TmtSM2.config(image=imgSMgry)
    l_TmtSM3.config(image=imgSMgry)
    l_TmtSM4.config(image=imgSMgry)
    active_counter = False
    focusTime = False
    breakTime = False
    timeoutTime = False
    l_time.after_cancel(timerSleep)
    startButton.config(text ="Start New Session", command = startBtn, bd=0, padx=0, pady=0, background=grnButton, font=('Times',18), activebackground=grnButtonH)


def endBreakLong():
    # This is only called when the break has ended on its own
    print("[NOTICE] End BreakLong- CALLED")
    global breakLongTime
    breakLongTime = False
    l_TmtSM1.config(image=imgSMgry)
    l_TmtSM2.config(image=imgSMgry)
    l_TmtSM3.config(image=imgSMgry)
    l_TmtSM4.config(image=imgSMgry)
    l.config(text = "Long Break Ended; Good Job!")
    l_time.config(text="0:00")
    startButton.config(text ="Begin New Session", command = startBtn, bd=0, padx=0, pady=0, background=grnButton, font=('Times',18), activebackground=grnButtonH)



###
def calcTimePrnt(differnceIn, counterType):
    global active_counter
    statusStr = ""
    remaingTimeStr = ""
    remaingTimeTitleStr = ""

    if counterType == 0: # Focus Mode (Default)
        print("Default Mode : Counter -- TICK TICK")
        if differnceIn.total_seconds() >= 0:
            statusStr = "Focus Session Started"
            diffM = divmod(differnceIn.total_seconds(), 60)
            diffS = diffM[1]
            if differnceIn.total_seconds() >= 60:
                remaingTimeStr = ('%d minutes, %d seconds remaining' % (diffM[0],diffS))
                remaingTimeTitleStr = ('Pomodoro Timer - Focus %d:%d' % (diffM[0],diffS))
            else:
                remaingTimeStr = ('%d seconds remaining' % (diffS))
                remaingTimeTitleStr = ('Pomodoro Timer - Focus %d:%d' % (diffM[0],diffS))
        if differnceIn.total_seconds() <= 0:
            if sessionCounter >= 4:
                breakTimerLong()
            else:
                breakTimer()

    if counterType == 1: # Short Break Mode
        print("Break Mode : Counter -- TICK TICK")
        if differnceIn.total_seconds() >= 0:
            statusStr = "Relax, Break Time"
            bdiffM = divmod(differnceIn.total_seconds(), 60)
            bdiffS = bdiffM[1]
            if differnceIn.total_seconds() >= 60: # Show Minutes and Seconds in Time Str / Title
                remaingTimeStr = ('%d minutes, %d seconds remaining' % (bdiffM[0],bdiffS))
                remaingTimeTitleStr = ('Pomodoro Timer - Break %d:%d' % (bdiffM[0],bdiffS))
            else:
                remaingTimeStr = ('%d seconds remaining' % (bdiffS))
                remaingTimeTitleStr = ('Pomodoro Timer - Break %d:%d' % (bdiffM[0],bdiffS))
        if differnceIn.total_seconds() <= 0:
            timeoutTimer()
    if counterType == 2: # LONG Break Mode
        print("BreakLong Mode : Counter -- TICK TICK")
        if differnceIn.total_seconds() >= 0:
            statusStr = "Congrats Take a Long Break!"
            bdiffM = divmod(differnceIn.total_seconds(), 60)
            bdiffS = bdiffM[1]
            if differnceIn.total_seconds() >= 60: # Show Minutes and Seconds in Time Str / Title
                remaingTimeStr = ('%d minutes, %d seconds remaining' % (bdiffM[0],bdiffS))
                remaingTimeTitleStr = ('Pomodoro Timer - Long Break: %d:%d' % (bdiffM[0],bdiffS))
            else:
                remaingTimeStr = ('%d seconds remaining' % (bdiffS))
                remaingTimeTitleStr = ('Pomodoro Timer - Long Break: %d:%d' % (bdiffM[0],bdiffS))
        if differnceIn.total_seconds() <= 0:
            active_counter = 0
            endBreakLong()


    if counterType == 3: # Timeout Mode
        print("TimeOut Mode : Counter -- TICK TICK")
        if differnceIn.total_seconds() >= 0:
            statusStr = "Timeout Soon; Will Reset in:"
            bdiffM = divmod(differnceIn.total_seconds(), 60)
            bdiffS = bdiffM[1]
            if differnceIn.total_seconds() >= 60: # Show Minutes and Seconds in Time Str / Title
                remaingTimeStr = ('%d minutes, %d seconds remaining' % (bdiffM[0],bdiffS))
                remaingTimeTitleStr = ('Pomodoro Timer - Timeout: %d:%d' % (bdiffM[0],bdiffS))
            else:
                remaingTimeStr = ('%d seconds remaining' % (bdiffS))
                remaingTimeTitleStr = ('Pomodoro Timer - Timeout: %d:%d' % (bdiffM[0],bdiffS))
        if differnceIn.total_seconds() <= 0:
            active_counter = 0
            sessionTimeout()

    if statusStr != "": 
        l.config(text=statusStr)
    if remaingTimeStr != "":
        l_time.config(text=remaingTimeStr)
    if remaingTimeTitleStr != "":
        top.title(remaingTimeTitleStr)
    



  


# Each Tick = 1000 MS (Each Tick is called after 1 Second, Repeatedly unless Active_Counter = FALSE)
def tick():
    if active_counter:
        # If active, after 1000 ms (1 sec) recall yourself (tick)
        global breakSet, breakTime, focusSet, focusTime, timeoutSet, timeoutTime, breakLongSet, breakLongTime, timerSleep
        
        if focusTime == True and breakTime == False and breakLongTime == False and timeoutTime == False:
            difference = (focusSet - datetime.now())
            calcTimePrnt(difference, 0) # Counter type 0 = Default

        if breakTime == True and focusTime == False and breakLongTime == False and timeoutTime == False:
            breakDiff = (breakSet - datetime.now())
            calcTimePrnt(breakDiff, 1) # Counter type 1 = Break

        if breakLongTime == True and focusTime == False and breakTime == False and timeoutTime == False:
            breakLongDiff = (breakLongSet - datetime.now())
            calcTimePrnt(breakLongDiff, 2) # Counter type 2 = Long Break

        if timeoutTime == True:
            timeoutDiff = (timeoutSet - datetime.now())
            calcTimePrnt(timeoutDiff, 3) # Counter type 3 = Timeout

        timerSleep = l_time.after(1000, tick)




def startBtn():
    print("You Pushed The Start Button")
    startButton.config(text ="Pause Session", command = pauseBtn, bd=0, padx=0, pady=0,background=redButton, font=('Times',18), activebackground=redButtonH)
    global active_counter, sessionCounter
    focusTimer() # Star the Focus Timer
    active_counter = 1
    sessionCounter = 1
    addTomato()
    tick()

    # This is a reset, So if you push this button it resets the timer

def startNxtBtn():
    print("You Pushed The Start Next Button")
    startButton.config(text ="Pause Session", command = pauseBtn, bd=0, padx=0, pady=0,background=redButton, font=('Times',18), activebackground=redButtonH)
    global active_counter, sessionCounter, timeoutTime, breakTime, focusTime, timerSleep, breakLongTime
    active_counter = 1
    sessionCounter += 1
    timeoutTime = False
    breakTime = False
    breakLongTime = False
    focusTime = False
    l_time.after_cancel(timerSleep)
    addTomato()
    focusTimer() # Star the Focus Timer
    tick()

def pauseBtn():
    print("You Pushed the Pause Button")

def resumeBtn():
    print("You Pushed the Resume Button")
      
def rstBtn():
    print("You Pushed the Reset Button")
    resetTimers();

if __name__ == "__main__":
    main();