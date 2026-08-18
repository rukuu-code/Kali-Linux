import argparse
import re

def check_password_strength(password):
    """Evaluate password strength based on criteria."""
    # Initialize score and feedback list
    score = 0
    feedback = []

#Length requirement (>8 chars)
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password must be at least 8 characters long.")

#Uppercase letter requirement
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")

#Lowercase letter requirement
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")

#Digit requirement
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Include at least one digit.")

#Special character requirement
    if re.search(r'[!@#$%^&(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^& etc.).")

#Return score and feedback
    return score, feedback

def main():
    parser = argparse.ArgumentParser(description="Password Strength Auditor")
    parser.add_argument("password", help="Password to audit")
    args = parser.parse_args()

    score, feedback = check_password_strength(args.password)

    print(f"Password Strength Score: {score}/5")
    if score < 5:
        print("\nFeedback:")
        for item in feedback:
            print(f"- {item}")

if __name__ == "__main__":
    main()