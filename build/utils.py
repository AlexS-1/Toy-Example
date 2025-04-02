def functionality(variable):
    # BLOCK: If-Else Block
    # BLOCK: To execute multiple lines of code
    res = ""
    if variable == True:
        res += ("Variable is True")
    else:
        res += ("Variable is not True")

    # BLOCK: For Loop
    # BLOCK: To iterate over a sequence
    for i in range(int(variable*10)):
        res += f"\nVariable is bigger than 0, {i}"
    
    print(res)
    return res