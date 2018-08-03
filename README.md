# ALUN
> ArchLinux Update Notifier

# Getting Started

ALUN is a script written in `python3`, created to help you keep your Arch
updated.

* ALUN uses `crontab` to autorun the script every 30 minutes.
* ALUN will automatically open the terminal for you, and all you need is to
  enter your user password.
* ALUN uses the native notification to notify you when there is an update.
* ALUN uses `checkupdates` to check for updates.
* Default installation path is in `/opt/ALUN`.

# Installation
The installation process is too simple all you have to do is:
* Clone or download the current repository.
* Launch the `install.py` script.

## Clone method
```bash
$ cd /tmp
$ git clone https://github.com/HOuadhour/ALUN.git
$ python install.py
```

# Configuration
No configuration is required, but let's say you want to change the default
terminal.
<br />
Or simply you would like to change the time interval from every 30 minutes to
another time.

## Changing terminal
There is a file called `term` inside the installation directory.
<br />
Change it to the terminal you like.
> Change the terminal name inside `term` after the installation.

## Changing time
Changing the time requires knowledge about `crontab` syntax.
<br />
Type the following command inside your terminal.
```bash
$ crontab -e
```

# Connect with me

* [LinkedIn](https://www.linkedin.com/in/HOuadhour)
* [Twitter](https://www.twitter.com/HOuadhour)
* [Telegram](https://t.me/Houadhour)
