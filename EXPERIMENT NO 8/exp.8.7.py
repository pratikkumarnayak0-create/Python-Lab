def count_vowel(ch):
    count=0
    for i in ch:
        if i in "A,E,I,O,U,a,e,i,o,u":
            count+=1
            return count
ch=input("enter a string:")
vowel=count_vowel(ch)
if vowel>0:
      print("number of vowel is:",vowel)
else:
        print("not a avalable")