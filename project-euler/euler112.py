import sys


def is_bouncy(number):
    test = str(number)
    if len(test) < 2:
        return False
    elif test[0] < test[1]:
        increasing = True
    else:
        increasing = False
    for i in range(1, len(test) - 1):
        if increasing and test[i] > test[i + 1]:
            return True
        elif not increasing and test[i] < test[i + 1]:
            return True
    return False

def n_number(l, d):
    prod = 1
    for i in range(l):
        prod *= d + i
        prod //= i + 1
    return prod

def non_bouncy(length, digit):
    return n_number(length - 1, 10 - digit) + n_number(length - 1, digit + 1) - 1

def main():
    limit = .99
    ans = 0
    length, count, addition, total, last = 1, 0, 1, 0, 0
    bouncyDict = dict()
    while True:
        innerDict = dict()
        for digit in range(1, 10):
            last = innerDict[digit] = addition - non_bouncy(length, digit)
            count += innerDict[digit]
            total += addition
            bouncyPercentage = count/total
            if bouncyPercentage > limit:
                break
        bouncyDict[length] = innerDict
        if bouncyPercentage > limit:
            break
        length += 1
        addition *= 10
    count -= bouncyDict[length][digit]
    total -= addition
    for 
    print(bouncyDict, length, digit, count)

if __name__ == "__main__":
    sys.exit(main())
