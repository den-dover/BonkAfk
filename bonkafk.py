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
Monitor = input('what is the current monitor, e.g., laptop, left hp, main dell, old tvs ')
time.sleep(0.2)
WatchGame = input('what game would you like to watch? e.g., 1, 2 ')

def StartGameButton():
    if Monitor == 'left hp':
        gui.leftClick(-686, 1383)
    elif Monitor == 'laptop':
        gui.leftClick(1302, 902)
    elif Monitor == 'old tvs':
        gui.leftClick()

def RedJoin():
    if Monitor == 'left hp':
        gui.leftClick(-1152, 1111)
    elif Monitor == 'laptop':
        gui.leftClick(711, 554)
    elif Monitor == 'old tvs':
        gui.leftClick()

def BlueJoin():
    if Monitor == 'left hp':
        gui.leftClick(-1273, 1111)
    elif Monitor == 'laptop':
        gui.leftClick(568, 560)
    elif Monitor == 'old tvs':
        gui.leftClick()

def GreenJoin():
    if Monitor == 'left hp':
        gui.leftClick(-1028, 1112)
    elif Monitor == 'laptop':
        gui.leftClick(866, 555)
    elif Monitor == 'old tvs':
        gui.leftClick()

def YellowJoin():
    if Monitor == 'left hp':
        gui.leftClick(-1028, 1112)
    elif Monitor == 'laptop':
        gui.leftClick(1006, 553)
    elif Monitor == 'old tvs':
        gui.leftClick()

def FirstTab():
    if Monitor == 'left hp':
        gui.leftClick(-1801, 609)
    elif Monitor == 'laptop':
        gui.leftClick(104, 21)
    elif Monitor == 'old tvs':
        gui.leftClick()

def SecondTab():
    if Monitor == 'left hp':
        gui.leftClick(-1537, 605)
    elif Monitor == 'laptop':
        gui.leftClick(318, 23)
    elif Monitor == 'old tvs':
        gui.leftClick()

def ThirdTab():
    if Monitor == 'left hp':
        gui.leftClick(-1317, 604)
    elif Monitor == 'laptop':
        gui.leftClick(515, 26)
    elif Monitor == 'old tvs':
        gui.leftClick()

def ForthTab():
    if Monitor == 'left hp':
        gui.leftClick(-1317, 604)
    elif Monitor == 'laptop':
        gui.leftClick(692, 23)
    elif Monitor == 'old tvs':
        gui.leftClick()

def FifthTab():
    if Monitor == 'left hp':
        gui.leftClick(-1317, 604)
    elif Monitor == 'laptop':
        gui.leftClick(871, 26)
    elif Monitor == 'old tvs':
        gui.leftClick()

def SixthTab():
    if Monitor == 'left hp':
        gui.leftClick(-1317, 604)
    elif Monitor == 'laptop':
        gui.leftClick(1047, 12)
    elif Monitor == 'old tvs':
        gui.leftClick()

def SeventhTab():
    if Monitor == 'left hp':
        gui.leftClick(-1317, 604)
    elif Monitor == 'laptop':
        gui.leftClick(1256, 19)
    elif Monitor == 'old tvs':
        gui.leftClick()

def EighthTab():
    if Monitor == 'left hp':
        gui.leftClick(-1317, 604)
    elif Monitor == 'laptop':
        gui.leftClick(1480, 34)
    elif Monitor == 'old tvs':
        gui.leftClick()

def MapFav():
    if Monitor == 'left hp':
        gui.leftClick(-970, 1268)
    elif Monitor == 'laptop':
        gui.leftClick(951, 758)
        favasdasd = 0

def HostTab():
    if CurrentGameHost == 1:
        FirstTab()
    elif CurrentGameHost == 2:
        SecondTab()
    elif CurrentGameHost == 3:
        ThirdTab()
    elif CurrentGameHost == 4:
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

def SecondGame():
    if Game2FirstTeam == 'red':
        FifthTab()
        time.sleep(0.2)
        MapFav()
        time.sleep(0.3)
        BlueJoin()
        Game2FirstTeam = 'blue'
        time.sleep(0.2)
        SixthTab()
        time.sleep(0.2)
        MapFav()
        time.sleep(0.3)
        RedJoin()
        Game2SecondTeam = 'red'
        time.sleep(0.2)
        SeventhTab()
        time.sleep(0.3)
        MapFav()
        time.sleep(0.3)
        GreenJoin()
        Game2ThirdTeam = 'green'
        time.sleep(0.2)
        EighthTab()
        time.sleep(0.3)
        MapFav()
        time.sleep(0.3)
        YellowJoin()
        Game2ForthTeam = 'yellow'
    elif Game2FirstTeam == 'blue':
        FifthTab()
        time.sleep(0.3)
        MapFav()
        time.sleep(0.2)
        YellowJoin()
        Game2FirstTeam = 'yellow'
        time.sleep(0.2)
        SixthTab()
        time.sleep(0.3)
        MapFav()
        time.sleep(0.2)
        BlueJoin()
        Game2SecondTeam = 'blue'
        time.sleep(0.2)
        SeventhTab()
        time.sleep(0.3)
        time.sleep(0.2)
        MapFav()
        RedJoin()
        Game2ThirdTeam = 'red'
        time.sleep(0.2)
        EighthTab()
        time.sleep(0.3)
        MapFav()
        time.sleep(0.3)
        GreenJoin()
        Game2ForthTeam = 'green'
    elif Game2FirstTeam == 'green':
        FifthTab()
        time.sleep(0.3)
        time.sleep(0.2)
        MapFav()
        GreenJoin()
        Game2FirstTeam = 'green'
        time.sleep(0.2)
        SixthTab()
        time.sleep(0.3)
        time.sleep(0.2)
        MapFav()
        YellowJoin()
        Game2SecondTeam = 'yellow'
        time.sleep(0.2)
        SeventhTab()
        time.sleep(0.3)
        time.sleep(0.2)
        MapFav()
        BlueJoin()
        Game2ThirdTeam = 'blue'
        time.sleep(0.2)
        EighthTab()
        time.sleep(0.3)
        MapFav()
        time.sleep(0.3)
        RedJoin()
        Game2ForthTeam = 'red'
    elif Game2FirstTeam == 'yellow':
        FifthTab()
        time.sleep(0.3)
        time.sleep(0.2)
        MapFav()
        RedJoin()
        Game2FirstTeam = 'red'
        time.sleep(0.2)
        SixthTab()
        time.sleep(0.3)
        time.sleep(0.2)
        MapFav()
        GreenJoin()
        Game2SecondTeam = 'green'
        time.sleep(0.2)
        SeventhTab()
        time.sleep(0.3)
        time.sleep(0.2)
        MapFav()
        YellowJoin()
        Game2ThirdTeam = 'yellow'
        time.sleep(0.2)
        EighthTab()
        time.sleep(0.3)
        MapFav()
        time.sleep(0.3)
        BlueJoin()
        Game2ForthTeam = 'blue'

def GameStart():
    time.sleep(1)
    HostTab()
    if DefinedHostTab == 'true':
        time.sleep(0.5)
        StartGameButton()
        time.sleep(0.3)
    else: 
        print("no game host tab defined, couldn't start game")
    
time.sleep(3)
while True:
    time.sleep(0.2)
    FirstTab()
    time.sleep(0.5)
    First
    
    if WatchGame == 1:
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
    else:
        if Game2FirstTeam == 'blue':
            FifthTab()
            print('fifth tab was blue')
        else:
            if Game2SecondTeam == 'blue':
                SixthTab()
                print('sixth tab was blue')
            else:
                if Game2ThirdTeam == 'blue':
                    SeventhTab()
                    print('seventh tab was blue')
                else:
                    if Game2ForthTeam == 'blue':
                        EighthTab()
                        print('eighth tab was blue')
                    else:
                        print('no tab with team blue found')
    time.sleep(61)
