def renter(konto):
    
    rente = 0

    if konto <= 100000:
        rente = konto * 0.0235
    elif konto <= 500000:
        rente = 100000 * 0.0235
        rente += (konto - 100000) * 0.0255
    else:
        rente = 100000 * 0.0235
        rente += 400000 * 0.0255
        rente += (konto - 500000) * 0.0305
    
    return rente

try:
    konto = float(input("innskudd: "))
    print("rente: ", round(renter(konto)), "kr")

except ValueError:
    print("Feil: Skriv inn et gyldig tall.")