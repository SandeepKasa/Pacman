import random
from Person import *
from Pacman import *
from Ghost import *
matrix=[
[".",".",".",".",".",".",".",".",".",".",".","X",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".","X",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".","X",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".","P",".",".",".",".",".",".",".","X",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".","X",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","G",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".","X",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
["X","X","X","X",".","X","X","X","X","X",".","X","X","X","X","X","X","X","X","X",".","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X"],
[".",".","X","X",".",".",".",".",".",".",".","X",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".","X",".",".",".",".",".",".",".","X",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".","X",".",".",".",".",".",".",".","X",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".","X",".",".",".",".",".",".",".","X",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".","X",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".","X",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
]
def printit():
	for i in range(15):
		for j in range(35):
			print(matrix[i][j]),
		print("\n"),
def coins():
	numb=random.randint(25,35)
	numb2=numb
	for i in range(numb):
		a=random.randint(0,14)
		b=random.randint(0,34)
		if(matrix[a][b]=="X" or matrix[a][b]=="P" or matrix[a][b]=="G"):
		    numb2=numb2-1
		else:
		    matrix[a][b]="C"
        return numb2

if __name__ == '__main__':
        max=coins()
	printit()
	print "Score:","0"
	ob1=Pacman()
	ob2=Ghost()
	ob1.x=3
	ob1.y=3
	ob2.x=5
	ob2.y=18
	while(1):
		if(max==ob1.t):
		    ob1.t=0
	            max=coins()
		print "Enter move:",
	        var=raw_input()
	        matrix=ob2.ghostPosition(matrix)
	        if(ob2.temp==1):
		    print "Final Score:",ob1.getscore()
		    print "GAME OVER",
		    break
	      	if(var=="w"):
		    if(ob1.x-1<0):
		       	printit()
			print "Score:",ob1.getscore()
	            else:
	                matrix[ob1.x][ob1.y]="."
			ob1.x=ob1.x-1
	                res=ob1.checkGhost(matrix)
		        res1=ob1.checkWall(matrix)
		        if(res==0):
#			    print "1"
		            print "Final Score:",ob1.getscore()
			    print "GAME OVER"
			    break
		        if(res1!=0):
#			    print "2"
#	                    print "Halou"
		            matrix=ob1.collectCoins(matrix)
			elif(res1==0):
#			    print "3"
			    ob1.x=ob1.x+1
			    matrix[ob1.x][ob1.y]="P"
	                printit()
    		        print "Score:",ob1.getscore()

	                    
		elif(var=="a"):
		    if(ob1.y-1<0):
			    printit()
			    print "Score:",ob1.getscore()

		    else:
			    matrix[ob1.x][ob1.y]="."
		            ob1.y=ob1.y-1
		            res=ob1.checkGhost(matrix)
                            res1=ob1.checkWall(matrix)
		            if(res==0):
				print "Final Score:",ob1.getscore()
				print "GAME OVER"
				break
                            if(res1!=0):        
		                matrix=ob1.collectCoins(matrix)
			    elif(res1==0):
				ob1.y=ob1.y+1
				matrix[ob1.x,ob1.y]="P"
			    printit()
			    print "Score:",ob1.getscore()

	       	elif(var=="s"):
		     if(ob1.x+1>=15):
			    printit()
			    print "Score:",ob1.getscore()

		     else:
			    matrix[ob1.x][ob1.y]="."
			    ob1.x=ob1.x+1
                            res=ob1.checkGhost(matrix)
                            res1=ob1.checkWall(matrix)
		            if(res==0):
				print "Final Score:",ob1.getscore()
				print "GAME OVER"
				break
                            if(res1!=0):        
		                matrix=ob1.collectCoins(matrix)
			    elif(res1==0):
			       	ob1.x=ob1.x-1
		                matrix[ob1.x][ob1.y]="P"

			    printit()
			    print "Score:",ob1.getscore()

	        elif(var=="d"):
		    if(ob1.y+1>=35):
			    printit()
			    print "Score:",ob1.getscore()

	            else:
			    matrix[ob1.x][ob1.y]="."
			    ob1.y=ob1.y+1
                            res=ob1.checkGhost(matrix)
	                    res1=ob1.checkWall(matrix)
		            if(res==0):
				    print "Final Score:",ob1.getscore()
				    print "GAME OVER"
				    break
                            if(res1!=0):        
		                matrix=ob1.collectCoins(matrix)
			    elif(res1==0):
				ob1.y=ob1.y-1
				matrix[ob1.x][ob1.y]="P"
			    printit()
			    print "Score:",ob1.getscore()

       	        elif(var=="q"):
		    print "Final Score: ",ob1.getscore()
		    print "GAME STOPPED"
		    break
	        else:
		    print "Invalid Entry.."


	
