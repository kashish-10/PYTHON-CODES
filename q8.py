string = input("Enter any string>>> ")
n=0
for i in string:
    if(i.isdigit()):
        n=n + int(i)
print(n)
