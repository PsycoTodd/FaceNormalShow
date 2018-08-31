import sys
import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def showNormal(str):
	normal_list = []
	with open(str, "r") as fo:
		print("get into the file\n")
		for line in fo:
			if(line[0:2] == "vn"):
				x = np.fromstring(line[3:], dtype = np.float, sep=' ')
				normal_list.append(x)
	# subsample 1000 to print
	rand_normals = random.sample(normal_list, 1000)
	#Visualize the data
	x = [0] * len(rand_normals)
	y = x
	z = x
	u = []
	v = []
	w = []
	for line in rand_normals:
		#print(np.sum(line**2)) # So we prove that the normal vector is normalized.
		u.append(line[0])
		v.append(line[1])
		w.append(line[2])
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.quiver(x, y, z, u, v, w)
	ax.set_xlim(-1, 1)
	ax.set_ylim(-1, 1)
	ax.set_zlim(-1, 1)
	plt.show()


if __name__ == "__main__":
	showNormal(sys.argv[1])