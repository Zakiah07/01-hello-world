message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😊",
    ":(": "☹"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)

#if we type Good Morning Sunshine, we get a list of 3 items, each one is string

