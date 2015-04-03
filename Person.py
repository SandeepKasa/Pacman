class Person:
	def __init__(self):
		self.x=0
		self.y=0
	def checkWall(self,matrix):
		if(matrix[self.x][self.y]!="X"):
		    return 0
		else:
		    return 1
	
