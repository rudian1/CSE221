def mod_exp(base, exp, mod):
    """Calculate (base^exp) % mod using exponentiation by squaring."""
    result = 1
    base = base % mod
    while exp > 0:
        if (exp % 2) == 1:  # If exp is odd
            result = (result * base) % mod
        exp = exp >> 1  # Divide exp by 2
        base = (base * base) % mod  # Square the base
    return result

def solve():
    import sys
    
    # Read all input at once
    input_data = sys.stdin.read().strip().splitlines()
    
    # The first line contains the number of test cases
    T = int(input_data[0])
    results = []
    
    for i in range(1, T + 1):
        # Read a, n, m for each test case
        a, n, m = map(int, input_data[i].strip().split())
        
        if a == 1:
            result = n % m
        else:
            # Calculate a^n % m
            a_n_mod_m = mod_exp(a, n, m)
            # Calculate (a^n - 1) % m
            numerator = (a_n_mod_m - 1 + m) % m  # (a^n - 1) % m
            denominator = (a - 1) % m
            
            # Calculate the modular inverse of denominator mod m
            denominator_inv = mod_exp(denominator, m - 2, m)
            
            # Calculate the result using the geometric series formula
            result = (a * numerator % m * denominator_inv % m) % m
        
        results.append(result)
    
    # Print all results
    for res in results:
        print(res)

# Call the solve function
if __name__ == "__main__":
    solve()