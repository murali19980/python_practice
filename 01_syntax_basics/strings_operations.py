"""
Practice: String Operations
"""
def reverse_string(s: str) -> str:
    return s[::-1]

def is_palindrome(s: str) -> bool:
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def count_vowels(s: str) -> int:
    vowels = "aeiou"
    return sum(1 for ch in s.lower() if ch in vowels)

def capitalize_words(s: str) -> str:
    return " ".join(word.capitalize() for word in s.split())

def are_anagrams(s1: str, s2: str) -> bool:
    return sorted(s1.lower().replace(" ", "")) == sorted(s2.lower().replace(" ", ""))

if __name__ == "__main__":
    text = "Hello World"
    print(f"Reverse of '{text}': {reverse_string(text)}")
    print(f"Is 'Madam' palindrome? {is_palindrome('Madam')}")
    print(f"Vowels in '{text}': {count_vowels(text)}")
    print(f"Capitalized: {capitalize_words('hello world from python')}")
    print(f"Are 'listen' and 'silent' anagrams? {are_anagrams('listen', 'silent')}")
