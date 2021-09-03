"""
The racer example using inheteritance 
(not requiuired for the course, just some extra material)
"""


# You need the file graphics.py from https://mcsp.wartburg.edu/zelle/python/
from graphics import *

speedLimit = 5 # How fast is the racer allowed to move
animationSpeed = 50 # How fast does time progress (higher value makes it faster), unit is updates per second

"""
  Models a race-car, keeping track of its current position and velocity
  this class has no graphics-code
"""
class Racer:
    def __init__(self):
        self.xvelocity = 0
        self.yvelocity = 0
        self.xpos = 0
        self.ypos = 0

    def _moveRelative(self, xDiff,yDiff):
        self.xpos += xDiff
        self.ypos += yDiff

    def _moveAbsolute(self, x,y):
        self._moveRelative(x-self.getX(),y-self.getY())
    
    def accelerate(self, xacc, yacc):
        self.xvelocity += xacc
        self.yvelocity += yacc
        # Enforce the speedlimit
        self.yvelocity = min(speedLimit, self.yvelocity)
        self.yvelocity = max(-speedLimit, self.yvelocity)
        self.xvelocity = min(speedLimit, self.xvelocity)
        self.xvelocity = max(-speedLimit, self.xvelocity)
        
    def slowDown(self):
        self.xvelocity *= 0.9
        self.yvelocity *= 0.9

    """ Drive for one time-unit of time """
    def drive(self):
        self._moveRelative(self.xvelocity, self.yvelocity)

    """ Return to position (0,0) and stop """
    def reset(self):
        self._moveAbsolute(0,0)
        self.xvelocity = 0
        self.yvelocity = 0

    def getX(self):
        return self.xpos;

    def getY(self):
        return self.ypos;



"""
  Extends the Racer class, adding graphics.
  This class will automatically have all methods that Racer has.
"""
class GraphicRacer(Racer):
    """
      Constructor for GraphicRacer. Note that unlike the constructor for Racer
      it takes one argument. 
    """
    def __init__(self, win):
        # This line calls the constructor of the superclass (Racer)
        # If this line is removed, the constructor for Racer is never run
        #   and nothing will work
        super().__init__()

        # Create graphic components for the race car
        self.circle = Circle(Point(0,0), 10)
        self.circle.setFill('blue')
        self.circle.draw(win)

        self.letter = Text(Point(0,0), "R")
        self.letter.setTextColor('red')
        self.letter.draw(win)

    """
      Synchronize the graphics with the current state of the model
      Note how we use e.g. self.getX() which is a method from Racer. 
    """
    def sync(self):
        # Move the circle and text to wherever the car is
        c = self.circle
        t = self.letter

        # Move the circle and text elements to the current position of the model
        c.move(self.getX()-c.getCenter().getX(), self.getY()-c.getCenter().getY())
        t.move(self.getX()-t.getAnchor().getX(), self.getY()-t.getAnchor().getY())

    """
      This overrides the drive method from the Racer class.
      Adding this definition changes the behavior of drive() in GraphicRacer
        compared to Racer. 
    """
    def drive(self):
        # This line calls the drive method from the superclass (Racer)
        super().drive()

        # After running drive() from Racer, we synchronize the graphics
        self.sync()


# Create the main window. Disabling autoflush means the window will only be updated when update() is called.
win = GraphWin("Racer" , 640, 480, autoflush=False)
# This line sets (0,0) to be the middle of the window
win.setCoords(-320, -240, 320, 240)

# Create a graphical race car immediately.
# Because we are using inheritence, racer will also be a Racer-object,
# combining model and graphics
racer = GraphicRacer(win)

# Main animation loop
#  * If the user presses an arrow key accelerate in that direction (up to speed limit)
#  * If the user presses space, apply breaks to reduce speed
#  * If the user presses backspace the simulation is restarted
#  The speed of the loop is controlled by the update() function 
while(True):
    key = win.checkKey() # The key being pressed (if any)
    
    if key == "Up":
        racer.accelerate(0,1)
    elif key == "Down":
        racer.accelerate(0,-1)
    elif key == "Right":
        racer.accelerate(1,0)
    elif key == "Left":
        racer.accelerate(-1,0)
    elif key == "space":
        racer.slowDown()
    elif key == "BackSpace":
        racer.reset()

    # Move the racer based on current veclocity
    racer.drive()

    # Waits for the animation step to finish based on animationspeed, then redraws the window 
    update(animationSpeed)


