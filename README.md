# Connect-Four---Play-v2-Python

# Q5: Connect Four - Play v2
Weight: 20%

Last update: 18 Oct, 7am

In this question, we are providing you with a partial solution that you will have to extend. Play a few games to familiarize yourself with what the program does. Note: It is similar to Q3 of Assignment 1. 

Your task in this question is to forbid illegal moves and detect winning/draw conditions. If a player attempts to drop a disc in a column that is already full it is called an illegal move. The move will be ignored at the same player will be prompted again. If player X has won the game by being the first to form a horizontal, vertical, or diagonal line of four of his/her own discs, the game will output Player X has won!. If player O has won the game by being the first to form a horizontal, vertical, or diagonal line of four of his/her own discs, the game will output Player O has won!. If there is draw, i.e., no players can place any discs any more because the board is full, the game will output Draw!.

Investigate the following sample runs to understand the I/O requirements. Test your program extensively by playing games for various win conditions.

```

Standard game? (y/n): n
r? (2 - 20): 2
c? (2 - 20): 2
1 · · 
0 · · 
  0 1 
playerX (col #): 0
1 · · 
0 X · 
  0 1 
playerO (col #): 0
1 O · 
0 X · 
  0 1 
playerX (col #): 0
1 O · 
0 X · 
  0 1 
playerX (col #): e
bye

Standard game? (y/n): n
r? (2 - 20): 2
c? (2 - 20): 3
1 · · · 
0 · · · 
  0 1 2 
playerX (col #): 2
1 · · · 
0 · · X 
  0 1 2 
playerO (col #): 2
1 · · O 
0 · · X 
  0 1 2 
playerX (col #): 1
1 · · O 
0 · X X 
  0 1 2 
playerO (col #): 2
1 · · O 
0 · X X 
  0 1 2 
playerO (col #): 2
1 · · O 
0 · X X 
  0 1 2 
playerO (col #): 1
1 · O O 
0 · X X 
  0 1 2 
playerX (col #): 0
1 · O O 
0 X X X 
  0 1 2 
playerO (col #): 0
1 O O O 
0 X X X 
  0 1 2 
Draw!
bye

Standard game? (y/n): n
r? (2 - 20): 2
c? (2 - 20): 4
1 · · · · 
0 · · · · 
  0 1 2 3 
playerX (col #): 0
1 · · · · 
0 X · · · 
  0 1 2 3 
playerO (col #): 1
1 · · · · 
0 X O · · 
  0 1 2 3 
playerX (col #): 2
1 · · · · 
0 X O X · 
  0 1 2 3 
playerO (col #): 3
1 · · · · 
0 X O X O 
  0 1 2 3 
playerX (col #): 0
1 X · · · 
0 X O X O 
  0 1 2 3 
playerO (col #): 0
1 X · · · 
0 X O X O 
  0 1 2 3 
playerO (col #): 2
1 X · O · 
0 X O X O 
  0 1 2 3 
playerX (col #): 2
1 X · O · 
0 X O X O 
  0 1 2 3 
playerX (col #): 3
1 X · O X 
0 X O X O 
  0 1 2 3 
playerO (col #): 1
1 X O O X 
0 X O X O 
  0 1 2 3 
Draw!
bye

Standard game? (y/n): n
r? (2 - 20): 4
c? (2 - 20): 3
3 · · · 
2 · · · 
1 · · · 
0 · · · 
  0 1 2 
playerX (col #): 0
3 · · · 
2 · · · 
1 · · · 
0 X · · 
  0 1 2 
playerO (col #): 0
3 · · · 
2 · · · 
1 O · · 
0 X · · 
  0 1 2 
playerX (col #): 0
3 · · · 
2 X · · 
1 O · · 
0 X · · 
  0 1 2 
playerO (col #): 0
3 O · · 
2 X · · 
1 O · · 
0 X · · 
  0 1 2 
playerX (col #): 0
3 O · · 
2 X · · 
1 O · · 
0 X · · 
  0 1 2 
playerX (col #): 0
3 O · · 
2 X · · 
1 O · · 
0 X · · 
  0 1 2 
playerX (col #): 2
3 O · · 
2 X · · 
1 O · · 
0 X · X 
  0 1 2 
playerO (col #): 2
3 O · · 
2 X · · 
1 O · O 
0 X · X 
  0 1 2 
playerX (col #): 2
3 O · · 
2 X · X 
1 O · O 
0 X · X 
  0 1 2 
playerO (col #): 1
3 O · · 
2 X · X 
1 O · O 
0 X O X 
  0 1 2 
playerX (col #): 1
3 O · · 
2 X · X 
1 O X O 
0 X O X 
  0 1 2 
playerO (col #): 1
3 O · · 
2 X O X 
1 O X O 
0 X O X 
  0 1 2 
playerX (col #): 1
3 O X · 
2 X O X 
1 O X O 
0 X O X 
  0 1 2 
playerO (col #): 1
3 O X · 
2 X O X 
1 O X O 
0 X O X 
  0 1 2 
playerO (col #): 2
3 O X O 
2 X O X 
1 O X O 
0 X O X 
  0 1 2 
Draw!
bye

Standard game? (y/n): y
5 · · · · · · · 
4 · · · · · · · 
3 · · · · · · · 
2 · · · · · · · 
1 · · · · · · · 
0 · · · · · · · 
  0 1 2 3 4 5 6 
playerX (col #): 0
5 · · · · · · · 
4 · · · · · · · 
3 · · · · · · · 
2 · · · · · · · 
1 · · · · · · · 
0 X · · · · · · 
  0 1 2 3 4 5 6 
playerO (col #): 4
5 · · · · · · · 
4 · · · · · · · 
3 · · · · · · · 
2 · · · · · · · 
1 · · · · · · · 
0 X · · · O · · 
  0 1 2 3 4 5 6 
playerX (col #): 0
5 · · · · · · · 
4 · · · · · · · 
3 · · · · · · · 
2 · · · · · · · 
1 X · · · · · · 
0 X · · · O · · 
  0 1 2 3 4 5 6 
playerO (col #): 4
5 · · · · · · · 
4 · · · · · · · 
3 · · · · · · · 
2 · · · · · · · 
1 X · · · O · · 
0 X · · · O · · 
  0 1 2 3 4 5 6 
playerX (col #): 0
5 · · · · · · · 
4 · · · · · · · 
3 · · · · · · · 
2 X · · · · · · 
1 X · · · O · · 
0 X · · · O · · 
  0 1 2 3 4 5 6 
playerO (col #): 4
5 · · · · · · · 
4 · · · · · · · 
3 · · · · · · · 
2 X · · · O · · 
1 X · · · O · · 
0 X · · · O · · 
  0 1 2 3 4 5 6 
playerX (col #): 0
5 · · · · · · · 
4 · · · · · · · 
3 X · · · · · · 
2 X · · · O · · 
1 X · · · O · · 
0 X · · · O · · 
  0 1 2 3 4 5 6 
Player X has won!
bye

Standard game? (y/n): n
r? (2 - 20): 4
c? (2 - 20): 4
3 · · · · 
2 · · · · 
1 · · · · 
0 · · · · 
  0 1 2 3 
playerX (col #): 0
3 · · · · 
2 · · · · 
1 · · · · 
0 X · · · 
  0 1 2 3 
playerO (col #): 1
3 · · · · 
2 · · · · 
1 · · · · 
0 X O · · 
  0 1 2 3 
playerX (col #): 1
3 · · · · 
2 · · · · 
1 · X · · 
0 X O · · 
  0 1 2 3 
playerO (col #): 2
3 · · · · 
2 · · · · 
1 · X · · 
0 X O O · 
  0 1 2 3 
playerX (col #): 2
3 · · · · 
2 · · · · 
1 · X X · 
0 X O O · 
  0 1 2 3 
playerO (col #): 3
3 · · · · 
2 · · · · 
1 · X X · 
0 X O O O 
  0 1 2 3 
playerX (col #): 2
3 · · · · 
2 · · X · 
1 · X X · 
0 X O O O 
  0 1 2 3 
playerO (col #): 3
3 · · · · 
2 · · X · 
1 · X X O 
0 X O O O 
  0 1 2 3 
playerX (col #): 3
3 · · · · 
2 · · X X 
1 · X X O 
0 X O O O 
  0 1 2 3 
playerO (col #): 0
3 · · · · 
2 · · X X 
1 O X X O 
0 X O O O 
  0 1 2 3 
playerX (col #): 3
3 · · · X 
2 · · X X 
1 O X X O 
0 X O O O 
  0 1 2 3 
Player X has won!
bye

Standard game? (y/n): n
r? (2 - 20): 4
c? (2 - 20): 4
3 · · · · 
2 · · · · 
1 · · · · 
0 · · · · 
  0 1 2 3 
playerX (col #): 3
3 · · · · 
2 · · · · 
1 · · · · 
0 · · · X 
  0 1 2 3 
playerO (col #): 3
3 · · · · 
2 · · · · 
1 · · · O 
0 · · · X 
  0 1 2 3 
playerX (col #): 3
3 · · · · 
2 · · · X 
1 · · · O 
0 · · · X 
  0 1 2 3 
playerO (col #): 3
3 · · · O 
2 · · · X 
1 · · · O 
0 · · · X 
  0 1 2 3 
playerX (col #): 2
3 · · · O 
2 · · · X 
1 · · · O 
0 · · X X 
  0 1 2 3 
playerO (col #): 2
3 · · · O 
2 · · · X 
1 · · O O 
0 · · X X 
  0 1 2 3 
playerX (col #): 2
3 · · · O 
2 · · X X 
1 · · O O 
0 · · X X 
  0 1 2 3 
playerO (col #): 2
3 · · O O 
2 · · X X 
1 · · O O 
0 · · X X 
  0 1 2 3 
playerX (col #): 1
3 · · O O 
2 · · X X 
1 · · O O 
0 · X X X 
  0 1 2 3 
playerO (col #): 1
3 · · O O 
2 · · X X 
1 · O O O 
0 · X X X 
  0 1 2 3 
playerX (col #): 2
3 · · O O 
2 · · X X 
1 · O O O 
0 · X X X 
  0 1 2 3 
playerX (col #): 1
3 · · O O 
2 · X X X 
1 · O O O 
0 · X X X 
  0 1 2 3 
playerO (col #): 0
3 · · O O 
2 · X X X 
1 · O O O 
0 O X X X 
  0 1 2 3 
playerX (col #): 1
3 · X O O 
2 · X X X 
1 · O O O 
0 O X X X 
  0 1 2 3 
playerO (col #): 0
3 · X O O 
2 · X X X 
1 O O O O 
0 O X X X 
  0 1 2 3 
Player O has won!
bye

```
