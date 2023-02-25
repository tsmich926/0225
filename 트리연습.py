def preorder(root):
        if root:
            preorder(leftc[root])
            preorder(rightc[root])
            print(root)

N = 13
s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
lst = list(map(int,s.split()))

leftc=[0]*(N+1)
rightc=[0]*(N+1)

for idx in range(0,len(lst),2):
    p = lst[idx]
    c = lst[idx+1]

    if leftc[p] == 0: #비었다
        leftc[p] = c
    else:
        rightc[p] = c
# print(leftc)
# print(rightc)
preorder(1)
