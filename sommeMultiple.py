def somme_multiples(n):
    somme = 0
    if 1<n<1000:
        for i in range(1, n):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                somme += i
        return somme

n = 11
resultat = somme_multiples(n)
print(resultat)

