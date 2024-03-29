﻿# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False):

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice (NOTE: To customize appearance and how it's displayed, check the bottom of options.rpy)
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        left_padding 10
        right_padding 10
        top_padding 26
        bottom_padding 26

        draggroup:
            $ i = 0
            for caption, action, chosen in items:

                if action:
                    drag:
                        draggable True
                        drag_raise True
                        style "menu_choice_button" 
                        ymaximum 55
                        ypos (68 * i)
                        clicked action
                        # button style "menu_window" action action yminimum 30 ymaximum 30

                        text caption style "menu_choice"

                else:
                    drag:
                        text caption style "menu_caption"
                $ i += 1

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is input_prompt:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" color "#000" size 8 font "assets/ChicagoFLF.ttf"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    $ renpy.music.play("sounds/warm-anolog-tech-synth.mp3", channel="music", fadein=20.0, loop=True)
    
    #You can replace the default main menu here and reconfigure the hotspots for any buttons. Make sure to clear the cache afterwards.
    imagemap:
        ground "images/menuground.png"
        hover "images/menuhover.png"
        
        hotspot (128, 185, 66, 66) action Start()
        hotspot (196, 185, 66, 66) action ShowMenu("load")
        hotspot (264, 185, 66, 66) action ShowMenu("preferences")
        hotspot (332, 185, 66, 66) action Quit(confirm = False)

##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
# NOTE: Currently there is no button to delete saves, they instead must be deleted from the saves folder within the game file structure.
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker():

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"

            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save():

    # This ensures that any other menu screen is replaced.
    tag menu

    imagemap:
        ground "IMAGES/SAVEGROUND.png"
        idle "IMAGES/SAVEGROUND.png"
        hover "IMAGES/SAVEHOVER.png"
        cache False
        
        hotspot (256, 317, 30, 20) clicked FilePage(1)
        hotspot (290, 317, 30, 20) clicked FilePage(2)
        hotspot (324, 317, 30, 20) clicked FilePage(3)
        hotspot (358, 317, 30, 20) clicked FilePage(4)
        
        hotspot (38, 82, 222, 31) clicked FileSave(1):
            use load_save_slot(number=1)
        hotspot (38, 118, 222, 31) clicked FileSave(2):
            use load_save_slot(number=2)
        hotspot (38, 154, 222, 31) clicked FileSave(3):
            use load_save_slot(number=3)
        hotspot (38, 190, 222, 31) clicked FileSave(4):
            use load_save_slot(number=4)
        hotspot (38, 226, 222, 31) clicked FileSave(5):
            use load_save_slot(number=5)
        hotspot (38, 262, 222, 31) clicked FileSave(6):
            use load_save_slot(number=6)
        hotspot (265, 82, 222, 31) clicked FileSave(7):
            use load_save_slot(number=7)
        hotspot (265, 118, 222, 31) clicked FileSave(8):
            use load_save_slot(number=8)
        hotspot (265, 154, 222, 31) clicked FileSave(9):
            use load_save_slot(number=9)
        hotspot (265, 190, 222, 31) clicked FileSave(10):
            use load_save_slot(number=10)
        hotspot (265, 226, 222, 31) clicked FileSave(11):
            use load_save_slot(number=11)
        hotspot (265, 262, 222, 31) clicked FileSave(12):
            use load_save_slot(number=12)
        
        hotspot (460, 317, 30, 20) action Return()
        hotspot (222, 317, 30, 20) action ShowMenu('load')
        hotspot (426, 317, 30, 20) action MainMenu(confirm=True)
        hotspot (392, 317, 30, 20) action ShowMenu('preferences')

screen load():

    # This ensures that any other menu screen is replaced.
    tag menu

    imagemap:
        ground "IMAGES/loadground.png"
        idle "IMAGES/loadground.png"
        hover "IMAGES/loadhover.png"
        cache False
        
        hotspot (256, 317, 30, 20) clicked FilePage(1)
        hotspot (290, 317, 30, 20) clicked FilePage(2)
        hotspot (324, 317, 30, 20) clicked FilePage(3)
        hotspot (358, 317, 30, 20) clicked FilePage(4)
        
        hotspot (38, 82, 222, 31) clicked FileLoad(1):
            use load_save_slot(number=1)
        hotspot (38, 118, 222, 31) clicked FileLoad(2):
            use load_save_slot(number=2)
        hotspot (38, 154, 222, 31) clicked FileLoad(3):
            use load_save_slot(number=3)
        hotspot (38, 190, 222, 31) clicked FileLoad(4):
            use load_save_slot(number=4)
        hotspot (38, 226, 222, 31) clicked FileLoad(5):
            use load_save_slot(number=5)
        hotspot (38, 262, 222, 31) clicked FileLoad(6):
            use load_save_slot(number=6)
        hotspot (265, 82, 222, 31) clicked FileLoad(7):
            use load_save_slot(number=7)
        hotspot (265, 118, 222, 31) clicked FileLoad(8):
            use load_save_slot(number=8)
        hotspot (265, 154, 222, 31) clicked FileLoad(9):
            use load_save_slot(number=9)
        hotspot (265, 190, 222, 31) clicked FileLoad(10):
            use load_save_slot(number=10)
        hotspot (265, 226, 222, 31) clicked FileLoad(11):
            use load_save_slot(number=11)
        hotspot (265, 262, 222, 31) clicked FileLoad(12):
            use load_save_slot(number=12)
        
        hotspot (222, 317, 30, 20) action ShowMenu('save')
        hotspot (426, 317, 30, 20) action MainMenu(confirm=True)
        hotspot (392, 317, 30, 20) action ShowMenu('preferences')
        hotspot (460, 317, 30, 20) action Return()
        
screen load_save_slot:
    $ file_text = "% 2s. %s\n%s" % (
        FileSlotName(number, 12),
        FileTime(number, empty=_("Empty Slot")),
        FileSaveName(number))

    text file_text xpos 37 ypos 10 size 8 color "#000000" font "ASSETS/M 8pt.ttf"
    
    key "save_delete" action FileDelete(number)

##############################################################################
# Preferences
#
# NOTE: The only Preferences that are enabled are Music Volume, Sound Volume, and Text Speed.
# You can implement any others you may need by adding the appropriate buttons/sliders/bars.
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    tag menu

    imagemap:
        ground "IMAGES/PREFGROUND.png"
        idle "IMAGES/PREFGROUND.png"
        hover "IMAGES/PREFHOVER.png"
        
        hotspot (460, 317, 30, 20) action Return()
        hotspot (392, 317, 30, 20) action ShowMenu('save')
        hotspot (426, 317, 30, 20) action MainMenu(confirm=True)
        
        bar pos (77, 91) value Preference("music volume") style "pref_slider"
        bar pos (77, 123) value Preference("sound volume") style "pref_slider"
        bar pos (77, 155) value Preference("text speed") style "pref_slider"


init -2 python:
    
    style.pref_slider.left_bar = "IMAGES/BAR.png"
    style.pref_slider.right_bar = "IMAGES/BAR.png"
    
    style.pref_slider.xmaximum = 104
    style.pref_slider.ymaximum = 13
    
    style.pref_slider.thumb = "IMAGES/TAB2.png"
    style.pref_slider.thumb_offset = 5
    style.pref_slider.thumb_shadow = None
    
##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True

    if message == layout.OVERWRITE_SAVE:

        imagemap:
            ground "images/overwriteground.png"
            hover "images/overwritehover.png"
        
            hotspot (354, 229, 80, 20) action yes_action
            hotspot (262, 229, 80, 20) action no_action

    elif message == layout.QUIT:

        imagemap:
            ground "images/quitground.png"
            hover "images/quithover.png"
        
            hotspot (354, 229, 80, 20) action yes_action
            hotspot (262, 229, 80, 20) action no_action        

    else:

        imagemap:
            ground "images/yesground.png"
            hover "images/yeshover.png"
        
            hotspot (354, 229, 80, 20) action yes_action
            hotspot (262, 229, 80, 20) action no_action


##############################################################################
# Quick Menu
#
# NOTE: This has been disabled, but feel free to reimplement.
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.

screen quick_menu():

#     Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"

screen text_screen(arg="Click to Continue", cps=20, xalign=0.0, yalign=0.0, color="#000"):

    zorder 100

    text _(arg):
        size 9
        font "assets/ChicagoFLF.ttf"
        color color
        xalign xalign
        yalign yalign
        slow_cps cps

screen desktop(loading=0.0):
    tag menu
    
    imagemap:
        ground "images/cyan.png"
        idle "images/cyan.png"
        hover "images/cyan.png"

        image "images/choicehover.png" yzoom 1.6 xzoom 2.45 xalign 0.5 yalign 1.021 delay loading
        # pause 0.1
        image "images/BUTTONS & MENUS/RECTANGLE BUTTON SHADOW.png" xalign 0.005 yalign 0.993 delay loading
        # pause 0.1
        image "images/tab.png" xzoom 0.4 yzoom 0.8 xalign 0.2 yalign 0.985 delay loading
        # pause 0.1
        image "choiceground.png" xzoom 0.2 xalign 0.995 yalign 0.993 delay loading
        # pause 0.1
        $ now = datetime.now().strftime("%H:%M")
        text "[now]":
            xalign 0.98 # 0.984
            yalign 0.98 # 0.984
        # pause 0.1

        if waldo_escaped and clipster_escaped:
            text "You Win!" at truecenter size 30

screen files(type):
    modal True
    
    imagemap:
        ground "IMAGES/base.png"
        idle "IMAGES/base.png"
        hover "IMAGES/base.png"
        
        hotspot (500, 1, 20, 20) action Call("desktopy")
        image "images/ASSORTED ICONS/39.png" zoom 0.5 xalign 0.99 yalign 0.01

screen txt(content, save_action):
    modal True

    # key "mouseup_3" action Show()

    imagemap:
        ground "IMAGES/base.png"
        idle "IMAGES/base.png"
        hover "IMAGES/base.png"
        
        hotspot (500, 1, 20, 20) action [save_action, Jump("desktopy")]
        image "txt.png"
        draggroup:
            drag:
                drag_name "x"
                draggable False
                droppable True
                xpos 503 
                ypos 3
                image "images/ASSORTED ICONS/39.png" zoom 0.5 xalign 0.99 yalign 0.01

            drag:
                drag_name "clipster"
                draggable True 
                dragged drag_placed
                xpos 222 
                ypos 51
                image "images/COMMUNICATION/Communication2.png" zoom 0.5

        input color "#000" size 8 font "assets/ChicagoFLF.ttf" xpos 175 ypos 82 xmaximum 217 ymaximum 200 default content id "id"

screen cmd(character):
    modal True

    imagemap:
        ground "IMAGES/base.png"
        idle "IMAGES/base.png"
        hover "IMAGES/base.png"
        
        hotspot (500, 1, 20, 20) action Jump("desktopy")
        image "black.png"
        draggroup:
            drag:
                drag_name "x"
                draggable False
                droppable True
                xpos 503 ypos 3
                image "images/ASSORTED ICONS/39.png" zoom 0.5 #xalign 0.99 yalign 0.01

            drag:
                drag_name "waldo"
                draggable True
                dragged drag_placed
                ymaximum 55
                xpos 453 
                ypos 304
                image "images/MAC SYSTEM/184.png" 

screen blank(name="black.png", txt="", save_action=None):
    modal True
    
    imagemap:
        ground "IMAGES/base.png"
        idle "IMAGES/base.png"
        hover "IMAGES/base.png"
        
        hotspot (500, 1, 20, 20) action If(save_action, true=[save_action, Jump("desktopy")], false=Jump("desktopy"))
        image "images/ASSORTED ICONS/39.png" zoom 0.5 xalign 0.99 yalign 0.01

        image name
        text txt color "#000" size 8 font "assets/ChicagoFLF.ttf" xpos 175 ypos 82 xmaximum 217 ymaximum 200

screen menu_please:
    on "show" action MainMenu(confirm=False)

init python:
    from datetime import datetime

    config.keymap['game_menu'].remove('mouseup_3')

    def save_welcome():
        persistent.welcome_txt = renpy.get_displayable("txt", "id").content
        renpy.save_persistent()
    def save_ipsum():
        persistent.ipsum_txt = renpy.get_displayable("txt", "id").content
        renpy.save_persistent()
    def save_blank():
        persistent.blank_txt = renpy.get_displayable("txt", "id").content
        renpy.save_persistent()

    def drag_placed(drags, drop):
        if not drop:
            return
        
        store.draggable = drags[0].drag_name
        store.droppable = drop.drag_name

        return True
