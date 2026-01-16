#Cgecking for equal subsets in an array using native approach
def isEqual(a, b):
    if len(a) != len(b):
        return False
    return sorted(a) == sorted(b)

#Checking if the both subsest are equal using hashing
def isEqualHashing(a, b):
    n, m = len(a), len(b)
    if n != m:
        return False
    
    mp = {}
    for element in a:
        # if element in mp:
        #     mp[element] += 1
        # else:
        #     mp[element] = 1
        mp[element] = mp.get(element, 0) + 1
    
    for element in b:
        if element not in mp:
            return False
        if mp[element] == 0:
            return False
        mp[element] -= 1
    return True
        
if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    b = [5, 4, 3, 2, 1]

    print("Using native approach, are the two arrays equal?:", isEqual(a, b))
    print("using hashing, are the two arrays equal?:", isEqualHashing(a, b))
