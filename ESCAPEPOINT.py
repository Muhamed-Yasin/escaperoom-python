import sys
import os
import time

screen_width = 500

f = open("saved.txt","w")
t = 0
s = 0

class player:
    def __init__(self):
        self.name = ''
        self.location = 'c3'
        
myPlayer = player()

def texteffect(string, n = 0.005):
    q = string
    for character in q:
        if character == None:
            break
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(n)

def prompt():
    global t
    t += 1
    print('\n' + '============================')
    print("What would you like to do?\nEnter move, examine, or quit.")
    action = input ("> ")
    acceptable_actions = ['move', 'm', 'go', 'travel', 'walk', 'examine', 'e','inspect', 'interact', 'look', 'quit']
    while action.lower() not in acceptable_actions:
        print("Unknown action, please try again.\n")
        action = input ("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'm', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'e', 'inspect', 'interact', 'look']:
        player_examine(action.lower())

        
ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'

UP = 'up','north'
DOWN = 'down','south'
LEFT = 'left','west'
RIGHT = 'right','east'    

zone_map = {
        'a1':{
            ZONENAME: 'a1',
            DESCRIPTION: '',
            EXAMINATION: 'The door with a smart lock asking for the password.',
            UP: '',
            DOWN: 'a2',
            LEFT: '',
            RIGHT: 'b1'   
                },
        'b1':{
            ZONENAME: 'b1',
            DESCRIPTION: '',
            EXAMINATION: 'The smartboard with "window" written on it',
            UP: '',
            DOWN: 'b2',
            LEFT: 'a1',
            RIGHT: 'c1'         
                },    
        'c1':{
            ZONENAME: 'c1',
            DESCRIPTION: '',
            EXAMINATION: '''You find a window with something beside it.
            You pick it up and it turns out to be a journal with Imran written
            in it ''',
            UP: '',
            DOWN: 'c2',
            LEFT: 'b1',
            RIGHT: ''
                },
                
        'a2':{
            ZONENAME: 'a2',
            DESCRIPTION: '',
            EXAMINATION: 'There is a strange cupboard',
            UP: 'a1',
            DOWN: 'a3',
            LEFT: '',
            RIGHT: 'b2'         
                },
        'b2':{
            ZONENAME: 'b2',
            DESCRIPTION: '',
            EXAMINATION: 'A mobile phone lying on the ground.',
            UP: 'b1',
            DOWN: 'b3',
            LEFT: 'a2',
            RIGHT: 'c2'      
                },    
        'c2':{
            ZONENAME: 'c2',
            DESCRIPTION: '',
            EXAMINATION: '''There are lots of computers....as you pass your gaze
along the room you see a red blur on the ceiling.
                        You look up and your blood freezes in your veins.
                        You find the word Jump written in blood''',
            UP: 'c1',
            DOWN: 'c3',
            LEFT: 'b2',
            RIGHT: ''         
                },
                
        'a3':{
            ZONENAME: 'a3',
            DESCRIPTION: '',
            EXAMINATION: '''You find nothing worthwhile except something written
on the floor
            You look down to find the word Kill written on the floor''',
            UP: 'a2',
            DOWN: '',
            LEFT: '',
            RIGHT: 'b3'         
                },
        'b3':{
            ZONENAME: 'b3',
            DESCRIPTION: 'You find the assistants computer towards '
            'your left and see the smartboard ahead',
            EXAMINATION: 'Upon examination you find something glowing in'
            'front of you.',
            UP: 'b2',
            DOWN: '',
            LEFT: 'a3',
            RIGHT: 'c3'         
                },    
        'c3':{
            ZONENAME: 'c3',
            DESCRIPTION: '',
            EXAMINATION: '''You see 3 rows of computers
            Upon examination you find nothing in the area, but you spot
            a faint glow to your northwest''',
            UP: 'c2',
            DOWN: '',
            LEFT: 'b3',
            RIGHT: ''         
                } 
        }
### PRINTS PLAYER LOCATION ###
def movement_handler(destination):
    
    myPlayer.location = destination
    print('\n' + ('#' * (4 + len(zone_map[myPlayer.location][ZONENAME]))))
    print('# ' + zone_map[myPlayer.location][ZONENAME] + ' #')
    print(('#' * (4 + len(zone_map[myPlayer.location][ZONENAME])))) 
    print ('########################')
    print ("You are now in block " + destination + '.\n')
    printmap()
    print ('\n' + 'x ' + zone_map[myPlayer.location][DESCRIPTION])
    
### HANDLES PLAYER MOVEMENT ###           
def player_move(moveAction):
    """	
    This function handles player movement
    """
    properdirection = False
    while properdirection == False:
        ask = "Where would you like to move to?\n"
        dest = input(ask)
        if dest not in ['up', 'north', 'down', 'south', 'left', 'west', 'right', 'east']:
            print("Invalid direction, please use up, down, left, or right.")  
            
        elif dest in ['up', 'north']:
            destination = zone_map[myPlayer.location][UP]
            if destination == '':
                print("You cannot move that way, please try again.")
            else:
                properdirection = True
                movement_handler(destination)
        elif dest in ['down', 'south']:
            destination = zone_map[myPlayer.location][DOWN]
            if destination == '':
                print("You cannot move that way, please try again.")
            else:
                properdirection = True
                movement_handler(destination)
        elif dest in ['left', 'west']:
            destination = zone_map[myPlayer.location][LEFT]
            if destination == '':
                print("You cannot move that way, please try again.")
            else:
                properdirection = True
                movement_handler(destination)
        elif dest in ['right', 'east']:
            destination = zone_map[myPlayer.location][RIGHT]
            if destination == '':
                print("You cannot move that way, please try again.")
            else:
                properdirection = True
                movement_handler(destination)
       
def player_examine(examineAction):
    print(zone_map[myPlayer.location][EXAMINATION])
    if myPlayer.location == 'b2':
        texteffect('''The screen shows:
                He who makes it, has no need for it.
                He who buys it, has no use for it.
                He who uses it, doesn't know it.
                What is it ?''')
        y = input("> ")
        while y not in ['coffin' ]:
            print("Thats not it")
            y = input("> ")
        else :
            texteffect('''The phone unlocks and you see one word flashing
prominently on the screen.
                       "Yasin"''')
            global s
            s+=10
            printmap( )
    if myPlayer.location == 'a2' :
        texteffect('''you see a lock with the following on it
                What Is The Next Letter In The Progression
                W I T N L I T _
                Read the beginning carefully
                remember your grammar classes.''')
        x = str(input("> "))
        while x != 'p':
            print("That's not it")
            x = input("> ")
        else:
            texteffect('''The safe unlocks.......but it is very hard to open.
You pull at it and suddenly it springs open.
A solitary piece of paper lies in it.
You pick it up and find the word "Arshad" written on it.
You turn it over and find "Jawad" written on the other side.''')
            #global s
            s += 10
            printmap( )
            
    if myPlayer.location == 'a1':
        print("""'''_ _ _
            You know it already........if not go around and find it'''
(the names you found)
(in alphabetical order obviously}
(only four alphabets).""")
        y = input("> ")
        if y != "aijy":
            print("That's not it. Try moving around to find it")
            prompt( )
        else:
            texteffect('''The door unlocks............
and a projecter clicks on.On the other wall you see images that will haunt
you forever
the images slowly fade and suddenly a warning appears.....
Death awaits those who go through this door..... to succeed blood must flow.
        You go through your options and realize that there are two
        and only two exits out of the lab.......the door and the window.
do you ignore the warning and go through the door.''')
        #global s
        s +=10
        ans = input("> ")
        while ans not in ['y','yes','n','no']:
            print("Invalid input. Please enter yes or no.")
            ans = input("> ")
        else:
            while ans not in ['y','yes'] :
                texteffect('''Logic goes out the window along with you.
            You see shimmering shards of glass shattering on the pavement
            beneath you and you find out what pure uncaged fear feels like as
            you see the ground rushing up to meet you.
            Suddenly the whole world goes dark.
            Surprisingly you feel no pain.
            Suddenly pain courses through your body causing you to open your
            eyes.You get up and find yourself in an unfamiliar place.
            The sterile smell of hospitals assault your nose.
            You sit up and find rows and rows of hospital beds with people
            lying on it as far as the eye can see.
            Suddenly a man dressed in black slacks and shirt appears at your
            bedside and explains what happened to you. Apparently the world has
            changed from what you know.
            Because of bad leadership World War III started.
            World superpowers brought out the nukes and then it was just
            plain, brutal, savage war.
            Cities got destroyed, billions died.
            Concerned people saved as much of the young generation as possible
            and brought them to a safe place.
            Here they started entering them into simulations in the hope of
            finding someone who could lead this world out of this apocalypse.
            But the hope started diminishing when they couldn't find anyone.
            After 10 years of searching you are the first person to finish the
            simulation.''')
                print("you took",t,"turns")        
                break
            else:
                texteffect('''You know that jumping out the window will end in
                really painful death.
                So you opt to disobey the warning and go through the door.
                Suddenly alarm bells start clanging and you start running.
                Suddenly you are knocked of your feet by the force of an
                explosion. When you turn back you find the lab in flames.
                You sprint faster down the tunnel to find the exit.
                You can hear explosions as you sprint down the tunnel.
                Suddenly you hit a wall and break your nose.
                You desperately search for an exit but come up with nothing.
                You can see the flames moving closer and you close your eyes and
                wait for it.
                And deep in your mind you know that somewhere you made the wrong
                choice.''')
                print("you took",t,"turns")  
                
                f.write(myPlayer.name,",",s)
                sys.exit( )
    prompt( )                
    

def printmap():
        print("\n    A   B   C ")
        print("  -------------")
        if myPlayer.location == 'a1':
            print("1 | x |   |   |")
        elif myPlayer.location == 'b1':
            print("1 |   | x |   |")
        elif myPlayer.location == 'c1':
            print("1 |   |   | x |")
        else:
            print("1 |   |   |   |")
        print("  -------------")
        if myPlayer.location == 'a2':
            print("2 | x |   |   |")
        elif myPlayer.location == 'b2':
            print("2 |   | x |   |")
        elif myPlayer.location == 'c2':
            print("2 |   |   | x |")
        else:
            print("2 |   |   |   |")
        print("  -------------")
        if myPlayer.location == 'a3':
            print("3 | x |   |   |")
        elif myPlayer.location == 'b3':
            print("3 |   | x |   |")
        elif myPlayer.location == 'c3':
            print("3 |   |   | x |")
        else:
            print("3 |   |   |   |")
        print("  -------------")
        prompt( )

def start_game( ):
    texteffect(''' The computer unlocks, you try to find how you got here....
but the search yields nothing.
You try again.And again.And again
Same result.
Now in a frenzy you open random directories trying to find a scrap of
information.......and a file named ESCAPEPOINT catches your eye.
You open it ....and \n''')
    title_screen( )
def setup_game( ):
    texteffect('''The following instructions flash across the screen in a
endless loop.
Move to the lab.
Move to the lab.
Move to the lab.
You move to the door leading to the other cabin.you open the door and move to
the other side warily.The door slams shut behind you.
You jump in fear. Then gulping you move to the door connecting the cabin to the lab.
It seems it is a bad day for you because ,you find a smart lock stopping you
from opening the door.
the following is displayed on the screen of the lock.
Solve this for the password.
M1Y LIF11E1
("how many ones?")
(remove the ones)
(four ones in ...)
''')
    a = str(input("> ") )       
    while a.lower( ) not in ['for once in my life','four ones in my life']:    
        print('Thats not it')
        a = input("> ")
    else:
        texteffect('''


YOU OPEN THE DOOR WITH A LOUD SCREECH AND FIND A TRUSTY MAP TO FIND YOUR WHERABOUTS


''')
        global s
        s += 10
        printmap( )
         
def title_screen_selections():
    option = ''
    while option.lower not in ["help", "quit", "play"]:
        print("Please enter play, help, or quit")
        option = str(input("> "))
        if option.lower() == "play":
            setup_game()
            break
        elif option.lower() == "help":
            help_menu( )
        elif option.lower() == "quit":
            sys.exit()
        
def help_menu():
    """
    Creates the help menu
    """
    print('\n##################################################')
    print('################     Help Menu     ###############')  
    print('##################################################')
    print(' Type move or examine for each turn')      
    print(' If moving, type up, down, left, or right')
    print(' If examining, you may need to answer yes or no')
    print('##################################################\n')
    title_screen_selections()
    
def title_screen( ):
    print('''
____ ____ ____ ____ ___  ____    ___  ____ _ _  _ ___ 
|___ [__  |    |__| |__] |___    |__] |  | | |\ |  |  
|___ ___] |___ |  | |    |___    |    |__| | | \|  |

''')
                                                      
    print('\n ################################')      
    print(' -            .Play.           - ')
    print(' -            .Help.           - ')
    print(' -            .Quit.           - ')
    print('################################\n') 
    print('© 2013 escape industries.  All rights reserved')
    title_screen_selections()



texteffect('''You open your eyes to find darkness. You look around.
A faint glow shows that you are in Hamid sir's cabin.
You try to get up and almost black out.
5 mins later.....

You get up and your legs give away and you fall on the floor.
You try crawling to the sink and look at yourself in the mirror.
You see a complete stranger.
Your eyes are red, your hair stick out at random angles,you have a splitting
headache and you feel sore all over your body.
But impossibly you dont feel any pain. You wash your face in the sink to clear
your head.
You look up and see something written on the wall behind you.
You turn around and read it.

"TRY THE COMPUTER,MATE."

You stumble to the computer and switch it on only to find it locked.

You try a few common passwords, and there is a flash across the screen that
says:-
"Solve this puzzle to get what you want"

H2OMLLN

This is not a word scramble, the word has a chemical formula
it depicts a fruit, join these words to get that password.''')

o = input("\n > ")
while o.lower( ) not in  ['watermelon']:   
    print('Thats not it')
    o = input("> ")
else:
    start_game( )

    
