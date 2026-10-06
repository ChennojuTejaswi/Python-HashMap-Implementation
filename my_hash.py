class MyHashMap:

    CHARS = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

    def __init__(self):

        self.capacity = 8
        self.size = 0

        self.table = self.make_empty_table(self.capacity)

    def my_length(self, text):

        count = 0

        for ch in text:
            count += 1

        return count
    
    # Create empty hash table
    def make_empty_table(self, capacity):

        table = []

        i = 0

        while i < capacity:

            table = table + [None]

            i += 1

        return table

    # Convert character to number

    def char_value(self, ch):

        i = 0

        while i < 95:

            if MyHashMap.CHARS[i] == ch:

                return i + 1

            i += 1

        return 0

    # Custom hash function

    def my_hash(self, key):

        h = 0

        i = 0

        length = self.my_length(key)

        while i < length:

            h = h * 31 + self.char_value(key[i])

            i += 1

        return h

    # Find a key inside its bucket

    def find_node(self, key):

        index = self.my_hash(key) % self.capacity

        current = self.table[index]

        while current is not None:

            if current[0] == key:

                return current

            current = current[2]

        return None

    # PUT

    def put(self, key, value):

        # First calculate the bucket
        index = self.my_hash(key) % self.capacity

        current = self.table[index]

        # Check whether key already exists
        while current is not None:

            if current[0] == key:

                # Existing key
                # Only update the value
                current[1] = value

                return

            current = current[2]

        # Key is new
        # Check whether resize is required
        if (self.size + 1) * 100 >= self.capacity * 70:

            self.resize()

        # Capacity may have changed,
        # so calculate the index again
        index = self.my_hash(key) % self.capacity

        # Create new node
        new_node = [
            key,
            value,
            self.table[index]
        ]

        # Insert at beginning of linked list
        self.table[index] = new_node

        self.size += 1

    # GET

    def get(self, key):

        index = self.my_hash(key) % self.capacity

        current = self.table[index]

        while current is not None:

            if current[0] == key:

                return current[1]

            current = current[2]

        return None

    # REMOVE

    def remove(self, key):

        index = self.my_hash(key) % self.capacity

        current = self.table[index]

        previous = None

        while current is not None:

            if current[0] == key:

                # Removing first node
                if previous is None:

                    self.table[index] = current[2]

                # Removing middle or last node
                else:

                    previous[2] = current[2]

                self.size -= 1

                return True

            previous = current

            current = current[2]

        return False


    # RESIZE

    def resize(self):

        old_table = self.table

        old_capacity = self.capacity

        # Double capacity
        self.capacity = old_capacity * 2

        # Create new empty table
        self.table = self.make_empty_table(self.capacity)

        # Visit every old bucket
        i = 0

        while i < old_capacity:

            current = old_table[i]

            # Visit every node in the chain
            while current is not None:

                # Save next node before moving current
                next_node = current[2]

                # Calculate new bucket
                index = self.my_hash(current[0]) % self.capacity

                # Link current node into new bucket
                current[2] = self.table[index]

                self.table[index] = current

                # Continue through old chain
                current = next_node

            i += 1