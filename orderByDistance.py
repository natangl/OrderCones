import math

"""
Function takes orders cones by distance to car
"""

def takeThird(elem):
	return elem[2]

def orderByDis(bluePoints, yellowPoints, carPos, carDir):
	for point in bluePoints:
		point.append(math.sqrt((carPos[0] - point[0])**2 + (carPos[1] - point[1])**2))
	for point in yellowPoints:
		point.append(math.sqrt((carPos[0] - point[0])**2 + (carPos[1] - point[1])**2))
		
	bluePoints.sort(key=takeThird)
	yellowPoints.sort(key=takeThird)

	count = 0
	for point in bluePoints:
		point[2] = count
		count += 1
	count = 0
	for point in yellowPoints:
		point[2] = count
		count += 1
		
	return carPos, carDir, bluePoints, yellowPoints	