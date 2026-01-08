# main.py

from genetic_code import GENETIC_CODE, STOP_CODONS
from peptides import KNOWN_PEPTIDES

MAX_LENGTH = 20


def ribosome():
    print("\nRibosom simulator")
    print("Du er et mRNA.")
    print("Skriv inn kodoner (A, U, C, G)")
    print("START = AUG | STOP = UAA / UAG / UGA")
    print("Skriv Q for å avslutte (evt UAA, UAG, UGA\n")

    started = False
    peptide = []

    while True:
        codon = input("mRNA → ").upper().strip()

        if codon == ("STOPP", "Q"):
            print("Simulering avsluttet.")
            return

        if len(codon) != 3 or any(b not in "AUCG" for b in codon):
            print("Ugyldig kodon! Bruk 3 bokstaver fra mRNA alfabetet (A, U, C, G)")
            continue

        if not started:
            if codon == "AUG":
                started = True
                peptide.append("Met")
                print("START kodon oppdaget ('Metionin' lagt til i polypeptidkjeden)")
            else:
                print("Venter på START kodon (AUG)")
            continue

        if codon in STOP_CODONS:
            print("STOPP kodon oppdaget")
            break

        amino_acid = GENETIC_CODE.get(codon, "Ukjent")
        peptide.append(amino_acid)
        print(f"+ {amino_acid} Lagt til")

        if len(peptide) >= MAX_LENGTH:
            print("Maks aminosyre lengde nådd.")
            break

    print("\nOversetting fullført")
    print("Polypeptidkjede:")
    print(" - ".join(peptide))

    peptide_tuple = tuple(peptide)
    if peptide_tuple in KNOWN_PEPTIDES:
        print(f"Kjent peptid: {KNOWN_PEPTIDES[peptide_tuple]}")
    else:
        print("Peptidet er ukjent (men biologisk sannsynlig!)")


if __name__ == "__main__":
    ribosome()
