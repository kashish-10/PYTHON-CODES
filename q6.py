n1 = int(input("Enter the lower limit >>> "))
n2 = int(input("Enter the upper limit >>> "))

for x in range(n1,n2+1):
    if x>1:
        for i in range(2,x):
            if (x%i==0):
                break
        else:
            print(x)
        
