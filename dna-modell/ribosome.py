# main.py

from genetic_code import GENETIC_CODE, STOP_CODONS
from peptides import KNOWN_PEPTIDES
import random

MAX_LENGTH = 20

# --- Mutering instillinger (NEW) ---
MUTATION_RATE_PER_CODON = 0.5  # 1.0 = 100%, 0.5 = 50% - sjanse per kodon etter startkodon
SHOW_MUTATION_LOG = True        # print når mutering skjer?


def maybe_mutate_codon(codon: str, mutation_rate: float) -> tuple[str, bool, str]:
    """
    Muligens mutere EN base i kodon med sjansen mutation_rate.
    Returns: (new_codon, mutated_bool, log_message)
    """
    if random.random() >= mutation_rate:
        return codon, False, ""

    bases = ["A", "U", "C", "G"]
    i = random.randrange(3)
    old_base = codon[i]
    choices = [b for b in bases if b != old_base]
    new_base = random.choice(choices)

    new_codon = codon[:i] + new_base + codon[i + 1:]
    log = f"Mutasjon! {codon} → {new_codon} (pos {i+1}: {old_base}->{new_base})"
    return new_codon, True, log


def remove_initiator_methionine(peptide):
    """
    Simulerer posttranslasjonell fjerning av start kodon.
    Returnerer (ny_peptide_liste, om_det_ble_fjernet_bool)
    """
    if peptide and peptide[0] == "Met":
        return peptide[1:], True
    return peptide, False


def ask_yes_no(prompt: str) -> bool:
    while True:
        ans = input(prompt).strip().lower()
        if ans in ("j", "ja", "y", "yes"):
            return True
        if ans in ("n", "nei", "no"):
            return False
        print("Skriv 'ja' eller 'nei' (j/n).")


def ribosome():
    print("\nRibosom simulator")
    print("Du er et mRNA.")
    print("Skriv inn kodoner (A, U, C, G)")
    print("START = AUG | STOP = UAA / UAG / UGA")
    print("Skriv Q for å avslutte (evt UAA, UAG, UGA)")
    print(f"Mutasjonsrate per kodon: {MUTATION_RATE_PER_CODON*100:.2f}%\n") 

    started = False
    peptide = []

    while True:
        codon = input("mRNA → ").upper().strip()

        if codon in ("STOPP", "Q"):
            print("Simulering avsluttet.")
            return

        if len(codon) != 3 or any(b not in "AUCG" for b in codon):
            print("Ugyldig kodon! Bruk 3 bokstaver fra mRNA alfabetet (A, U, C, G)")
            continue

        # NEW: apply mutation only after translation has started
        if started:
            codon, mutated, log = maybe_mutate_codon(codon, MUTATION_RATE_PER_CODON)
            if mutated and SHOW_MUTATION_LOG:
                print(log)

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
        print(f"+ {amino_acid} lagt til")

        if len(peptide) >= MAX_LENGTH:
            print("Maks aminosyre lengde nådd.")
            break

    print("\nTranslasjon fullført")

    # Spør om enzym skal fjerne start aminosyren
    if started and peptide:
        if ask_yes_no("Vil du kjøre posttranslasjon med metionin-aminopeptidase? (j/n) → "):
            peptide, removed = remove_initiator_methionine(peptide)
            if removed:
                print("Posttranslasjon: start kodon ble fjernet.")
            else:
                print("Posttranslasjon: ingen start kodon å fjerne.")
        else:
            print("Posttranslasjon ikke kjørt: start kodon beholdes.")

    print("Polypeptidkjede:")
    print(" - ".join(peptide) if peptide else "(tom kjede)")

    peptide_tuple = tuple(peptide)
    if peptide_tuple in KNOWN_PEPTIDES:
        print(f"Kjent peptid: {KNOWN_PEPTIDES[peptide_tuple]}")
    else:
        print("Peptidet er ukjent (men biologisk sannsynlig!)")


if __name__ == "__main__":
    ribosome()
