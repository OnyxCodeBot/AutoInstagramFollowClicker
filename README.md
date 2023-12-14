# AutoInstagramFollowClicker
Automates the process of following every Follower of a specific Instagram account using the pyautogui library

<strong>Install the pyautogui library before starting!!!</strong>

<h2>Remember the following:</h2>
<ol>
<li>After executing the main file you will be asked to put in some parameters, the Instagram acount url should look like this: https://www.instagram.com/AcountName/followers/ </li>
<li>In the 'search_image' folder you need to add a png of the 'Instagram Follow Button' and name the image 'this.png' -> Example: /search_image/this.png </li>
<li>This was made for MacBook Pro with macOS Sonoma, if you use Windows then read point 4. </li>
<li></li> On Windows you may need to change the 'clickfollowbutton()' function into something ike this: </li>
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
   For some reason the 'pyautogui.locateOnScreen()' function returnes the x and y coordinates multiplied by 2 so i needed to manually divide them 
</ol>

<h3>Known Errors and Limitations:</h3>
- If the first valid Follow-Button is not visible even after the list was scrolled down the program will end
