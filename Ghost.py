from Person import *
import random
class Ghost(Person):
	def __init__(self):
		Person.__init__(self)
		self.flag=0
                self.temp=0
        def ghostPosition(self,matrix):
		p=random.randint(-1,1)
		q=random.randint(-1,1)
		self.x=self.x+p
		self.y=self.y+q
		if(self.x>=15 or self.y>=35 or  self.x<0 or self.y<0 or matrix[self.x][self.y]=="X"):
		    self.x=self.x-p
		    self.y=self.y-q
		    self.temp=-1
		if(self.flag==1):
		    matrix[self.x-p][self.y-q]="C"
#                   self.flag=0
		if(matrix[self.x][self.y]=="P"):
		    self.temp=1
		if(matrix[self.x][self.y]=="C"):
		    matrix[self.x][self.y]="G"
		    if(not self.flag):
		    	matrix[self.x-p][self.y-q]="."
		    self.flag=1
	        if(matrix[self.x][self.y]=="."):
	            matrix[self.x][self.y]="G"
	      	    if(not self.flag):
	            	matrix[self.x-p][self.y-q]="."
		    else:
			self.flag = 0
                return matrix
