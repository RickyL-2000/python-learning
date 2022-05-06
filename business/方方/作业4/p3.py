def varify(email):
    email = email.lower()
    for c in email:
        if c.isalnum() or c in "_-.@":
            continue
        else:
            return False
    if email.count("@") == 1:
        if email[0] == "@" or email[-1] == "@":
            return False
    else:
        return False
    at_idx = email.find("@")
    if email[at_idx:].count(".") >= 1:
        if email[at_idx+1] == "." or email[-1] == ".":
            return False
    else:
        return False
    return True

email = input("请输入邮箱地址: ")
valid = varify(email)
print(f"{email} 为有效电子邮件吗？{valid}")
