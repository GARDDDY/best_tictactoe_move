tictactoe = []
for i in range(3):
    tictactoe += [x for x in input()]
X, O = tictactoe.count('X'), tictactoe.count('O')
next_is = "X" if X == O else "O"

WINS = [ 
    [0, 1, 2, 3],
    [0, 3, 6, 1],
    [0, 4, 8, -1],
    [2, 4, 6, -1]
]

def get_range(list: list):
    if (list[1]) < 0:
        list[1] = 0
    return [list[1] + x for x in list[0]]

def sort_bests (bests: list):
    attack = []
    defense = []
    for i in bests:
        if (i == -1):
            continue
        if (i[1] == 2):
            defense.append(i)
        else:
            attack.append(i)

    if (len(attack) + len(defense) == 0):
        print("no free places to move")
        quit()
    else:
        best = -1
        best2 = -1
        for x in range(len(attack)):
            if ((attack[x][0]-attack[x][2])*(attack[x][1]+1) == -1):
                best = x
            if ((attack[x][0]-attack[x][2])*(attack[x][1]+1) == 1):
                best2 = x
                   
    if ((best != -1 and len(defense) > 0) or (best != -1 and len(defense) == 0)):
        return attack[best]
    elif (len(defense) > 0 and best == -1):
        return defense[0] 
    elif (len(defense) == 0 and best == -1):
        if (best2 != -1):
            return attack[best2]
        else:
            return attack[0]

def analyze_bests (bests: list, board: str, was_filtered: bool):
    if (not was_filtered):
        for i in range(len(bests)):
            if (bests[i][2] == 3 or bests[i][1] == 3):
                range_ = get_range(bests[i][3])
                string = f"{range_[0]+1}-{range_[1]+1}-{range_[2]+1}"
                print(f"Victory of {board[range_[0]]} on {string}!")
                quit()
            
            if (bests[i][0] == 0):
                bests[i] = -1
                continue

        analyze_bests(bests, board, True)
    else:
        best = sort_bests (bests)
        range_ = get_range(best[3])

        for x in range_[:3]:
            if (board[x] == ' '):
                print(f"Best move of {next_is} on {x+1} cell\n{x // 2 + 1 if x // 2 == 0 else x // 2} row {x % 3 + 1} cell!")
                quit()
                
def best_move (board: str, next: str):
    bests = []

    for win_arr in WINS:
        for n in range(0, win_arr[3]*3 if (win_arr[3] > 0) else 1, win_arr[3] if (win_arr[3] > 0) else 1):
            bests.append([0, 0, 0, [win_arr[:3], n]])
            for win_arr_only_values in win_arr[0:3]:
                if (board[win_arr_only_values + n] == ' '):
                    bests[len(bests)-1][0] += 1
                elif (board[win_arr_only_values + n] != next):
                    bests[len(bests)-1][1] += 1
                elif (board[win_arr_only_values + n] == next):
                    bests[len(bests)-1][2] += 1

    analyze_bests(bests, board, False)

best_move(tictactoe, next_is)