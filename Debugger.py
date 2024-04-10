from panda3d.bullet import BulletDebugNode

class Debugger:
    def __init__(self, render, world):
        self.node = BulletDebugNode("Debug")
        self.node.showWireframe(True)
        self.node.showConstraints(True)
        self.node.showBoundingBoxes(False)
        self.node.showNormals(False)
        self.nodepath = render.attachNewNode(self.node)
        world.setDebugNode(self.nodepath.node())

    def toggleDebug(self):
        if self.nodepath.isHidden():
            self.nodepath.show()
        else:
            self.nodepath.hide()