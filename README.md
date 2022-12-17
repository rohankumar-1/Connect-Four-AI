# Connect Four with "Artificial Intelligence"


## How to Run

The top files are ConnectFourGame.py or ConnectFourGUI.py. The first one will implement a Connect Four game in the terminal. This game is customizable, the user can choose between a second human player, a computer with random-generated moves, or a computer with AI and a specificied number of lookahead moves. The second one uses **pygame** to create an applet where a user plays against an AI with an input number of lookahead moves that is displayed nicely on a traditional Connect Four game board.

To download **pygame**, first install pip, and then in the python environment, run
`pip install pygame`.
This should install pygame within that environment, and so ConnectFourGUI.py will be able to run.

## Ideas

There are 3 main parts to this projects, in which problem-solving was paramount:

1. **Game mechanics**: Connect Four runs on a loop, like most games, where at each turn, the program checks whether the game has been won/tied. If not, the next loop of the game occurs. At each loop, the user places a piece down (given that the chosen column is valid), and then the other human/computer also places a piece down, until the condition of winning/tied occurs.

2. **Algorithms**: there were two main problems to solve, the first was checking for a winner, and the second was creating the AI

    1. To check for a winner, one must check horizontals and verticals for 4 pieces of the same color in a row, which is not challenging. However, to check diagonals, the system gets much more complex. Instead of having to run multiple loops, I tried a much easier and intuitive approach. By creating buffers on the sides of each row according to the row position, and simply checking the verticals of those columns, I can find if there are 4 in a diagonal (Pictured Below). By creating positive and negative buffers I can check left to right.
    
    2. To implement the AI capable of looking ahead a certain number of moves, the basic approach is this: for some given lookahead number N, create another AI opponenet with lookahead N-1, and then play that AI recursively until the original AI finds the best possible move, predicting N moves ahead of it. For example, an AI with lookahead 1 will play an AI with lookahead 0 (random), and for each move, it will check every column using recursive backtracking to find any possible way to win. The way that the AI knows which column to choose is from scoring the columns according to win percentage. For example, a column that will certainly lead to victory is 100, and a column that will certainly lead to defeat is 0. A random AI starts will all columns at 50. In the case of multiple columns with the same score, the AI chooses randomly. However, as the AI adds moves, this becomes less and less up to randomness.
    
3. **Graphics**: 

## What I learnt
