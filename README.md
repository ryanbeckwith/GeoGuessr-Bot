# GeoGuessr-Bot
A bot that allows users to create GeoGuessr game links automatically.

Originally this bot was supposed to be for a discord bot, however when making this bot I realized that this bot can be run by itself. Therefore I made the script usable through the command line.

## Requirements
<ul>
<li>Python 3.5+</li>
<li>Selenium</li>
<li>A browser, preferably Google Chrome. (To use other browsers, change the selenium initializations respectively</li>
<li> <a href="https://sites.google.com/a/chromium.org/chromedriver/downloads">Latest version of chromedriver</a> (only if you are using Google Chrome with Selenium)</li>
<li> <strong><em>GeoGuessr Pro Account</em></strong> </li>
</ul>


## Using the Bot
1. Go to secret.py and edit the file to include the path of the chrome driver, GeoGuessr username, and GeoGeussr password.
```
PATH = "put chrome driver path here"
username = "put GeoGuesser username here"
password = "put GeoGuesser password here"
```
2. Open a new command prompt window or terminal window. Make sure you have python installed.
3. Check the inputs.py to see all the maps and rules that you can use.
4. Run the script in command prompt or terminal. To run the script, use the following syntax:
```
python geoguessr.py [map] [rule]
```
5. Enjoy the game! You can `Press X to close program` after you grabbed the game link from the command line. Below is a sample output of the program.

```
Output:
Bot Initialized
GeoGuessr login successful.
Enter the Map you want and rule: usa nm
Game link generated:
https://www.geoguessr.com/challenge/wYjPeOmTi2oDmZ7K

```

### Notes:
* Maps are all hardcoded in `inputs.py`. You can add onto the `maps{}` section with any type of map you can find. See more below.
* The script needs two arguments to run. `[maps]` is the name of the map you would like to play. `[rule]` is the rule you want to set for the GeoGuessr game. You can find each rule below:
  #### Game Rules
  ```
  default = default
  no move = nm
  no zoom = nz
  no move, no zoom = nmnz
  no move, no pan, no zoom = nmnpnz
  
  ```
  Example of using the bot:
  ```python geoguessr.py usa nm```
 * Custom Maps can be used. However, you will need to manually add an if statement to the `inputs.py` so the bot understands to read the custom map. Add custom maps in the `maps{}` section.
 
    ```
    #custom maps
    "5e818e96b3ec17842c0bcce8",
    "59a1514f17631e74145b6f47",
    ```
    Then add an if-statement to the `checkCustom()` function to bind the hash value of the custom map with your own alias. (Do not use spaces)
    
    ```
    def checkCustom(map):
      if map == "uw-nrbr":
          map = "5e818e96b3ec17842c0bcce8"
          return map
      if map == "dw":
          map = "59a1514f17631e74145b6f47"
          return map
      else:
          return map
    ```
    
  
### Final Comments
This bot is still very much in development. If you have any suggestions or bug reports, please let me know!

#### Future Enhancements:
* Convert to discord bot.
* Add timer rule functionality.
* Make customization more user friendly.

