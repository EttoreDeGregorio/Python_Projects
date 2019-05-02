#Recursive Factorial Function

def main():
    n = int(input("Inserisci n: "))
    print("Il fattoriale di {} e': {}".format(n, fact(n)))

def fact(n):
    if n == 1:
        return 1
    
    result = fact(n-1) * n
    return result

if __name__ == "__main__":
    main()

