def find_lines_containing(filename, keyword):
    """
    Returns a list of (line_number, line_text) for lines that contain
    keyword (case-insensitive). Line numbers start at 1.
    """
    matches = []

    with open(filename, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if keyword.lower() in line.lower():
                matches.append((line_number, line.rstrip("\n")))

    return matches
