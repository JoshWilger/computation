﻿# This is the base image which displays the Mac OS8 window frame
image UI = "images/base.png"
# This is a plan white background that goes over the UI
image white = "images/white.png"
# This sets up an animation for a flashing arrow in the text box, you can change the image, animation speed, and location.
# Every character will need to have (ctc = "ctc_animation", ctc_position = "fixed") added in order to have the animation display.
image ctc_animation = Animation("images/ctcwhite.png", 0.5, "images/ctcblack.png", 0.5, xpos=0, ypos=0, xanchor=0, yanchor=0)

# Creates the narrator as a character to enable the ctc animation
define narrator = Character(ctc = "ctc_animation", ctc_position = "fixed")

define s = Character("Snippy")

image beast = "images/BEASTS/Beasts10.png"

# The game starts here.

label start:

    # Displays the background
    show UI onlayer master

    s "Hi there!"
    show beast at truecenter
    pause 0.1
    hide beast
    s "What was THAT?"
    s "Oh well."
    s "My name is Snippy!"
    $ x = renpy.input("What's your name?")
    s "Hi there, [x]!"

    return
