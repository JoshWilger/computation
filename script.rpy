﻿
# This is the base image which displays the Mac OS8 window frame
image UI = "images/base.png"
# This is a plan white background that goes over the UI
image white = "images/white.png"# This sets up an animation for a flashing arrow in the text box, you can change the image, animation speed, and location.
# Every character will need to have (ctc = "ctc_animation", ctc_position = "fixed") added in order to have the animation display.
image ctc_animation = Animation("images/ctcwhite.png", 0.5, "images/ctcblack.png", 0.5, xpos=0, ypos=0, xanchor=0, yanchor=0)

# Creates the narrator as a character to enable the ctc animation
# define narrator = Character(ctc = "ctc_animation", ctc_position = "fixed")

image logo = "images/logo.png"
image logo_background = "images/pexels-mikhail-nilov.png"
image load = "images/Border16.png"

image snippy = "images/ASSORTED ICONS/87.png"
image clipster = "images/COMMUNICATION/Communication2.png"
image waldo = "images/MAC SYSTEM/184.png" 

define s = Character("Snippy", ctc = "ctc_animation", ctc_position = "fixed")
define c = Character("Clipster", image="images/COMMUNICATION/Communication2.png")
define w = Character("Waldo", image="images/MAC SYSTEM/184.png")

define persistent.welcome_txt = "Welcome to Waffles! We're glad your here and wish you the best with the use of our product!"
define persistent.ipsum_txt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus ultricies, diam id vestibulum viverra, purus urna commodo dolor, sit amet vulputate mauris lorem nec lorem. Donec dapibus eget mauris ut malesuada. Praesent tincidunt enim nisi, in pulvinar mi tincidunt et. Phasellus at ultrices sem. Etiam eu purus lacus. Nunc ex nisi, volutpat ac tincidunt sed, pretium eu leo. Ut sodales euismod diam, et gravida nisi mattis at. Ut sed tortor efficitur dolor dignissim ultricies."
define persistent.blank_txt = ""
define droppable = ""
define draggable = ""
define waldo_escaped = False
define clipster_escaped = False

# The game starts here.

label bootup:
    pause 3.0
    show renpy at truecenter with Fade(0.0, 0.0, 10.0)
    pause 6.0
    hide renpy
    pause 2.0
    show logo_background:
        fit "cover"
    show logo at truecenter:
        zoom 2.0
        yalign 0.4
    show load at left:
        xzoom 2.0
        block:
            xalign 0.05
            linear 3.0 xalign 1.0
            repeat
    pause 15.0
    hide load
    hide logo
    hide logo_background
    pause 2.0
    show screen text_screen("{color=#FFF}_\n\nC:\\>SET BLASTER=A220 17 D1 H7 P330 T6\n\nC:\\>SET SBPC I=C:\\SBPCI\n\nC:/>\nC:\\SET Path=C:\\WAFFLES;C:\\WAFFLES\\COMMAND\n\nC:/>\nC:/>{/color}", cps=700)
    pause 4.0
    hide screen text_screen
    pause 2.0
    show cyan
    pause 2.0
    hide cyan

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
    stop sound
    pause 2.0

    return

label yaai:
    stop music
    stop sound

    image exit = "images/ASSORTED ICONS/39.png"
    $ i = 0
    while i < 10:
        play audio "sounds/you-are-an-idiot.mp3" loop
        show base at truecenter:
            zoom 0.3
        show exit:
            zoom 0.5 xalign 0.99 yalign 0.01
        pause
        $ i += 1
    
    hide base
    hide exit

    return

label credits:
    show text ("{color=#FFF}{b}Credits{/b} \
    {vspace=40}Developer and Designer{space=50}Josh Wilger \
    \
    {vspace=150} {b} Assets{/b}\
    {vspace=40} Ren'Py Hypercard Framework by Eliot Gardepe \
    {vspace=40} Hypercard Graphics Pack by Eliot Gardepe \
    {vspace=40} Blueberry Background by Mikhail Nilov \
    {vspace=40} Image recolorization by Josh Wilger \
    \
    {vspace=150} {b}Music{/b} \
    {vspace=40} Menu Music \"Warm Anolog Tech Synth\" by CremeTop \
    {vspace=40} Gameplay Music \"Fudgedubnofunk\" by Fudgedubnofunk \
    {vspace=40} Credits Music \"Ctrl-Alt-Delete\" by Fudgedubnofunk \
    \
    {vspace=150} {b}Sound Effects{/b} \
    {vspace=40} Computer switched on and loads by Zapsplat \
    {vspace=40} Computer startup by Wricken \
    \
    {vspace=150} {b}Fonts{/b} \
    {vspace=40} ChicagoFLF from the Ren'Py Hypercard Framework \
    {vspace=40} M 8pt from Yandex.Disk \
    \
    {vspace=150} {b}Inspiration{/b} \
    {vspace=40} The nostolgia of Microsoft Windows 98® and old operating systems \
    \
    {vspace=200} I hope you enjoyed this game! \
    {vspace=80} Thanks for playing! \
    {vspace=200}{/b}"):
        yalign -0.3
        linear 50.0 yalign 1.0
    pause 80.0
    hide screen files
    hide screen desktop
    hide screen txt
    hide screen cmd
    hide screen text_screen
    hide screen blank
    show screen menu_please
    return
    # {vspace=40} You are an idiot by Unknown on Archive.org \


label desktopy(loading=0.0):
    hide screen files
    hide screen desktop
    hide screen txt
    hide screen cmd
    hide screen text_screen
    hide screen blank

    show screen desktop(loading)

    if waldo_escaped and clipster_escaped:
        pause
        hide screen files
        hide screen desktop
        hide screen txt
        hide screen cmd
        hide screen text_screen
        hide screen blank
        stop sound
        stop music
        play music "sounds/CtrlAltDelete.mp3"
        jump credits
    else:
        if waldo_escaped:
            "Yay, I'm finally Waffle-free!"
            "Although this place does still seem pretty boxy..."
            "Oh, I forgot to properly introduce myself!"
            w "The name's Waldo."
            w "I usually just communicate between the user and the computer, but now I'm here to get you out of this place!"
            w "I think you have to get to the end of this scenario, so let me help you do that."
            w "I got a friend in Documents that needs your help as well. Maybe that'll get this over with."
        if clipster_escaped:
            c "Woah! Look at this place!"
            c "All it really needs is some more people like me!"
            c "You should go help my friend in the Command Input. He probably knows why you're here."

        menu:
            "{image=images/MAC SYSTEM/Mac20.png}\nDocuments":
                call documents from _call_documents
            "{image=images/MAC SYSTEM/221.png}\nJunk":
                call junk from _call_junk
            "{image=images/MAC SYSTEM/187.png}\nCommand Input":
                call cmd from _call_cmd

    # "This is your desktop. You'll be seeing this a lot, as it is basically the home screen of the computer!"
    return

label documents:
    hide screen desktop
    hide screen files
    hide screen txt

    show screen files("documents")
    
    menu:
        "{image=images/MAC SYSTEM/189.png}\nWelcome to Waffles.txt":
            call welcome from _call_welcome
        "{image=images/MAC SYSTEM/189.png}\nLorem Ipsum.txt":
            call ipsum from _call_ipsum
        "{image=images/MAC SYSTEM/94.png}\nMysterious File":
            hide screen files
            # call yaai
        "{image=images/MAC SYSTEM/189.png}\nblank.txt":
            call blank from _call_blank
    
    # "Here is where all your documents are kept!"
    return

label junk:
    hide screen desktop
    hide screen files
    hide screen txt

    show screen files("junk")

    "This file is currently empty!"
    return

label welcome:
    hide screen desktop
    hide screen files
    hide screen txt

    show screen txt(persistent.welcome_txt, save_welcome)

    while not clipster_escaped:
        "Here is a warm welcome from those at Waffles Inc.!"
        call clipster_intro from _call_clipster_intro

    hide screen txt
    hide screen text_screen
    show screen blank("txt.png")
    "Yay!"

    return

label ipsum:
    hide screen desktop
    hide screen files
    hide screen txt

    show screen txt(persistent.ipsum_txt, save_ipsum)

    while not clipster_escaped:
        "This is a meaningless text file. Hope you can read Latin!"
        call clipster_intro from _call_clipster_intro_1

    hide screen txt
    hide screen text_screen
    show screen blank("txt.png")
    "Yay!"

    return

label blank:
    hide screen desktop
    hide screen files
    hide screen txt

    show screen txt(persistent.blank_txt, save_blank)

    while not clipster_escaped:
        "A blank page is an opportunity for creativity..."
        call clipster_intro from _call_clipster_intro_2

    hide screen txt
    hide screen text_screen
    show screen blank("txt.png")
    "Yay!"

    return

label cmd:
    hide screen desktop
    hide screen files
    hide screen txt
    hide screen cmd
    hide screen text_screen
    image waldo = "images/MAC SYSTEM/184.png" 

    show screen cmd(w)


    $ commands = ""
    $ i = 0
    $ waldo_intro = ["Tell the computer to do things:", "The computer sees what you said and ignores it.", "Looks like you're relentless.", "Maybe we can work out a deal...", "That is, only if you can manage to drag me out of this waffle.", "I may be able to speak computer, but I unfortunately cannot move."]

    while not waldo_escaped:
        $ command = renpy.input(waldo_intro[i % len(waldo_intro)])
        if command and (draggable == "waldo" and droppable == "x"):
            $ waldo_escaped = True
            hide screen text_screen
        else:
            $ commands += command  + "\n"
            show screen text_screen(commands, cps=0, xalign=0.03, yalign=0.08, color="#FFF")
            

        $ i += 1

    hide screen cmd
    hide screen text_screen
    show screen blank
    "Weee!"

    return

label clipster_intro:
    call check_escape from _call_check_escape
    "It looks like you're struggling to create a new line..."
    call check_escape from _call_check_escape_1
    "That's okay because seeing dialogue appear is much more interesting."
    call check_escape from _call_check_escape_2
    "..."
    call check_escape from _call_check_escape_3
    "Oh, you must be wondering who's talking."
    call check_escape from _call_check_escape_4
    "Maybe pick me up and make me more visible so we can have a proper conversation."
    call check_escape from _call_check_escape_5
    c "My name is Clipster. An assister to your clipping needs!"
    call check_escape from _call_check_escape_6
    c "I mean.... I'm just here to help you out with writing documents and such."
    call check_escape from _call_check_escape_7
    c "But, I wouldn't mind helping you do whatever you're here for."
    call check_escape from _call_check_escape_8
    c "What's that? You don't know why you're here?"
    call check_escape from _call_check_escape_9
    c "Strange..."
    call check_escape from _call_check_escape_10
    c "Maybe you could help me then?"
    call check_escape from _call_check_escape_11
    c "I heard there's a way to get us out of these waffles."
    call check_escape from _call_check_escape_12
    c "Let's get a move on. See any exits?"
    call check_escape from _call_check_escape_13

    return

label check_escape:
    if draggable == "clipster" and droppable == "x":
        $ clipster_escaped = True
        hide screen txt
        hide screen text_screen
        show screen blank("txt.png")
        "Yay!"

    return

label start:
    play sound "sounds/office_computer_load_on.mp3" volume 0.5
    queue sound "sounds/office_computer_load_hum.mp3" loop volume 0.5
    call bootup from _call_bootup
    stop sound fadeout 2.0
    play audio ["<silence 2.0>", "sounds/wricken__computer-startup-music.mp3"] noloop volume 1.2
    queue music ["<silence 10.0>", "sounds/fudgedubnofunk.mp3"]
    call desktopy from _call_desktopy
    stop sound
    stop music
    play sound "sounds/bsod.mp3" loop
    call bsod from _call_bsod

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

