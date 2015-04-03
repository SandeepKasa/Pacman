import os
import stat
import string,time,pwd,grp,shutil
from datetime import datetime
k=0
def lishidden():
	wow=os.listdir(".")
	wow.sort(key=lambda z:z.lower())
	for i in range(len(wow)):
		print wow[i],
        print("\n"),
def newlishidden(moo):
	try:
	    wow=os.listdir(moo)
	    wow.sort(key=lambda z:z.lower())
	except Exception,exp:
	    print exp
	    return 0
	for i in range(len(wow)):
            print wow[i],
	    print("\n"),
def lis():
   	wow=os.listdir(".")
	wow.sort(key=lambda z:z.lower())
	for i in range(len(wow)):
	    if(wow[i][0]!="."):
	        print wow[i],
        print("\n"),
def newlis(moo):
	try:
	    wow=os.listdir(moo)
	    wow.sort(key=lambda z:z.lower())
	except Exception,exp:
	    print exp
	    return 0
	for i in range(len(wow)):
	    if(wow[i][0]!="."):
	        print wow[i],
	print("\n"),
	
def lislong(lo,moo):
	try:
	    name=os.listdir(moo)
	    name.sort(key=lambda z:z.lower())
	except Exception,exp:
	    print exp
	    return 0
	usr=[]
	for i in range(len(name)):
            idiot=moo+ '/' + name[i]
            rofl=stat.S_ISDIR(os.stat(idiot).st_mode)
            if(rofl):
	        usr.append('d')
	    else:
	        usr.append('-')
	    num=oct(os.stat(idiot).st_mode)
#           print num
            temp=list(num)
	    if len(str(num))==7:
                a=4
		b=7
	    else:
		a=3
		b=6
            for j in range(a,b):
	        if(temp[j]=='7'):
	            a=usr[i]
		    usr[i]=a+'rwx'
                elif(temp[j]=='1'):
		    a=usr[i]
		    usr[i]=a+'--x'
                elif(temp[j]=='2'):
	            a=usr[i]
		    usr[i]=a+'-w-'
                elif(temp[j]=='4'):
                    a=usr[i]
	            usr[i]=a+'r--'
	        elif(temp[j]=='6'):
	            a=usr[i]
	            usr[i]=a+'rw-'
	        elif(temp[j]=='3'):
      		    a=usr[i]
	            usr[i]=a+'-wx'
	        else:
        	    a=usr[i]
	            usr[i]=a+'r-x'
 
	for i in range(len(name)):
            hard = os.stat(idiot).st_nlink
            s =    os.stat(idiot).st_size
            you  = pwd.getpwuid(os.stat(idiot).st_uid)[0]
            me   = grp.getgrgid(os.stat(idiot).st_gid)[0]
            tim = time.ctime(os.stat(idiot).st_mtime)
	    tim = tim.split()
     	    tim.remove(tim[0])
	    fog= tim[2].split(':')
            del(fog[2])
            tim[2] = string.join(fog,":")
	    if (int(tim[3]) == datetime.now().year):
                tim.remove(tim[3])
	    else:
	        tim.remove(tim[2])
	    tim = string.join(tim, ' ')
#           print lo
	    if(lo=="-al"):
	        print usr[i]+' '+str(hard) + ' ' + you + ' ' + me + ' ' +  str(s) + ' ' + str(tim) + ' ' +name[i]
	    if(lo=="-l"):
		if(name[i][0]!="."):
		    print usr[i]+' '+str(hard)+' '+you+  ' '+me + ' '+str(s) + ' '+str(tim) + ' '+name[i]
            

		    
	    
def co(a,b):
	try:
	    shutil.copy(a,b)
	except Exception,exp:
	    print exp

def codir(a,b):
	try:
	    shutil.copytree(a,b)
	except Exception,exp:
	    print exp

def mov(a,b):
	try:
	    shutil.move(a,b)
	except Exception,exp:
	    print exp

def dell(a):
	try:
            os.remove(a)
	except Exception,exp:
	    print exp

def deldir(a):
	try:
	    shutil.rmtree(a)
	except Exception,exp:
	    print exp
def dirstr(pat,level):
	try:
	    luv=os.listdir(pat)
	    luv.sort(key=lambda z:z.lower())
	    k=len(luv)
	except Exception,exp:
	    print exp
	    return 0
	if(k==0):
	    print "\n",
	    print "                 (EMPTY FOLDER)"
	    return 0
	
        else:
	    for i in range(len(luv)):
		koo=pat+'/'+luv[i]
	        if(not stat.S_ISDIR(os.stat(koo).st_mode)):
		    for j in range(2 * level):
			if j==level and pat!=".":
			    print "|",
			else:
	                    print " ",
	            print "|"
	            for j in range(2 * level):
			if j==level and pat!=".":
			    print "|",
			else:
			    print " ",
	            print "#-"+luv[i]
	        else:
	            for j in range(2 * level):
			if j==level and pat!=".":
			    print "|",
			else:
	       	            print " ",
	            print "|"
	            for j in range(2 * level):
			if j==level and pat!=".":
			    print "|",
			else:
			    print " ",
		    print "#--------  Folder Name:"+" "+luv[i]+'/'+" "+"--------#"
		    mywish = pat + '/' + luv[i]
		    dirstr(mywish,level+1)
        return 0	 
if __name__ == '__main__':
    kas=0
    while(1):
	if kas==0:
	    print "This is your terminal...Enter your bash commands: "
	print "$",
      	var=raw_input()  
        cop=var.split()
#	print cop
#	print cop[0],cop[1],cop[2]
        if(cop[0]=="ls" and len(cop)==2 and var!="ls -a" and var!="ls -l" and var!="ls -al"):
	    if(os.path.exists(cop[1])):
	        newlis(cop[1])
	    else:
	        print "ls: cannot access"+" "+ cop[1]+" "+": No such file or directory"
	elif(var=="exit"):
	    break
        elif(cop[0]=="ls" and len(cop)==1):
            lis()
	elif(var=="ls -a" and len(cop)==2):
	    lishidden()
        elif(var!="dirstr"):
            if( cop[1]=="-a" and len(cop)==3):
                if(os.path.exists(cop[2])):
                    newlishidden(cop[2])
	        else:
		    print "ls: cannot access"+" "+ cop[2]+" "+": No such file or directory"

    	    elif( cop[1]=="-l" or cop[1]=="-al"):
	        if(len(cop)==2):
	            lislong(cop[1],"./")
	        else:
		    if(os.path.exists(cop[2])):
	                lislong(cop[1],cop[2])
	            else:
		        print "ls: cannot access"+" "+ cop[2]+" "+": No such file or directory"

        elif(cop[0]=="cp" and cop[1]!="-r"):
	    
#	    print cop[0],cop[1],cop[2]
	    if(os.path.exists(cop[1])):
                roll=stat.S_ISDIR(os.stat(cop[1]).st_mode)
	    if(not os.path.exists(cop[1])):
	        print "cp: cannot copy"+" '"+cop[1]+"'"+": No such file or directory"
	    elif(roll):
		print("cp: omitting directory"+" '"+cop[1]+"'")

            else:
	        co(cop[1],cop[2])

    	elif(cop[0]=="cp" and cop[1]=="-r"):
	    if(os.path.exists(cop[2])):
                codir(cop[2],cop[3])
	    else:
	        print "cp: cannot copy"+" '"+cop[2]+"'"+": No such file or directory"
    	elif(cop[0]=="mv"):
	    if(not os.path.exists(cop[1])):
		print "mv: cannot move"+" '"+cop[1]+"'"+": No such file or directory"
	    else:
    	        mov(cop[1],cop[2])
    	elif(cop[0]=="rm" and cop[1]!="-r"):
	    for i in range(1,len(cop)):
		if(os.path.exists(cop[1])):
	            roll=stat.S_ISDIR(os.stat(cop[1]).st_mode)
		if(not os.path.exists(cop[1])):
		    print "rm: cannot remove"+" '"+cop[1]+"'"+": No such file or directory"
	        elif(roll):
		    print("rm: cannot remove"+" '" +cop[1]+"'"+": Is a directory")
		else:
		    dell(cop[i])

        elif(cop[0]=="rm" and cop[1]=="-r"):
	    for i in range(2,len(cop)):
	        if(not os.path.exists(cop[2])):
		    print "rm: cannot remove"+" '"+cop[2]+"'"+": No such file or directory"
		else:
		    deldir(cop[i])

        elif(var=="dirstr"):
	    fool=os.getcwd()
	    fool=fool.split("/")
	    fool=fool[len(fool)-1]
	    print "#---------  Folder Name:"+" "+fool+'/'+" "+"--------#"
	    dirstr(".",1)
	else:
	    print "Command Entry not found----"

        kas=kas+1
	    
	    

	  






	    

