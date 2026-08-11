def caesar(text, shift, choice):
    result = ""

    if choice == "d":
        shift = -shift

    for ch in text:
        if ch.isalpha():
            if ch.islower():
                result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += ch

    return result


text = input("Enter text: ")
shift = int(input("Enter shift value: "))
choice = input("Encrypt or Decrypt (e/d): ")

print("Result:", caesar(text, shift, choice))