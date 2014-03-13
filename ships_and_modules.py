class Projectile(MassiveObject):
    pass

class Missile:
    pass


class Module( MassiveObject ):
    """Modules make up ships"""
    def __init__(self):
        self.is_powered = False
        self.is_commanded = False #commanded modules follow commands from captain
        self.destroyed = False
        self.power = 0 #power consumption when on. negatives are power drains, positives are power producers
