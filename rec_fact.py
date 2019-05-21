#Recursive Factorial Function

def main():
    n = int(input("Inserisci n: "))
    print("Il fattoriale di {} e': {}".format(n, fact(n)))

def fact(n):
    if n == 1:
        return 1

    return fact(n-1) * n

if __name__ == "__main__":
    main()