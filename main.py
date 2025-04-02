from matplotlib.pylab import rand
from build.utils import functionality
from build.test import test

def main():
    """
    DOCSTRING, BLOCK: Main function
    """

    # NORMAL: Random number between 0 and 1
    variable = rand()
    
    # NORMAL: Standard If-Else Block
    if True:
        print("This is True") # INLINE: Just for test purposes
    else:
        # print("This is False") # COMMENTED-OUT: Both lines will not be executed
        pass
    
    functionality(variable)

main()
test()