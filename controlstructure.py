#sequential control structure it executes line by line
#selection control structure it executes only one block of code among many
#iterative control structure it executes a block of code repeatedly
n=int(input("enter a number"))
if n<=5:
    print("num is less than or equal to 5")
else:
    print("num is greater than 5")
#now elif statements 
i=int(input("enter a number"))
if i<35:
    print("fail")
elif i<60 and i>=35:
    print("c grade")
elif i<80 and i>=60:
    print("b grade")
else:
    print("a grade")
#iterative control structure
n=int(input())
for i in range(1,11):
    print(f"{n}X{i}={n*i}")