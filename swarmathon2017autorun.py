##Elizabeth E. Esterly
##The University of New Mexico
##NASA Swarmathon HS Division 2017
##autorun
##last revised 03/01/2017

#INPUT: python swarmathon2017autorun.py -path to folder of submissions to be processed- -path to text file to record results-


from py4j.java_gateway import JavaGateway
from os import listdir
import sys

#open bridge to Netlogo
gw = JavaGateway()
bridge = gw.entry_point

path = sys.argv[1] #path to code submissions
files = [c for c in listdir(path) if not (c.startswith('.')) and not c is "parkinglot.jpg"] #toss .DS_store and img file from list of files

for i in range(0, len(files)): #run each file in the path specified in commandline args
    name = files[i]  
    print("opening " + name) #shell notification for convenience 
    p = path + name
    bridge.openModel(p)

    #setup the model and setup values for run 1.
    bridge.command("setup")
    bridge.command("ask patches [set pcolor black]")
    # set 500 random patches to yellow
    bridge.command("ask n-of 500 patches [if pcolor != yellow [set pcolor yellow]]")
    random = bridge.report("count patches with [pcolor = yellow]")
    bridge.exportView(name + "random500.png")

    #setup the model and setup values for run 2.
    bridge.command("setup")
    bridge.command("ask patches [set pcolor black]")
    #make 1 large cluster of 500 patches
    bridge.command("ask patches with [pxcor > 30 and pycor > 25] [set pcolor yellow]")
    square = bridge.report("count patches with [pcolor = yellow]")
    bridge.exportView(name + "square500.png")

    #tally total score and add to dictionary
    total = 1000 - random + square

    ##export performance
    results = sys.argv[2]
    with open (results, 'a') as f:
        f.write(name + " results\nRandom: " + str(500 - random) + "\nSquare: " + str(500 - square) + "\nTotal: " + str(total) + "\n\n")
        f.close()

    #keep a dictionary of performance
        
    bridge.closeModel()
    bridge.refresh()

 
