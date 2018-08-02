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

from HOPkger import PackageInstaller
import os
import subprocess

# Initiate and create your package installer
alun = PackageInstaller()

# .desktop file information (GUI Programs only).
# alun.setName()
# alun.setGenericName()
# alun.setIconPath()

# Both CLI and GUI programs.
alun.setSource(os.getcwd()+"/ALUN")
alun.setDestination("/opt")
alun.setBinaryName("alun")
alun.setExecPath("/opt/ALUN/alun.py")

# Set dependencies of your program
dependencies = ["pacman-contrib", "cronie"]
alun.setDependencies(dependencies)
alun.installPackages()

# Set services needed for your program
services = ["cronie"]
alun.setServices(services)

# Uncomment only if you need to enable the service
alun.enableServices()

# Uncomment only if you need to start the service
alun.startServices()

# Start your installation
alun.startInstall()

# Create your executable command, run program from terminal
# (Both CLI and GUI programs)
alun.createBinary()

# Create your desktop program file (Only for GUI programs)
# alun.createDesktop()

# Create your uninstall command, alun-uninstall
alun.createUninstaller(gui=False)

###############################################
#### THIS CODE DOES NOT BELONGS TO HOPkger ####
###############################################

terminals = ["gnome-terminal", "konsole", "urxvt", "xterm", "mate-terminal",
             "xfce4-terminal", "terminator"]

# get the current open terminal from ths list.
# if two terminals are open get the first one.
# check with pgrep if we a PID, it means the terminal is open

term = None
for terminal in terminals:
    cmdOutput = subprocess.run(["pgrep", terminal],
                              stdout = subprocess.PIPE,
                              stderr = subprocess.PIPE)
    if cmdOutput.stdout.decode("utf-8").rstrip().isdigit():
        term = terminal

os.system("sudo sed -i -e 's/konsole/{}/g' /opt/ALUN/term".format(term))
os.system("sudo crontab -u $USER /opt/ALUN/crontabFile")
