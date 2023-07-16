message = input (">")
#goes through the string and any time it finds the passed char it uses it as a boundrary to seperate the string into multiple words, then it will return a list
def emojiConverter (message):
    split_words = message.split (" ")
    output = ""
    emojis = {
        ":)": "😹",
        ":(": "😢",
        "0_0": "😳"
    }
    for word in split_words:
        output += emojis.get (word, word) + " " #if it isn't mapped just return the word
    return output


print (emojiConverter(message))