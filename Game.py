from direct.showbase.ShowBase import ShowBase
from InputHandler import InputHandler
from Debugger import Debugger
from Vehicle import Vehicle
from Checkpoint import Checkpoint
from Level import Level
from panda3d.bullet import BulletBoxShape, BulletWorld, BulletRigidBodyNode, BulletPlaneShape, BulletVehicle
from panda3d.core import Vec3
import simplepbr
import sys

class Game(ShowBase):
    def __init__(self):
        super().__init__(self)
        simplepbr.init()

        


        self.inputHandler = InputHandler()
        self.world = BulletWorld()
        self.world.setGravity(Vec3(0, 0, -9.81))

        self.level = Level(self.render, self.world)
        self.checkpoint = Checkpoint(self.render, self.world, Vec3(0, 3, 0))
        self.vehicle = Vehicle(self.render, self.world, Vec3(0, 0, 2))
        
        #base.disableMouse()
        #base.camera.reparentTo(self.vehicle.nodepath)
        #base.camera.setPos(0, -3, 0)
        #Ground

        self.ground = BulletRigidBodyNode("ground")
        self.ground.addShape(BulletPlaneShape(Vec3(0, 0, 1), -5))
        self.groundNP = render.attachNewNode(self.ground)
        self.groundNP.setPos(0, 0, 4)
        self.world.attachRigidBody(self.ground)

        self.debugger = Debugger(self.render, self.world)

        self.taskMgr.add(self.update, 'update')
        self.accept("f1", self.debugger.toggleDebug)
        self.accept("escape", sys.exit)

    def update(self, task):
        dt = globalClock.getDt()
        self.world.doPhysics(dt)
        self.vehicle.engineForce = 0
        self.vehicle.brakeForce = 0
        if self.inputHandler.keymap["accelerate"]:
            self.vehicle.accelerate()
        elif self.inputHandler.keymap["reverse"]:
            self.vehicle.reverse()
        if self.inputHandler.keymap["steerLeft"]:
            self.vehicle.steerLeft()
        elif self.inputHandler.keymap["steerRight"]:
            self.vehicle.steerRight()
        if self.inputHandler.keymap["brake"]:
            self.vehicle.brake()
        self.vehicle.update()
        self.checkpoint.checkGhost()
        return task.cont

game = Game()
game.run()