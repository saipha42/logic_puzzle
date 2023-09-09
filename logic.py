
n = 6

boards = []
for i in range(0, n) :
    row = []
    for k in range(0, n) :
        row.append(0)
    boards.append(row)

def check(row, col) :

    row_exist = False
    col_exist = False
    diagonal_exist = False

    current_row = boards[row]
    if current_row.__contains__(1) :
        row_exist = True
    
    for i in range(0, len(boards)) :

        for k in range(0, len(boards[i])) :
            if k == col :
                if boards[i][k] == 1 :
                    col_exist = True
                break
    
    rev_next_col = col
    next_col = col

    for i in range(row, n) :
        if next_col < n :
            if boards[i][next_col] == 1 :
                diagonal_exist = True
                break
        if rev_next_col > -1 :
            if boards[i][rev_next_col] == 1 :
                diagonal_exist = True
                break
        rev_next_col -= 1
        next_col += 1
    
    rev_next_col = col
    next_col = col 

    for i in range(row, -1, -1) :
        
        if next_col < n :
            if boards[i][next_col] == 1 :
                diagonal_exist = True
                break
        if rev_next_col > -1 :
            if boards[i][rev_next_col] == 1 :
                diagonal_exist = True
                break
        rev_next_col -= 1
        next_col += 1
    

    return not (row_exist or col_exist or diagonal_exist)

col = 0

while col < len(boards) :

    available = False

    for row in range(0, len(boards)) :

        if check(row, col) :
            
            boards[row][col] = 1
            available = True
            break
    

    if available == False :
        cur_col = col -1
        while cur_col > -1 :

            
            row = 1
           
            for i in range(n) :
                
                if boards[i][cur_col] == 1 :
                    row += i
                boards[i][cur_col] = 0
            
            

            for i in range(row, n) :
                
                if check(i, cur_col) :
                    boards[i][cur_col] = 1
                    available = True
                    break
            
            if available :
                col = cur_col
                break
            cur_col = cur_col-1
            
    col += 1

if not (1 in boards[0]) :
    print("No solution")
    exit()


for i in boards :
    print(i)


