'''
 .....*
.....***
....*****
...*******
..*********
.***********
'''

num=int(input("enter num"))
for i in range(1,num):
    for j in range(num-i):
        print(".",end="")
    print("*"*i,end="")
    print("*"*(i-1),end="")
    print()