'''
      1
    1 1
  1 1 1
1 1 1 1
    '''

num=int(input("enter num"))
for i in range(1,num):
    for j in range(num-i):
        print(" ",end="")
    print("1"*i,end="")
    print()