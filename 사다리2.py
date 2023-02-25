T = 10
for test_case in range(1, 2):
    _ = int(input())
    arr = [ list(map(int, input().split())) for _ in range(100)]

    #2의 좌표찾기
    for i in range(99):
        if arr[99][i] == 2:
            col = i
            
    row = 99
    
    while col != 0:     
    
        if row-1 >= 0 and arr[col][row-1] == 1:
            while row-1 >= 0 and arr[col][row-1] == 1:   
                row -= 1
 
         
        elif row+1 < 100 and arr[col][row+1] == 1:
            while row+1 < 100 and arr[col][row+1] == 1:   
                row += 1
 
         
        col -= 1
 
    print(f"#{t+1}", row)