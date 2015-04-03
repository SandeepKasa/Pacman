Question 1:

In my game,the coins are generated randomly . The coins are regenerated after all of them are collected by Pacman . Each time ,they are regenerated the number of coins keep changing . The number of coins range between 25-35.
The Wall in my games are fixed at the start of the game.
Wrong Entry will print 'Invalid Entry'

OOPS---
--->Inheritance  -- The classes Pacman and Ghost in my code inherit from Person Class......
--->Polymorphism -- checkWall() function is present both in Person Class and Pacman Class but their functionality is a bit different....As we 
                    already know Pacman class is inherited from Person Class so when an object of Pacman is created and checkWall() method is called...then the checkWall() function present in the Pacman Class gets executed..This exhibits the principle of Polymorphism...
--->Encapsulation-- The local variable 'score' present in the Pacman class is encapsulated by writing __ before the variabel...
--->Modularity   -- In my code , I'v imported the 'random' module and used randint() method from it....Also , My Person Class,Pacman Class and 
                    and Ghost Class are written in different files and are imported in main file A.py.....Modularity is exhibited.

Question 2:

Apart from ls,ls -l,cp,rm,mv,dirstr , I'v included few other functions also:
-->ls -a , ls -al , ls 'path',ls -a 'path',ls -al'path,ls -l 'path'
-->cp,cp -r ,rm,rm -r for multiple files and directories 
-->Exception handling was done to most of the exceptions
-->Program terimates on typing 'exit' command
-->Any other command will print 'Command Entry Not Found' 
