text = input("Enter a sentence: ")

# Convert to lowercase and remove punctuation
text = text.lower()
for ch in ".,!?;:":
    text = text.replace(ch, "")

words = text.split()

print("Total words:", len(words))

print("Palindrome words:")
for word in words:
    if word == word[::-1] and len(word) > 1:
        print(word)

print("\nWord Frequency:")
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

for word, count in frequency.items():
    print(word, ":", count)