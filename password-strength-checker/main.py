import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[ @!#$%^&*()<>?/\|}{~:]", password) is None

    errors = {
        "Too short (min 8 characters)": length_error,
        "Missing a digit": digit_error,
        "Missing an uppercase letter": uppercase_error,
        "Missing a lowercase letter": lowercase_error,
        "Missing a special symbol": symbol_error
    }

    if any(errors.values()):
        print("\n❌ Weak password. Issues:")
        for issue, has_error in errors.items():
            if has_error:
                print(f"  - {issue}")
    else:
        print("\n✅ Strong password!")

if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    check_password_strength(pwd)
