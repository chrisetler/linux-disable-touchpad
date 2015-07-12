# How To Toggle the Touchpad with a Keybinding on Linux
Hello, and welcome. I recently bought an old ThinkPad x220, and while the keyboard and trackpoint are absolutely amazing,
I'm not a big fan of the touchpad and have found it to be constantly activating accidentally
even though I have palm detection enabled. Since I hardly ever use it I decided to just disable it and create a key combo
in case I ever want to use it again. This guide will show you how to create a script to toggle the touchpad on a linux system, and then bind that script to a key combination. I will be using Ubuntu 14.04 with the following packages/languages:

1. xbindkeys
2. xinput
3. python

For me, xinput and python were already installed, and xbindkeys is in the Ubuntu Software Center.

## Step 1. Setting Up xbindkeys

The first thing you will want to do is install xbindkeys a la `sudo apt-get install xbindkeys`.
Once you have xbindkeys, you will want to create a config file in your home directory
by typing `xbindkeys -d > ~/.xbindkeysrc`. This will create a config file with the default settings,
where you can add your custom key binding. The way you add a keybinding is as follows:
```
"command"
keys
```

So to create a binding to open gedit using Ctrl+g, you would write
```
"gedit"
ctrl + g
```

To get the exact code for each key type `xbindkeys -k` into the command line, followed by the key you want to use, and it
will return the corresponding code. Ignore any Mod1, Mod2, etc, as those are codes for CapsLock, NumLock, etc, and are by default
ignored.

## Step 2. The script

I have uploaded the python script needed to toggle the touchpad on and off as `script.py`, so for the most part all you
need to do is download it and set that as the command. You will however likely have to change the device number. On my laptop,
the device is number 11. To find out what is is, go into the command line and type `xinput` and find the id for the touchpad.
It's that simple. Once you have it, edit `script.py` and change `DEVICE_NUM = '11'` to the proper id number. Make sure to keep the quotes. Next, use `chmod` to make the script executable. Once you have done this simply add the command (something like `~/script.py`) and key combo. Finally, reset xbindkeys by simply running `xbindkeys` and you should be good to go.

If that does not work, try reseting your computer, and the new config should be loaded when you log in. If there is still an issue, try executing the script directly and see if it produces any errors.
