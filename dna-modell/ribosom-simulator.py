# =========================================
# Interactive Ribosome Simulator
# You play the mRNA, the program is the ribosome
# =========================================

# Genetic code (small but illustrative)
GENETIC_CODE = {
    "AUG": "Met",      # Start codon
    "GGG": "Gly",
    "GGA": "Gly",
    "AAA": "Lys",
    "AAG": "Lys",
    "CCA": "Pro",
    "CCG": "Pro",
    "UUU": "Phe",
    "UUC": "Phe",
    "GCU": "Ala",
    "GCC": "Ala",
}

STOP_CODONS = {"UAA", "UAG", "UGA"}

# Some known peptides (toy examples)
KNOWN_PEPTIDES = {
    ("Met", "Gly", "Lys", "Gly", "Pro"): "Toy peptide (example)",
    ("Met", "Phe", "Ala", "Lys"): "Another known peptide"
}

MAX_LENGTH = 10


def ribosome():
    print("\nRibosomsimulator startet")
    print("Du er mRNA i dette spillet.")
    print("Skriv kodoner som: AUG, GGG, AAA")
    print("START = AUG | STOP = UAA / UAG / UGA\n")

    started = False
    peptide_chain = []

    while True:
        codon = input("mRNA kodon → ").upper().strip()

        if codon == "QUIT":
            print("Simulation ended.")
            return

        if len(codon) != 3 or any(base not in "AUCG" for base in codon):
            print("⚠️ Invalid codon. Use A, U, C, G only.")
            continue

        if not started:
            if codon == "AUG":
                started = True
                peptide_chain.append("Met")
                print("▶ START codon recognized (Met added)")
            else:
                print("⏸ Ribosome waiting for START codon (AUG)")
            continue

        if codon in STOP_CODONS:
            print("⛔ STOP codon reached")
            break

        amino_acid = GENETIC_CODE.get(codon, "Unknown")
        peptide_chain.append(amino_acid)
        print(f"➕ {amino_acid} added")

        if len(peptide_chain) >= MAX_LENGTH:
            print("⚠️ Maximum peptide length reached")
            break

    print("\n🧪 Translation complete")
    print("Polypeptidkjede:")
    print(" - ".join(peptide_chain))

    peptide_tuple = tuple(peptide_chain)
    if peptide_tuple in KNOWN_PEPTIDES:
        print(f"Known peptide: {KNOWN_PEPTIDES[peptide_tuple]}")
    else:
        print("Peptidet er ukjent (men fortsatt et ekte peptid!)")


if __name__ == "__main__":
    ribosome()
