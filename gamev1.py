from ursina import *

#starters of animations
#with keyanimations

def update():
    if held_keys ['a']:

        test_square.x -= 1 * time.dt

    if held_keys ['s']:
        test_square.x += 1 * time.dt
# Creating a variable for the engine
app = Ursina()


#creating basic objects
# we can use the scale to scale the objests
test_square = Entity(model = 'quad' , color = color.red , scale = (1 , 4) , position = (5,4))




#running the engine (creates a window )

app.run()