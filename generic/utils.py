from django.utils.text import slugify

alphabet = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "e",
    "ё": "yo",
    "ж": "zh",
    "з": "z",
    "и": "i",
    "й": "j",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "kh",
    "ц": "ts",
    "ч": "ch",
    "ш": "sh",
    "щ": "shch",
    "ы": "i",
    "э": "e",
    "ю": "yu",
    "я": "ya",
}


def generate_slug(input_str):
    input_str = slugify(input_str)
    input_str = transliterate(input_str)
    return input_str


def transliterate(input_str):
    input_str = "".join(alphabet.get(w, w) for w in input_str.lower())
    return input_str
