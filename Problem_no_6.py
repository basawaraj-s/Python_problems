"""Find the difference between sum of squares and square of sum"""



# def sum_and_square(x):
#     sum = x*(x+1)//2
#     sum_sqaure = sum*sum

#     sum_of_square = (x)*(x+1)*(2*x+1)//6

#     diff = sum_sqaure- sum_of_square 

#     return f"Sqaure of sum {sum_sqaure},\nSum of sqaure: {sum_of_square} \n Difference between them is {diff}"

# print(sum_and_square(100))


def square_of_sum(n):
    sqr = n*(n+1)//2
    return sqr * sqr

def sum_of_square(n):
    return (n)*(n+1)*(2*n+1)//6

def diff(n):
    return  f"{square_of_sum(n) - sum_of_square(n)}" 

print(diff(100))
