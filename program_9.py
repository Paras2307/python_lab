# Function to clean text
def clean_text(text):
    return text.replace(" ", "").lower()


# Function to check anagrams using sorting
def check_anagram(word1, word2):
    word1 = clean_text(word1)
    word2 = clean_text(word2)

    return sorted(word1) == sorted(word2)


# Function to count character frequency
def count_characters(text):
    text = clean_text(text)
    count = {}

    for ch in text:
        count[ch] = count.get(ch, 0) + 1

    return count


# Function to find anagram groups using tuple keys
def group_anagrams(words):
    groups = {}

    for word in words:
        key = tuple(sorted(clean_text(word)))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return groups


# Main program
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

if check_anagram(word1, word2):
    print("The words are anagrams.")
else:
    print("The words are not anagrams.")

# Character frequency
print("\nCharacter Frequency:")
print(count_characters(word1))

# Group anagrams
words = ["listen", "silent", "hello", "enlist", "below", "elbow"]

print("\nAnagram Groups:")
print(group_anagrams(words))