## MINIMAX algorithm 

MINIMAX is one of the classical AI algorithms in game theory, used to find the optimal move for a given player. It is used in a 2 player turn-based game (e.g.: Tic-Tac-Toe, chess, ...).


In MINIMAX the 2 players are called maximizer and minimizer, the first one tries to get the highest score possible meanwhile the second tries to do the opposite which is getting the lowest score possible.
Every board state has a value associated with it, these values are calculated by some heuristics which are different from game to game.


An example:

Let’s consider a game with 4 final states each one got a value assigned to it. Assuming you are the maximizer player who got the first play, which mean you are the root and you opponent at the next level. 


![Image of the first tree]( https://github.com/fouadkouzmane/minimax-python-implementation/blob/readme(modif)/images/minmax.png)


Since Minimax is a backtracking algorithm, we are going to test all possible paths and go back in order to choose the right move to do.

In this example the minimizer is going to choose 3 for the first two state and 2 for the next ones. 

![Image of the first tree]( https://github.com/fouadkouzmane/minimax-python-implementation/blob/readme(modif)/images/minmax1.png )


Then you are going to choose the maximum of these two values which is 3. 


## Python Implementation: 

We are going to create 2 classes, for the simple nodes called node and for the leaves called nodef which will allow us to create the building nodes of our tree.


Then we are going to define 4 methods: 
 
`makeTree(node,nodex,nodey):` connect a root (node) with his two childs (nodex,nodey)

`minimax(root):` return the best choice (the best nodes value) based on a given root node 

`MAX_VALUE(nodez):`  
if nodez is a leaf this function returns its value.

Else it returns the max of a given number (initialized at -1000) and the minimum value of the childs using the MIN_VALUE function 

`MIN_VALUE(nodez):`
if nodez is a leaf this function returns its value.

Else it returns the min of a given number (initialized at 1000) and the maximum value of the childs using the MAX_VALUE function  

ps : for the generated values on the leaves, we used the randrange function from the random package  

In the testing section, we created the nodes by naming them and mention the depth number and node number (node11= the first node in the level of depth 1, supposing the root exists in the level 0)and connecting them using the makeTree function.

Then we are going to print the results in a good curated way like we have a real tree.

enjoy this brief and comprehensive implementation of minimax algorithm in python3 😁


