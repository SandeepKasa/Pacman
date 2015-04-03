from Person import *
class Pacman(Person):
	def __init__(self):
            Person.__init__(self) 
	    self.__score=0
   	    self.t=0
	def checkWall(self,matrix):
   	    if(matrix[self.x][self.y]=="X"):
	        return 0
	    else:
	        return 1
        def checkGhost(self,matrix):
            if(matrix[self.x][self.y]=="G"):
		return 0
	    else:
		return 1
        def collectCoins(self,matrix):
#	    print self.x,self.y
	    if(matrix[self.x][self.y]=="C"):
		self.__score=self.__score+1
		self.t=self.t+1
# 	    matrix[self.x][self.y]="P"
#           return matrix

	def MakeIt(self,matrix): 
	    matrix[self.x][self.y]="P"
	    return matrix
	def getscore(self):
	    return self.__score
