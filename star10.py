'''
.*************
..***********
...*********
....*******
.....*****
......***
.......*
'''

num=int(input("enter num"))
for i in range(num,0,-1):
    for j in range(0,num-i+1):
        print(".",end="")
    print("*"*i,end="")
    print("*"*(i-1),end="")
    print()