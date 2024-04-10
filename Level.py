from Tilemap import Tilemap
from panda3d.core import Vec3, PointLight, AmbientLight

class Level:
    def __init__(self, render, world):
        self.sun = loader.loadModel("assets/sphere.obj")
        self.light = PointLight("light")
        self.light.setColor((0.2, 0.2, 0.2, 0))
        self.lightpath = render.attachNewNode(self.light)
        #self.sun.copyTo(self.lightpath)
        self.lightpath.setPos(10, 20, 10)

        self.alight = AmbientLight('alight')
        self.alight.setColor((0.2, 0.2, 0.2, 1))
        self.alnp = render.attachNewNode(self.alight)
        render.setLight(self.alnp)

        render.setLight(self.lightpath)
        for i in range(10):
            for j in range(10):
                Tilemap(render, world, Vec3(i * 4, j * 4, 1))