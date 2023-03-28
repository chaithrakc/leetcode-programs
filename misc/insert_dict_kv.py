# https://techbeamers.com/python-program-insert-a-key-value-pair-to-the-dictionary/

# Call the update() method to insert the key-value pair to the dictionary.

aKey = 10
aValue = 500

aDict = {10:100, 15:120, 16:200}

# update works like upsert
aDict.update({aKey:aValue}) # it updates the value if key is already present
aDict.update({'Chaithra':'Casey'}) # adds the key-value pair if key is not present
print(aDict)