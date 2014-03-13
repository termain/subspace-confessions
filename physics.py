"""Subspace physics will be 2-D, L1 norm"""
import numerics

class GlobalConstants:
    """Class containing global constants like the speed of light"""
    speed_of_light = float('inf') #crazy newton like infinite c
    ticks_per_second = 1000
    seconds_per_turn = 1
    dimensions = 2
    norm = 1

global global_constants
global_constants = GlobalConstants()



class MassiveObject:
    """The base class of massive objects"""
    def __init__(self):
        self.mass = 1 #fake kg
        self.size = 1 #fake m
        self.heat_capacity = 1 #fake J
        self.toughness = 1 #fake J
        self.max_temp = 1 #fake K
        self.heat = 1 #fake J
        self.position = new_vector( global_constants.dimensions ) #fake m
        self.velocity = new_vector( global_constants.dimensions ) #fake m/tick
        self.acceleration = new_vector( global_constants.dimensions ) #fake m/tick**2


    def sum_forces( self, *list_of_force_vectors):
        pass

    def set_acceleration( self, force_vector ):
        self.acceleration = force_vector.divide( self.mass  )

    def current_distance( self, other ):
        """Distance at current moment in time"""
        return (self.distance-other.distance).norm()

    def tick( self, time_step = global_constants.tick_length ):
        """Advance the object one time step. Happens before collisions are checked for"""
        state_vector = self.position.concatenate( self.velocity )
        state_derivative_vector = self.velocity.concatenate( self.acceleration )

        

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

    def map_type(self):
        return "unknown"


        

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

        
        
