def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)" : "😀",
        ":(" : "😔"
    }

    output = ""

    for word in words:
        output += emojis.get(word, word) + " "
    
    return output

def intro():
    # functions are used to store programming code into chunks for better organization
    pass

def main():
    message = input("> ")
    print(emoji_converter(message=message))

if __name__ == '__main__':
    main()