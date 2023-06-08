def factorial(n):
    if n==0: #check if the number is zero so the factioral of it is one
        return 1
    else:
        return (n * factorial(n-1))
while True:
    number=int(input("Enter a number\n"))
    print (f"le factorial de {number} est {factorial(number)} ")
