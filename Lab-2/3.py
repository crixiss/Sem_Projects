sentence = input("Enter a sentence: ")
words = sentence.split()
unique_words = []
count = []
for word in words:
    if word not in unique_words:
        unique_words.append(word)
        count.append(1)
    else:
        index = unique_words.index(word)
        count[index] += 1
for i in range(len(unique_words)):
    print(f"{unique_words[i]}: {count[i]}")