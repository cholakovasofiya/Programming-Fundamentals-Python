def password_check_digits(password):
    counter_digits = 0
    for i in password_input:
        if i.isnumeric():
            counter_digits += 1
    if counter_digits < 2:
        messages_output.append("Password must have at least 2 digits")
        return False
    else:
        return True


def password_check_length(password):
    if not 6 <= len(password) <= 10:
        messages_output.append("Password must be between 6 and 10 characters")
        return False
    else:
        return True


def password_check_isalnum(password):
    if not password.isalnum():
        messages_output.append("Password must consist only of letters and digits")
        return False
    else:
        return True


password_input = input()
messages_output = []
is_password_ok = password_check_isalnum(password_input)
is_password_ok = password_check_length(password_input)
is_password_ok = password_check_digits(password_input)

if is_password_ok:
    print("Password is valid")

else:
    print("\n" .join(messages_output))
