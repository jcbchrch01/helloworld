def newtonSquare(x, estimate=1.0):
    if abs(x-estimate ** 2) <= 0.000001:
        return estimate
    else:
        return newtonSquare(x, (estimate + x / estimate) / 2)

def main():
    while(True):
        num = input('Enter a positive number or enter/return to quit: ')
        if num.strip() == ''  or num == '/return':
             break

        print()
        # note below, we are not passing estimate's value
        print('%-35s%s' % ('The Program\'s estimate is', str(newtonSquare(int(num)))))
        print('%-35s%s\n' % ('Python\'s estimate is', str(int(num)**0.5)))


main()
