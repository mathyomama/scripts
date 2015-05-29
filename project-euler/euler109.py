import sys
from copy import deepcopy


bullseye = 25 # outer ring is 25, the inner ring is double, 50
areas = range(1, 21) + [bullseye] # the number of possible targets on a dart board excluding bullseye

def checkout(number):
    ans = 0
    # first pass
    firstPass = [list() for _ in range(number)]
    for i in areas:
        if 2*i < number:
            firstPass[2*i] = [[(2, i)]]
            ans += 1
    #print "first pass", firstPass

    # second pass
    secondPass = [list() for _ in range(number)]
    for m in range(1, 4): # m is the multiplier
        for i in areas: # i in the space on the board
            if m == 3 and i == bullseye: continue
            for j, collection in enumerate(firstPass):
                if collection is None: continue
                #print m, i, j
                index = m*i + j
                if index >= number:
                    break
                else:
                    for score in deepcopy(collection):
                        #print score
                        score.append((m, i))
                        secondPass[index].append(score)
                        ans += 1
    #print "second pass", secondPass
    #print "first pass", firstPass

    # third pass
    thirdPass = [list() for _ in range(number)]
    for m in range(1, 4):
        for i in areas:
            if m == 3 and i == bullseye: continue
            for j, collection in enumerate(secondPass):
                if collection is None: continue
                index = m*i + j
                if index >= number:
                    break
                else:
                    for score in deepcopy(collection):
                        if score[-1] == (m, i):
                            ans += 1
                        else:
                            ans += 0.5
                        score.append((m, i))
                        thirdPass[index].append(score)
                        #print index, thirdPass[index]
    #print "third pass", thirdPass
    return ans

def checkpass(aPass, number):
    newPass = number*[0] # counter for double checkouts, derived from firstPass
    for m in range(1, 4): # for the singles, doubles, and triples
        for i in areas:
            if m == 3 and i == bullseye: continue # bullseye doesn't have a triple
            for j, count in enumerate(aPass):
                index = m*i + j
                if index >= number:
                    break
                elif count != 0:
                    newPass[index] += count
    return newPass

def main():
    print checkout(100)

if __name__ == "__main__":
    sys.exit(main())
