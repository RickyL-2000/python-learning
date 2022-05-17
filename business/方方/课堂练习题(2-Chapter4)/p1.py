while True:
    string = input("Please enter a line:").strip()
    if string == "":
        break
    cnt = {"letter": 0, "digit": 0, "blank": 0, "other": 0}
    for c in string:
        if c.isalpha():
            cnt["letter"] += 1
        elif c.isdigit():
            cnt["digit"] += 1
        elif c == " ":
            cnt["blank"] += 1
        else:
            cnt["other"] += 1
    for key in cnt:
        print(f"{key}: {cnt[key]}")
