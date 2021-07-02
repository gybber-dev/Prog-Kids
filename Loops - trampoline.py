import mc

from mc import world, player

x,y,z=7,-1,-7
#world.setCuboid(7,-1,-7, 11,-1,-11, 57)
world.setBlock(x,y,z, 57)
world.setCuboid(14,-1,-37,-16,-1,-57, 57)
world.setCuboid(13,0,-38,-15,0,-56, 171)
world.setCuboid(13,-1,-38,-15,-1,-56, 165)
#print (player.getPos())

while True:
	x_p, y_p, z_p = mc.player.getPos()
	if x_p==x and y_p==y+1 and z_p==z:
		player.setPos(-1,100,-47)