n = 0 # starter teller for figurnummer
total = 0 # totalt antall deler så langt

figur = 3 # figur 1 starter med 3 deler
grense = 1000 # maks antall deler før loopen stopper

while total <= grense: # loopen kjører så lenge total er mindre enn eller lik 1000
    n = n + 1 # øker figur tallet med 1 for hver runde i loopen
    print(f'figur {n} har {figur} deler') # skriver ut verdien av variablene.
    total = total + figur # summen av alle delene  hittil. 
    figur = figur + 2 # vi legger til 2 deler på figuren for hver runde i loopen
    print(f"resultat:\nn = {n}\ntotal = {total}") # skriver ut verdien av variablene

# når man bruker print inne i en loop, så printes det hver runde i loopen