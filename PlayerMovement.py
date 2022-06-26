import bge
from collections import OrderedDict
from mathutils import Vector

if not hasattr(bge,'__component__'):
    scene = bge.logic.getCurrentScene()
    key = bge.logic.keyboard.inputs
    ms = bge.logic.mouse.inputs
    
    W = key[bge.events.WKEY]
    A = key[bge.events.AKEY]
    S = key[bge.events.SKEY]
    D = key[bge.events.DKEY]   
    SPACE = key[bge.events.SPACEKEY]   
    
    lmb = ms[bge.events.LEFTMOUSE]
    rmb = ms[bge.events.RIGHTMOUSE]
    
    

class Movement(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ('Speed', 0.0)
    ])

    def start(self, args):
        self.speed   = args['Speed']
        self.char = bge.constraints.getCharacter(self.object)

        
    def update(self):
        if W.active:
            self.object.applyMovement([0,self.speed,0], 1)
        
        if S.active:
            self.object.applyMovement([0,-self.speed,0], 1)
        
        if A.active:
            self.object.applyMovement([-self.speed,0,0], 1)
        
        if D.active:
            self.object.applyMovement([self.speed,0,0], 1) 
        
        if SPACE.active:
            self.char.jump()       