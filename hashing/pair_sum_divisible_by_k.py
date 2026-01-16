def pair_sum(arr, k):
    if len(arr) % 2 != 0:
        return False

    freq = [0] * k

    for x in arr:
        rem = x % k
        
        if freq[(k - rem) % k] != 0:
            freq[(k - rem) % k] -= 1
        
        else:
            freq[rem] += 1

    for count in freq:
        if count != 0:
            return False

    return True

arr = [102, 108, 57, 93, 240, 60, 110, 90]
k = 10
print("True" if pair_sum(arr, k) else "False")