import re

allwords = open(r"C:\Users\Ollie\.vscode\Projects\hangmansolver 2.0\allwords.txt", "r").read().splitlines() 

unknown = input('enter the word with "_" for each unknown: ')
unknown = [char.lower() for char in unknown]
wordlength = len(unknown)

shortlist = []
for word in allwords:  #removes words that do not have the same length as the partially known word
    if len(word) == wordlength:
        shortlist.append(word)

allwords = shortlist

for letterIndex in range(len(unknown)):
    letter = unknown[letterIndex]

    shortlist = []

    if letter == "_":
        pass
    else:
        for word in allwords:
            if word[letterIndex] == letter:
                shortlist.append(word)

        allwords = shortlist

print( allwords)
print("\n","total results: ", len(allwords))

## this finds the most common letter in the remaining words

letters = {
    'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0,'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0,'w':0, 'x':0, 'y':0, 'z':0
          }

for word in allwords:
    for letter in word:
        if re.search("[a-zA-Z]", letter):
            letters[letter] += 1

for key, value in letters.items():
    if value == max(letters.values()):
        print("recomended next guess:", key)
