import sys

INTERNAL_LINKS = ('pybit.es', 'codechalleng.es')


def make_html_links():
    for line in sys.stdin:
        line = str(line.decode('ASCII'))
        parts = line.split(',')
        if len(parts) != 2:
            continue
        link_href = parts[0].strip()
        if not link_href.startswith("https://"):
            continue
        link_name = parts[1].strip()

        target_blank = ' target="_blank"'
        for internal_link in INTERNAL_LINKS:
            if internal_link in link_href:
                target_blank = ""
                break
        print(f'<a href="{link_href}"{target_blank}>{link_name}</a>'.encode('ASCII'))