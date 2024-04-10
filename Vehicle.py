from panda3d.bullet import BulletDebugNode, BulletBoxShape, BulletWorld, BulletRigidBodyNode, BulletPlaneShape, BulletVehicle
from panda3d.core import Vec3, TransformState

class Vehicle:
    def __init__(self, render, world, pos):

        self.model = loader.loadModel("assets/raceCarRed.obj")
        self.model.setP(90)
        self.model.setZ(-0.5)
        self.node = BulletRigidBodyNode("chassis")
        self.node.addShape(BulletBoxShape(Vec3(0.4, 0.7, 0.1)), TransformState.makePos(Vec3(0, 0, -0.2)))
        self.node.setMass(800)
        self.node.setDeactivationEnabled(False)
        self.node.setCcdMotionThreshold(1e-7)
        self.node.setCcdSweptSphereRadius(0.5)
        self.nodepath = render.attachNewNode(self.node)
        self.nodepath.setPos(pos)
        self.model.copyTo(self.nodepath)
        world.attachRigidBody(self.node)

        self.vehicle = BulletVehicle(world, self.node)
        world.attachVehicle(self.vehicle)

        self.wheelFL = self.addWheel(Vec3(0.3, 0.3, -0.1), True)

        self.wheelFR = self.addWheel(Vec3(-0.3, 0.3, -0.1), True)

        self.wheelBL = self.addWheel(Vec3(0.3, -0.5, -0.1), False)

        self.wheelBR = self.addWheel(Vec3(-0.3, -0.5, -0.1), False)

        self.engineForce = 0
        self.brakeForce = 0
        self.steering = 0
        self.steeringClamp = 45
        self.steeringIncrement = 120

    def addWheel(self, pos, front):
        wheel = self.vehicle.createWheel()
        wheel.setChassisConnectionPointCs(pos)
        wheel.setFrontWheel(front)
        wheel.setWheelDirectionCs(Vec3(0, 0, -1))
        wheel.setWheelAxleCs(Vec3(1, 0, 0))
        wheel.setWheelRadius(0.1)
        wheel.setMaxSuspensionTravelCm(40)
        wheel.setSuspensionStiffness(40)
        wheel.setWheelsDampingRelaxation(2.3)
        wheel.setWheelsDampingCompression(4.4)
        wheel.setFrictionSlip(100.0)
        wheel.setRollInfluence(0.1)
        return wheel

    def accelerate(self):
        self.engineForce = 1000
        self.brakeForce = 0
        
    def reverse(self):
        self.engineForce = -100
        self.brakeForce = 0
        
    def brake(self):
        self.engineForce = 0
        self.brakeForce = 100

    def steerLeft(self):
        self.steering += globalClock.getDt() * self.steeringIncrement
        self.steering = min(self.steering, self.steeringClamp)

    def steerRight(self):
        self.steering -= globalClock.getDt() * self.steeringIncrement
        self.steering = max(self.steering, -self.steeringClamp)

    def steerRelax(self):
        if self.steering > 0:
            self.steering -= globalClock.getDt() * self.steeringIncrement
            self.steering = max(self.steering, 0)
        elif self.steering < 0:
            self.steering += globalClock.getDt() * self.steeringIncrement
            self.steering = min(self.steering, 0)

    def update(self):
        self.vehicle.applyEngineForce(self.engineForce, 2)
        self.vehicle.applyEngineForce(self.engineForce, 3)
        self.vehicle.setBrake(self.brakeForce, 2)
        self.vehicle.setBrake(self.brakeForce, 3)
        self.vehicle.setSteeringValue(self.steering, 0)
        self.vehicle.setSteeringValue(self.steering, 1)