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
        self.updateCmd = "sudo -p 'Type your password to start the update: ' pacman -Syu --noconfirm"
    
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

    def startUpdate(self):
        # change to the configuration directory
        # only needed in the installation package
        # os.chdir("/etc/alun")
        import conf
        self.term = conf.terminal
        cmd = "{} -e {}".format(self.term, self.updateCmd)
        os.system(cmd)

update = updateNotifier()
if update.checkUpdate():
    update.startUpdate()

