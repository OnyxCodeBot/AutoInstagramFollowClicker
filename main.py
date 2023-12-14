import pyautogui # Needs to be installed
import webbrowser
import time


def clickfollowbutton(buttonlocationvar, betweenclicks):
    x = buttonlocationvar[0] / 2
    y = buttonlocationvar[1] / 2
    pyautogui.moveTo(x, y)
    pyautogui.click(x, y, 1)
    time.sleep(betweenclicks)


def instagrammfollowautomation(loopstopvar, sleepbetweenclicks, web_url, scroll):
    start_status = input("Please type in 'start' if you are ready: ")
    if start_status == "start":
        print("Starting....")
        webbrowser.open(web_url)
        print("Waiting for the site to load... 10s")
        time.sleep(8)
        pyautogui.moveTo(794, 416)

        while loopstopvar is True:
            try:
                usericon = pyautogui.locateOnScreen("search_image/this.png")
                clickfollowbutton(usericon, sleepbetweenclicks)
            except:
                # move the mouse left and scroll when check for button again if not found set goOn to False
                pyautogui.moveTo(973, 567)
                scrollInt = int(scroll)
                pyautogui.scroll(-scrollInt)
                print("try to scroll")
                pyautogui.sleep(sleepbetweenclicks)
                try:
                    usericon = pyautogui.locateOnScreen('search_image/this.png')
                    clickfollowbutton(usericon, sleepbetweenclicks)
                except:
                    loopstopvar = False
                    errormessage = "Button Not Found Error"

    if errormessage:
        print(errormessage)
    else:
        print("There is no Error")


print("--------- INSTAGRAM FOLLOW AUTOMATION ---------")
print("This is a Application using the Python library 'pyautogui' to automate the process")
print("of following the Followers of a specific Instagram account.")
print('---')
print('---')
print("IMPORTANT: If you are using this on windows you may need to open the code and change the 'clickfollowbutton' function")
print("           so that the 'buttonlocationvar[0]' and 'buttonlocationvar[1]' are no longer divided by two.")
print("           If the 'Follow Button' should for some reason change it's color then change the image 'this.png' to match the new look ")
print('---')
print('---')
goOn = True
delay = int(input("How much time is there before the next button is clicked?: "))
url = input("Input the path to the Followers of the Instagram account: ")
scrolldistance = input("How far should it scroll down if it doesn't find a button?(Standart ist 8): ")

instagrammfollowautomation(goOn, delay, url, scrolldistance)

