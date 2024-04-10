from panda3d.bullet import BulletBoxShape, BulletGhostNode
from panda3d.core import Vec3, BitMask32, TransformState
import time

class Checkpoint:
    def __init__(self, render, world, pos):
        self.node = BulletGhostNode("checkpoint")
        self.model = loader.loadModel("assets/overheadRoundColored.obj")
        self.model.setPos(7.25, 1.25, 0)
        self.model.setP(90)
        self.model.setScale(8)
        self.shape = BulletBoxShape(Vec3(6, 1, 3))
        self.node.addShape(self.shape, TransformState.makePos(Vec3(0, 0, 2.5)))
        self.nodepath = render.attachNewNode(self.node)
        self.nodepath.setPos(pos)
        self.nodepath.setCollideMask(BitMask32(0x0f))
        world.attachGhost(self.node)
        self.model.copyTo(self.nodepath)
        self.point = 0

    def checkGhost(self):
        for node in self.node.getOverlappingNodes():
            if node.getName() == "chassis":
                self.nodepath.setY(self.nodepath.getY() + 10)
                self.point += 1
                print(f"Checkpoint passed: {self.point}")
                break
