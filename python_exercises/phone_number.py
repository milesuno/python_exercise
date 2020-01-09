# Convert numbers into words

phone_number = input("Enter Phone #: ")

num_to_words_list = ""

# Dictionaries (Objs) can be used or looking up collected data vlookup style.
number_book = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

for num in phone_number:
    if number_book[num]:
        num_to_words_list += f"{number_book[num]} "
    else:
        print("Please enter a # between 0-9")
print(num_to_words_list)




