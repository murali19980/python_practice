"""
Practice: Regular Expressions
"""
import re

def extract_emails(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)

def validate_phone(phone):
    pattern = r'^(\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4})$'
    return bool(re.match(pattern, phone))

def replace_digits(text):
    return re.sub(r'\d', '#', text)

if __name__ == "__main__":
    text = "Contact me at test@example.com or john.doe@company.org"
    print("Emails:", extract_emails(text))
    print("Validate (123-456-7890):", validate_phone("123-456-7890"))
    print("Validate ((123) 456-7890):", validate_phone("(123) 456-7890"))
    print("Replace digits in 'abc123def456':", replace_digits("abc123def456"))
