from urllib.parse import urlparse
from django.template.defaultfilters import slugify as django_slugify

   
alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
'я': 'ya'}

def transliterate(input_str):
    url_without_whitespaces_begin_end = remove_whitespaces_begin_end(input_str)
    url_without_whitespaces =  replace_whitespaces_with_underscores(url_without_whitespaces_begin_end)
    quated_url = django_slugify(''.join(alphabet.get(w, w) for w in s.lower()))
    input_str = urlparse(quated_url).geturl()
    return input_str

def remove_whitespaces_begin_end(url : str) -> str:
    return url.strip()

def replace_whitespaces_with_underscores(url : str) ->str:
    return url.replace(' ', '_')
