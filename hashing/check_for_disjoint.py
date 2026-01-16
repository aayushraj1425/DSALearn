#Checking for disjoint elements in an array using hashing
#O(n) time complexity and O(n) space complexity

def is_disjoint(a, b):
    st = set(a)
    for element in b:
        if element in st:
            return False
    return True

if __name__ == "__main__":
    a = [1, 2, 3, 2, 4, 5, 1, 6, 3]
    b = [7, 8, 9, 2]
    result = is_disjoint(a, b)
    print("Are the two arrays disjoint?:", result)