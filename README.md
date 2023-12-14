# Skee-Ball

This repository contains all code for our PIE Skeeball project. The code in C++ is
run in the Arduino IDE, and it reads sensor data and serially transmits it to
Python. The Arduino code is also responsible for controlling the motors that
are part of the ball return mechanism. 

The Python code is mainly responsible for the display. The display was created
using the Pygame library. The Python script also parses the binary array message
sent by the IDE. An important note when running the code is that in order
for serial communication to be effective, the Arduino code must be uploaded to
the Arduino, the IDE window must be closed, and then the Python script should
be run. If the IDE window and the Python window are both open, serial communication
will not work. 

## Installation Instructions
In order to play the game, run pip install -r requirements.txt. Make sure to copy the
Arduino code into the Arduino IDE. After that, clone this repository, run the
skee_ball.py file and enjoy!

Have fun!
