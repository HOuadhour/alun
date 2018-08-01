#!/usr/bin/python3

"""This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>."""

# Copyright (c) 2018, Muhammad Al-Habib Ouadhour

# Email: HOuadhour@yandex.com
# LinkedIn: linkedin.com/in/HOuadhour
# Twitter: twitter.com/HOuadhour
# Telegram: @HOuadhour
# Github: github.com/HOuadhour

import os
import subprocess

class updateNotifier():
    """Check if there are updates available.
    Notify the user if so.
    """
    def __init__(self):
        self.updateCmd = "sudo pacman -Syu --noconfirm"
        self.terminals = {}
        self.terminals["konsole"] = "konsole -e " + self.updateCmd
        self.terminals["lxterminal"] = "lxterminal -e " + self.updateCmd
        self.terminals["gnome-terminal"] = "gnome-terminal -e " + \
                self.updateCmd
        self.terminals["xfce4-terminal"] = "xfce4-terminal -e " + \
                self.updateCmd
        self.terminals["mate-terminal"] = "mate-terminal -e " + \
                self.updateCmd
        self.terminals["terminator"] = "terminator -e " + self.updateCmd

    
    def checkUpdate(self):
        cmdOutput = subprocess.run("checkupdates",
                                   stdout = subprocess.PIPE,
                                   stderr = subprocess.PIPE)
        self.packages = cmdOutput.stdout.decode("utf-8").rstrip().split("\n")

        if len(self.packages) == 1 and len(self.packages[0]) != 0:
            self.notifyUser("There is 1 update available.")
            return True
        
        elif len(self.packages) > 1:
            self.notifyUser("There are {} updates available.".format(
                len(self.packages)))
            return True
        return False
    
    def notifyUser(self, message):
        os.system("notify-send -u normal -t 10000 'ALUN' '{}'"\
                  .format(message
                  ))

    def startUpdate(self, term):
        print("Start upgrading your os...")
        os.system(self.terminals[term])
        self.notifyUser("Your system has been upgraded successfully.")
        quit = input("Press enter to quit ...")

    def getCurrentTerm(self):
        data = open("/opt/ALUN/term", "r").readline().rstrip()
        return data



update = updateNotifier()
term = update.getCurrentTerm()
if update.checkUpdate():
    update.startUpdate(term)

