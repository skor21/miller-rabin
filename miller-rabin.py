def is_probably_prime(n, a):
    if n == 2:  # Handle the case for the smallest prime
        return True
    if n <= 1 or n % 2 == 0:  # Handle even numbers and negatives
        return False

    m, k = n - 1, 0
    while m % 2 == 0:
        m //= 2
        k += 1

    t = pow(a, m, n)
    if t == 1 or t == n - 1:
        return "a prime"

    for _ in range(k):
        t = pow(t, 2, n)
        if t == n - 1:
            return "a prime"
        if t == 1:
            return "a composite"

    return "a composite"

def main():
    while True:
        user_input = input("Enter a number or 'quit' to exit: ").strip().lower()

        if user_input == 'quit':
            break

        try:
            number = int(user_input)
            base = 2  # You can choose any base you want, e.g., 2, 3, 5, 7...
            result = is_probably_prime(number, base)
            print(f"{number} is {result}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
