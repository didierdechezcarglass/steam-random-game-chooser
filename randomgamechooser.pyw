import tkinter as tk
from tkinter import *
from tkinter import simpledialog
from random import randint
import steamfront
import sys

    
def getgame(a,i):
    if a[i] == None : return "random game error, please click on the choose another game button"
    app = a[i]
    try:
        app = client.getApp(appid = app.appid)
    except steamfront.errors.AppNotFound: return "couldn't find the app but the app id is " + app.appid
    app = client.getApp(appid = app.appid)
    if a[i].play_time/60 >= 1:
        if a[i].play_time/60 == 1 or a[i].play_time/60 == 0: syntax = "hour"
        else: syntax = "hours"
        playtime = str(round(a[i].play_time/60,1)) + " " + syntax + " of play!"
    else:
        if a[i].play_time == 1 or a[i].play_time == 0: syntax = "minute"
        else: syntax = "minutes"
        playtime = str(round(a[i].play_time,0)) +" " + syntax + " of play!"
    return app.name + " , " + playtime

def popupmsgg(msg):
    popup = tk.Tk()
    def leavemini():
        popup.destroy()
        sys.exit()
    def getanother():
        label.config(text = getgame(apps,randint(0,len(apps))))
    popup.wm_title("the chosen game is!")
    label = tk.Label(popup,text=msg,font = ("Verdana",12))
    label.pack(side = "top",fill="x",pady = 10)
    b1= tk.Button(popup,text = "ok", command = leavemini)
    b1.pack()
    b2= tk.Button(popup,text = "choose another game", command = getanother)
    b2.pack()
    popup.mainloop()
    
client = steamfront.Client('DC96266ED3CBD75C816769ED78D006A9')
root = tk.Tk()
root.withdraw()
inp = simpledialog.askinteger(title = "id64 grabber",prompt= 'please enter your steam id64\nYour id64 is found on your steam profile url if it is not  a custom url \nCopy the number found after https://steamcommunity.com/id/ \nIf you have a custom url, your id64 can be found on: \nhttps://steamid.io/ \nClicking on cancel will quit the program!')
while True:
    try:
        user = client.getUser(id64 = int(inp))
    except steamfront.errors.UserNotFound:
        inp = simpledialog.askinteger(title = "id64 grabber",prompt= 'error, your id64 was not found, please try again.\nSteam id64 can be found on https://steamid.io/ or on your profile url.\nclicking on cancel will quit the program!')
    except TypeError:
        sys.exit()
    else:
        break
apps = user.apps
game = getgame(apps,randint(0,len(apps) - 1))
popupmsgg(game)
sys.exit()
