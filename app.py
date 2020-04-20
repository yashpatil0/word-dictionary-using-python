import json

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()

    if word in data:
        return data[word]
    else:
        return "word doesn't exist."

word = input("enter any word: ")
print(".................")
print("")
print(translate(word))
print("")
print(".................")

