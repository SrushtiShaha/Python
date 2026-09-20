from typing import List

# Convert string to binary (ASCII-based)
def string_to_binary(s: str) -> str:
    return ''.join(format(ord(c), '08b') for c in s.lower())


# Hamming distance (for equal-length strings)
def hamming_distance(b1: str, b2: str) -> int:
    length = min(len(b1), len(b2))
    return sum(c1 != c2 for c1, c2 in zip(b1[:length], b2[:length])) + abs(len(b1) - len(b2))


# Similarity score (0 to 1)
def similarity_score(b1: str, b2: str) -> float:
    max_len = max(len(b1), len(b2))
    dist = hamming_distance(b1, b2)
    return 1 - dist / max_len


# Fuzzy match function
def fuzzy_match(input_str: str, database: List[str]):
    input_bin = string_to_binary(input_str)

    best_match = None
    best_score = -1

    for city in database:
        city_bin = string_to_binary(city)
        score = similarity_score(input_bin, city_bin)

        if score > best_score:
            best_score = score
            best_match = city

    return best_match, best_score


# Example database of standard city names
city_db = [
    "Mumbai", "Delhi", "Bangalore", "Hyderabad",
    "Chennai", "Kolkata", "Pune", "Ahmedabad"
]

# Test
query = "Mumbay"   # intentionally misspelled

match, score = fuzzy_match(query, city_db)

print(f"Input: {query}")
print(f"Best Match: {match}")
print(f"Similarity Score: {score:.2f}")