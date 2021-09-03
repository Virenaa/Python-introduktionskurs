# Imports everything from both model and graphics
from gamemodel import *
from gamegraphics import *


# Here is a nice little method you get for free
# It fires a shot for the current player and animates it until it stops
def graphicFire(game, graphics, angle, vel):
    player = game.getCurrentPlayer()
    # create a shot and track until it hits ground or leaves window
    proj = player.fire(angle, vel)
    while proj.isMoving():
        proj.update(1/50)
        graphics.sync() # This deals with all graphics-related issues
        update(50) # Waits for a short amount of time before the next iteration
    return proj

def graphicInput(game):
    player = game.getCurrentPlayer()
    wind = game.getCurrentWind()
    oldAngle, oldVel = player.getAim()    
    dialog = InputDialog(oldAngle, oldVel, wind)
    if dialog.interact() == "Quit":
        sys.exit()
    else:
        ang, vel = dialog.getValues()
        dialog.close()
    
    return ang, vel

def graphicFinishShot(game, ggame, proj):
    # The current player
    player = game.getCurrentPlayer()
    # The player opposing the current player
    other = game.getOtherPlayer()

    # Check if we won
    distance = other.projectileDistance(proj) 
    if distance == 0.0:
        player.increaseScore()
        # Start a new round
        game.newRound()

    # Switch active player
    game.nextPlayer()
    ggame.sync()

    

def graphicPlay():
    game = Game(10,3)
    ggame = GameGraphics(game)

    while True:
        angle,vel = graphicInput(game)
        projectile = graphicFire(game, ggame, angle, vel)
        graphicFinishShot(game, ggame, projectile)

# Run the game with graphical interface
graphicPlay()
