# Assuming the first line of code refers to a function for minimum
# min_value(a,b):
#   return a if a<b else b

# Assuming the second line of code refers to a function for maximum
# max_value(a,b):
#   return a if a>b else b

def main():
    # Assuming the line 'a=1.0' is a placeholder or a default value not meant for the final code
    
    # Read membership functions for two sets (f_a and f_b)
    f_a = float(input("Enter membership function of first set: "))
    f_b = float(input("Enter membership function of second set: "))
    
    # Calculate membership function for Intersection (min)
    # The paper uses: min_val(f_a, f_b)
    # Standard Python equivalent: min(f_a, f_b)
    f_intersection = min(f_a, f_b) 
    
    # Calculate membership function for Union (max)
    # The paper uses: max_val(f_a, f_b)
    # Standard Python equivalent: max(f_a, f_b)
    f_union = max(f_a, f_b)
    
    # Calculate membership function for Complement (NOT)
    # The paper uses: x-f_a and x-f_b where x is likely 1.0 (for fuzzy logic)
    # Standard Python equivalent: 1 - f_a and 1 - f_b
    f_complement_a = 1.0 - f_a
    f_complement_b = 1.0 - f_b

    # Display results
    print(f"The membership function of intersection (f_a \u2229 f_b): {f_intersection}")
    print(f"The membership function of union (f_a \u222a f_b): {f_union}")
    print(f"The membership function of complement of first set (f_a'): {f_complement_a}")
    print(f"The membership function of complement of second set (f_b'): {f_complement_b}")

if __name__ == "__main__":
    main()