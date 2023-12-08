class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self, key):
        return key % self.size

    def rehash(self, key):
        return 7 - (key % 7)  

    def put(self, key, data):
        hashvalue = self.hashfunction(key)

        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  
            else:
                nextslot = (hashvalue + self.rehash(key)) % self.size
                while self.slots[nextslot] is not None and self.slots[nextslot] != key:
                    nextslot = (nextslot + self.rehash(key)) % self.size

                if self.slots[nextslot] is None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
        
                    print("Table is full. Unable to insert key:", key)

    def get(self, key):
        startslot = self.hashfunction(key)
        data = None
        stop = False
        found = False
        position = startslot

        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = (position + self.rehash(key)) % self.size
                if position == startslot:
                    stop = True 
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)



H = HashTable()
H[69] = 'A'
H[66] = 'B'
H[80] = 'C'
H[35] = 'D'
H[18] = 'E'
H[52] = 'F'
H[89] = 'G'
H[70] = 'H'
H[12] = 'I'
for key, value in HashTable:
    H[key] = value


print("Slots:", H.slots)
print("Data:", H.data)
print("Value for key 52:", H[52])


def new_secondary_hash(key):
    return 3 - (key % 3)  

H.rehash = new_secondary_hash  


print("\nUpdated Slots:", H.slots)
print("Updated Data:", H.data)
print("Value for key 52 with updated hash function:", H[52])
