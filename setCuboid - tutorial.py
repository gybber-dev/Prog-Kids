import mc

# How setCuboid is working

# cube
x0, y0, z0 = 1, 1, 1 # start point
x1, y1, z1 = 5, 5, 5 # end point

# Start and end points could be located anywhere
# even on a same line
# Column
# x0, y0, z0 = -1, 2, -1
# x1, y1, z1 = -1, 5, -1

# even on a same height/plane
# x0, y0, z0 = -1, 2, -1
# x1, y1, z1 = 3, 2, 3

mc.world.setCuboid(x0, y0, z0, x1, y1, z1, 20)
mc.world.setBlock(x0, y0, z0, 14)
mc.world.setBlock(x1, y1, z1, 14)