Grid = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]]
turn = "X"
AltTurn = "O"
Playing = True
def PlayAgainMethod():
    PlayAgain = input("Type 'Yes' to start: ")
    if PlayAgain == str("Yes"):
        Grid = [
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0]]
        turn = "X"
        AltTurn = "O"
        return Grid
    else:
        PlayAgainMethod()
        
def PlayerMoveMethod():   
    PlayerVar = input("Player " +turn+ " move: ")
    
    
    if PlayerVar in ["1","2","3","4","5","6","7"]:
            PlayerVarInt = int(PlayerVar)
            PlayerVarInt -= 1
            count = 0
            for i in Grid[PlayerVarInt]:
                if i != 0:
                  i = 1
                count += i
            Grid[PlayerVarInt][ 5-count] = turn
            print(count)
    else:
            print("please put one of the numbers")
            PlayerMoveMethod()

while Playing:
    GridNumberDown = 0
    while GridNumberDown < 6 :                  #Drawing grid
        Line = ""
        GridNumberAcross = 0
        while GridNumberAcross < 7 :
            add = str(Grid[GridNumberAcross][GridNumberDown])
            if add == "0" :
                add = " "
            Line += add + "|"
            GridNumberAcross += 1
        print("|"+Line)     
        GridNumberDown += 1
    print(" 1 2 3 4 5 6 7")
    
    PlayerMoveMethod()
    

    ColumnNum = -1
    Winning = 0
    for Column in Grid:
        ColumnNum += 1
        RowNum = -1
        for Row in Column:
            RowNum += 1
            if Row != 0:
                if ColumnNum <= 3 and RowNum <= 2:
                    if Grid[ColumnNum + 1][RowNum + 1] == Grid[ColumnNum][RowNum]:
                        if Grid[ColumnNum + 2][RowNum + 2] == Grid[ColumnNum][RowNum]:
                            if Grid[ColumnNum + 3][RowNum + 3] == Grid[ColumnNum][RowNum]:
                                Winning += 1
                if ColumnNum <= 3:
                    if Grid[ColumnNum + 1][RowNum] == Grid[ColumnNum][RowNum]:
                        if Grid[ColumnNum + 2][RowNum] == Grid[ColumnNum][RowNum]:
                            if Grid[ColumnNum + 3][RowNum] == Grid[ColumnNum][RowNum]:
                                Winning += 1
                if ColumnNum <= 3 and RowNum >= 3:
                    if Grid[ColumnNum + 1][RowNum - 1] == Grid[ColumnNum][RowNum]:
                        if Grid[ColumnNum + 2][RowNum - 2] == Grid[ColumnNum][RowNum]:
                            if Grid[ColumnNum + 3][RowNum - 3] == Grid[ColumnNum][RowNum]:
                                Winning += 1
                if RowNum <= 2:
                    if Grid[ColumnNum][RowNum + 1] == Grid[ColumnNum][RowNum]:
                        if Grid[ColumnNum][RowNum + 2] == Grid[ColumnNum][RowNum]:
                            if Grid[ColumnNum][RowNum + 3] == Grid[ColumnNum][RowNum]:
                                Winning += 1
                if RowNum >= 3:
                    if Grid[ColumnNum][RowNum - 1] == Grid[ColumnNum][RowNum]:
                        if Grid[ColumnNum][RowNum - 2] == Grid[ColumnNum][RowNum]:
                            if Grid[ColumnNum][RowNum - 3] == Grid[ColumnNum][RowNum]:
                                Winning += 1
                if ColumnNum >= 3 and RowNum <= 2:
                    if Grid[ColumnNum - 1][RowNum + 1] == Grid[ColumnNum][RowNum]:
                        if Grid[ColumnNum - 2][RowNum + 2] == Grid[ColumnNum][RowNum]:
                            if Grid[ColumnNum - 3][RowNum + 3] == Grid[ColumnNum][RowNum]:
                                Winning += 1
                if ColumnNum >= 3:
                    if Grid[ColumnNum - 1][RowNum] == Grid[ColumnNum][RowNum]:
                        if Grid[ColumnNum - 2][RowNum] == Grid[ColumnNum][RowNum]:
                            if Grid[ColumnNum - 3][RowNum] == Grid[ColumnNum][RowNum]:
                                Winning += 1
                if ColumnNum >= 3 and RowNum >= 3:
                    if Grid[ColumnNum - 1][RowNum - 1] == Grid[ColumnNum][RowNum]:
                        if Grid[ColumnNum - 2][RowNum - 2] == Grid[ColumnNum][RowNum]:
                            if Grid[ColumnNum - 3][RowNum - 3] == Grid[ColumnNum][RowNum]:
                                Winning += 1
    if Winning > 0:
        

        GridNumberDown = 0
        while GridNumberDown < 6 :                  #Drawing grid
            Line = ""
            GridNumberAcross = 0
            while GridNumberAcross < 7 :
                add = str(Grid[GridNumberAcross][GridNumberDown])
                if add == "0" :
                    add = " "
                Line += add + "|"
                GridNumberAcross += 1
            print("|"+Line)     
            GridNumberDown += 1
        print(" 1 2 3 4 5 6 7")
        print( "Player " + turn + " Wins!")

    if Winning > 0:
        print("Would you like to play again?")
        Grid = PlayAgainMethod()
        
        
    temp = turn
    turn = AltTurn
    AltTurn = temp




    

