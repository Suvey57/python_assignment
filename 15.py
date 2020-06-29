def insert_string_middle(brackets,word):
    length = len(brackets)
    a=int(length/2)
    print(brackets[:a]+word+brackets[a:]

brackets = input("Enter the brackets\n")
word = input("Enter the word\n")
insert_string_middle(brackets,word)
