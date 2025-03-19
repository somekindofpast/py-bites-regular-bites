from collections import Counter

def calculate_gc_content(sequence: str) -> float:
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    counter = Counter()
    for base in sequence:
        if base.upper() in "ACGT":
            counter[base.upper()] += 1.0
    return round(float(counter['G'] + counter['C']) / float(counter['A'] + counter['C'] + counter['G'] + counter['T']) * 100.0, 2)


if __name__ == '__main__':
    dna1 = """tagtgaaagatattcatttcgaaggccttcagcgtgtcgccgttggtgcggccctcctca"
            "gtatgccggtgcgcacaggcgacacggttaatgatgaagatatcagtaataccattcgcg"
            "ctctgtttgctaccggcaactttgaggatgttcgcgtccttcgtgatggtgatacccttc"
            "tggttcaggtaaaagaacgtccgaccattgccagcattactttctccggtaacaaatcgg"
            "tgaaagatgacatgctgaagcaaaacctcgaggcttctggtgtgcgtgtgggcgaatccc"
            "tcgatcgcaccaccattgccgatatcgagaaaggtctggaagacttctactacagcgtcg"
            "gtaaatatagcgccagcgtaaaagctgtcgtgaccccgctgccgcgcaaccgtgttgacc"
            "taaaactggtgttccaggaaggtgtgtcagctgaaatccagcaaattaacattgttggta"
            "accatgctttcaccaccgacgaactgatctctcatttccaactgcgtgacgaagtgccgt"
            "ggtggaacgtggtaggcgatcgtaaataccagaaacagaaactggcgggcgaccttgaaa"
            "ccctgcgcagctactatctggatcgcggttatgcccgtttcaacatcgactctacccagg"
            "tcagtctgacgccagataaaaaaggtatttacgtcacggtgaacatcaccgaaggcgatc"
            "agtacaagctttctggcgttgaagtgagcggcaaccttgccgggcactccgctgaaattg"
            "agcagctgactaagatcgagccgggtgagctgtataacggcaccaaagtgaccaagatgg"
            "aagatgacatcaaaaagcttctcggtcgctatggttatgcctatccgcgcgtacagtcga"
            "tgcccgaaattaacgatgccgacaaaaccgttaaattacgtgtgaacgttgatgcgggta"
            "accgtttctacgtgcgtaagatccgttttgaaggtaacgatacctcgaaagatgccgtcc"
            "tgcgtcgcgaaatgcgtcagatggaaggtgcatggctggggagcgatctggtcgatcagg"
            "gtaaggagcgtctgaatcgtctgggcttctttgaaactgtcgataccgatacccaacgtg"
            "ttccgggtagcccggaccaggttgatgtcgtctacaaggtaaaagagcgcaacaccggta"
            "gcttcaactttggtattggttacggtactgaaagtggcgtgagcttccaggctggtgtgc"""
    print(calculate_gc_content(dna1))