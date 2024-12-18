from matplotlib.pylab import rand

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

    # BLOCK: If-Else Block
    # BLOCK: To execute multiple lines of code
    if variable == True:
        print("Variable is True")
    else:
        print("Variable is False")

    # BLOCK: For Loop
    # BLOCK: To iterate over a sequence
    for i in range(int(variable*10)):
        print("Variable is bigger than 0,", i)

main()