def gcd(a, b):
    # The Euclidean algorithm
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    # Using our core mathematical relationship
    return (a * b) // gcd(a, b)

def solve_euler_5(limit):
    # Keeping a running cumulative LCM starting at 1
    running_lcm = 1
    for i in range(1, limit + 1):
        running_lcm = lcm(running_lcm, i)
    return running_lcm

# Calculate the smallest multiple for numbers 1 to 20
result = solve_euler_5(20)
print("The smallest multiple is:", result)



import math

def find_smallest_integer(limit):

    lcm_store = 1

    for i in range(1,limit+1):
        gcd_cal = gcd(lcm_store,i)
        lcm_store= (lcm_store * i )// gcd_cal

    return lcm_store

print(find_smallest_integer(20))
