import re
from getpass import getpass

# Load dictionary words (optional)
def load_dictionary(file_path):
    try:
        with open(file_path, "r") as f:
            return set(line.strip().lower() for line in f)
    except FileNotFoundError:
        return set()

# Evaluate password strength
def evaluate_password(password, dictionary_words):
    feedback = []
    strength = 0

    # Check length
    if len(password) >= 12:
        strength += 1
    else:
        feedback.append("Increase the length to at least 12 characters.")

    # Check complexity
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Include at least one uppercase letter.")
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Include at least one lowercase letter.")
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Include at least one digit.")
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Include at least one special character.")

    # Check dictionary words
    if dictionary_words and any(word in password.lower() for word in dictionary_words):
        feedback.append("Avoid using dictionary words or common patterns.")

    # Provide overall assessment
    if strength >= 4:
        return "Strong: Your password is secure!", feedback
    elif 2 <= strength < 4:
        return "Moderate: Improve the following aspects for a stronger password:", feedback
    else:
        return "Weak: Your password is not secure!", feedback

if __name__ == "__main__":
    dictionary_path = "example_dictionary.txt"
    dictionary_words = load_dictionary(dictionary_path)

    print("Welcome to the Password Strength Checker!")
    password = getpass("Enter a password to evaluate: ")

    strength, feedback = evaluate_password(password, dictionary_words)
    print("\nStrength: ", strength)
    if feedback:
        print("Suggestions:")
        for suggestion in feedback:
            print(f"- {suggestion}")
