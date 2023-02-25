def preorder(root):
    global ans
    if root:
        preorder(c1[root])
        preorder(c2[root])
        ans += 1

T = int(input()) 
for tc in range(1, T+1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 0

    c1 = [0]*(E+2)
    c2 = [0]*(E+2)
    for i in range(E):
        p = lst[2*i]
        c = lst[2*i+1]
        if c1[p] == 0:
            c1[p] = c
        else:
            c2[p] = c

    preorder(N)
    print(f'#{tc} {ans}')