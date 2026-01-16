def calculateFraction(a, b):
  
    if a == 0:
        return "0"

    res = "-" if (a < 0) ^ (b < 0) else ""

    a = abs(a)
    b = abs(b)

    res += str(a // b)

    rem = a % b

    if rem == 0:
        return res

    res += "."
    mp = {}

    while rem > 0:

        if rem in mp:
            res = res[:mp[rem]] + "(" + res[mp[rem]:] + ")"
            break

        mp[rem] = len(res)

        rem = rem * 10

        res += str(rem // b)
        rem = rem % b

    return res

if __name__ == "__main__":
    a = 1
    b = 3
    print(calculateFraction(a, b))