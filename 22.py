T = 10
 
for t in range(T):
    case = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]
     
    col, row = 0, 0
    for end in range(100):
        if arr[99][end] == 2:
            col = 99
            row = end
            break
 
     
    while col != 0:     
         
        if row-1 >= 0 and arr[col][row-1] == 1:
            while row-1 >= 0 and arr[col][row-1] == 1:   
                row -= 1
 
         
        elif row+1 < 100 and arr[col][row+1] == 1:
            while row+1 < 100 and arr[col][row+1] == 1:   
                row += 1
 
         
        col -= 1
 
    print(f"#{t+1}", row)