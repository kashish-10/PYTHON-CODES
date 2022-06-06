import random
arr=[]
n=int(input("Enter the length of array: "))
for i in range(0,n):
    arr.append(random.randint(1,99))
    
print(n)
count=0
max=0
ele=0
count=0
for i in range(0,n):
    for j in range(0,n):
        if(arr[i]==arr[j]):
            count+=1
    if(count>max):
        max=count
        ele=n[i]
print("Highest frequency element is ",ele)
