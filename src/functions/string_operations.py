def reverse_string(text):
    # Return the text in reverse order.
    pass


def is_palindrome(text):
    # Check if text reads the same backward, ignoring case and spaces.
    # Only letter case and the space character " " are ignored - punctuation still counts.
    pass


def count_vowels(text):
    # Count the vowels in text.
    # Vowels are a, e, i, o, u in either case (not y, not letters with accents).
    pass


def capitalize_words(text):
    # Make the first letter of each word uppercase.
    # Words are separated by spaces. Only the first letter changes - the other letters
    # and the spaces stay as they are ("hELLO  it's" -> "HELLO  It's").
    pass


def count_words(text):
    # Count the words in text.
    # Words are separated by any whitespace (spaces, tabs, new lines).
    pass


def count_character(text, character):
    # Count how many times character appears in text. character is a single character (case-sensitive).
    pass


def truncate(text, max_length, suffix="..."):
    # Shorten text to max_length characters, including suffix: "Hello world", 8 -> "Hello...".
    # Text that already fits is returned unchanged. The result is never longer than max_length:
    # if even the suffix does not fit, return text[:max_length] without a suffix.
    pass


def case_variants(text):
    # Return (text.upper(), text.lower(), text.capitalize()).
    # capitalize() makes only the first character uppercase and the rest lowercase.
    pass


def normalize(text):
    # Return text without leading/trailing whitespace (strip()) and in lowercase.
    # Use lower() (casefold() would also change letters like "ß" into "ss").
    # Strings are immutable: methods return a new string and the original is not changed.
    pass


def replace_word(text, old, new):
    # Return text with every occurrence of old replaced by new (str.replace). old is not empty.
    pass


def find_position(text, sub):
    # Return the index where sub first appears in text, or -1 if it is missing (str.find).
    pass


def split_csv(line):
    # Split line on commas and strip spaces around each part: " a, b ,c" -> ["a", "b", "c"].
    # strip() removes any whitespace around a part, also tabs.
    # Empty fields are kept: "a,,b" -> ["a", "", "b"].
    pass


def join_words(words, separator):
    # Return the words joined with separator (separator.join(words)). Non-string elements raise TypeError.
    pass


def starts_and_ends(text, prefix, suffix):
    # Return (text.startswith(prefix), text.endswith(suffix)).
    pass


def char_at(text, index):
    # Return the character at index (negative indexes count from the end). Out of range raises IndexError.
    pass


def escape_lengths():
    # Return the tuple (len("a\tb"), len("a\nb"), len(r"a\nb"), len("\\")).
    # \t and \n are ONE character each; in a raw string r"..." the backslash is a normal character; "\\" is one backslash.
    pass


def classify_char(char):
    # Return "digit", "letter", "space" or "other" using char.isdigit(), char.isalpha() and char.isspace().
    pass
