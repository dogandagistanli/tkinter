n = int(input('Enter a number: '))


for i in range(n):
    if(i==0 or i==n-1):
        for j in range(n):
            print('*',end='')
        print(" ")
    else:
        for k in range(0,1):
            print('*',end="")
        for c in range(0,n-2):
            print(" ",end="")   
        print('*',end="")       
        print(" ")  