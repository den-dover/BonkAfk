import time, random
import pyautogui as gui

Loop = 0
TeamChange = 0
Game1FirstTeam = 'undefined'
Game1SecondTeam = 'undefined'
Game1ThirdTeam = 'undefined'
Game1ForthTeam = 'undefined'
Game2FirstTeam = 'undefined'
Game2SecondTeam = 'undefined'
Game2ThirdTeam = 'undefined'
Game2ForthTeam = 'undefined'
CurrentGameHost = 'undefined'
DefinedHostTab = 'true'
gui.PAUSE = 0.000001
Game1FirstTeam = input('what is the current first tab team? ')
time.sleep(0.2)
Monitor = input('what is the current monitor, e.g., laptop, left hp, main dell ')

def GameStart():
    if Monitor == 'left hp':
        gui.leftClick(-686, 1383)
    elif Monitor == 'laptop':
        gui.leftClick(1302, 902)

def RedJoin():
    if Monitor == 'left hp':
        gui.leftClick(-1152, 1111)
    elif Monitor == 'laptop':
        gui.leftClick(711, 554)

def BlueJoin():
    if Monitor == 'left hp':
        gui.leftClick(-1273, 1111)
    elif Monitor == 'laptop':
        gui.leftClick(568, 560)

def GreenJoin():
    if Monitor == 'left hp':
        gui.leftClick(-1028, 1112)
    elif Monitor == 'laptop':
        gui.leftClick(866, 555)

def YellowJoin():
    if Monitor == 'left hp':
        gui.leftClick(-1028, 1112)
    elif Monitor == 'laptop':
        gui.leftClick(1006, 553)

def FirstTab():
    if Monitor == 'left hp':
        gui.leftClick(-1801, 609)
    elif Monitor == 'laptop':
        gui.leftClick(155, 23)

def SecondTab():
    if Monitor == 'left hp':
        gui.leftClick(-1537, 605)
    elif Monitor == 'laptop':
        gui.leftClick(446, 16)

def ThirdTab():
    if Monitor == 'left hp':
        gui.leftClick(-1317, 604)
    elif Monitor == 'laptop':
        gui.leftClick(742, 19)

def ForthTab():
    if Monitor == 'left hp':
        gui.leftClick(-1317, 604)
    elif Monitor == 'laptop':
        gui.leftClick(1039, 28)

def MapFav():
    if Monitor == 'left hp':
        gui.leftClick(-970, 1268)
    elif Monitor == 'laptop':
        gui.leftClick(951, 758)
        favasdasd = 0

def HostTab():
    if CurrentGameHost = 1:
        FirstTab()
    elif CurrentGameHost = 2:
        SecondTab()
    elif CurrentGameHost = 3:
        ThirdTab()
    elif CurrentGameHost = 4:
        ForthTab()
    else:
        golbal = DefinedHostTab
        DefinedHostTab = 'false'

def FirstGame():
    if Game1FirstTeam == 'red':
        FirstTab()
        time.sleep(0.2)
        MapFav()
        time.sleep(0.3)
        BlueJoin()
        Game1FirstTeam = 'blue'
        time.sleep(0.2)
        SecondTab()
        time.sleep(0.2)
        MapFav()
        time.sleep(0.3)
        RedJoin()
        Game1SecondTeam = 'red'
        time.sleep(0.2)
        ThirdTab()
        time.sleep(0.3)
        MapFav()
        time.sleep(0.3)
        GreenJoin()
        Game1ThirdTeam = 'green'
        time.sleep(0.2)
        ForthTab()
        time.sleep(0.3)
        MapFav()
        time.sleep(0.3)
        YellowJoin()
        Game1ForthTeam = 'yellow'
    elif Game1FirstTeam == 'blue':
        FirstTab()
        time.sleep(0.3)
        MapFav()
        time.sleep(0.2)
        YellowJoin()
        Game1FirstTeam = 'yellow'
        time.sleep(0.2)
        SecondTab()
        time.sleep(0.3)
        MapFav()
        time.sleep(0.2)
        BlueJoin()
        Game1SecondTeam = 'blue'
        time.sleep(0.2)
        ThirdTab()
        time.sleep(0.3)
        time.sleep(0.2)
        MapFav()
        RedJoin()
        Game1ThirdTeam = 'red'
        time.sleep(0.2)
        ForthTab()
        time.sleep(0.3)
        MapFav()
        time.sleep(0.3)
        GreenJoin()
        Game1ForthTeam = 'green'

    elif Game1FirstTeam == 'green':
        FirstTab()
        time.sleep(0.3)
        time.sleep(0.2)
        MapFav()
        GreenJoin()
        Game1FirstTeam = 'green'
        time.sleep(0.2)
        SecondTab()
        time.sleep(0.3)
        time.sleep(0.2)
        MapFav()
        YellowJoin()
        Game1SecondTeam = 'yellow'
        time.sleep(0.2)
        ThirdTab()
        time.sleep(0.3)
        time.sleep(0.2)
        MapFav()
        BlueJoin()
        Game1ThirdTeam = 'blue'
        time.sleep(0.2)
        ForthTab()
        time.sleep(0.3)
        MapFav()
        time.sleep(0.3)
        RedJoin()
        Game1ForthTeam = 'red'
    elif Game1FirstTeam == 'yellow':
        FirstTab()
        time.sleep(0.3)
        time.sleep(0.2)
        MapFav()
        RedJoin()
        Game1FirstTeam = 'red'
        time.sleep(0.2)
        SecondTab()
        time.sleep(0.3)
        time.sleep(0.2)
        MapFav()
        GreenJoin()
        Game1SecondTeam = 'green'
        time.sleep(0.2)
        ThirdTab()
        time.sleep(0.3)
        time.sleep(0.2)
        MapFav()
        YellowJoin()
        Game1ThirdTeam = 'yellow'
        time.sleep(0.2)
        ForthTab()
        time.sleep(0.3)
        MapFav()
        time.sleep(0.3)
        BlueJoin()
        Game1ForthTeam = 'blue'

def GameStart():
    time.sleep(1)
    HostTab()
    if DefinedHostTab == 'true':
        time.sleep(0.5)
        GameStart()
        time.sleep(0.3)
    else: 
        print("no game host tab defined, couldn't start game")
    
time.sleep(3)
while True:
    time.sleep(0.2)
    FirstTab()
    time.sleep(0.5)
    
    if Game1FirstTeam == 'blue':
        FirstTab()
        print('first tab was blue')
    else:
        if Game1SecondTeam == 'blue':
            SecondTab()
            print('second tab was blue')
        else:
            if Game1ThirdTeam == 'blue':
                ThirdTab()
                print('third tab was blue')
            else:
                if Game1ForthTeam == 'blue':
                    ForthTab()
                    print('forth tab was blue')
                else:
                    print('no tab with blue found')
    time.sleep(61)