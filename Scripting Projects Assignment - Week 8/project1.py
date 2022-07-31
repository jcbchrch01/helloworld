import math

tolerance = 0.000001

def newton(x):
    estimate = 1.0
    while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= tolerance:
            break
        return estimate


def main():
    while True:
        x = input("Please enter a positive number or press enter to end the progam: ")
        if x == "":
            break
        x = float(x)
        print("The programs square root of ", x,"is ", round(newton(x),2))
        print("Pythons estimate of the square root is", math.sqrt(x))

main()
