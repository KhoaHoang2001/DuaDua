from panda3d.bullet import BulletBoxShape, BulletRigidBodyNode
from panda3d.core import Vec3

class Tilemap:
    def __init__(self, render, world, pos):
        self.node = BulletRigidBodyNode("tilemap")
        self.model = loader.loadModel("assets/grass.obj")
        self.model.setPos(4, 4, 0)
        self.model.setP(90)
        self.model.setScale(8)
        self.shape = BulletBoxShape(Vec3(4, 4, 0.05))
        self.node.addShape(self.shape)
        self.nodepath = render.attachNewNode(self.node)
        self.nodepath.setPos(pos)
        world.attachRigidBody(self.node)
        self.model.copyTo(self.nodepath)
