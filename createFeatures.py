import os, sys, time, datetime
from pynput.mouse import Button, Controller

def timer(start, end, task):
    diff = end - start
    print "Task: {0} took {1} seconds".format(task, diff.seconds)

mouse = Controller()

time.sleep(2) # switch to ArcMap
#right click on the first layer
mouse.position = (116, 182)
mouse.click(Button.right)
#go to edit
mouse.position = (163, 433)
time.sleep(1)
#go to edit features
mouse.position = (456, 435)
#click start editing
mouse.click(Button.left)
time.sleep(2)
#MAKE SURE TO ADD POINT tool TO THE TOOLBAR
#click create features
mouse.position = (1036, 66)
mouse.click(Button.left)
#click the feature
mouse.position = (901, 186)
mouse.click(Button.left)
time.sleep(2)
#click on the point tool
mouse.position = (19, 64)
mouse.click(Button.left)

numberOfPoints = 20
#create points
xy = (534, 622)
startFeatureTime= datetime.datetime.now()
for i in range(numberOfPoints):
    mouse.position = (xy)
    #click on the map to create teh feature
    mouse.click(Button.left)
    #change teh coordinate
    x = xy[0] + 10
    y = xy[1] + 10
    xy = (x, y)
    time.sleep(1)
endFeatureTime = datetime.datetime.now()
timer(startFeatureTime, endFeatureTime, "Creating Features")
    
    


print "Done"
