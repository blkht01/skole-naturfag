# mini kalkulator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: vi kan ikke dele med null :)"

print("velkommen til min lille kalkulator!")

x = float(input("Skriv inn et tall: "))
y = float(input("Skriv inn et nytt tall: "))

print("Velg en operasjon:")
print("1 = pluss")
print("2 = minus")
print("3 = gange")
print("4 = dele")

choice = input("Velg hva du vil gjore (1/2/3/4): ")

if choice == "1":
    result = add(x, y)
elif choice == "2":
    result = subtract(x, y)
elif choice == "3":
    result = multiply(x, y)
elif choice == "4":
    result = divide(x, y)
else:
    result = "Ikke et gyldig valg! Prov igjen"

print(f"Result: {result}")
