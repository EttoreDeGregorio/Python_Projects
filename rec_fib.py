#Recursive Fibonacci Sequence

def main():
    n = int(input("Inserisci n: "))
    print("Il valore della sequnza di fibonacci al volore {} e': {}".format(n, fib(n)))

def fib(n):
    if n == 1 or n == 2:
        return 1
    
    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    main()