esc = "\033["
red = esc+"1;31m"
magenta = esc+"1;35m"
green = esc+"1;32m"
blue = esc+"1;34m"
cyan = esc+"1;36m"
reset = esc+"0;0m"
def color(aColor, aString):
    esc = "\033["
    red = esc+"1;31m"
    magenta = esc+"1;35m"
    green = esc+"1;32m"
    blue = esc+"1;34m"
    cyan = esc+"1;36m"
    reset = esc+"0;0m"
    if aColor == "pink":
        print(magenta + aString + reset)
    if aColor == "red":
        print(red + aString + reset)
    if aColor == "green":
        print(green + aString + reset)
    if aColor == "blue":
        print(blue + aString + reset)
    if aColor == "cyan":
        print(cyan + aString + reset)
    else:
        print(aString)
