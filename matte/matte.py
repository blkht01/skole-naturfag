def figurtall (n):
    F = 7
    for i in range (1, n+1):
        print(i, F)
        F = F + 3
figur = int(input("Enter a number: "))
figurtall(figur)