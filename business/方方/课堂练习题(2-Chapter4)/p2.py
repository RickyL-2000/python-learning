while True:
    string = input("Please enter a letter string:").strip()
    if not string.isalpha():
        print("Invalid input! Please input again.")
        continue
    if string[0] in "aeiou":
        string = string + "ay"
    else:
        string = string[1:] + string[0] + "ay"
    print("Result:", string)
    break
