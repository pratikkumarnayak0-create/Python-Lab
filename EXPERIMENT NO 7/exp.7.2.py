m = int(input("Enter starting number: "))
n = int(input("Enter ending number: "))

print("Prime numbers between", m, "and", n, "are:")

for num in range(m, n + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
