##Elizabeth E. Esterly
##The University of New Mexico
##NASA Swarmathon HS Division 2017
##autorun
##last revision 03/08/2017

#INPUT: python swarmathon2017autorun.py -path to folder of submissions to be processed- -path to text file to record results-


from py4j.java_gateway import JavaGateway
from os import listdir
import sys

def setupRun():
    bridge.command("setup")
    bridge.command("ask patches [set pcolor black]")
    bridge.command("resize-world -50 50 -50 50") ##force set world size

def makeRandomDistribution():
    bridge.command("ask n-of 500 patches [if pcolor != yellow [set pcolor yellow]]")

def makeSquareDistribution():
    bridge.command("ask patches with [pxcor > 30 and pycor > 25] [set pcolor yellow]")

def makeNASALogo():
    #make circle
    bridge.comand("ask patches with [distancexy 0 0 < 40 and distancexy 0 0 > 39][set pcolor yellow]")
   
    #make N 
    bridge.command("ask patches with [pxcor = -30 and pycor >= -8 and pycor <= 8] [set pcolor yellow]")
    bridge.command("ask patches with [pxcor = -20 and pycor >= -8 and pycor <= 8] [set pcolor yellow]")
    bridge.command("ask patches with [pycor >= -1.6  * pxcor + -40 and pycor <= -1.6 * pxcor - 38 and pycor >= -8 and pycor <= 8][set pcolor yellow]")
    
    #make A
    bridge.command("ask patches with [pycor >= 2 * (pxcor + 11)  and pycor <= 2 * (pxcor + 12) and pycor >= -8 and pycor <= 8][set pcolor yellow]")
    bridge.command("ask patches with [pycor >= -2 * (pxcor + 4)  and pycor <= -2 * (pxcor + 3) and pycor >= -8 and pycor <= 8][set pcolor yellow]")
    bridge.command("ask patches with [pycor = 0 and pxcor >= -11 and pxcor <= -4][set pcolor yellow]")
    
    #make S
    bridge.command("ask patches with [pycor = -8 and pxcor >= 3 and pxcor <= 11][set pcolor yellow]")
    bridge.command("ask patches with [pycor = 8 and pxcor >= 3 and pxcor <= 11][set pcolor yellow]")
    bridge.command("ask patches with [pycor <= 8 and pycor >= 1 and pxcor = 3 ][set pcolor yellow]")
    bridge.command("ask patches with [pycor = 0 and pxcor >= 3 and pxcor <= 11][set pcolor yellow]")
    bridge.command("ask patches with [pycor >= -8 and pycor <= 0 and pxcor = 11 ][set pcolor pink]")
    
    #make 2nd A
    bridge.command("ask patches with [pycor >= 2 * (pxcor - 20)  and pycor <= 2 * (pxcor - 19) and pycor >= -8 and pycor <= 8][set pcolor yellow]")
    bridge.command("ask patches with [pycor >= -2 * (pxcor - 28)  and pycor <= -2 * (pxcor - 29) and pycor >= -8 and pycor <= 8][set pcolor yellow]")
    bridge.command("ask patches with [pycor = 0 and pxcor <= 28 and pxcor >= 20][set pcolor yellow]")
    bridge.command("while[count patches with [pcolor = yellow] < 500][ask one-of patches [if pcolor != yellow and distancexy 0 0 > 40 [set pcolor yellow]]]")

   
    
#open bridge to Netlogo
gw = JavaGateway()
bridge = gw.entry_point

path = sys.argv[1] #path to code submissions
files = [c for c in listdir(path) if not (c.startswith('.')) and not c is "parkinglot.jpg"] #toss .DS_store and img file from list of files

for i in range(0, len(files)): #run each file in the path specified in commandline args
    name = files[i]
    p = path + name
    print("opening " + name) #shell notification for convenience 
    bridge.openModel(p)

    #setup the model and setup values for run 1.
    setupRun()
    # set 500 random patches to yellow
    makeRandomDistribution()
    random = bridge.report("count patches with [pcolor = yellow]")
    bridge.exportView(name + "random500.png")

    #setup the model and setup values for run 2.
    setupRun()
    #make 1 large cluster of 500 patches
    makeSquareDistribution()
    square = bridge.report("count patches with [pcolor = yellow]")
    bridge.exportView(name + "square500.png")

    #setup the model and setup values for run 3.
    setupRun()
    makeNASALogo()
    bridge.exportView(name + "NASA.png")

    #tally total score and add to dictionary
    total = random + square

    ##export performance
    results = sys.argv[2]
    with open (results, 'a') as f:
        f.write(name + " results\nRandom: " + str(500 - random) + "\nSquare: " + str(500 - square) + "\nTotal: " + str(total) + "\n\n")
        f.close()
        
    bridge.closeModel()
    bridge.refresh()

 
