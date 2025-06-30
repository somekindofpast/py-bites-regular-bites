import os
from pathlib import Path
from typing import List
import unicodedata
from urllib.request import urlretrieve


def _get_spanish_dictionary_words() -> List[str]:
    filename = "spanish.txt"
    # source of file
    # https://raw.githubusercontent.com/bitcoin/bips
    # /master/bip-0039/spanish.txt
    url = f"https://bites-data.s3.us-east-2.amazonaws.com/{filename}"
    tmp_folder = os.getenv("TMP", "/tmp")
    local_filepath = Path(tmp_folder) / filename
    if not Path(local_filepath).exists():
        urlretrieve(url, local_filepath)
    return local_filepath.read_text(encoding="utf8").splitlines()


SPANISH_WORDS = _get_spanish_dictionary_words()


def get_accentuated_sentence(
    text: str, words: List[str] = SPANISH_WORDS
) -> str:
    res = ""
    for word in text.split():
        found_word = False
        for i in range(len(words)):
            norm = unicodedata.normalize('NFKD', words[i]).encode('ascii', 'ignore').decode('ascii')
            if word.strip(',') == norm:
                found_word = True
                res += words[i]
                if word[-1] == ',':
                    res += ','
                break

        if not found_word:
            res += word
        res += ' '

    return res.strip()


if __name__ == '__main__':
    print(get_accentuated_sentence("Cuando era pequeno me gustaba jugar en la via"))
    print(get_accentuated_sentence("un dos tres ... accion"))
    print(get_accentuated_sentence("anadir otra aficion"))
    print(get_accentuated_sentence("bajo el arbol descansando vi un avion"))
    print(get_accentuated_sentence("no tomes mucho azucar o hay que evitar la bascula"))
    print(get_accentuated_sentence("vehiculo volando, utopia o realidad pronto ...?"))
    print(get_accentuated_sentence("telefono publico ... apenas ya no se ve en esta epoca"))
    print(get_accentuated_sentence("me falta jamon y jabon"))
    print(get_accentuated_sentence("leyendo un libro en el jardin ... tarde de exito"))
    print(get_accentuated_sentence("sesion de escribir, primera pagina de mi poesia hecha"))