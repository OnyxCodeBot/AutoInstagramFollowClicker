# AutoInstagramFollowClicker
Automates the process of following every Follower of a specific Instagram account using the pyautogui library

Install the pyautogui library before starting

Remember the following:
1. After executing the main file you will be asked to put in some parameters, the Instagram acount url should look like this: https://www.instagram.com/AcountName/followers/
2. In the 'search_image' folder you need to add a png of the 'Instagram Follow Button' and name the image this.png. -> Example: /search_image/this.png
3. This was made for MacBook Pro with macOS Sonoma, if you use Windows then read point 4.
4. On Windows you may need to change the 'clickfollowbutton()' function into something ike this:
   <pre>
   <code class='language-python'>
   def clickfollowbutton(buttonlocationvar, betweenclicks):
    x = buttonlocationvar[0]
    y = buttonlocationvar[1]
    pyautogui.moveTo(x, y)
    pyautogui.click(x, y, 1)
    time.sleep(betweenclicks)
   </code>
   </pre>
