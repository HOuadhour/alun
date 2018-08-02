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

import subprocess
import os

class PackageInstaller():
    def __init__(self):
        pass

    # Set the name of your program.
    def setName(self, name):
        # name, is the name of your desktop icon program
        # It can contain spaces (e.g Open Broadcast Studio)
        # will be used to generate a .desktop file
        self.name = name
    
    # Set the generic name of your program.
    def setGenericName(self, genericName):
        # genericName, is another name that describes your program role.
        # In instance Firefox is a [Web browser].
        # will be used to generate a .desktop file.
        self.genericName = genericName

    # Set the exec path file of your program.
    def setExecPath(self, execPath):
        # execPath, is the executable file's path of your program.
        # will be used to generate a .desktop file.
        self.execPath = execPath

    # Set the icon's path of your program. 
    def setIconPath(self, iconPath):
        # iconPath, is the icon's path of your desktop program.
        # will be used to generate a .desktop file.
        self.iconPath = iconPath

    # Set the binary name of your program.
    def setBinaryName(self, binaryName):
        # binaryName, is the name of your executable program command
        # it will be located inside /usr/local/bin
        # binary name must not contains space.
        # It is not recommended to use special characters except
        # The underscore _ and the dash -
        # The execute attribute will be added automatically
        self.binaryName = binaryName

    # Set the source directory of your program.
    def setSource(self, source):
        # source, is the directory which contains all the necessary files.
        # The source directory will be copied to the destination directory.
        self.source = source

    # Set the installation directory path of your program.
    def setDestination(self, destination):
        # destination, where we will install the program.
        # Absolute path is the recommended one.
        # Use relative only if you know what are you doing.
        # if the chosen destination is already there, it will be overwritten.
        # will be used with the name of your source firectory as Path in .desktop file
        self.destination = destination

    # Set the dependencies packages name of your program.
    def setDependencies(self, dependencies):
        # dependencies is a list of packages names.
        # dependencies = ["pacman", "pacman-contrib", "python-pyqt5"]
        # Package name, is the name of the package on the official arch repo not AUR.
        self.dependencies = dependencies

    # Set the services to be enabled or started for your program.
    def setServices(self, services):
        # services is a list of services names.
        # services = ["dhcpcd", "cronie", "sshd"]
        # Service name, is the systemd service name.
        self.services = services 

    # Create a .desktop file of your program.
    def createDesktop(self):
        # Get the name of your program directory
        directory = self.source.split("/")[-1]
        path = self.destination + "/{}".format(directory)
        text = "[Desktop Entry]\n"
        text += "Encoding=UTF-8\n"
        text += "Type=Application\n"
        text += "Name={}\n".format(self.name)
        text += "GenericName={}\n".format(self.genericName)
        text += "Comment={}\n".format(self.name)
        text += "Icon={}\n".format(self.iconPath)
        text += "Exec={}\n".format(self.execPath)
        text += "Path={}\n".format(path)
        
        home = os.getenv("HOME")
        home += "/.local/share/applications"
        filename = home + "/{}.desktop".format(self.binaryName)

        self.printInfo(">>> Creating the desktop file...")
        desktop = open(filename, "w")
        desktop.writelines(text)
        desktop.close()
        self.printSuccess(">>> Desktop file has been created successfully.")
        
        self.printInfo(">>> Adding the execute attribute to the desktop file...")
        cmdOutput = subprocess.run(["chmod", "a+x", filename], 
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if cmdOutput.returncode == 0:
            self.printSuccess(">>> The execute attribute has been added successfully.")
        else:
            self.printError(
                "An error has been occurred while adding the execute attribute")

    # Create program command so we can execute it from the terminal.
    def createBinary(self):
        self.printInfo(">>> Linking your executable file to [/usr/local/bin]...")
        if os.path.islink("/usr/local/bin/{}".format(self.binaryName)):
            self.printInfo(">>> Deleting your old executable link...")
            cmdOutput = subprocess.run(["sudo", "-p", "Please enter your user password: ",
                                        "rm", "-rf",
                                        "/usr/local/bin/{}".format(self.binaryName)],
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if cmdOutput.returncode == 0:
                self.printSuccess(">>> Old executable link has been deleted successfully")
            else:
                self.printError(
                    "An error has been occurred while deleting the old executable link.")
        directory = self.source.split("/")[-1]
        path = self.destination + "/{}".format(directory)
        text = "#!/usr/bin/bash\ncd {}\npython {}".format(path, self.execPath)
        start = open("/tmp/start.sh", "w")
        start.writelines(text)
        start.close()

        cmdOutput = subprocess.run(["sudo", "-p", "Please enter your user password: ",
                                    "cp", "-r", "/tmp/start.sh", path],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        cmdOutput = subprocess.run(["sudo", "-p", "Please enter your user password: ",
                                    "chmod", "a+x", "{}/start.sh".format(path)],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        cmdOutput = subprocess.run(["sudo", "-p", "Please enter your user password: ",
                                    "ln", "-s", "{}/start.sh".format(path),
                                    "/usr/local/bin/{}".format(self.binaryName)],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if cmdOutput.returncode == 0:
            self.printSuccess(
                ">>> Executable file has been linked successfully.")
        else:
            self.printError(
                "An error has been occurred while linking the executable file.")

    # Create uninstall command to uninstall the program
    def createUninstaller(self, gui=False):
        self.printInfo(">>> Creating the uninstall file...")
        directory = self.source.split("/")[-1]
        path = self.destination + "/{}".format(directory)
        text = "#!/usr/bin/bash\n"
        text += "sudo rm -rf {}\n".format(path)
        text += "sudo rm -rf /usr/local/bin/{}\n".format(self.binaryName)
        text += "sudo rm -rf /usr/local/bin/{}-uninstall\n".format(
            self.binaryName)
        if gui:
            text += "sudo rm -rf $HOME/.local/share/applications/{}.desktop".format(
                self.binaryName
            )
        uninstaller = open("/tmp/uninstall.sh", "w")
        uninstaller.writelines(text)
        uninstaller.close()

        cmdOutput = subprocess.run(["sudo", "-p", "Please enter your user password: ",
                                    "cp", "-r", "/tmp/uninstall.sh", path],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        cmdOutput = subprocess.run(["sudo", "-p", "Please enter your user password: ",
                                    "chmod", "a+x", "{}/uninstall.sh".format(path)],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        cmdOutput = subprocess.run(["sudo", "-p", "Please enter your user password: ",
                                    "ln", "-sf", "{}/uninstall.sh".format(path),
                                    "/usr/local/bin/{}-uninstall".format(
                                        self.binaryName)],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if cmdOutput.returncode == 0:
            self.printSuccess(
                ">>> Uninstall file has been created successfully.")
        else:
            self.printError(
                "An error has been occurred while creating the uninstall file.")

    # Install your program to the destination directory.
    def startInstall(self):
        directory = self.source.split("/")[-1]
        path = self.destination + "/{}".format(directory)
        self.printInfo(">>> Copying files to [{}]...".format(path))
        if os.path.exists(path):
            self.printInfo(">>> Deleting your old installation directory...")
            cmdOutput = subprocess.run(["sudo", "-p", "Please enter your user password: ", 
                                        "rm", "-rf", path],
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if cmdOutput.returncode == 0:
                self.printSuccess(
                    ">>> Old installation directory has been deleted successfully")
            else:
                self.printError(
                    "An error has been occurred while deleting the old installation directory.")

        cmdOutput = subprocess.run(["sudo", "-p", "Please enter your user password: ",
                                    "cp", "-r", self.source, path],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if cmdOutput.returncode == 0:
            self.printSuccess(">>> All files has been copied successfully.")
            self.printInfo(
                ">>> Adding the execute attribute to your program file...")
            cmdOutput = subprocess.run(["sudo", "-p", "Please enter your user password: ",
                                        "chmod", "a+x", self.execPath],
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if cmdOutput.returncode == 0:
                self.printSuccess(
                    ">>> The execute attribute has been added successfully to your file.")
            else:
                self.printError(
                    "An error has been occurred while adding the execute attribute.")
        else:
            self.printError(
                "An error has been occurred while copying the files.")

    # Check if a systemd service is already enabled or not
    def serviceEnabled(self, service):
        cmdOutput = subprocess.run(["systemctl", "is-enabled", service], 
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if cmdOutput.returncode == 0:
            return True
        return False

    # Check if a systemd service is already started or not.
    def serviceStarted(self, service):
        cmdOutput = subprocess.run(["systemctl", "is-active", service], 
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if cmdOutput.returncode == 0:
           return True
        return False

    # Enable systemd services.
    def enableServices(self):
        self.printInfo(">>> Checking for enabled services...")
        for service in self.services:
            if self.serviceEnabled(service):
                self.printSuccess(
                    ">>> [{}] is already enabled on your machine.".format(service))
            else:
                self.printInfo(">>> Enabling [{}]...".format(service))
                cmdOutput = subprocess.run(["sudo", "-p", "Please enter your user password: ", 
                                            "systemctl", "enable", service], 
                                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if cmdOutput.returncode == 0:
                    self.printSuccess(">>> [{}] has been enabled successfully.".format(service))

                else:
                    self.printError("An error has been occurred while enabling the service.")
                    self.printError("Please try to run the command manually later.")
                    self.printError("sudo systemctl enable {}".format(service))

    # Start systemd services.
    def startServices(self):
        self.printInfo(">>> Checking for started services...")
        for service in self.services:
            if self.serviceStarted(service):
                self.printSuccess(
                    ">>> [{}] is already started on your machine.".format(service))
            else:
                self.printInfo(">>> Starting [{}]...".format(service))
                cmdOutput = subprocess.run(["sudo", "-p", "Please enter your user password: ", 
                                        "systemctl", "start", service], 
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if cmdOutput.returncode == 0:
                    self.printSuccess(">>> [{}] has been started successfully.".format(service))
                else:
                    self.printError("An error has been occurred while starting the service.")
                    self.printError("Please try to run the command manually later.")
                    self.printError("sudo systemctl start {}".format(service))
    
    # Install packages using pacman.
    # Used as a dependency installer.
    def installPackages(self):
        self.printInfo(">>> Checking for dependencies...")
        for package in self.dependencies:
            if self.packageInstalled(package):
                self.printSuccess(
                    ">>> [{}] is already installed on your machine.".format(package))
            else:
                self.printInfo(">>> Installing {}...".format(package))
                cmdOutput = subprocess.run(["sudo", "-p", "Please enter your user password: ", 
                                            "pacman", "-Syq","--noconfirm", package], 
                                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if cmdOutput.returncode == 0:
                    self.printSuccess(
                        ">>> [{}] has been installed successfully.".format(package))

                else:
                    self.printError(
                        "An error has been occurred during the installation of [{}].".format(package))
                    self.printError(
                        "Please check your connection availability.")

    # Check if a package is already installed or not.
    # Used as a dependency verifier.
    def packageInstalled(self, package):
        cmdOutput = subprocess.run(["pacman", "-Qq", package], stdout=subprocess.PIPE, 
                                   stderr=subprocess.PIPE)
        if cmdOutput.returncode == 0:
            return True
        return False

    # Print an error message colored with red/pink.
    def printError(self, message):
        # Linux command to change the color of the font.
        os.system("tput setaf 197")
        print(message)
        os.system("tput sgr0")

    # Print a success message colored with green/yellow.
    def printSuccess(self, message):
        os.system("tput setaf 76")
        print(message)
        os.system("tput sgr0")

    # Print an info message colored with blue.
    def printInfo(self, message):
        os.system("tput setaf 27")
        print(message)
        os.system("tput sgr0")
