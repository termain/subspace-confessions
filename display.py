from collections import defaultdict

ascii_symbols = {
    "ship":"S",
    "missile":"M",
    "portal": "P",
    "empty": ".",
    "unknown": "?",
    "multiple": "!",
    "newline":"\n",
    "vertical_separator":"|",
    "horizontal_separator":"_"
}

colors = {

}
class Quadrant:
    def __init__( self, xsize=40, ysize=20, symbols = ascii_symbols ):
        self.xsize=xsize
        self.ysize=ysize
        self.symbols=ascii_symbols
        self.create_empty_quadrant()


    def create_empty_quadrant( self ):
        self.map = [ [self.symbols["empty"]]*self.xsize ]*self.ysize

    def draw_row( self, index ):
        return ''.join( self.map[index] )

class Map:
    """Quadrants are indexed 1-4 starting in the upper right hand and moving 
    clockwise"""
    def __init__( self, quad_xsize=40, quad_ysize=20, symbols = ascii_symbols ):
        self.quadrants = [ Quadrant(quad_xsize, quad_ysize, symbols ) ]*4
        self.quad_xsize = quad_xsize
        self.quad_ysize = quad_ysize
        self.symbols = symbols

    def draw( self ):
        rows = [ self.symbols["vertical_separator"].join( 
            (self.quadrants[3].draw_row(index), self.quadrants[0].draw_row(index)) )
            for index in range(self.quad_ysize) ]

        rows.append( self.symbols["horizontal_separator"]*(self.quad_xsize*2+1) )

        rows.extend( [ self.symbols["vertical_separator"].join( 
            (self.quadrants[2].draw_row(index), self.quadrants[1].draw_row(index)) )
            for index in range(self.quad_ysize) ] )

        return self.symbols["newline"].join( rows )

test = Map()
print( test.draw() )

                
        
