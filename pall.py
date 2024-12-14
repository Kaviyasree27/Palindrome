def is_palindrome(string):
   
    word = []
    for i in string:
        if i.isalnum():  # Keep only alphanumeric m
            word.append(i.lower())  # Convert to lowercase and add to the list

    # Check if the cleaned list reads the same backward
    return word == word[::-1]

user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
