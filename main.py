import pyautogui
from threading import *
import tkinter
import webbrowser
import time
from random import randrange




root = tkinter.Tk()
root.title("INSTAGRAM FOLLOW AUTOMATION")
root.geometry('500x600')

def threading():
    t1 = Thread(target=update_textbox)
    t2 = Thread(target=clickfollowbutton)
    t3 = Thread(target=clickfollowbuttonwindows)
    t4 = Thread(target=instagrammfollowautomation)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    if t1.start():
        print("t1 has started")

def testthread():
    t5 = Thread(target=showvalue)
    t5.start()

def disableentrythread():
   t6 = Thread(target=disablefield)
   t6.start()

def update_textbox(textbox, data):
    textbox.config(state=tkinter.NORMAL)
    textbox.insert(tkinter.END, "\n"+str(data))
    textbox.config(state=tkinter.DISABLED)
    textbox.see(tkinter.END)


def clickfollowbutton(buttonlocationvar, betweenclicks):
    x = buttonlocationvar[0] / 2
    y = buttonlocationvar[1] / 2
    pyautogui.moveTo(x, y)
    pyautogui.click(x, y, 1)
    update_textbox(statusfield, "Found a Button!")
    time.sleep(int(betweenclicks))


def clickfollowbuttonwindows(buttonlocationvar, betweenclicks):
    x = buttonlocationvar[0]
    y = buttonlocationvar[1]
    pyautogui.moveTo(x, y)
    pyautogui.click(x, y, 1)
    update_textbox(statusfield, "Found a Button!")
    time.sleep(int(betweenclicks))


def instagrammfollowautomation():
    loopstopvar = True
    random = israndom.get()
    if random == 0:
      sleepbetweenclicks = delayInput.get()
    else:
      randomvalue = randrange(4, 14)
      sleepbetweenclicks = randomvalue

    web_url = urlInput.get()
    scroll = scrolldistanceInput.get()
    operationsystem = opsystemInput.get()


    update_textbox(statusfield, "Starting...")
    webbrowser.open(web_url + "/followers")
    update_textbox(statusfield, "Waiting for Site to load... 10sec")
    time.sleep(8)

    followersection = pyautogui.locateOnScreen('search_image/followersection.png')
    clickfollowbutton(followersection, sleepbetweenclicks)

    while loopstopvar is True:
        try:
            update_textbox(statusfield, "Searching for Button1...")
            usericon = pyautogui.locateOnScreen("search_image/this.png")
            if operationsystem == "Mac":
              clickfollowbutton(usericon, sleepbetweenclicks)
            else:
              clickfollowbuttonwindows(usericon, sleepbetweenclicks)
        except:
            # move the mouse left and scroll when check for button again if not found set goOn to False
            pyautogui.moveTo(973, 567)
            scrollInt = int(scroll)
            pyautogui.scroll(-scrollInt)
            update_textbox(statusfield, "Trying to scroll...")
            pyautogui.sleep(int(sleepbetweenclicks))
            try:
                update_textbox(statusfield, "Searching for Button2...")
                usericon2 = pyautogui.locateOnScreen('search_image/this.png')
                if operationsystem == "Mac":
                    clickfollowbutton(usericon2, sleepbetweenclicks)
                else:
                    clickfollowbuttonwindows(usericon2, sleepbetweenclicks)
            except:
                loopstopvar = False
                errormessage = "Error: Button Not Found"

    if errormessage:
        update_textbox(statusfield, errormessage)
    else:
        update_textbox(statusfield, errormessage)


def showvalue():
    random = israndom.get()
    if random == 0:
      sleepbetweenclicks = delayInput.get()
      print(sleepbetweenclicks)
    else:
      randomvalue = randrange(4, 7)
      sleepbetweenclicks = randomvalue
      print("here")
      print(sleepbetweenclicks)


def disablefield():
    if israndom.get() == 1:
        delayInput.configure(state='disabled')
    else:
        delayInput.configure(state='normal')

# ------------------------ GUI ------------------------------------


israndom = tkinter.IntVar()
delayInt = tkinter.IntVar()



description = tkinter.Message(root, text="This is a Application using the Python library 'pyautogui' to automate the process of following the Followers of a specific Instagram account.", width="400")
delayLabel = tkinter.Label(root, text="Verzögerung zwischen Buttonclicks:")
delayInput = tkinter.Entry(root, textvariable=delayInt)
randomdelaycheckbox = tkinter.Checkbutton(root, text="Random(3-10 Sekunden) Empfohlen", variable=israndom, command=disablefield)
urlLabel = tkinter.Label(root, text="URL des Instagram Accounts:")
urlInput = tkinter.Entry(root)
scrollLabel = tkinter.Label(root, text="Scrolldistanz")
scrolldistanceInput = tkinter.Entry(root)
opsystemLabel = tkinter.Label(root, text="Operating System(Mac, Windows, Linux,...)")
opsystemInput = tkinter.Entry(root)
submitbutton = tkinter.Button(root, text="Start", command=threading)
statusfield = tkinter.Text(root, state='disabled')


description.pack()
delayLabel.pack(pady=6)
delayInput.pack(pady=6)
randomdelaycheckbox.pack(pady=6)
urlLabel.pack(pady=6)
urlInput.pack(pady=6)
scrollLabel.pack(pady=6)
scrolldistanceInput.pack(pady=6)
opsystemLabel.pack(pady=6)
opsystemInput.pack(pady=6)
submitbutton.pack(pady=6)
statusfield.pack(padx=50, pady=6)
root.mainloop()

