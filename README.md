# Automount
How the robot automounts and executes scripts on a USB stick

A basic explanation on how this works:

* The udev rule, found in 90-autorun.rules, specifies that the script should be ran, when something connects as one of the sd devices.
* The mounting script, mounting_script.sh, which has the connected sd kernel passed in as a variable. Which mounts the usb stick, runs main.py on the usb stick, and then unmounts it.
* The example main.py, which at the moment just creates a test file, with some test data.

##Save Locations

The files should not be saved together they should be saved in the following locations.
* 90-autorun.rules should be saved in /etc/udev/rules.d
* mounting_script.sh should be saved in /home/pi/automount, this can be changed as required.
* main.py should be saved on the root of the usb stick.


##To Do:

A list of what is planned:

- [x] MVP, script runs when usb is inserted and will run the script on the usb.
- [] Improvements to the example python, probably with an inclusion of the robot's library.
- [] Improvements to the mounting script, having it save an error to file main.py is not found on the usb, making it case insensitive.
