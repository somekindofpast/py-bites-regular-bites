def filter_accents(text: str):
    """Return a sequence of accented characters found in
       the passed in lowercased text string
    """
    return [c.lower() for c in text if not ord(c) < 128]


if __name__ == '__main__':
    texts = (
        ("Denominada en Euskera como Donostia, está "
         "situada en el Golfo de Vizcaya en la provincia "
         "de Guipúzcoa. San Sebastián no es solo conocida "
         "por su afamado festival de cine, sino también "
         "por la belleza de sus calles, las cuales tienen "
         "un corte francés y aburguesado que atraen cada "
         "año a centenares de turistas."),
        ("La capital de Cataluña, es la ciudad más visitada "
         "de España y la segunda más poblada. Barcelona es "
         "también una de las ciudades europeas más "
         "cosmopolitas y todo un símbolo cultural, "
         "financiero, comercial y turístico. Para muchos "
         "Barcelona es la ciudad más atractiva de España y "
         "una de las más bonitas."),
        ("Sevilla es la capital de Andalucía, y para muchos, "
         "la ciudad más bonita de España. Pasear por sus calles, "
         "contemplar la Giralda, la Catedral o la Torre del Oro "
         "es una auténtica gozada. En primavera el olor a azahar "
         "lo envuelve todo. Al igual que Granada, toda la ciudad "
         "es una auténtica delicia. Su clima hace propensa la "
         "visita en casi cualquier época del año."),
        ("The 5 French accents;"
         "The cédille (cedilla) Ç ..."
         "The accent aigu (acute accent) é ..."
         "The accent circonflexe (circumflex) â, ê, î, ô, û ..."
         "The accent grave (grave accent) à, è, ù ..."
         "The accent tréma (dieresis/umlaut) ë, ï, ü"),
    )
    print(filter_accents(texts[0]))
    print(filter_accents(texts[1]))
    print(filter_accents(texts[2]))
    print(filter_accents(texts[3]))