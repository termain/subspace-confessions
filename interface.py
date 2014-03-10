import curses

class CommandLineOptions:
    """Class to read in the command line options and store them. Parses
    command line at initialization"""
    def __init__(self):
        pass

class ShlexInterface:
    """The shlex module based interface... simpler than curses"""
    def __init__( self ):
        self.initialize_command_dictionary()

    def not_found( self, *args ):
        """Print command not found message"""
        print( args )
        print( "Bad Command" )

    def no_op( self, *args ):
        """Do nothing"""
        pass
        
    def initialize_command_dictionary( self ):
        self.cmd_dict ={
            "": self.no_op
            }

def curses_main( stdscr, cmd_line_options ):
    """The main function to run inside of curses"""
    pass

def shlex_main( cmd_line_options ):
    """The main function using a shlex interpretter"""
    pass


def _test_suite( ):
    CommandLineOptions()
    ShlexInterface()
    return True


def main():
    """The main function"""
    cmd_line_options = CommandLineOptions()
    curses.wrapper( curses_main, cmd_line_options )
