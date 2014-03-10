class GlobalConstants:
    """Class containing global constants like the speed of light"""
    speed_of_light = 3e8
    base_timestep = 1 #1 second

global global_constants
global_constants = GlobalConstants()

class Vector:
    """Vectors"""
    def __init__(self, *values ):
        self.values = tuple(values)

    def __get_item__(self, index ):
        return self.values[index]

    def __len__( self ):
        return len( self.values ) 

    def scale( self, scalar ):
        return Vector( [value*scalar for value in self.values] )

    def add( self, other ):
        return Vector( [ self[index]+other[index] for index in range(len(self)) ] )

    def subtract( self, other ):
        return Vector( [ self[index]-other[index] for index in range(len(self)) ] )      

def new_vector( length, value = 0.0 ):
    """Construct a vector of length `length` with the same value in each element"""
    return Vector( [value]*length )

class PhysicalObject:
    """The base class of physical objects"""
    def __init__(self):
        self.mass = 1.0
        self.radius = 1.0
        self.position = new_vector( 3 )
        self.velocity = new_vector( 3 )
        self.acceleration = new_vector( 3 )

    def set_acceleration( self, force_vector ):
        self.acceleration = force_vector.scale( 1.0/self.mass )

    def current_distance( self, other ):
        """Distance at current moment in time"""
        pass

    def minimum_distance_across_previous_tick( self, other ):
        """Minimum distance between self and other across the previous tick,
        so we check for collisions after advancing"""
        #determine times at which minimum occurs
        
        #keep negative time solutions since we're looking backwards
        pass


class Module( PhysicalObject ):
    """Modules make up ships"""
    def __init__(self):
        self.is_powered = False
        self.is_commanded = False #commanded modules follow commands from captain
        

class World:
    def __init__(self):
        self.physical_objects = {}

    def tick( self,  stepsize = global_constants.base_timestep ):
        pass

def _test_suite():
    Vector()
    PhysicalObject()
    Module()
    PhysicalObject()
    return True

        
        
