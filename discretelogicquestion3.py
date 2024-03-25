
''''4. Theorem: For every integer k, if k > 0 then 𝑘2 +2𝑘 + 1 is composite. Write Python
program to verify it.
"Proof: Suppose k is any integer such that k > 0. If 𝑘2 +2𝑘 + 1 is composite, then
𝑘2 +2𝑘 + 1 = 𝑟𝑠 for some integers r and s such that
1 < 𝑟 < 𝑘2 + 2𝑘 + 1
and
1 < 𝑠 < 𝑘2 + 2𝑘 + 1
Since
𝑘2 + 2𝑘 + 1 = 𝑟𝑠
and both r and s are strictly between 1 and 𝑘2 +2𝑘 + 1, then 𝑘2 +2𝑘 + 1 is not prime.
Hence 𝑘2 +2𝑘 + 1 is composite as was to be shown."'''



def is_composite(k):
    """
    Function to check if k^2 + 2k + 1 is composite for a given integer k.
    """
    expression = k**2 + 2*k + 1
    # Check if the expression is divisible by any number other than 1 and itself
    for i in range(2, expression):
        if expression % i == 0:
            return True  # Composite
    return False  # Prime

k = int(input("Enter the value of k (k > 0): "))

def verify_theorem():
   if is_composite(k):
      print(f"For k = {k}, k^2 + 2k + 1 is composite.")
   else:
    print(f"For k = {k}, k^2 + 2k + 1 is prime.")

verify_theorem()
