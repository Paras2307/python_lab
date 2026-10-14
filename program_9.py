word1 = input("Enter first word: ").lower()
word2 = input("Enter second word: ").lower()

# Remove spaces
word1 = word1.replace(" ", "")
word2 = word2.replace(" ", "")

# Check anagram
if sorted(word1) == sorted(word2):
    print("Words are Anagrams")
else:
    print("Words are not Anagrams")

# Dictionary character counting
count = {}
for ch in word1:
    count[ch] = count.get(ch, 0) + 1

print("Character Count:", count)

# Tuple key
key = tuple(sorted(word1))
print("Tuple Key:", key)