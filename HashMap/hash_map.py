from calendar import TUESDAY


class HashMap:
    def __init__(self, size):
        self.size = size
        self.hashMap =  self.createBucket()

    def createBucket(self):
        return [[] for _ in range(self.size)]
    
    def setVal(self, key, value):
        hashedKey = hash(key) % self.size
        bucket = self.hashMap[hashedKey]

        foundKey = False
        for index, record in enumerate(bucket):
            recordKey, recordValue = record

            if recordKey == key:
                foundKey = True
                break
        
        if foundKey:
            bucket[index] = (key, value)
        else:
            bucket.append((key, value))

    def getVal(self, key):
        hashedKey = hash(key) % self.size
        bucket = self.hashMap[hashedKey]

        foundKey = False
        for index, record in enumerate(bucket):
            recordKey, recordVal = record

            if recordKey == key:
                foundKey = True
                break
            
        if foundKey:
            return recordVal
        else:
            return "No record found"
    def deleteVal(self, key):
        hashedKey = hash(key) % self.size
        bucket = self.hashMap[hashedKey]

        foundKey = True
        for index, record in enumerate(bucket):
            recordKey, recordVal = record
            
            if recordKey == key:
                foundKey = True
                break

        if foundKey:
            bucket.pop(index)
        return

    # ! Print items of hashMap
    def __str__(self):
        return "".join(str(item) for item in self.hashMap)

hmap = HashMap(30)
print(hmap)
hmap.setVal("hahaha", "lol")
hmap.setVal("huhuhu", "cry")
print(hmap)
print(hmap.getVal("hahaha"))
hmap.deleteVal("huhuhu")
print(hmap)