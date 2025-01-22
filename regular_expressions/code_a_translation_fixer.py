import re
from collections import deque


def fix_translation(org_text, trans_text):
    """Receives original English text as well as text returned by translator.
       Parse trans_text restoring the original (English) code (wrapped inside
       code and pre tags) into it. Return the fixed translation str
    """
    fixed_text = _fix_tag_in_text(org_text, trans_text, "code")
    return _fix_tag_in_text(org_text, fixed_text, "pre")


def _fix_tag_in_text(org_text: str, trans_text: str, tag_name: str) -> str:
    open_tag = "<" + tag_name + ">"
    close_tag = "</" + tag_name + ">"
    pattern = re.compile(open_tag + r".+?" + close_tag, re.DOTALL)
    org_tags = deque(pattern.findall(org_text))
    fixed_text = ""
    for text in trans_text.split(close_tag):
        if open_tag in text:
            text += close_tag
            text = pattern.sub(org_tags.popleft(), text)
        fixed_text += text
    return fixed_text


if __name__ == "__main__":
    bite_15_en = '''<p>Iterate over the given <code>names</code> and <code>countries list</code>s, <strong>printing</strong> them prepending the number of the loop (starting at 1). Here is the output you need to deliver:<pre>
    1. Julian     Australia
    2. Bob        Spain
    3. PyBites    Global
    4. Dante      Argentina
    5. Martin     USA
    6. Rodolfo    Mexico
    </pre></p><p>Notice that the 2nd column should have a fixed width of 11 chars, so between <i>Julian</i> and <i>Australia</i> there are 5 spaces, between <i>Bob</i> and <i>Spain</i>, there are 8. This column should also be aligned to the left.</p><p>Ideally you use only one for loop, but that is not a requirement.</p><p>Good luck and keep calm and code in Python!</p>'''
    bite_15_it = '''<p>Iterare i <code>nomi</code> e le <code>liste dei paesi</code>s indicati, <strong>stampandoli</strong> anteponendo il numero del ciclo (a partire da 1). Ecco l'output che devi consegnare:<pre> 1. Julian Australia 2. Bob Spagna 3. PyBites Global 4. Dante Argentina 5. Martin Stati Uniti d'America 6. Rodolfo Messico </pre></p><p>Si noti che la seconda colonna dovrebbe avere una larghezza fissa di 11 caratteri, quindi tra <i>Julian</i> e <i>Australia</i> ci sono 5 spazi, tra <i>Bob</i> e <i>Spagna</i> , ci sono 8. Questa colonna dovrebbe anche essere allineata a sinistra. </p><p>Idealmente si utilizza solo uno for loop, ma questo non è un requisito. </p><p>Buona fortuna e mantenere la calma e codice in Python! </p>'''
    bite_15_it_fixed = '''<p>Iterare i <code>names</code> e le <code>countries list</code>s indicati, <strong>stampandoli</strong> anteponendo il numero del ciclo (a partire da 1). Ecco l'output che devi consegnare:<pre>
    1. Julian     Australia
    2. Bob        Spain
    3. PyBites    Global
    4. Dante      Argentina
    5. Martin     USA
    6. Rodolfo    Mexico
    </pre></p><p>Si noti che la seconda colonna dovrebbe avere una larghezza fissa di 11 caratteri, quindi tra <i>Julian</i> e <i>Australia</i> ci sono 5 spazi, tra <i>Bob</i> e <i>Spagna</i> , ci sono 8. Questa colonna dovrebbe anche essere allineata a sinistra. </p><p>Idealmente si utilizza solo uno for loop, ma questo non è un requisito. </p><p>Buona fortuna e mantenere la calma e codice in Python! </p>'''

    print(fix_translation(bite_15_en, bite_15_it))
    assert fix_translation(bite_15_en, bite_15_it) == bite_15_it_fixed