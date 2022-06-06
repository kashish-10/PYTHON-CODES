def function(arr,command):
    if command == "asc":
        arr.sort()
    elif command == "desc":
        arr.sort(reverse = True)
    elif command == "none":
        pass
    print(arr)

        
arr=[]
for i in range(0,5):
    arr.append(int(input()))
y=input("enter the sorting parameter(asc/desc/none): ")
function(arr,y)
