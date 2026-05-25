KNOWN_PEPTIDES = {
    # --- ikke-ribosomale / lages av enzymer, ikke ribosom. De minste peptidkjedene
    # --- (ingen kodon i virkeligheten for enkelte komponenter)
    ("Tyr", "Arg"): "Kyotorphin (ikke-ribosomalt dipeptide)",

    # --- Tripeptider ---
    ("Glu", "Cys", "Gly"): "Glutathione (GSH)",  # ofte skrevet som γ-Glu-Cys-Gly
    ("Gly", "Pro", "Glu"): "GPE (Gly-Pro-Glu)",

    # TRH er ribosomatisk kodet, men modifisert; forenklet her som 3 aminosyrer.
    ("Glu", "His", "Pro"): "TRH (simplified; pGlu-His-Pro)",

    # --- 4–5 aminosyrepeptider ---
    ("Thr", "Lys", "Pro", "Arg"): "Tuftsin (TKPR)",

    # Kodet forløperform (glysin er amid-donor). Modent peptid er FMRF-NH₂
    ("Fen", "Met", "Arg", "Fen", "Gly"): "FMRFamide (encoded precursor: FMRFG)",

    # Met-enkefalin og Leu-enkefalin – klassiske opioidpeptider
    ("Tyr", "Gly", "Gly", "Fen", "Met"): "Met-enkephalin",
    ("Tyr", "Gly", "Gly", "Fen", "Leu"): "Leu-enkephalin",

    # Noen andre kjente korte peptider med signalfunksjon
    ("Ala", "Gly", "Cys", "Gly"): "AGCG (example short motif peptide)",

    # --- 8 aminosyrepeptider ---
    ("Val", "Pro", "Pro", "Gly", "Fen", "Ser", "Pro", "Fen"): "Bradykinin (forenklet)",

    # --- 9 aminosyrepeptider ---
    ("Cys", "Tyr", "Fen", "Gln", "Asn", "Cys", "Pro", "Arg", "Gly"): [
        "Oxytocin",
        "nonapeptid",
        "C-terminal amidert"
    ],

    # Vasopressin-familien (forenklet; variantene skiller seg ved posisjon 3 og 8)
    ("Cys", "Tyr", "Fen", "Gln", "Asn", "Cys", "Pro", "Arg", "Gly"): "Vasopressin (forenklet)",

    # --- 10 aminosyrepeptider ---
    ("Gly", "Trp", "Met", "Asp", "Fen", "Gly", "Lys", "Pro", "Val", "Gly"): "Substance P fragment (lærevennlig)",

    # --- 11 aminosyrepeptider ---
    ("His", "Ser", "Asp", "Ala", "Val", "Fen", "Thr", "Asn", "Tyr", "Thr", "Arg"): "Angiotensin II (forenklet skole peptid)",

    # --- 13 aminosyrepeptider ---
    ("Pro", "Gly", "Glu", "Lys", "Lys", "Gly", "Gly", "Lys", "Gly", "Gly", "Gly", "Lys", "Gly"): "Generisk ribosomalt mikropeptid (skole)",

    # --- 14 aminosyrepeptider ---
    ("Tyr", "Pro", "Fen", "Pro", "Gly", "Pro", "Ile", "Pro", "Asn", "Ser", "Leu", "Pro", "Tyr", "Asn"): "Somatostatin-14 (forenklet)",

    # --- 18–20 aminosyrepeptider (common signaling hormones) ---
    ("Gly", "Cys", "Thr", "Ser", "Ile", "Cys", "Ser", "Leu", "Tyr", "Gln", "Leu", "Glu", "Asn", "Tyr", "Cys", "Asn", "Fen", "Val", "Asn", "Gln"): "Insulin fragment (skole; ikke full insulin sekvens)",
    ("Met", "Leu", "Leu", "Leu", "Val"): "Signalpeptidsekvens! (hypotetisk)",

    # --- Noen flere her, hypotetiske for skole bruk ---
    ("Met", "Gly", "Lys"): "Eksempel tripeptid (hypotetisk)",
    ("Met", "Ala", "Gly", "Pro"): "Syntetisk forskningspeptid (hypotetisk)",
    ("Met", "Fen", "Val", "Asn", "Gln"): "Peptid fragment (hypotetisk)",
    ("Met", "Gly", "Glu", "Cys", "Cys"): "Insulin fragment (hypotetisk)",
}
