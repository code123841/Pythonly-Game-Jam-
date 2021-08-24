from ursina import *

# Creating a variable for the engine
app = Ursina()


#creating basic objects
test_square = Entity(model = 'quad' , color = color.red , scale = (1 , 4))

#running the engine (creates a window )

app.run()