'''
1
12
123
1234
'''
num=int(input("enter num"))
for i in range(num):
    for j in range(i):
        print(j,end="")
    print()
