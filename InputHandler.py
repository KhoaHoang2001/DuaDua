from direct.showbase.DirectObject import DirectObject

class InputHandler(DirectObject):
    def __init__(self):
        DirectObject.__init__(self)
        self.keymap = {
            "accelerate": False,
            "reverse": False,
            "brake": False,
            "steerLeft": False,
            "steerRight": False
        }
        self.accept("arrow_up", self.updateKeymap, ["accelerate", True])
        self.accept("arrow_up-up", self.updateKeymap, ["accelerate", False])
        self.accept("arrow_down", self.updateKeymap, ["reverse", True])
        self.accept("arrow_down-up", self.updateKeymap, ["reverse", False])
        self.accept("space", self.updateKeymap, ["brake", True])
        self.accept("space-up", self.updateKeymap, ["brake", False])
        self.accept("arrow_left", self.updateKeymap, ["steerLeft", True])
        self.accept("arrow_left-up", self.updateKeymap, ["steerLeft", False])
        self.accept("arrow_right", self.updateKeymap, ["steerRight", True])
        self.accept("arrow_right-up", self.updateKeymap, ["steerRight", False])
    
    def updateKeymap(self, key, value):
        self.keymap[key] = value