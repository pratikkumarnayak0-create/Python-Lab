def largest(a,b,c):
    if a>b and a>c:
        return "a is largest"
    elif b>a and b>c:
        return "b is largest"
    else:
        return "c is largest"
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
print("largest value is:",largest(a,b,c))