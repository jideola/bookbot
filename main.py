with open("../../../frankenstein.txt") as f:
    file = f.read()
word = file.split()
alphabets = {}
def count_letters(word):
    for word in word:
        for alphabet in word:
            alphabet = alphabet.lower()
            # if alphabet not in ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "\"", "|", "?", ">", "<", "/", ".", ",", ":", ";", "'", "[", "]", "{", "}"]:
            if alphabet not in alphabets:
                alphabets[alphabet] = 1
            else:
                alphabets[alphabet] +=1

count_letters(word)
for key in alphabets:
    value = alphabets[key]
    print(f"The '{key}' character was found {value} times")
print("--- End report ---")