from ursina import *

# Make Blank Game Window
app = Ursina()

# Add A Simple Square, Quad is a square, cube is a cube
mySquare = Entity(model='quad')


# Main Update Loop (Happens Every Frame)
def update():
    # Change Rotation by 1
    mySquare.rotation_z += 1


# Start Game
app.run()