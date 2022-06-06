def func(n1,op,n2):
    if op == "+" :
        print(n1+n2)
    elif op == "-":
        print(n1-n2)
    elif op == "/":
        print(n1/n2)
    elif op == ".":
        print(n1*n2)

n1 = input("Enter 1st no. >> ")
n2 = input("Enter 2nd no. >> ")
op = input("Enter operator in string form >> ")
result = func(n1,op,n2)
print(result)



