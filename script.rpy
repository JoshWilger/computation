init python:
    from datetime import datetime

# This is the base image which displays the Mac OS8 window frame
image UI = "images/base.png"
# This is a plan white background that goes over the UI
image white = "images/white.png"# This sets up an animation for a flashing arrow in the text box, you can change the image, animation speed, and location.
# Every character will need to have (ctc = "ctc_animation", ctc_position = "fixed") added in order to have the animation display.
image ctc_animation = Animation("images/ctcwhite.png", 0.5, "images/ctcblack.png", 0.5, xpos=0, ypos=0, xanchor=0, yanchor=0)

# Creates the narrator as a character to enable the ctc animation
# define narrator = Character(ctc = "ctc_animation", ctc_position = "fixed")

image logo = "images/ODDS AND ENDS/Odds58.png"
image logo_background = "images/CARDS/Dynamic.png"
image load = "images/BORDERS/Border16.png"

image snippy = "images/ASSORTED ICONS/87.png"

define persistent.welcome_txt = "Welcome to Waffles! We're glad your here and wish you the best with the use of our product!"
define persistent.ipsum_txt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus ultricies, diam id vestibulum viverra, purus urna commodo dolor, sit amet vulputate mauris lorem nec lorem. Donec dapibus eget mauris ut malesuada. Praesent tincidunt enim nisi, in pulvinar mi tincidunt et. Phasellus at ultrices sem. Etiam eu purus lacus. Nunc ex nisi, volutpat ac tincidunt sed, pretium eu leo. Ut sodales euismod diam, et gravida nisi mattis at. Ut sed tortor efficitur dolor dignissim ultricies."
define persistent.blank_txt = ""

# The game starts here.

label bootup:
    pause 1.0
    show logo_background:
        fit "cover"
    show logo at truecenter
    show load at left:
        xzoom 2.0
        block:
            xalign 0.05
            linear 3.0 xalign 1.0
            repeat
    pause 12.0
    hide load
    hide logo
    hide logo_background
    pause 2.0
    show screen text_screen("{color=#FFF}_\n\nC:\\>SET BLASTER=A220 17 D1 H7 P330 T6\n\nC:\\>SET SBPC I=C:\\SBPCI\n\nC:/>\nC:\\SET Path=C:\\WAFFLES;C:\\WAFFLES\\COMMAND\n\nC:/>\nC:/>{/color}", cps=700)
    pause 4.0
    hide screen text_screen
    pause 2.0

    return

label bsod:
    $ gametime = str(renpy.get_game_runtime())
    show blue
    show text ("{color=#FFF}{b}WAFFLES{/b}\n\nA fatal exception 0E has occurred at [gametime]. The current session will be terminated.\n\n   *    Press space to terminate the current session.\n   *    Press ALT+F4 to restart the session. You will\n           lose any unsaved information in all applications. \n\nPress space to continue _{/color}"):
        xalign 0.4
        yalign 0.6
    pause
    hide text
    hide blue
    pause 2.0

    return

label desktopy(loading=0.0):
    hide screen files
    hide screen desktop
    hide screen txt

    show screen desktop(loading)

    menu:
        "{image=images/MAC SYSTEM/Mac20.png}\nDocuments":
            call documents
        "{image=images/MAC SYSTEM/94.png}\nScrap":
            call scrap

    # "This is your desktop. You'll be seeing this a lot, as it is basically the home screen of the computer!" 
    return

label documents:
    hide screen desktop
    hide screen files
    hide screen txt

    show screen files("documents")
    
    menu:
        "{image=images/MAC SYSTEM/189.png}\nWelcome to Waffles.txt\n":
            call welcome
        "{image=images/MAC SYSTEM/189.png}\nLorem Ipsum.txt\n":
            call ipsum
        "{image=images/MAC SYSTEM/94.png}\nMysterious File\n":
            hide screen files
        "{image=images/MAC SYSTEM/189.png}\nblank.txt":
            call blank
    
    # "Here is where all your documents are kept!"
    return

label scrap:
    hide screen desktop
    hide screen files
    hide screen txt

    show screen files("scrap")

    "This file is currently empty!"
    return

label welcome:
    hide screen desktop
    hide screen files
    hide screen txt

    show screen txt(persistent.welcome_txt, save_welcome)

    "Here is a warm welcome from those at Waffles Inc.!"
    return

label ipsum:
    hide screen desktop
    hide screen files
    hide screen txt

    show screen txt(persistent.ipsum_txt, save_ipsum)

    "This is a meaningless text file. Hope you can read Latin!"
    return

label blank:
    hide screen desktop
    hide screen files
    hide screen txt

    show screen txt(persistent.blank_txt, save_blank)

    "A blank page is an opportunity for creativity..."
    return

label start:
    call bootup
    call desktopy
    call bsod

    return

label test:
    define s = Character("Snippy", ctc = "ctc_animation", ctc_position = "fixed")
    image beast = "images/BEASTS/Beasts10.png"

    # Displays the background
    show UI onlayer master
    
    # menu:
    #     "I am savvy with my mouse!":
    #         "weeeeee!!!!"
    #     "Typing is terrific!":
    #         $ text = "\t Hello and welcome to Ren'Py - a place where you can code with a language similar to Python. It is often used to create visual novels, but we are using it to create a fantastic game instead :) \n\n Hope you enjoy it!\n:D"
    #         $ a = renpy.input("Time to type!!", default = text, exclude="012345678910~`_=+\|]}[{<>/@#$%^*", length=32)

    show snippy at truecenter:
        zoom 2.0
        # Show the logo at the upper right side of the screen.
        xalign 1.0 yalign 0.0

        # Take 1.0 seconds to move things back to the left.
        linear 1.0 xalign 0.0

        # Take 1.0 seconds to move things to the location specified in the
        # truecenter transform. Use the ease warper to do this.
        ease 1.0 truecenter

        # Just pause for a second.
        pause 1.0

        # Set the location to circle around.
        alignaround (.5, .5)

        # Use circular motion to bring us to spiral out to the top of
        # the screen. Take 2 seconds to do so.
        linear 2.0 yalign 0.0 clockwise circles 3

        # Use a spline motion to move us around the screen.
        linear 2.0 align (0.5, 1.0) knot (0.0, .33) knot (1.0, .66)

        # Changes xalign and yalign at thje same time.
        linear 2.0 xalign 1.0 yalign 1.0

        # The same thing, using a block.
        linear 2.0:
            xalign 0.2
            yalign 0.5

    s "Hi there!"
    show beast at truecenter

    pause 0.5
    hide beast
    s "What was THAT?"
    s "Oh well."
    s "My name is Snippy!"
    $ x = renpy.input("What's your name?")
    s "Hi there, [x]!"

    "hillo"

    return

