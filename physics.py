"""Subspace physics will be 2-D, L1 norm"""

class GlobalConstants:
    """Class containing global constants like the speed of light"""
    speed_of_light = float('inf') #crazy newton like infinite c
    tick_lengths = 10 #10 second ticks
    dimensions = 2
    norm = 1
    phi = (1618034,1000000) #numerator, denominator tuple for phi for integer gss

global global_constants
global_constants = GlobalConstants()

"""
def golden_section_search( function, lower_bound, upper_bound, tol=2 ):
    phi = global_constants.phi
    c0 = phi[0]-phi[1] #numerator of phi minus one over phi's denominator
    ff=function

    x_lb = lower_bound
    x_ub = upper_bound
    f_lb = ff(x_lb)
    f_ub = ff(x_ub)

    x_lt = ((x_ub-x_lb)*c0)//phi[1]+x_lb#lower test point
    f_lt = ff(x_lt)
    if f_lt > max( f_lb, f_ub ):
        if f_lb > f_ub:
            return x_ub
        else:
            return x_lb


    while x3-x1>=tol:
        delta = x3-x1
    
        aa = (delta*c0)//phi[1]
        bb = (x2*phi[0])//phi[1]

        x2 = aa+x1
        x4 = x3-bb

        f2 = ff(aa)
        f4 = ff(bb)

        if f4>
"""

        





class Vector:
    """Vectors"""
    def __init__(self, *values ):
        self.values = tuple(values)

    def __getitem__(self, index ):
        return self.values[index]

    def __len__( self ):
        return len( self.values ) 

    def scale( self, scalar ):
        return Vector( *[value*scalar for value in self.values] )

    def divide( self, scalar ):
        return Vector( *[value//scalar for value in self.values] )

    def add( self, other ):
        return Vector( *[ self[index]+other[index] for index in range(len(self)) ] )

    def subtract( self, other ):
        return Vector( *[ self[index]-other[index] for index in range(len(self)) ] )

    def __abs__(self):
        return Vector( *[abs(value) for value in self.values] )

    def norm( self ):
        """L1 length"""
        return sum( self )

    def distance( self, other ):
        return self.subtract(other).norm()

    def __repr__(self):
        return "Vector({values})".format(values=','.join([str(value) for value in self.values]))

    def __add__(self, other ):
        return self.add(other)

    def __sub__(self, other ):
        return self.subtract(other)

def new_vector( length, value = 0 ):
    """Construct a vector of length `length` with the same value in each element"""
    values = [value]*length
    return Vector( *values )

def isqrt(nn):
    """Integer square root ripped shamelessly from StackOverflow:
http://stackoverflow.com/questions/15390807/integer-square-root-in-python
and
http://programmingpraxis.com/2012/06/01/square-roots/"""
    xx = nn
    yy = (xx + nn // xx) // 2
    while yy < xx:
        xx = yy
        yy = (xx + nn // xx) // 2
    return xx

class MassiveObject:
    """The base class of massive objects"""
    def __init__(self):
        self.mass = 1
        self.size = 1
        self.heat_capacity = 1
        self.toughness = 1
        self.max_temp = 1
        self.heat = 1
        self.position = new_vector( global_constants.dimensions )
        self.velocity = new_vector( global_constants.dimensions )
        self.acceleration = new_vector( global_constants.dimensions )


    def sum_forces( self, *list_of_force_vectors):
        pass

    def set_acceleration( self, force_vector ):
        self.acceleration = force_vector.divide( self.mass  )

    def current_distance( self, other ):
        """Distance at current moment in time"""
        return (self.distance-other.distance).norm()

    def minimum_distance_across_previous_tick( self, other ):
        """Minimum distance between self and other across the previous tick,
        so we check for collisions after advancing"""
        #determine times at which potential minima occur
        raise NotImplemented

        a1 = self.acceleration
        a2 = other.acceleration

        v1 = self.velocity
        v2 = other.velocity

        #if the relative accelerations are nonzero
        
        #keep negative time solutions since we're looking backwards

    def collision_check( self, other ):
        """Return true if self and other collide"""
        pass

    def collide( self, other ):
        """Affect self and other according to collision rules"""
        pass

    def contigent_collide( self, other ):
        """Compose `collision_check` and `collide`"""
        pass

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
        

class World:
    def __init__(self):
        self.physical_objects = []
        self.name_map = {}

    def detect_collisions( self ):
        for index1, obj1 in enumerate(self.physical_objects):
            for index2 in range(index1+1, len(self.physical_objects) ):
                obj1.contigent_collide( self.physical_objects[other] )

    def tick( self,  stepsize = global_constants.base_timestep ):
        pass

def _test_suite():
    Vector()
    PhysicalObject()
    Module()
    MassiveObject()
    return True

if __name__=="__main__":
    #Manual test code
    a=new_vector(2)
    b=Vector(-1,-2)

        
        
