"""
Practice: Useful One-Liners
"""
def flatten(lst):
    return [item for sublist in lst for item in sublist]

def is_anagram(s1, s2):
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())

def chunk_list(lst, size):
    return [lst[i:i+size] for i in range(0, len(lst), size)]

def most_frequent(lst):
    return max(set(lst), key=lst.count)

if __name__ == "__main__":
    print("Flatten [[1,2],[3,4]]:", flatten([[1,2],[3,4]]))
    print("Anagram 'listen' 'silent':", is_anagram("listen", "silent"))
    print("Chunk [1,2,3,4,5] size 2:", chunk_list([1,2,3,4,5], 2))
    print("Most frequent in [1,2,2,3,3,3]:", most_frequent([1,2,2,3,3,3]))
