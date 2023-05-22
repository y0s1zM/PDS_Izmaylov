words = ["apple", "banana", "orange", "kiwi", "grape", "melon", "pear"]

filtered_words = [word for word in words if len(word) <= 5 and word[0].lower() in "aeiou"]

print(filtered_words)
