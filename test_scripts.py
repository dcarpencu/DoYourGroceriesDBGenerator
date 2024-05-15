import re


def parse_string(input_string, blacklist):
    # Tokenize the input string
    words = re.findall(r'\b[\w.]+\b', input_string)

    # print(words)

    # Filter out unwanted words
    filtered_words = [word for word in words if
                      len(word) > 2 and word not in blacklist and not any(char.isdigit() for char in word) and not any(char == '.' for char in word)]

    # print(filtered_words)

    # # Remove words that end in '.' (period) from the filtered list
    # filtered_words = [word for word in filtered_words if not word.endswith('.')]

    # Join the remaining words into a list of strings
    tags = filtered_words

    return tags


# Test the function
blacklist = [
    'g', 'de', 'din', '+/-', 'la', 'un', 'kg', 'G', '%', 'cu', ',', 'l', 'punga', 'to',
    'auchan', 'cuburi', 'ready', 'eat', 'fresh', 'pe', 'bucata', 'pret', 'bucati',
    'netratate', 'dupa', 'recoltare', 'dupa', 'si', 'eco', 'red', 'delicious', 'golden',
    'idared', 'jonaprince', 'caserola', 'plasa', 'agriro', 'drink', 'grasime', 'ml', 'gr',
    'vrac', 'buc', 'pls', 'ptr', 'fiert', 'nrg', 'x', 'dz', 'pet', 'trk', 't', 'mg',
    'doza', 'nrgb', 'per',
]

input_strings = [
    'Beck S 5% Ep.11,2 0,75L St',
    'Becks Bere 5%  Ep. 11,2 St.Neret 0,33L'
]

for input_string in input_strings:
    tags = parse_string(input_string, blacklist)
    print(tags)
