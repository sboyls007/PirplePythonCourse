# Homework 6
# Draw a board game
# | |  0
#----- 1
# | |  2
#----- 3
# | |  4
#12345

Rows = 5
Columns = 6

def DrawBoard(rows, columns):
    for row in range(Rows):
        if row % 2 == 0:
            for col in range(1,columns):
                if col % 2 == 1:
                    if col != 5:
                        print(" ", end="")
                    else:
                        print(" ")
                else:
                    print("|", end="")
        else:
            print("-----")
    return True
                    

print(DrawBoard(Rows, Columns))