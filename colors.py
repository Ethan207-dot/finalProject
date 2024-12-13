#This file contains the function required to color certain strings like "You win" and "Game Over"

#This function takes a string and a color modifies it to be the color and returns the string
def color(aColor, aString):
    esc = "\033["
    red = esc+"1;31m"
    magenta = esc+"1;35m"
    green = esc+"1;32m"
    blue = esc+"1;34m"
    cyan = esc+"1;36m"
    reset = esc+"0;0m"
    if aColor == "pink":
        aString = magenta + aString + reset
    if aColor == "red":
        aString = red + aString + reset
    if aColor == "green":
        aString = green + aString + reset
    if aColor == "blue":
        aString = blue + aString + reset
    if aColor == "cyan":
        aString = cyan + aString + reset
    else:
        aString
    return aString
