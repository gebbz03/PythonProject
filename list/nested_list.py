#Nested List

matrix=[[1,2,3,4,5],
        [4,5,6,7,8],
        [1,1,1,1,1],
        [0,0,0,0,0]
        ]

for x in matrix:
    for y in x:
        print(y,end=' ')
    print()            