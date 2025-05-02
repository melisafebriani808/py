message = input(">")
words = message.split(' ')
emojis = {
    ":)": "🙂",
    ":(": "🙁",
    ":D": "😄",
    "._.": "😶",
    "T_T": "😭",
    "^_^": "😊",
    "-_-": "😑",
    "o_O": "😳"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)