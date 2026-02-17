import string

with open("sample-file.txt", "r") as file:
    text = file.read()


tokens = text.split()

cleaned_tokens = []

for token in tokens:

    token = token.lower()


    token = token.strip(string.punctuation)


    alpha_count = sum(1 for c in token if c.isalpha())
    if alpha_count >= 2:
        cleaned_tokens.append(token)


word_counts = {}

for word in cleaned_tokens:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1


sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)


for word, count in sorted_words[:10]:
    print(f"{word} -> {count}")
