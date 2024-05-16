#!/usr/bin/python3
"""
some randome game
"""


def getPrimes(newL):
    """
    get all prime number from list
    using Sieve of Eratosthenes alvorithm
    """
    prime = []
    while (True):
        i = newL[0:1]
        if (i):
            i = i[0]
            if i == 1:
                del newL[0]
                continue
            Pn = newL[0]
            prime.append(Pn)
            newL = [i for i in newL if i % Pn != 0]
        else:
            break
    return prime


def play(newL, primes):
    """
    player play by optimally choosing
    a prime number and remove all multiple
    of that prime number from the list
    """
    temp = []
    for i in primes:
        temp2 = []
        if i > max(newL):
            break
        if i not in newL:
            continue
        for j in newL:
            if j % i == 0:
                temp2.append(j)
        temp.append(temp2)
    if len(temp) == 0:
        return None
    toRemove = max(temp, key=len)
    for i in toRemove:
        newL.remove(i)
    return newL


def getSubW(newL, primes):
    """
    player maria and ben playing a round
    """
    users = ["Maria", "Ben"]
    while (True):
        # maria plays
        for i in range(len(users) - 1):
            newL = play(newL, primes)
            print(newL)
            if newL:
                if len(newL) == 0:
                    # this user wins
                    return users[i]
            else:
                # the other user wins
                return users[i - 1]
    return


def isWinner(x, nums):
    """
    main func
    """
    benW = 0
    mariaW = 0
    primes = [[], 0]
    # players going multiple round
    for i in nums:
        newL = list(range(1, i + 1))
        if (i > primes[1]):
            primes[1] = i
            primes[0] = getPrimes(newL[:])
        # get one round winner
        win = getSubW(newL, primes[0])
        if win == "Ben":
            benW += 1
        else:
            mariaW += 1
    if benW > mariaW:
        return "Ben"
    elif benW < mariaW:
        return "Maria"
    else:
        return None
