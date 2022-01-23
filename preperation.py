play_board = [
    [1,8,9,7,0,0,0,1,3],
    [1,8,9,7,0,0,0,1,3],
    [1,8,9,7,0,0,0,1,3],
    [1,8,9,7,0,0,0,1,3],
    [1,8,9,7,0,0,0,1,3],
    [1,8,9,7,0,0,0,1,3],
    [1,8,9,7,0,0,0,1,3],
    [1,8,9,7,0,0,0,1,3],
    [1,8,9,7,0,0,0,1,3]
]

def valid(pbo,num,loc):
    for i in range(len(pbo[0])):
        #Row checking
        if pbo[loc[0]][i] == num and loc[1] != i :
            return False
        #Column Checking
        if pbo[i][loc[1]] == num and loc[0] != i :
            return False
        #Box Checking





def display_playboard(pbo):
    for i in range(len(pbo)):
        if i % 3 == 0 and i != 0:
            print("--------------------------------------")
        for j in range(len(pbo[0])):
            if j % 3 == 0 and j != 0:
             print(" | ", end = "")
            if j==8:
              print(pbo[i][j])
            else:
                 print(str(pbo[i][j]) + " ", end = "")

#display_playboard(play_board)

def empty_search(pbo): # function for find the empty square on the play board
    for i in range(len(pbo)):
        for j in range(len(pbo[0])):
            if pbo[i][j] == 0:
                print(i,j)#y,x
    return None
#empty_search(play_board)