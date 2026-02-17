import string

# dictionary to store normalized line -> list of (line_number, original_line)
groups = {}

with open("sample-file.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):
        original_line = line.rstrip("\n")

        # normalize: lowercase + remove whitespace + remove punctuation
        normalized = original_line.lower()
        normalized = "".join(
            ch for ch in normalized
            if ch not in string.whitespace and ch not in string.punctuation
        )

        # group lines by normalized form
        if normalized in groups:
            groups[normalized].append((line_number, original_line))
        else:
            groups[normalized] = [(line_number, original_line)]

# keep only sets with more than one line (actual duplicates)
duplicate_sets = [group for group in groups.values() if len(group) > 1]

# print number of sets
print("Number of near-duplicate sets:", len(duplicate_sets))

# print first two sets
for i, group in enumerate(duplicate_sets[:2], start=1):
    print(f"\nSet {i}:")
    for line_number, text in group:
        print(f"{line_number}: {text}")
