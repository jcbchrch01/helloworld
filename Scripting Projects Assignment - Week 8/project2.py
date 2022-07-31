import math

def newton(x, estimate):
    if abs (x-estimate ** 2) <= 0.000001:
        return estimate
    else:
        estimate = newton(x, (estimate + x/estimate)/2)
    return estimate

def main():
    while True:
        x = float(input("Please enter a positive number or press enter to end the program: "))
        if (x) == 0:
            break
        print("The program's estimate of the square root of", x, "is ", newton(x, x/2))
        print("Python's value of the square root is ", math.sqrt(x))

main()

