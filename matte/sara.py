innskudd = 275000
prosent_rente = 6.8
BSU = 0

for år in range (2024, 2034):
    BSU = BSU + innskudd
    renter = BSU * prosent_rente / 100
    BSU = BSU + renter
    print(år, round(renter), round(BSU))