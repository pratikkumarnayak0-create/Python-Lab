m=int(input("Enter the m value of the list: "))
n=int(input("Enter the n value of the list: "))
natural_number=[]
 
for x in range(m,n):
    natural_number.append(x)

result=[]
largest= natural_number[0]
small=natural_number[0]
sum=0
average=0

for x in natural_number:
    sum+= x
    if x>largest:
        largest=x
    if x<small:
        small=x
print(f"the sum of the list is {sum}:  , and the average of the list is {sum/len(natural_number)}: ")
print(f"the largest value is {largest}: ,and the smallest value is {small}: ")
