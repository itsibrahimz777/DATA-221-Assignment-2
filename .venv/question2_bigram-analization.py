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


bigrams = []
for i in range(len(cleaned_tokens) - 1):
    bigram = (cleaned_tokens[i], cleaned_tokens[i + 1])
    bigrams.append(bigram)


bigram_counts = {}

for bg in bigrams:
    if bg in bigram_counts:
        bigram_counts[bg] += 1
    else:
        bigram_counts[bg] = 1


sorted_bigrams = sorted(bigram_counts.items(), key=lambda x: x[1], reverse=True)


for (word1, word2), count in sorted_bigrams[:5]:
    print(f"{word1} {word2} -> {count}")
