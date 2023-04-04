# This creates the Hash Table class that uses chaining.

class HashTable:
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=10):
        # Initializes the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table.
    def insert(self, key, item):
        # Gets the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Updates key if it already exists in the bucket list.
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        # Inserts the item to the end of the bucket list if the key doesn't yet exist in the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, key):
        # Gets the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]

        return None

    # Removes an item with matching key from the hash table.
    def remove(self, key):
        # Gets the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Removes the item from the bucket list if it is present.
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])
