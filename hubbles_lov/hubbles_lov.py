from astropy.cosmology import FlatLambdaCDM
import astropy.units as u

# Kosmologisk modell
H0 = 70
Om0 = 0.3
cosmo = FlatLambdaCDM(H0=H0, Om0=Om0)

# Konstanter
MPC_TO_LY = 3.26e6

def lysaar_til_mpc(lysaar):
    return lysaar / MPC_TO_LY

def mpc_til_lysaar(mpc):
    return mpc * MPC_TO_LY

print("\nVelkommen til Hubbles Lov-kalkulator!")
print("Du kan oppgi enten rødforskyvning (z), avstand i Mpc eller millioner lysår.")
print("Skriv 'q' når som helst for å avslutte.\n")

while True:
    valg = input("Vil du oppgi (1) z, (2) Mpc, eller (3) millioner lysår? Skriv 1/2/3 eller 'q' for å avslutte: ").strip()

    if valg.lower() == "q":
        print("Prøv å ikke flytte deg for fort relativt til bakgrunnsstrålingen.")
        break

    elif valg == "1":
        try:
            z_input = input("Skriv inn rødforskyvningen (z): ").strip()
            if z_input.lower() == "q":
                break
            z = float(z_input)

            if z < 0:
                raise ValueError("Rødforskyvning kan ikke være negativ.")
            elif z > 20:
                print("Advarsel: z > 20 er svært spekulativt, vi nærmer oss Big Bang!")

            distance = cosmo.comoving_distance(z)
            velocity = cosmo.H(z)

            print("\nResultater basert på rødforskyvning:")
            print(f"  Rødforskyvning (z): {z}")
            print(f"  Avstand: {distance.to(u.Mpc):.2f} Mpc")
            print(f"                     ≈ {mpc_til_lysaar(distance.value):,.0f} lysår")
            print(f"  Hastighet: {velocity:.2f}\n")

        except ValueError as e:
            print(f"Ugyldig input: {e}")

    elif valg == "2":
        try:
            avstand_input = input("Skriv inn avstanden i Mpc: ").strip()
            if avstand_input.lower() == "q":
                break
            avstand = float(avstand_input)

            if avstand < 0:
                raise ValueError("Avstanden kan ikke være negativ.")

            hastighet = H0 * avstand
            z_estimat = hastighet / 299_792.458

            print("\nResultater basert på Hubbles lov (Mpc):")
            print(f"  Avstand: {avstand:.2f} Mpc")
            print(f"           ≈ {mpc_til_lysaar(avstand):,.0f} lysår")
            print(f"  Hastighet: {hastighet:.2f} km/s")
            print(f"  Estimert rødforskyvning: z ≈ {z_estimat:.4f} (for små z)\n")

        except ValueError as e:
            print(f"Ugyldig input: {e}")

    elif valg == "3":
        try:
            lysaar_input = input("Skriv inn avstanden i millioner lysår: ").strip()
            if lysaar_input.lower() == "q":
                break
            lysaar_mill = float(lysaar_input)
            lysaar = lysaar_mill * 1_000_000

            if lysaar < 0:
                raise ValueError("Avstanden kan ikke være negativ.")

            mpc = lysaar_til_mpc(lysaar)
            hastighet = H0 * mpc
            z_estimat = hastighet / 299_792.458

            print("\nResultater basert på Hubbles lov (lysår):")
            print(f"  Avstand: {lysaar_mill:,.0f} millioner lysår")
            print(f"           ≈ {mpc:.2f} Mpc")
            print(f"  Hastighet: {hastighet:.2f} km/s")
            print(f"  Estimert rødforskyvning: z ≈ {z_estimat:.4f} (for små z)\n")

        except ValueError as e:
            print(f"Ugyldig input: {e}")

    else:
        print("Du må velge 1, 2, 3 eller 'q'. Prøv igjen.\n")
