import re


def is_valid_password(password):

    if len(password) < 6:
        return False, "Пароль має бути не менше 6 символів"
    
    if len(password) > 16:
        return False, "Пароль має бути меншим за 16 символів"
    
    if not re.search(r"\d", password):
        return False, "Пароль повинен містити хоча б одну цифру"
    
    if not re.search(r"[A-Z]", password):
        return False, "Пароль повинен містити хоча б одну велику літеру"
    
    if not re.search(r"[a-z]", password):
        return False, "Пароль повинен містити хоча б одну малу літеру"
    
    if not re.search(r"[@#$]", password):
        return False, "Пароль повинен містити хоча б один спеціальний символ (@,#,$)"
    
    return True, "пароль допустимо"

def main():
    password = input("введіть пароль: ")
    is_valid, message = is_valid_password(password)
    if is_valid:
        print("пароль допустимо")
    else:
        print("пароль неприпустимо ")

if __name__ == "__main__":
    main()
