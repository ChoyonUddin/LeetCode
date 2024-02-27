def christmas(height):
    layer = 1
    for i in range(height):
        print(" "*(height-1-i)+'*'*layer+" "*(height-1-i))
        layer +=2
christmas(11)