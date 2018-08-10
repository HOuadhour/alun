# ALUN
> ArchLinux Update Notifier

# Getting Started

ALUN is a script written in `python3`, created to help you keep your Arch
updated.

* `alun` uses `crontab` to autorun the script every 30 minutes (default).
* `alun` will automatically open the terminal for you, and all you need is to
  enter your password.
* ALUN uses the native notification to notify you when there is an update.
* ALUN uses `checkupdates` to check for updates.
* Default terminal is `konsole`.
* Default configuration file located inside `/etc/alun/conf.py` 

# Pre-Installation
* You need to install `git` to clone the repo.
```bash
$ sudo pacman -Sy git --needed
```
* Add the public key for signature verification.
```bash
$ gpg --receive-keys 6481A7A3E66A3AA39D0DD7302A60AB408C14BF70
```

# Installation
The installation process is too simple all you have to do is:
* Clone the repo.
* Build the package and install.

## Cloning the repo
```bash
$ git clone https://aur.archlinux.org/alun.git /tmp/alun
```

## Building and Installing
```bash
$ cd /tmp/alun
$ makepkg -si
```

# Post-Installation
After the installation you may want.

## Changing default terminal
* Open `/etc/alun/conf.py` with your preferred text editor as root.
* Change the `terminal` variable to your preferred `terminal`.
* **Note: Do not change the variable name itself, change `konsole`.**

## Adding crontab (Necessary)
### Create a new crontab
* This method will overwrite your old crontab if you alread have one.
```bash
$ crontab /etc/alun/crontab
```
### Appending to old crontab
* This method will append the crontab to your old one.
* You want lose your old crontab.
```bash
$ cat /etc/alun/crontab >> /var/spool/cron/$USER
```
# Configuration
Currently there is no configuration everything is manual.

# Connect with me

* [LinkedIn](https://www.linkedin.com/in/HOuadhour)
* [Twitter](https://www.twitter.com/HOuadhour)
* [Telegram](https://t.me/Houadhour)
