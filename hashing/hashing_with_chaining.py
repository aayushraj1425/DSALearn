class Hash:
    def __init__(self, buckets):
        # Number of buckets
        self.bucket_count = buckets

        # Create empty chains for each bucket
        self.table = [[] for _ in range(self.bucket_count)]

    # Insert a key into hash table
    def insert(self, key):
        # Compute hash index
        index = self.get_hash_index(key)

        # Append key to corresponding chain
        self.table[index].append(key)

    # Remove a key from hash table
    def remove(self, key):
        # Compute hash index
        index = self.get_hash_index(key)

        # Remove key if present in chain
        if key in self.table[index]:
            self.table[index].remove(key)

    # Display contents of hash table
    def display(self):
        for i in range(self.bucket_count):
            print(i, end="")

            # Print all keys in chain
            for key in self.table[i]:
                print(" -->", key, end="")

            print()

    # Hash function
    def get_hash_index(self, key):
        return key % self.bucket_count

if __name__ == "__main__":
    keys = [15, 11, 27, 8, 12, 7, 18, 29, 34, 5]

    hash_table = Hash(7)

    for key in keys:
        hash_table.insert(key)

    hash_table.remove(11)
    hash_table.display()