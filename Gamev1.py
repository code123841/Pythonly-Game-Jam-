from ursina import *
#the one player module imported 
from ursina.prefabs.first_person_controller import FirstPersonController
#bacis starter code

class Voxel(Button):

    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture='white_cube',
            color=color.white,
            highlight_color=color.lime
        )
        #when we arepressing this button thhen we are creaitng a new voxel here
    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                #for creating the voxel
                voxel = Voxel(position = self.position + mouse.normal)
            if key == 'right mouse down':
                #for destrying the voxel (or the block)
                destroy(self)



app = Ursina()
#loop for running 64 voxels
for z in range(10):
    for x in range(10):
        voxel = Voxel( position = (x,0,z) )
player = FirstPersonController()


app.run()
