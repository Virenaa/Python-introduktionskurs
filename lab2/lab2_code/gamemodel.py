from math import sin,cos,radians,copysign
import random

""" This is the model of the game"""
class Game:
    def __init__(self, cannonSize, ballSize):
        p1=Player("blue",-90,self,"right",0) #skapar p1
        p2=Player("red",90,self,"left",0) #skapar p2
        
        self.players=[p1,p2] #skapar två spelare 
        self.currentplayer=0
        self.cannonSize=cannonSize
        self.ballSize=ballSize
        self.newRound()

    """ A list containing both players """
    def getPlayers(self):
        return self.players #retunerar spelarna som finns i spelet

    """ The current player, i.e. the player whose turn it is """
    def getCurrentPlayer(self):
        return self.players[self.currentplayer]

    """ The opponent of the current player """
    def getOtherPlayer(self):
        return self.players[(self.currentplayer+1)%2]
        
    """ The number (0 or 1) of the current player. This should be the position of the current player in getPlayers(). """
    def getCurrentPlayerNumber(self):
        return self.currentplayer

    """ The height/width of the cannon """
    def getCannonSize(self):
        return self.cannonSize

    """ The radius of cannon balls """
    def getBallSize(self):
        return self.ballSize

    """ Set the current wind speed, only used for testing """
    def setCurrentWind(self, wind):
        self.wind=wind

    """ Get the current wind speed """
    def getCurrentWind(self):
        return self.wind

    """ Switch active player """
    def nextPlayer(self):
        self.currentplayer=(self.currentplayer+1)%2

    """ Start a new round with a random wind value (-10 to +10) """
    def newRound(self):
        self.wind = random.random()*20-10

""" Models a player """
class Player:
    def __init__(self, col, posX, game, direction,score):
        self.color=col 
        self.posX=posX
        self.game=game
        self.aim=(45,40)
        self.direction=direction
        self.score=score
        self.projectile=None
  
    """ Create and return a projectile starting at the centre of this players cannon. Replaces any previous projectile for this player. """
    def fire(self, angle, velocity):
        if self.direction == "right": #player 0
            actual_angle = angle
        else:
            actual_angle = 180 - angle

        self.projectile = Projectile(actual_angle,velocity, self.game.getCurrentWind(),self.posX, self.game.getCannonSize()/2, -110,110)
        self.aim=(angle,velocity)
        
        return self.projectile
    """ Returns the current projectile of this player if there is one, otherwise None """
    def getProjectile(self):
        return self.projectile

    """ Gives the x-distance from this players cannon to a projectile. If the cannon and the projectile touch (assuming the projectile is on the ground and factoring in both cannon and projectile size) this method should return 0"""
    def projectileDistance(self, proj):
        diff=proj.getX()-self.getX()
         
        if diff > 0:
            diff = diff - self.game.getCannonSize()/2- self.game.getBallSize()
            #missed to the right
        elif diff < 0:
            diff= diff + self.game.getCannonSize()/2 + self.game.getBallSize()
            #missed to the left 
        if diff>=-8 and diff<=8:
                return 0
        return diff

    """ The current score of this player """
    def getScore(self):
        return self.score

    """ Increase the score of this player by 1."""
    def increaseScore(self):
        self.score=(self.score+1)

    """ Returns the color of this player (a string)"""
    def getColor(self):
        return self.color

    """ The x-position of the centre of this players cannon """
    def getX(self):
        return self.posX

    """ The angle and velocity of the last projectile this player fired, initially (45, 40) """
    def getAim(self):
        return self.aim


""" Models a projectile (a cannonball, but could be used more generally) """
class Projectile:
    """
        Constructor parameters:
        angle and velocity: the initial angle and velocity of the projectile 
            angle 0 means straight east (positive x-direction) and 90 straight up
        wind: The wind speed value affecting this projectile
        xPos and yPos: The initial position of this projectile
        xLower and xUpper: The lowest and highest x-positions allowed
    """
    def __init__(self, angle, velocity, wind, xPos, yPos, xLower, xUpper):
        self.yPos = yPos
        self.xPos = xPos
        self.xLower = xLower
        self.xUpper = xUpper
        theta = radians(angle)
        self.xvel = velocity*cos(theta)
        self.yvel = velocity*sin(theta)
        self.wind = wind

    """ 
        Advance time by a given number of seconds
        (typically, time is less than a second, 
         for large values the projectile may move erratically)
    """
    def update(self, time):
        # Compute new velocity based on acceleration from gravity/wind
        yvel1 = self.yvel - 9.8*time
        xvel1 = self.xvel + self.wind*time
        
        # Move based on the average velocity in the time period 
        self.xPos = self.xPos + time * (self.xvel + xvel1) / 2.0
        self.yPos = self.yPos + time * (self.yvel + yvel1) / 2.0
        
        # make sure yPos >= 0
        self.yPos = max(self.yPos, 0)
        
        # Make sure xLower <= xPos <= mUpper   
        self.xPos = max(self.xPos, self.xLower)
        self.xPos = min(self.xPos, self.xUpper)
        
        # Update velocities
        self.yvel = yvel1
        self.xvel = xvel1
        
    """ A projectile is moving as long as it has not hit the ground or moved outside the xLower and xUpper limits """
    def isMoving(self):
        
        return 0 < self.getY() and self.xLower < self.getX() < self.xUpper

    def getX(self):
        return self.xPos

    """ The current y-position (height) of the projectile". Should never be below 0. """
    def getY(self):
        return self.yPos
