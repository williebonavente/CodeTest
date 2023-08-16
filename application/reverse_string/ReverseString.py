def reverse_string(string):
    return string[::-1]

def is_palindrome(string):
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    reversed_string = reverse_string(cleaned_string)
    return cleaned_string == reversed_string

def check_password_strength(password):
    if len(password) < 6:
        return "Weak: Password is too short."
    elif is_palindrome(password):
        return "Weak: Avoid using palindromic passwords."
    else:
        return "Strong: Password meets security criteria."

# Example usage for palindrome check
input_string = "A man, a plan, a canal, Panama!" # user-defined instead
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")

def main():
    
    # Example usage for password strength check
    password = "radar"
    strength = check_password_strength(password)
    print(strength)

if __name__ == "__main__":
    main()