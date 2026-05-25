# genetic_code.py

GENETIC_CODE = {
# Fenylalanin
"UUU": "Phe", "UUC": "Phe",

# Leucin
"UUA": "Leu", "UUG": "Leu",
"CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",

# Isoleucin
"AUU": "Ile", "AUC": "Ile", "AUA": "Ile",

# Metionin (START)
"AUG": "Met",

# Valin
"GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",

# Serin
"UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
"AGU": "Ser", "AGC": "Ser",

# Prolin
"CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",

# Treonin
"ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",

# Alanin
"GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",

# Tyrosin
"UAU": "Tyr", "UAC": "Tyr",

# Histidin
"CAU": "His", "CAC": "His",

# Glutamin
"CAA": "Gln", "CAG": "Gln",

# Asparagin
"AAU": "Asn", "AAC": "Asn",

# Lysin
"AAA": "Lys", "AAG": "Lys",

# Asparaginsyre
"GAU": "Asp", "GAC": "Asp",

# Glutaminsyre
"GAA": "Glu", "GAG": "Glu",

# Cystein
"UGU": "Cys", "UGC": "Cys",

# Tryptofan
"UGG": "Trp",

# Arginin
"CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
"AGA": "Arg", "AGG": "Arg",

# Glysin
"GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly",
}

STOP_CODONS = {"UAA", "UAG", "UGA"}
