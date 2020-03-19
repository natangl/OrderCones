from orderByDistance import *
from tkinter import *

"""
Take saved map and order cones by chosen function
"""
class NumberdMap:
	def readMap(self,fileName):
		toRead=open(fileName, 'r')

		carPos = [int(toRead.readline()),int(toRead.readline())]
		carDir = [int(toRead.readline()),int(toRead.readline())]

		bluePoints = []
		pointStr = toRead.readline()
		while pointStr != "break\n":
			a = pointStr.split(" ")
			newPoint = [int(a[0]),int(a[1])]
			bluePoints.append(newPoint)
			pointStr = toRead.readline()
			
		yellowPoints = []
		pointStr = toRead.readline()
		while pointStr != '':
			a = pointStr.split(" ")
			newPoint = [int(a[0]),int(a[1])]
			yellowPoints.append(newPoint)
			pointStr = toRead.readline()

		toRead.close()
		return carPos, carDir, bluePoints, yellowPoints
		

	def __init__(self,fileName):
		carPos, carDir, bluePoints, yellowPoints = self.readMap(fileName)
		
		#change function here
		self.carPos, self.carDir, self.bluePoints, self.yellowPoints = orderByDis(bluePoints, yellowPoints,carPos,carDir)
			
	def printMap(self):
		root = Tk()

		my_canvas = Canvas(root, width=500, height=500)

		for point in self.bluePoints:
			my_canvas.create_oval(point[0]-3,point[1]-3,point[0]+3,point[1]+3,fill="blue")
			label = Label(master = root,text=str(point[2]))
			label.place(x=point[0] - 5,y= point[1] - 30)
		for point in self.yellowPoints:
			my_canvas.create_oval(point[0]-3,point[1]-3,point[0]+3,point[1]+3,fill="yellow")
			label = Label(master = root,text=str(point[2]))
			label.place(x=point[0] - 5,y= point[1] - 30)
		my_canvas.create_oval(self.carPos[0]-3,self.carPos[1]-3,self.carPos[0]+3,self.carPos[1]+3,fill="purple")
		my_canvas.create_line(self.carPos[0],self.carPos[1],self.carPos[0]+self.carDir[0],self.carPos[1]+self.carDir[1],fill="red")
			
		my_canvas.pack()

		root.mainloop()

#change the name of the map to be loaded here
np = NumberdMap("Map1.txt")
np.printMap()
