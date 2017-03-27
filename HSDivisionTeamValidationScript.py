##Elizabeth E. Esterly
##The University of New Mexico
##NASA Swarmathon HS Division 2017
##team validation script beta 1.0
##last revised 03/23/2017

#Python 2.7.12

from py4j.java_gateway import JavaGateway
from os import listdir
import sys

global name
name = sys.argv[1]

def checkFor(code):
    if code in open(name).read():
        illegalCommandError(code)
    else:
        ok()
    
def illegalCommandError(command):
    print "WARNING! Illegal command " + command + " found.\n"

def ok():
    print "OK\n\n"

def genericError(errorMsg):
    print "WARNING! " + errorMsg

#RULES
#3 rounds
#3600 ticks
#512 resources
#Use this script to check if your code violates any rules specified in [Sw5] before submitting your code for the competition. The code will run with whatever values you have set on the slider bars.
#Put your netlogo file in the same directory with the files used here.
#Run this script from the command line: python HSDivisionTeamValidationScript.py yourfilename.nlogo 

#open bridge to Netlogo
gw = JavaGateway()
bridge = gw.entry_point

#get file info and open it
print "This script checks for rules violations in your program.\n If you are unclear on the rules, please review them in [Sw5].\n"
print "Opening" + name + ".\n"
if not name.endswith("_sw17.nlogo"):
    print "Your file is named incorrectly.\n"
else:
    ok()

#cleaning operations
cleaned = open('tested_' + name, 'w')
with open (name, 'r+') as f:
    while (True):
        c = f.readline()
        if "bitmap:copy-to-pcolors bitmap:import \"parkingLot.jpg\" true\n" not in c and "extensions[bitmap]\n" not in c:
            cleaned.write(c)
        if not c:
            break
    cleaned.close()

#open and setup the file
print "Testing setup functions...\n"
bridge.openModel('tested_' + name)
bridge.command("random-seed 1988")
bridge.command("setup")

#6 robots
print "Test for exactly 6 robots: "
agentCount = bridge.report("count turtles")
print agentCount
if agentCount != 6:
    genericError("You must have 6 robots.\n\n")
else:
    ok()

#robots spawn at the origin
print "Test for robots spawning at origin.\n"
notAtOrigin = bridge.report("count turtles with [xcor != 0 and ycor != 0]")
if notAtOrigin > 0:
    print str(notAtOrigin) + " robots were not spawned at (0, 0)."
    genericError("All 6 robots must begin at (0,0).\n\n")
else:
    ok()

#world size: max-pxcor = max-pycor = 50 and min-pxcor = min-pycor = -50
print "Test world size.\n"
maxX = bridge.report("max-pxcor")
minX = bridge.report("min-pxcor")
maxY = bridge.report("max-pycor")
minY = bridge.report("min-pycor")
if maxX != 50 or maxY != 50 or minX != -50 or minY != -50:
    print genericError("Your max x and y should be 50 and your min x and y should be -50.\n\n")
else:
    ok()

#Check for illegal commands in the file:
print "Checking for illegal commands...\n"
illegalCommands = ['move-to', 'setxy', 'hatch', 'die', 'sprout']
fileProblem = False
for i in illegalCommands:
    print i
    if checkFor(i):
        fileProblem = True

if fileProblem:
    genericError("Please remove the illegal commands in your program.\n")

#robot-control, run for 3600 ticks
print "Running program for 3600 ticks.\n"
for i in range (0, 3600):
    bridge.command("robot-control")
print "Complete."
bridge.closeModel()
gw.shutdown()









