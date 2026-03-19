text = "Pratik is a Good boy "

words = text.split()

word_count = len(words)
print("Total number of words:", word_count)

print("\nPalindrome words:")
for word in words:
    w = word.lower()
    if w == w[::-1] and len(w) > 1:
        print(word)

print("\nEach word in reverse order:")
for word in words:
    print(word[::-1], end=" ")
