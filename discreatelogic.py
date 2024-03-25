def verify_properties(m, n):
    is_even_a = (6*m + 8*n) % 2 == 0
    is_odd_b = (10*m*n + 7) % 2 == 1
    
    is_composite_c = False
    if m > n > 0:
        difference = m - n
        sum_ = m + n
        is_composite_c = difference > 1 and sum_ > 1  
    
    return is_even_a, is_odd_b, is_composite_c

m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))

result = verify_properties(m, n)


print(f"Is 6m + 8n even? : {result[0]}")
print(f"Is (10*m*n) + 7 odd? : {result[1]}")

if result[2]:
    print("m^2 - n^2 is composite")
else:
    print("m^2 - n^2 is not composite")
