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

    def concatenate( self, other ):
        """Return a new vector with `other` concatenated onto the end of `self`"""
        return Vector( *( list( self.values).extend( other.values ) ) )

    def slice( self, low_index, high ):
        return Vector( self[low_index:high_index])

def new_vector( length, value = 0 ):
    """Construct a vector of length `length` with the same value in each element"""
    values = [value]*length
    return Vector( *values )

class EulerIntegrator:
    """Numerical integration"""
    def __init__(self, tick_size = 1):
        self.tick_size = tick_size

    def integrate_1st_order_system( self, state_vector, derivative_vector ):
        """Integrate vector in place"""
        state_vector = state_vector+derivative_vector.scale( self.tick_size )
        
        
    def integrate_higher_order_system( self, *vectors ):
        """Integrate the vectors in place. If there are only two vectors, the first is the
        state vector and the second the state derivative. If there are more, the system is 
        assumed to be higher order with each additional argument being the next derivative.
        
        A system of DEs is build up from the input by concatenating when appropriate. 
        _e.g._ in a second order system, the first derivative is concatenated to the state vector
        to create a new state vector (but doesn't overwrite the original)
        and the second derivative is concatenated to the first derivative.

        Arguments are only overwritten after these new vectors are unpacked.

        Vectors are assumed to be the same length"""
        
        if len(vectors)<2:
            raise ValueError( "Must have at least a state and a state derivative vector as arguments")

        length = len(vectors[0])

        #packing
        elif len(vectors)==2:
            tmp_state = vectors[0]
            tmp_deriv = vectors[1]
        else:
            tmp_state = vectors[0].concatenate( vectors[1] )
            tmp_deriv = vectors[1].concatenate( vectors[2] )
            for index in range( 2, len(vectors)-1 ):
                tmp_state = tmp_state.concatenate( vectors[index] )
                tmp_deriv = tmp_deriv.concatenate( vectors[index+1] )

        #integrating        
        self.integrate_1st_order_system( tmp_state, tmp_deriv )
        
        #unpacking
        for index in range( 0, len(vectors)-1 ):
            vectors[index]=tmp_state.slice( index*length, (index+1)*length)
