def extract_vowels(sentence):
    vowels = "aeiouAEIOU"
    return set([char for char in sentence if char in vowels])

print(extract_vowels("This is a sentence."))
