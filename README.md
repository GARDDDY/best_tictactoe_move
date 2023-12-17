# How this code works
Let's call a sequence of three identical symbols a winning combination. And in general terms - a combination.

The WINS array contains all winning combinations. The first 3 numbers are the basic configuration. The last, fourth, is the parameter by which each of the first 3 numbers must be increased to obtain a similar winning combination. If the parameter is -1, then a similar combination cannot be obtained by simply adding a number, therefore, you just need to add all similar ones manually. Fortunately, there are only 2 such combinations - diagonally.

The best_move function goes through each combination (8 different ones in total, following the laws of arithmetic). In it, for each combination, the number of free cells occupied by others and yours is calculated. All this data is entered into an array, which is later passed to the analyze_bests function. In it, each combination will be checked for winning and for completion. If there is a win in the combination, a corresponding message will be displayed and the code will finish working. Fullness - is it possible to include at least 1 character in this combination or not? If not, then such a combination ceases to be an array and is skipped in the following functions.

Then the already sorted array goes into perhaps the most important function - sort_bests. Only the following combinations can be included:
* 3, 0, 0 
* 1, 1, 1 
* 1, 0, 2 
* 2, 0, 1 
* 1, 2, 0 
* 2, 1, 0
* number of free cells, number of occupied by strangers, number of occupied by our own

In this function, all combinations (that are included in it) are divided into 2 types: “defense” and “attack”.
* The “defense” type can only be a combination of 1, 2, 0. *Why?*  - *Because if we don’t put our symbol on a free cell in it, we’ll lose. 1 - the number of free cells, 2 - the number of strangers.*
* All other combinations have the “attack” type. A rating is formed for them, according to which the best combination is determined.]

Obviously, 1, 0, 2 is the best combination. *Now it’s our turn, all that remains is to place only one symbol, and the other 2 are ours. If we put our symbol in this combination, then it will be our victory.*
It should be taken into account that combinations with the same numbers but with their different order, are completely different. 1, 0, 2 is much better than 2, 0, 1. *Why? In the first, we are 1 move away from victory, and in the second, we cannot say for sure whether this combination will be winning.*
Therefore, for each combination, a ranking is compiled using the formula **(number of free cells - number of own cells)*(number of others + 1)**.

Thus, combinations with the same numbers, but with their different order, will have different ratings. The best combination has a rating of -1 (there is no such thing as the higher the rating, the better), a slightly worse one (2, 0, 1) has a rating of 1. 
*For each other combination, you can also calculate the rating and compare them, as in the code. I didn’t do this because it very rarely happens that there are no good combinations (with a rating of -1 and 1).*

Then comes a simple conditional construction. 
* If there is no best combination, but there is a defense combination, then the move will be the last one. 
* If there is the best combination - move in it.
* If there is neither this nor that, then it doesn’t matter where to go, but if there is a combination with a rating of 1, then there is still the most reasonable move.

That's all! I hope everything is clear
