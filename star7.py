'''
1
21
321
4321
'''  
num=int(input("enter num"))
for i in range(1,num):
    for j in range(i,0,-1):
        print(j,end="")
    print()