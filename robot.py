#Program: robot
#Description: Controls the robot via terminal with keyboard presses, using UP, DOWN, LEFT, RIGHT and ENTER for stop.
#Can also connect via SSH with Putty to control robot too
#Author: Matthew Wilson
#Student Number: EC1841586

#import curses packets used to read from keyboard
import RPi.GPIO as GPIO
import time
import curses

#Set the GPIO;s mode to Board
GPIO.setmode (GPIO.BOARD)

#Set the pin we want to use (7,13) and the purpose (input/output). 7,13 are forward.

GPIO.setup(7, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

#Pins 11, 15 are set for reverse.

GPIO.setup(11, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

#Get the curses window, turn off echoing of keytboard to screen, turn on
#instant key response and use special values for cursor keys

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)




try:
    while True:        
        char=screen.getch()        
        
        #q exits program and returns back to terminal
        if char == ord('q'):
            print ("Exiting")
            time.sleep(.5)
            break
        #Press DOWN arrow to reverse
        elif char == curses.KEY_DOWN:
            GPIO.output(11, True)
            GPIO.output(15, True)
            print ("DOWN")
        #Press UP arrow to move forward    
        elif char == curses.KEY_UP:
            GPIO.output (7, True)
            GPIO.output(13, True)            
            print ("UP")
        #Press LEFT arrow to turn left.    
        elif char == curses.KEY_LEFT:
            GPIO.output (13, True)
            print ("LEFT")
        #Press RIGHT arrow to turn right
        elif char == curses.KEY_RIGHT:
            GPIO.output (7, True)
            print ("RIGHT")
        #Press ENTER to stop robot.    
        elif char == 10:
            GPIO.output (7, False)
            GPIO.output(13, False)
            GPIO.output(11, False)
            GPIO.output(15,False)            
            print("stop")
finally:
    #Close down curses properly, including turn echo back on along with cleanup of all pins.
    curses.nocbreak(); screen.keypad(0); curses.echo(); curses.endwin()
    GPIO.cleanup()
    
