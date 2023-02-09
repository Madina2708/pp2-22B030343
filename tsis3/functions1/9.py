import math
def sphereVolume(r):
    
    volume = 4 / 3 * math.pi * math.pow(r, 3)
    return volume

print((sphereVolume(3)))