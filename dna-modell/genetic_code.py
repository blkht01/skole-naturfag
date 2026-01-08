# genetic_code.py

GENETIC_CODE = {
    # Fenylalanin
    "UUU": "Fenylalanin", "UUC": "Fenylalanin",
    # Leucin
    "UUA": "Leucin", "UUG": "Leucin",
    "CUU": "Leucin", "CUC": "Leucin", "CUA": "Leucin", "CUG": "Leucin",
    # Isoleucin
    "AUU": "Isoleucin", "AUC": "Isoleucin", "AUA": "Isoleucin",
    # Metionin (Og START!)
    "AUG": "Metionin",
    # Valin
    "GUU": "Valin", "GUC": "Valin", "GUA": "Valin", "GUG": "Valin",
    # Serin
    "UCU": "Serin", "UCC": "Serin", "UCA": "Serin", "UCG": "Serin",
    "AGU": "Serin", "AGC": "Serin",
    # Prolin
    "CCU": "Prolin", "CCC": "Prolin", "CCA": "Prolin", "CCG": "Prolin",
    # Treonin
    "ACU": "Treonin", "ACC": "Treonin", "ACA": "Treonin", "ACG": "Treonin",
    # Alanin
    "GCU": "Alanin", "GCC": "Alanin", "GCA": "Alanin", "GCG": "Alanin",
    # Tyrosin
    "UAU": "Tyrosin", "UAC": "Tyrosin",
    # Histidin
    "CAU": "Histidin", "CAC": "Histidin",
    # Glutamin
    "CAA": "Glutamin", "CAG": "Glutamin",
    # Aspargin
    "AAU": "Asparagin", "AAC": "Asparagin",
    # Lysin
    "AAA": "Lysin", "AAG": "Lysin",
    # Asparginsyre
    "GAU": "Asparaginsyre", "GAC": "Asparaginsyre",
    #Glutaminsyre
    "GAA": "Glutaminsyre", "GAG": "Glutaminsyre",
    # Cystein
    "UGU": "Cystein", "UGC": "Cystein",
    # Tryptofan
    "UGG": "Tryptofan",
    # Arginin
    "CGU": "Arginin", "CGC": "Arginin", "CGA": "Arginin", "CGG": "Arginin",
    "AGA": "Arginin", "AGG": "Arginin",
    # Glysin
    "GGU": "Glysin", "GGC": "Glysin", "GGA": "Glysin", "GGG": "Glysin",
}

STOP_CODONS = {"UAA", "UAG", "UGA"}
