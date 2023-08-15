from .hex_vector import HexVector

def lerp(a, b, t):
    """ Return the Hex Vector at the given timestep """
    return a + (b-a)*t

def line_to(destination, start=HexVector(0, 0)):
    """ Return the hexes that make up a line between the given destination and start """
    distance = (destination-start).magnitude
    lerp_coords = [lerp(start, destination, i/distance) for i in range(1, distance+1)]
        
    return [round(lerp_coord) for lerp_coord in lerp_coords]

def steps_to(destination, start=HexVector(0, 0)):
    """ Return the steps to take to reach the destination from the given start """
    steps = []
    last = start
    path = line_to(destination, start=start)
    
    for hex in path:
        steps.append(hex-last)
        last = hex
    return steps
