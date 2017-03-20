##Elizabeth E. Esterly
##The University of New Mexico
##NASA Swarmathon HS Division 2017
##team validation script
##last revised 03/17/2017

#Python 2.7.12

from py4j.java_gateway import JavaGateway
from os import listdir
import sys

global name
name = sys.argv[1]
print name

def checkFor(code):
    if code in open(name).read():
        illegalCommandError(code)
    else:
        ok()
    
def illegalCommandError(command):
    print "WARNING! Illegal command " + command + "found.\n"

def ok():
    print "OK\n"

def genericError(errorMsg):
    print "WARNING! " + errorMsg

#RULES
#3 rounds
#3600 ticks
#512 resources
#Use this script to check if your code violates any rules specified in [Sw5] before submitting your code for the competition. The code will run with whatever values you have set on the slider bars.
#Put your netlogo file in the same directory with the files used here.
#Run this script from the command line: python HSDivisionTeamValidationScript.py -yourfilename.nlogo- 

#open bridge to Netlogo and set random seed
gw = JavaGateway()
bridge = gw.entry_point
bridge.openModel(name)
bridge.command("random-seed 1988")

#get file info and open it

print "Opening" + name + ".\n"

#setup the file
print "Testing setup function...\n"
bridge.command("setup")
bridge.exportView("ttt")

#6 robots
print "Test for exactly 6 robots: "
agentCount = bridge.report("count turtles")
print agentCount
if agentCount != 6:
    genericError("You must have 6 robots.\n")
else:
    ok()

#robots spawn at the origin
print "Test for robots spawning at origin.\n"
atOrigin = bridge.report("count turtles with [xcor != 0 and ycor != 0]")
print atOrigin
if atOrigin == "illegal placement":
    genericError("All 6 robots must begin at (0,0).\n")
else:
    ok()

#world size: max-pxcor = max-pycor = 50 and min-pxcor = min-pycor = -50
print "Test world size.\n"
maxX = bridge.report("max-pxcor")
minX = bridge.report("min-pxcor")
maxY = bridge.report("max-pycor")
minY = bridge.report("min-pycor")
if maxX != 50 or maxY != 50 or minX != -50 or minY != -50:
    print genericError("Your max x and y should be 50 and your min x and y should be -50.\n")
else:
    ok()

#Check for illegal commands in the file:
print "Checking for illegal commands:\n\n"
illegalCommands = ['move-to', 'setxy', 'hatch', 'die', 'sprout']
fileProblem = False
for i in illegalCommands:
    if checkFor(i):
        fileProblem = True

if fileProblem:
    genericError("Please remove the illegal commands in your program.\n")

#robot-control, run for 3600 ticks
print "Running program for 3600 ticks.\n"
#for i in range (0, 3600):
#    bridge.command("robot-control")

#export stats and a view of the screen when finished







