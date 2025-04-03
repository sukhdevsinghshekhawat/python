'''
       *
      **
     ***
    ****
   *****
'''
num=int(input("enter num:="))

# for i in range(1,num):
#     for j in range(num-i,1,-1):
#         print(" ",end="")
#     for j in range(i):
#         print("*",end="")
#     print()

for i in range(1,num):
     for j in range(num-i,1,-1):
          print("-",end="")
     print("*"*i,end="") 
     print()
