# Create emoji converter using dictionary



user_input = input("What's up? ")

# Convert program to reusable function
def emoji_converter(input):
    emoji_dictionary = {
        ":)": "😊",
        ":(": "☹",
        ";)": "😉",
        ":@": "🤬",
        ":D": "😁",
        "8)": "🤓"
    }

    for emoji in emoji_dictionary:
        if emoji in input:
            return input.replace(emoji, emoji_dictionary[emoji])


print(emoji_converter(user_input))